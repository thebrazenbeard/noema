from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import math
import pickle
import time
import tracemalloc
from typing import Callable, Generic, TypeVar

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
    peak_memory_bytes: int


def durable_state_bytes(value: object) -> int:
    return len(pickle.dumps(value, protocol=5))


def measure_operation(operation: Callable[[], _T]) -> OperationMeasurement[_T]:
    tracemalloc.start()
    start = time.process_time_ns()
    try:
        result = operation()
        end = time.process_time_ns()
        _, peak = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    return OperationMeasurement(
        result=result,
        cpu_seconds=max(0.0, (end - start) / 1_000_000_000.0),
        peak_memory_bytes=max(0, int(peak)),
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
