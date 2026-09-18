from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import ctypes
import math
import pickle
import sys
import time
import tracemalloc
from typing import Callable, Generic, TypeVar

try:
    import resource as _resource
except ImportError:  # pragma: no cover - Windows path
    _resource = None

_RESOURCE_CLASSES = {
    "resident_memory",
    "durable_state",
    "update_compute",
    "query_compute",
    "replay_compute",
    "structural_compute",
    "scope_compute",
    "audition_compute",
    "base_shadow_compute",
    "checkpoint_restart",
}


@dataclass(frozen=True, slots=True)
class ResourceMeasurement:
    resource_class: str
    amount: float

    def __post_init__(self) -> None:
        if self.resource_class not in _RESOURCE_CLASSES:
            raise ValueError("unknown resource class")
        if not math.isfinite(self.amount) or self.amount < 0:
            raise ValueError("resource amount must be finite and nonnegative")


@dataclass(frozen=True, slots=True)
class ResourceLedger:
    measurements: tuple[ResourceMeasurement, ...] = ()
    unmeasured_classes: frozenset[str] = frozenset()

    def consume(self, resource_class: str, amount: float | int | None) -> "ResourceLedger":
        if resource_class not in _RESOURCE_CLASSES:
            raise ValueError("unknown resource class")
        if amount is None:
            return ResourceLedger(
                measurements=self.measurements,
                unmeasured_classes=self.unmeasured_classes | {resource_class},
            )
        measurement = ResourceMeasurement(resource_class, float(amount))
        return ResourceLedger(
            measurements=(*self.measurements, measurement),
            unmeasured_classes=self.unmeasured_classes,
        )

    def measured_total(self, resource_class: str) -> float | None:
        if resource_class not in _RESOURCE_CLASSES:
            raise ValueError("unknown resource class")
        if resource_class in self.unmeasured_classes:
            return None
        return sum(m.amount for m in self.measurements if m.resource_class == resource_class)


class SupportClass(str, Enum):
    DIRECT_STRONG = "DIRECT_STRONG"
    DIRECT_WEAK = "DIRECT_WEAK"
    OFF_POLICY_SUPPORTED = "OFF_POLICY_SUPPORTED"
    OFF_POLICY_WEAK = "OFF_POLICY_WEAK"
    TRANSPORTED_SUPPORT = "TRANSPORTED_SUPPORT"
    ZERO_OR_UNKNOWN_SUPPORT = "ZERO_OR_UNKNOWN_SUPPORT"
    RELEARNING = "RELEARNING"


@dataclass(frozen=True, slots=True)
class SupportRecord:
    support_class: SupportClass
    confidence: float
    representation_version: str = "unversioned"

    def __post_init__(self) -> None:
        if not math.isfinite(self.confidence) or not (0.0 <= self.confidence <= 1.0):
            raise ValueError("confidence must be in [0, 1]")
        if self.support_class is SupportClass.ZERO_OR_UNKNOWN_SUPPORT and self.confidence != 0.0:
            raise ValueError("zero or unknown support cannot carry positive confidence")
        if not self.representation_version:
            raise ValueError("representation_version must be nonempty")


_T = TypeVar("_T")


@dataclass(frozen=True, slots=True)
class OperationMeasurement(Generic[_T]):
    result: _T
    cpu_seconds: float
    resident_memory_bytes: int
    python_peak_allocated_bytes: int

    @property
    def peak_memory_bytes(self) -> int:
        return self.python_peak_allocated_bytes


