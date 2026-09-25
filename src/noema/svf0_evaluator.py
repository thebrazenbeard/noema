from __future__ import annotations

from dataclasses import dataclass
import math
import statistics

from .boundary import commit_prediction
from .svf0 import gaussian_nll
from .svf0_experiment import SVF0ExperimentResult, SVF0SeedResult
from .svf0_statistics import (
    FROZEN_WINDOWS,
    Gate1MetricResult,
    gate1_kill_required,
    holm_bonferroni,
    mean_seed_window_delta,
    primary_persistence_result,
    student_t_two_sided_p_n8,
)


_FROZEN_SEEDS = (101, 202, 303, 404, 505, 606, 707, 808)
_LATE_EXPECTED_PER_SEED = 32


@dataclass(frozen=True, slots=True)
class AdjustedPrimaryMetric:
    metric: Gate1MetricResult
    p_value: float
    holm_reject: bool
    pass_gate: bool


@dataclass(frozen=True, slots=True)
class Gate1Evaluation:
    c1_persistence: AdjustedPrimaryMetric
    c2_persistence: AdjustedPrimaryMetric
    c1_changed_dependency_adaptation_delta: float
    c1_stable_dependency_retention_delta: float
    c2_changed_dependency_adaptation_delta: float
    c2_stable_dependency_retention_delta: float
    c1_changed_dependency_adaptation_pass: bool
    c1_stable_dependency_retention_pass: bool
    c2_changed_dependency_adaptation_pass: bool
    c2_stable_dependency_retention_pass: bool
    negative_control_mean_nll_delta: float
    negative_control_pass: bool
    kill_required: bool
    overall_pass: bool


def _window_steps(name: str) -> range:
    try:
        start, end = FROZEN_WINDOWS[name]
    except KeyError as exc:
        raise ValueError(f"unknown frozen window: {name}") from exc
    return range(start, end + 1)


def _validate_seed_result(result: SVF0SeedResult, *, negative_control: bool) -> None:
    if result.negative_control is not negative_control:
        kind = "negative-control" if negative_control else "primary"
        raise ValueError(f"expected {kind} seed result")
    if len(result.steps) != 128:
        raise ValueError("SVF-0 seed result must contain exactly 128 steps")
    expected_candidates = {"c1_recurrent", "c2_recurrent_replay", "reset_ref"}
    for expected_step, step_result in enumerate(result.steps):
        event = step_result.learner_event
        if event.step != expected_step:
            raise ValueError("SVF-0 seed result steps must be contiguous 0..127")
        if event.intervention is not None:
            raise ValueError("SVF-0 evidence must not contain intervention packets")
        by_candidate = {
            record.ticket.candidate_id: record
            for record in step_result.candidate_records
        }
        if set(by_candidate) != expected_candidates or len(step_result.candidate_records) != 3:
            raise ValueError("each SVF-0 step must contain exactly the three frozen candidate records")
        outcome = tuple(event.channels)
        for candidate_id, record in by_candidate.items():
            if record.ticket.step != expected_step:
                raise ValueError("prediction ticket step does not match evidence step")
            if record.outcome != outcome:
                raise ValueError("candidate outcome differs from the learner-visible event")
            expected_ticket = commit_prediction(
                candidate_id,
                expected_step,
                record.ticket.prediction,
            )
            if expected_ticket.commitment != record.ticket.commitment:
                raise ValueError("prediction commitment does not match the frozen prediction payload")
            if len(record.channel_scores) != len(outcome):
                raise ValueError("channel score vector dimension does not match the outcome")
            recomputed = tuple(
                gaussian_nll(
                    outcome=(observed,),
                    mean=(mean,),
                    variance=(variance,),
                )
                for observed, mean, variance in zip(
                    outcome,
                    record.ticket.prediction.mean,
                    record.ticket.prediction.variance,
                    strict=True,
                )
            )
            if any(
                not math.isclose(stored, actual, rel_tol=1e-12, abs_tol=1e-12)
                for stored, actual in zip(record.channel_scores, recomputed, strict=True)
            ):
                raise ValueError("persisted channel score does not match recomputed Gaussian NLL")
            if not math.isclose(
                record.score,
                sum(recomputed),
                rel_tol=1e-12,
                abs_tol=1e-12,
            ):
                raise ValueError("persisted total score does not match recomputed channel scores")
            resources = record.resources
            numeric_resources = (
                resources.query_cpu_seconds,
                resources.update_cpu_seconds,
                float(resources.resident_memory_bytes),
                float(resources.durable_state_bytes),
                float(resources.python_peak_allocated_bytes),
            )
            if not all(math.isfinite(value) and value >= 0 for value in numeric_resources):
                raise ValueError("candidate resource evidence must be finite and nonnegative")
            if resources.envelope_valid and resources.violations:
                raise ValueError("valid resource evidence cannot carry violations")
            if not resources.envelope_valid and not resources.violations:
                raise ValueError("invalid resource evidence must name at least one violation")
        if by_candidate["c1_recurrent"].replay_updates != 0:
            raise ValueError("C1 evidence cannot contain replay updates")
        if by_candidate["reset_ref"].replay_updates != 0:
            raise ValueError("reset reference evidence cannot contain replay updates")
        expected_c2_replays = 0 if expected_step == 0 else 1
        if by_candidate["c2_recurrent_replay"].replay_updates != expected_c2_replays:
            raise ValueError("C2 replay evidence does not match the frozen strictly-prior policy")


