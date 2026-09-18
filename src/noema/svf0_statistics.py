from __future__ import annotations

from dataclasses import dataclass
import math
import statistics
from typing import Mapping


FROZEN_WINDOWS: dict[str, tuple[int, int]] = {
    "warmup_excluded": (0, 15),
    "pre_change": (16, 63),
    "early_post_change": (64, 79),
    "late_post_change": (96, 127),
    "negative_control_score": (16, 127),
}

_STUDENT_T_975_DF7 = 2.364624251
_PRIMARY_MEAN_DELTA_THRESHOLD = -0.02


@dataclass(frozen=True, slots=True)
class ConfidenceInterval:
    mean: float
    lower: float
    upper: float
    critical_value: float


@dataclass(frozen=True, slots=True)
class Gate1MetricResult:
    mean_delta: float
    ci_lower: float
    ci_upper: float
    threshold_pass: bool
    support_pass: bool
    pass_gate: bool


def _finite_values(values: tuple[float, ...], *, name: str) -> None:
    if not values:
        raise ValueError(f"{name} must not be empty")
    if not all(math.isfinite(value) for value in values):
        raise ValueError(f"{name} must contain only finite values")


def mean_seed_window_delta(
    target_scores: tuple[float, ...],
    comparator_scores: tuple[float, ...],
) -> float:
    _finite_values(target_scores, name="target_scores")
    _finite_values(comparator_scores, name="comparator_scores")
    if len(target_scores) != len(comparator_scores):
        raise ValueError("target and comparator score windows must have identical cardinality")
    return sum(
        target - comparator
        for target, comparator in zip(target_scores, comparator_scores, strict=True)
    ) / len(target_scores)


def student_t_ci_n8(seed_values: tuple[float, ...]) -> ConfidenceInterval:
    _finite_values(seed_values, name="seed_values")
    if len(seed_values) != 8:
        raise ValueError("frozen first-core Student-t interval requires exactly 8 seed values")
    mean = statistics.fmean(seed_values)
    sample_sd = statistics.stdev(seed_values)
    half_width = _STUDENT_T_975_DF7 * sample_sd / math.sqrt(8.0)
    return ConfidenceInterval(
        mean=mean,
        lower=mean - half_width,
        upper=mean + half_width,
        critical_value=_STUDENT_T_975_DF7,
    )



def _beta_continued_fraction(a: float, b: float, x: float) -> float:
    max_iterations = 200
    epsilon = 3.0e-14
    fp_min = 1.0e-300
    qab = a + b
    qap = a + 1.0
    qam = a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < fp_min:
        d = fp_min
    d = 1.0 / d
    h = d
    for m in range(1, max_iterations + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < fp_min:
            d = fp_min
        c = 1.0 + aa / c
        if abs(c) < fp_min:
            c = fp_min
        d = 1.0 / d
        h *= d * c

        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < fp_min:
            d = fp_min
        c = 1.0 + aa / c
        if abs(c) < fp_min:
            c = fp_min
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) <= epsilon:
            return h
    raise ArithmeticError("incomplete-beta continued fraction did not converge")


def _regularized_incomplete_beta(x: float, a: float, b: float) -> float:
    if not (0.0 <= x <= 1.0):
        raise ValueError("x must be in [0, 1]")
    if a <= 0.0 or b <= 0.0:
        raise ValueError("beta parameters must be positive")
    if x == 0.0:
        return 0.0
    if x == 1.0:
        return 1.0
    log_bt = (
        math.lgamma(a + b)
        - math.lgamma(a)
        - math.lgamma(b)
        + a * math.log(x)
        + b * math.log1p(-x)
    )
    bt = math.exp(log_bt)
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * _beta_continued_fraction(a, b, x) / a
    return 1.0 - bt * _beta_continued_fraction(b, a, 1.0 - x) / b


def student_t_two_sided_p_df7(t_statistic: float) -> float:
    if not math.isfinite(t_statistic):
        raise ValueError("t_statistic must be finite")
    degrees_freedom = 7.0
    x = degrees_freedom / (degrees_freedom + t_statistic * t_statistic)
    return _regularized_incomplete_beta(x, degrees_freedom / 2.0, 0.5)