def process_peak_resident_memory_bytes() -> int:
    if sys.platform.startswith("win"):  # pragma: no cover - platform specific
        from ctypes import wintypes

        class _PROCESS_MEMORY_COUNTERS(ctypes.Structure):
            _fields_ = [
                ("cb", wintypes.DWORD),
                ("PageFaultCount", wintypes.DWORD),
                ("PeakWorkingSetSize", ctypes.c_size_t),
                ("WorkingSetSize", ctypes.c_size_t),
                ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
                ("QuotaPagedPoolUsage", ctypes.c_size_t),
                ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
                ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                ("PagefileUsage", ctypes.c_size_t),
                ("PeakPagefileUsage", ctypes.c_size_t),
            ]

        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        psapi = ctypes.WinDLL("psapi", use_last_error=True)
        kernel32.GetCurrentProcess.argtypes = []
        kernel32.GetCurrentProcess.restype = wintypes.HANDLE
        psapi.GetProcessMemoryInfo.argtypes = [
            wintypes.HANDLE,
            ctypes.POINTER(_PROCESS_MEMORY_COUNTERS),
            wintypes.DWORD,
        ]
        psapi.GetProcessMemoryInfo.restype = wintypes.BOOL

        counters = _PROCESS_MEMORY_COUNTERS()
        counters.cb = ctypes.sizeof(counters)
        process = kernel32.GetCurrentProcess()
        ctypes.set_last_error(0)
        ok = psapi.GetProcessMemoryInfo(
            process,
            ctypes.byref(counters),
            counters.cb,
        )
        if not ok:
            error = ctypes.get_last_error()
            raise OSError(error, "GetProcessMemoryInfo failed")
        return int(counters.PeakWorkingSetSize)

    if _resource is None:
        raise RuntimeError("process peak resident-memory measurement is unavailable")
    peak = _resource.getrusage(_resource.RUSAGE_SELF).ru_maxrss
    if peak <= 0:
        raise RuntimeError("process peak resident-memory measurement returned a nonpositive value")
    if sys.platform == "darwin":
        return int(peak)
    return int(peak * 1024)


def durable_state_bytes(value: object) -> int:
    return len(pickle.dumps(value, protocol=5))


def measure_operation(operation: Callable[[], _T]) -> OperationMeasurement[_T]:
    tracemalloc.start()
    start = time.process_time_ns()
    try:
        result = operation()
        end = time.process_time_ns()
        _, python_peak = tracemalloc.get_traced_memory()
        resident_peak = process_peak_resident_memory_bytes()
    finally:
        tracemalloc.stop()
    return OperationMeasurement(
        result=result,
        cpu_seconds=max(0.0, (end - start) / 1_000_000_000.0),
        resident_memory_bytes=resident_peak,
        python_peak_allocated_bytes=max(0, int(python_peak)),
    )


@dataclass(frozen=True, slots=True)
class FixedEnvelope:
    max_resident_memory_bytes: int
    max_durable_state_bytes: int
    max_update_cpu_seconds_per_event: float
    max_query_cpu_seconds_per_event: float
    max_shadow_auditions_per_event: int

    def __post_init__(self) -> None:
        if self.max_resident_memory_bytes < 1 or self.max_durable_state_bytes < 1:
            raise ValueError("memory limits must be positive")
        if self.max_update_cpu_seconds_per_event <= 0 or self.max_query_cpu_seconds_per_event <= 0:
            raise ValueError("CPU limits must be positive")
        if self.max_shadow_auditions_per_event < 0:
            raise ValueError("shadow audition limit must be nonnegative")


@dataclass(frozen=True, slots=True)
class EnvelopeAdjudication:
    valid: bool
    violations: tuple[str, ...]


def adjudicate_fixed_envelope(
    envelope: FixedEnvelope,
    *,
    resident_memory_bytes: int | None,
    durable_state_bytes: int | None,
    update_cpu_seconds: float | None,
    query_cpu_seconds: float | None,
    shadow_auditions: int | None,
) -> EnvelopeAdjudication:
    values = {
        "resident_memory_bytes": resident_memory_bytes,
        "durable_state_bytes": durable_state_bytes,
        "update_cpu_seconds": update_cpu_seconds,
        "query_cpu_seconds": query_cpu_seconds,
        "shadow_auditions": shadow_auditions,
    }
    violations: list[str] = [name for name, value in values.items() if value is None]
    if resident_memory_bytes is not None and resident_memory_bytes > envelope.max_resident_memory_bytes:
        violations.append("resident_memory_bytes")
    if durable_state_bytes is not None and durable_state_bytes > envelope.max_durable_state_bytes:
        violations.append("durable_state_bytes")
    if update_cpu_seconds is not None and update_cpu_seconds > envelope.max_update_cpu_seconds_per_event:
        violations.append("update_cpu_seconds")
    if query_cpu_seconds is not None and query_cpu_seconds > envelope.max_query_cpu_seconds_per_event:
        violations.append("query_cpu_seconds")
    if shadow_auditions is not None and shadow_auditions > envelope.max_shadow_auditions_per_event:
        violations.append("shadow_auditions")
    ordered = tuple(dict.fromkeys(violations))
    return EnvelopeAdjudication(valid=not ordered, violations=ordered)