def _candidate_record(seed_result: SVF0SeedResult, step: int, candidate_id: str):
    step_result = seed_result.steps[step]
    matches = [
        record
        for record in step_result.candidate_records
        if record.ticket.candidate_id == candidate_id
    ]
    if len(matches) != 1:
        raise ValueError(
            f"step {step} must contain exactly one record for {candidate_id}"
        )
    return matches[0]


def _total_scores(
    seed_result: SVF0SeedResult,
    *,
    candidate_id: str,
    window_name: str,
) -> tuple[float, ...]:
    scores = tuple(
        _candidate_record(seed_result, step, candidate_id).score
        for step in _window_steps(window_name)
    )
    if not all(math.isfinite(score) for score in scores):
        raise ValueError("candidate total scores must be finite")
    return scores


def _channel_scores(
    seed_result: SVF0SeedResult,
    *,
    candidate_id: str,
    channel_index: int,
    window_name: str,
) -> tuple[float, ...]:
    if isinstance(channel_index, bool) or not isinstance(channel_index, int) or channel_index < 0:
        raise ValueError("channel_index must be a nonnegative integer")
    scores: list[float] = []
    for step in _window_steps(window_name):
        record = _candidate_record(seed_result, step, candidate_id)
        if channel_index >= len(record.channel_scores):
            raise ValueError("channel_index outside persisted channel score vector")
        score = record.channel_scores[channel_index]
        if not math.isfinite(score):
            raise ValueError("candidate channel scores must be finite")
        scores.append(score)
    return tuple(scores)


def seed_total_window_delta(
    seed_result: SVF0SeedResult,
    *,
    target_candidate_id: str,
    comparator_candidate_id: str,
    window_name: str,
) -> float:
    _validate_seed_result(seed_result, negative_control=seed_result.negative_control)
    return mean_seed_window_delta(
        _total_scores(
            seed_result,
            candidate_id=target_candidate_id,
            window_name=window_name,
        ),
        _total_scores(
            seed_result,
            candidate_id=comparator_candidate_id,
            window_name=window_name,
        ),
    )