def student_t_two_sided_p_n8(seed_values: tuple[float, ...]) -> float:
    _finite_values(seed_values, name="seed_values")
    if len(seed_values) != 8:
        raise ValueError("frozen first-core Student-t p-value requires exactly 8 seed values")
    mean = statistics.fmean(seed_values)
    sample_sd = statistics.stdev(seed_values)
    if sample_sd == 0.0:
        return 1.0 if mean == 0.0 else 0.0
    t_statistic = mean / (sample_sd / math.sqrt(8.0))
    return student_t_two_sided_p_df7(t_statistic)


def primary_persistence_result(
    *,
    seed_deltas: tuple[float, ...],
    scored_count: int,
    expected_count: int,
    worlds_completed: int,
    maximum_worlds: int,
    resource_accounting_complete: bool,
) -> Gate1MetricResult:
    if isinstance(scored_count, bool) or not isinstance(scored_count, int) or scored_count < 0:
        raise ValueError("scored_count must be a nonnegative integer")
    if isinstance(expected_count, bool) or not isinstance(expected_count, int) or expected_count < 1:
        raise ValueError("expected_count must be a positive integer")
    if isinstance(worlds_completed, bool) or not isinstance(worlds_completed, int) or worlds_completed < 0:
        raise ValueError("worlds_completed must be a nonnegative integer")
    if isinstance(maximum_worlds, bool) or not isinstance(maximum_worlds, int) or maximum_worlds < 1:
        raise ValueError("maximum_worlds must be a positive integer")
    if not isinstance(resource_accounting_complete, bool):
        raise ValueError("resource_accounting_complete must be boolean")

    ci = student_t_ci_n8(seed_deltas)
    threshold_pass = (
        ci.mean <= _PRIMARY_MEAN_DELTA_THRESHOLD
        and ci.upper < 0.0
    )
    support_pass = (
        scored_count == expected_count
        and worlds_completed == maximum_worlds
        and resource_accounting_complete
    )
    return Gate1MetricResult(
        mean_delta=ci.mean,
        ci_lower=ci.lower,
        ci_upper=ci.upper,
        threshold_pass=threshold_pass,
        support_pass=support_pass,
        pass_gate=threshold_pass and support_pass,
    )


def holm_bonferroni(
    p_values: Mapping[str, float],
    *,
    alpha: float,
) -> dict[str, bool]:
    if not p_values:
        raise ValueError("p_values must not be empty")
    if not math.isfinite(alpha) or not (0.0 < alpha < 1.0):
        raise ValueError("alpha must be in (0, 1)")
    normalized: list[tuple[str, float]] = []
    for name, value in p_values.items():
        if not name:
            raise ValueError("hypothesis names must be nonempty")
        if not math.isfinite(value) or not (0.0 <= value <= 1.0):
            raise ValueError("p-values must be finite and in [0, 1]")
        normalized.append((name, float(value)))

    ordered = sorted(normalized, key=lambda item: (item[1], item[0]))
    decisions = {name: False for name, _ in ordered}
    m = len(ordered)
    rejecting = True
    for index, (name, p_value) in enumerate(ordered):
        threshold = alpha / (m - index)
        if rejecting and p_value <= threshold:
            decisions[name] = True
        else:
            rejecting = False
    return decisions


def gate1_kill_required(
    *,
    c1_persistence_pass: bool,
    c2_persistence_pass: bool,
    c1_changed_dependency_adaptation_pass: bool,
    c1_stable_dependency_retention_pass: bool,
    c2_changed_dependency_adaptation_pass: bool,
    c2_stable_dependency_retention_pass: bool,
) -> bool:
    flags = (
        c1_persistence_pass,
        c2_persistence_pass,
        c1_changed_dependency_adaptation_pass,
        c1_stable_dependency_retention_pass,
        c2_changed_dependency_adaptation_pass,
        c2_stable_dependency_retention_pass,
    )
    if not all(isinstance(flag, bool) for flag in flags):
        raise ValueError("Gate-1 pass flags must be boolean")
    return not all(flags)
