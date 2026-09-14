from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import math

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