def seed_channel_window_delta(
    seed_result: SVF0SeedResult,
    *,
    candidate_id: str,
    channel_index: int,
    left_window_name: str,
    right_window_name: str,
) -> float:
    _validate_seed_result(seed_result, negative_control=seed_result.negative_control)
    left = _channel_scores(
        seed_result,
        candidate_id=candidate_id,
        channel_index=channel_index,
        window_name=left_window_name,
    )
    right = _channel_scores(
        seed_result,
        candidate_id=candidate_id,
        channel_index=channel_index,
        window_name=right_window_name,
    )
    return statistics.fmean(left) - statistics.fmean(right)


def _resource_accounting_complete(results: tuple[SVF0SeedResult, ...]) -> bool:
    return all(
        step.point_valid
        for result in results
        for step in result.steps
    )


def _validate_result_set(
    results: tuple[SVF0SeedResult, ...],
    *,
    negative_control: bool,
) -> tuple[str, str]:
    if len(results) != 8:
        raise ValueError("first-core Gate-1 evaluation requires exactly 8 seed results")
    seeds = tuple(result.seed for result in results)
    if seeds != _FROZEN_SEEDS:
        raise ValueError("seed results must match the frozen ordered 8-seed manifest")
    for result in results:
        _validate_seed_result(result, negative_control=negative_control)
    subjects = {result.logical_subject_id for result in results}
    commitments = {result.plan_commitment for result in results}
    if len(subjects) != 1:
        raise ValueError("seed results must share one logical subject")
    if len(commitments) != 1:
        raise ValueError("seed results must share one plan commitment")
    return next(iter(subjects)), next(iter(commitments))


def _primary_metric(
    results: tuple[SVF0SeedResult, ...],
    *,
    target_candidate_id: str,
) -> tuple[Gate1MetricResult, float]:
    seed_deltas = tuple(
        seed_total_window_delta(
            result,
            target_candidate_id=target_candidate_id,
            comparator_candidate_id="reset_ref",
            window_name="late_post_change",
        )
        for result in results
    )
    expected_count = len(results) * _LATE_EXPECTED_PER_SEED
    metric = primary_persistence_result(
        seed_deltas=seed_deltas,
        scored_count=expected_count,
        expected_count=expected_count,
        worlds_completed=len(results),
        maximum_worlds=8,
        resource_accounting_complete=_resource_accounting_complete(results),
    )
    return metric, student_t_two_sided_p_n8(seed_deltas)


def _mean_channel_delta(
    results: tuple[SVF0SeedResult, ...],
    *,
    candidate_id: str,
    channel_index: int,
    left_window_name: str,
    right_window_name: str,
) -> float:
    values = tuple(
        seed_channel_window_delta(
            result,
            candidate_id=candidate_id,
            channel_index=channel_index,
            left_window_name=left_window_name,
            right_window_name=right_window_name,
        )
        for result in results
    )
    return statistics.fmean(values)


