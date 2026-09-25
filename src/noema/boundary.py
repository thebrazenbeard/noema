from __future__ import annotations

from dataclasses import dataclass
import math

from .provenance import canonical_json_bytes, sha256_hex


def _finite_tuple(values: tuple[float, ...], *, name: str) -> None:
    if not values:
        raise ValueError(f"{name} must not be empty")
    if not all(math.isfinite(value) for value in values):
        raise ValueError(f"{name} must contain only finite values")


@dataclass(frozen=True, slots=True)
class InterventionPacket:
    target: int
    commanded_value: float

    def __post_init__(self) -> None:
        if self.target < 0:
            raise ValueError("intervention target must be nonnegative")
        if not math.isfinite(self.commanded_value):
            raise ValueError("commanded value must be finite")


@dataclass(frozen=True, slots=True)
class LearnerEvent:
    step: int
    channels: tuple[float, ...]
    intervention: InterventionPacket | None

    def __post_init__(self) -> None:
        if self.step < 0:
            raise ValueError("step must be nonnegative")
        _finite_tuple(self.channels, name="channels")
        if self.intervention is not None and self.intervention.target >= len(self.channels):
            raise ValueError("intervention target outside channel range")


@dataclass(frozen=True, slots=True)
class EvaluatorRecord:
    step: int
    hidden_family: str
    realized_score: float | None

    def __post_init__(self) -> None:
        if self.step < 0:
            raise ValueError("step must be nonnegative")
        if not self.hidden_family:
            raise ValueError("hidden_family must be nonempty evaluator-only provenance")
        if self.realized_score is not None and not math.isfinite(self.realized_score):
            raise ValueError("realized_score must be finite when present")


@dataclass(frozen=True, slots=True)
class Prediction:
    mean: tuple[float, ...]
    variance: tuple[float, ...]

    def __post_init__(self) -> None:
        _finite_tuple(self.mean, name="mean")
        _finite_tuple(self.variance, name="variance")
        if len(self.mean) != len(self.variance):
            raise ValueError("mean and variance dimensions must match")
        if any(value <= 0 for value in self.variance):
            raise ValueError("variance must be strictly positive")


@dataclass(frozen=True, slots=True)
class PredictionTicket:
    candidate_id: str
    step: int
    prediction: Prediction
    commitment: str


@dataclass(frozen=True, slots=True)
class ScopeTicket:
    candidate_id: str
    step: int
    scope_id: str
    selection_probability: float
    commitment: str


def _prediction_payload(candidate_id: str, step: int, prediction: Prediction) -> dict[str, object]:
    return {
        "candidate_id": candidate_id,
        "step": step,
        "mean": list(prediction.mean),
        "variance": list(prediction.variance),
    }


def commit_prediction(candidate_id: str, step: int, prediction: Prediction) -> PredictionTicket:
    if not candidate_id:
        raise ValueError("candidate_id must be nonempty")
    if step < 0:
        raise ValueError("step must be nonnegative")
    commitment = sha256_hex(canonical_json_bytes(_prediction_payload(candidate_id, step, prediction)))
    return PredictionTicket(candidate_id, step, prediction, commitment)


def commit_scope(
    candidate_id: str,
    step: int,
    scope_id: str,
    selection_probability: float,
) -> ScopeTicket:
    if not candidate_id or not scope_id:
        raise ValueError("candidate_id and scope_id must be nonempty")
    if step < 0:
        raise ValueError("step must be nonnegative")
    if not (0.0 < selection_probability <= 1.0):
        raise ValueError("selection_probability must be in (0, 1]")
    payload = {
        "candidate_id": candidate_id,
        "step": step,
        "scope_id": scope_id,
        "selection_probability": selection_probability,
    }
    commitment = sha256_hex(canonical_json_bytes(payload))
    return ScopeTicket(candidate_id, step, scope_id, selection_probability, commitment)
