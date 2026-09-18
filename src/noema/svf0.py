from __future__ import annotations

from dataclasses import dataclass
import hashlib
import math

from .boundary import LearnerEvent


def _finite(value: float, *, name: str) -> None:
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")


@dataclass(frozen=True, slots=True)
class SVF0WorldConfig:
    change_point: int
    coefficient_before: float
    coefficient_after: float
    stable_coefficient: float
    noise_half_width: float

    def __post_init__(self) -> None:
        if self.change_point < 1:
            raise ValueError("change_point must be at least 1")
        for name in ("coefficient_before", "coefficient_after", "stable_coefficient", "noise_half_width"):
            _finite(float(getattr(self, name)), name=name)
        if self.noise_half_width < 0:
            raise ValueError("noise_half_width must be nonnegative")
        if self.coefficient_before == self.coefficient_after:
            raise ValueError("regime change must alter the designated dependency coefficient")


@dataclass(frozen=True, slots=True)
class SVF0NegativeControlConfig:
    coefficient: float
    stable_coefficient: float
    noise_half_width: float

    def __post_init__(self) -> None:
        for name in ("coefficient", "stable_coefficient", "noise_half_width"):
            _finite(float(getattr(self, name)), name=name)
        if self.noise_half_width < 0:
            raise ValueError("noise_half_width must be nonnegative")


@dataclass(frozen=True, slots=True)
class SVF0WorldPoint:
    learner_event: LearnerEvent
    changed_coefficient: float
    stable_coefficient: float


def _unit_interval(seed: int, step: int, lane: int) -> float:
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError("seed must be an integer")
    if isinstance(step, bool) or not isinstance(step, int) or step < 0:
        raise ValueError("step must be a nonnegative integer")
    payload = f"NOEMA_SVF0_V1:{seed}:{step}:{lane}".encode("ascii")
    raw = int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")
    return raw / float(1 << 64)


def _symmetric(seed: int, step: int, lane: int) -> float:
    return 2.0 * _unit_interval(seed, step, lane) - 1.0


def svf0_point(*, seed: int, step: int, config: SVF0WorldConfig) -> SVF0WorldPoint:
    driver = _symmetric(seed, step, 0)
    changed_coefficient = (
        config.coefficient_before if step < config.change_point else config.coefficient_after
    )
    changed_noise = config.noise_half_width * _symmetric(seed, step, 1)
    stable_noise = config.noise_half_width * _symmetric(seed, step, 2)
    changed = changed_coefficient * driver + changed_noise
    stable = config.stable_coefficient * driver + stable_noise
    return SVF0WorldPoint(
        learner_event=LearnerEvent(
            step=step,
            channels=(driver, changed, stable),
            intervention=None,
        ),
        changed_coefficient=changed_coefficient,
        stable_coefficient=config.stable_coefficient,
    )


def svf0_negative_control_point(
    *,
    seed: int,
    step: int,
    config: SVF0NegativeControlConfig,
) -> SVF0WorldPoint:
    driver = _symmetric(seed, step, 10)
    changed_noise = config.noise_half_width * _symmetric(seed, step, 11)
    stable_noise = config.noise_half_width * _symmetric(seed, step, 12)
    changed = config.coefficient * driver + changed_noise
    stable = config.stable_coefficient * driver + stable_noise
    return SVF0WorldPoint(
        learner_event=LearnerEvent(
            step=step,
            channels=(driver, changed, stable),
            intervention=None,
        ),
        changed_coefficient=config.coefficient,
        stable_coefficient=config.stable_coefficient,
    )


def gaussian_nll(
    *,
    outcome: tuple[float, ...],
    mean: tuple[float, ...],
    variance: tuple[float, ...],
) -> float:
    if not outcome or len(outcome) != len(mean) or len(mean) != len(variance):
        raise ValueError("outcome, mean, and variance dimensions must match and be nonempty")
    total = 0.0
    for observed, expected, var in zip(outcome, mean, variance, strict=True):
        _finite(observed, name="outcome")
        _finite(expected, name="mean")
        _finite(var, name="variance")
        if var <= 0:
            raise ValueError("variance must be strictly positive")
        residual = observed - expected
        total += 0.5 * (math.log(2.0 * math.pi * var) + (residual * residual) / var)
    return total