def evaluate_gate1(
    *,
    primary_results: tuple[SVF0SeedResult, ...],
    negative_control_results: tuple[SVF0SeedResult, ...],
) -> Gate1Evaluation:
    primary_subject, primary_commitment = _validate_result_set(
        primary_results,
        negative_control=False,
    )
    negative_subject, negative_commitment = _validate_result_set(
        negative_control_results,
        negative_control=True,
    )
    if primary_subject != negative_subject:
        raise ValueError("primary and negative-control results must share one logical subject")
    if primary_commitment != negative_commitment:
        raise ValueError("primary and negative-control results must share one plan commitment")

    c1_metric, c1_p = _primary_metric(
        primary_results,
        target_candidate_id="c1_recurrent",
    )
    c2_metric, c2_p = _primary_metric(
        primary_results,
        target_candidate_id="c2_recurrent_replay",
    )
    holm = holm_bonferroni(
        {
            "P_C1_VS_RESET_LATE_POST": c1_p,
            "P_C2_VS_RESET_LATE_POST": c2_p,
        },
        alpha=0.05,
    )
    c1_adjusted = AdjustedPrimaryMetric(
        metric=c1_metric,
        p_value=c1_p,
        holm_reject=holm["P_C1_VS_RESET_LATE_POST"],
        pass_gate=c1_metric.pass_gate and holm["P_C1_VS_RESET_LATE_POST"],
    )
    c2_adjusted = AdjustedPrimaryMetric(
        metric=c2_metric,
        p_value=c2_p,
        holm_reject=holm["P_C2_VS_RESET_LATE_POST"],
        pass_gate=c2_metric.pass_gate and holm["P_C2_VS_RESET_LATE_POST"],
    )

    c1_changed = _mean_channel_delta(
        primary_results,
        candidate_id="c1_recurrent",
        channel_index=1,
        left_window_name="late_post_change",
        right_window_name="early_post_change",
    )
    c1_stable = _mean_channel_delta(
        primary_results,
        candidate_id="c1_recurrent",
        channel_index=2,
        left_window_name="late_post_change",
        right_window_name="pre_change",
    )
    c2_changed = _mean_channel_delta(
        primary_results,
        candidate_id="c2_recurrent_replay",
        channel_index=1,
        left_window_name="late_post_change",
        right_window_name="early_post_change",
    )
    c2_stable = _mean_channel_delta(
        primary_results,
        candidate_id="c2_recurrent_replay",
        channel_index=2,
        left_window_name="late_post_change",
        right_window_name="pre_change",
    )

    c1_changed_pass = c1_changed <= -0.02
    c1_stable_pass = c1_stable <= 0.02
    c2_changed_pass = c2_changed <= -0.02
    c2_stable_pass = c2_stable <= 0.02

    negative_seed_deltas = tuple(
        seed_total_window_delta(
            result,
            target_candidate_id="c2_recurrent_replay",
            comparator_candidate_id="c1_recurrent",
            window_name="negative_control_score",
        )
        for result in negative_control_results
    )
    negative_mean = statistics.fmean(negative_seed_deltas)
    negative_pass = (
        negative_mean <= 0.02
        and _resource_accounting_complete(negative_control_results)
    )

    kill = gate1_kill_required(
        c1_persistence_pass=c1_adjusted.pass_gate,
        c2_persistence_pass=c2_adjusted.pass_gate,
        c1_changed_dependency_adaptation_pass=c1_changed_pass,
        c1_stable_dependency_retention_pass=c1_stable_pass,
        c2_changed_dependency_adaptation_pass=c2_changed_pass,
        c2_stable_dependency_retention_pass=c2_stable_pass,
    )
    return Gate1Evaluation(
        c1_persistence=c1_adjusted,
        c2_persistence=c2_adjusted,
        c1_changed_dependency_adaptation_delta=c1_changed,
        c1_stable_dependency_retention_delta=c1_stable,
        c2_changed_dependency_adaptation_delta=c2_changed,
        c2_stable_dependency_retention_delta=c2_stable,
        c1_changed_dependency_adaptation_pass=c1_changed_pass,
        c1_stable_dependency_retention_pass=c1_stable_pass,
        c2_changed_dependency_adaptation_pass=c2_changed_pass,
        c2_stable_dependency_retention_pass=c2_stable_pass,
        negative_control_mean_nll_delta=negative_mean,
        negative_control_pass=negative_pass,
        kill_required=kill,
        overall_pass=(not kill) and negative_pass,
    )


def evaluate_experiment_result(result: SVF0ExperimentResult) -> Gate1Evaluation:
    if not result.authorization_id:
        raise ValueError("top-level experiment result must bind a nonempty authorization_id")
    all_results = (*result.primary_results, *result.negative_control_results)
    if not all_results:
        raise ValueError("top-level experiment result contains no seed evidence")
    if any(seed.logical_subject_id != result.logical_subject_id for seed in all_results):
        raise ValueError("top-level logical subject differs from seed evidence")
    if any(seed.plan_commitment != result.plan_commitment for seed in all_results):
        raise ValueError("top-level plan commitment differs from seed evidence")
    return evaluate_gate1(
        primary_results=result.primary_results,
        negative_control_results=result.negative_control_results,
    )
