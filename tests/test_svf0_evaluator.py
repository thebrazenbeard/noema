import math

from noema.accounting import FixedEnvelope
from noema.boundary import LearnerEvent, Prediction, commit_prediction
from noema.candidates import RecurrentC2State, RecurrentGaussianState, RecurrentReplayBuffer
from noema.svf0_evaluator import (
    evaluate_gate1,
    seed_channel_window_delta,
    seed_total_window_delta,
)
from noema.svf0_experiment import SVF0SeedResult
from noema.svf0_runner import CandidateStepRecord, StepResources, SVF0StepResult


def _resources(valid: bool = True) -> StepResources:
    return StepResources(
        query_cpu_seconds=0.001,
        update_cpu_seconds=0.001,
        resident_memory_bytes=1024,
        durable_state_bytes=256,
        python_peak_allocated_bytes=128,
        envelope_valid=valid,
        violations=() if valid else ("resident_memory_bytes",),
    )


def _record(candidate_id: str, step: int, channels: tuple[float, float, float], valid: bool = True):
    prediction = Prediction(mean=(0.0, 0.0, 0.0), variance=(1.0, 1.0, 1.0))
    ticket = commit_prediction(candidate_id, step, prediction)
    return CandidateStepRecord(
        ticket=ticket,
        outcome=(0.0, 0.0, 0.0),
        score=sum(channels),
        channel_scores=channels,
        resources=_resources(valid),
        replay_updates=0 if candidate_id != "c2_recurrent_replay" else 1,
    )


def _step(step: int, *, target_shift: float = 0.0, invalid: bool = False) -> SVF0StepResult:
    if step < 64:
        changed = 0.30
    elif step < 80:
        changed = 0.50
    elif step >= 96:
        changed = 0.30
    else:
        changed = 0.40
    stable = 0.30
    driver = 0.20

    c1_channels = (driver, changed + target_shift, stable)
    c2_channels = (driver, changed + target_shift, stable)
    reset_channels = (0.35, 0.35, 0.35)
    records = (
        _record("c1_recurrent", step, c1_channels, valid=not invalid),
        _record("c2_recurrent_replay", step, c2_channels, valid=not invalid),
        _record("reset_ref", step, reset_channels, valid=not invalid),
    )
    return SVF0StepResult(
        state=None,
        learner_event=LearnerEvent(step=step, channels=(0.0, 0.0, 0.0), intervention=None),
        candidate_records=records,
    )


def _primary_seed(seed: int, *, invalid_step: int | None = None) -> SVF0SeedResult:
    return SVF0SeedResult(
        seed=seed,
        negative_control=False,
        logical_subject_id="NOEMA_SVF0_RECURRENT_GATE1_V4",
        plan_commitment="a" * 64,
        steps=tuple(
            _step(step, invalid=(step == invalid_step))
            for step in range(128)
        ),
    )


def _negative_step(step: int, delta: float = 0.01) -> SVF0StepResult:
    c1 = (0.20, 0.20, 0.20)
    c2 = (0.20 + delta / 3.0, 0.20 + delta / 3.0, 0.20 + delta / 3.0)
    reset = (0.35, 0.35, 0.35)
    return SVF0StepResult(
        state=None,
        learner_event=LearnerEvent(step=step, channels=(0.0, 0.0, 0.0), intervention=None),
        candidate_records=(
            _record("c1_recurrent", step, c1),
            _record("c2_recurrent_replay", step, c2),
            _record("reset_ref", step, reset),
        ),
    )


def _negative_seed(seed: int, delta: float = 0.01) -> SVF0SeedResult:
    return SVF0SeedResult(
        seed=seed,
        negative_control=True,
        logical_subject_id="NOEMA_SVF0_RECURRENT_GATE1_V4",
        plan_commitment="a" * 64,
        steps=tuple(_negative_step(step, delta=delta) for step in range(128)),
    )


def _seeds() -> tuple[int, ...]:
    return (101, 202, 303, 404, 505, 606, 707, 808)


def test_seed_total_window_delta_uses_target_minus_comparator():
    result = seed_total_window_delta(
        _primary_seed(101),
        target_candidate_id="c1_recurrent",
        comparator_candidate_id="reset_ref",
        window_name="late_post_change",
    )
    assert math.isclose(result, -0.25, abs_tol=1e-12)


def test_seed_channel_window_delta_computes_late_minus_early_changed_channel():
    seed = _primary_seed(101)
    result = seed_channel_window_delta(
        seed,
        candidate_id="c1_recurrent",
        channel_index=1,
        left_window_name="late_post_change",
        right_window_name="early_post_change",
    )
    assert math.isclose(result, -0.20, abs_tol=1e-12)


def test_gate1_evaluation_passes_complete_fabricated_evidence():
    primary = tuple(_primary_seed(seed) for seed in _seeds())
    negative = tuple(_negative_seed(seed) for seed in _seeds())
    result = evaluate_gate1(primary_results=primary, negative_control_results=negative)

    assert result.c1_persistence.metric.pass_gate is True
    assert result.c2_persistence.metric.pass_gate is True
    assert result.c1_persistence.holm_reject is True
    assert result.c2_persistence.holm_reject is True
    assert result.c1_persistence.pass_gate is True
    assert result.c2_persistence.pass_gate is True
    assert result.c1_changed_dependency_adaptation_pass is True
    assert result.c1_stable_dependency_retention_pass is True
    assert result.c2_changed_dependency_adaptation_pass is True
    assert result.c2_stable_dependency_retention_pass is True
    assert result.negative_control_pass is True
    assert result.kill_required is False
    assert result.overall_pass is True


def test_resource_invalid_point_breaks_primary_support_and_overall_gate():
    primary = tuple(
        _primary_seed(seed, invalid_step=100 if seed == 101 else None)
        for seed in _seeds()
    )
    negative = tuple(_negative_seed(seed) for seed in _seeds())
    result = evaluate_gate1(primary_results=primary, negative_control_results=negative)
    assert result.c1_persistence.metric.support_pass is False
    assert result.c2_persistence.metric.support_pass is False
    assert result.overall_pass is False


def test_negative_control_failure_blocks_overall_without_rewriting_six_kill_flags():
    primary = tuple(_primary_seed(seed) for seed in _seeds())
    negative = tuple(_negative_seed(seed, delta=0.03) for seed in _seeds())
    result = evaluate_gate1(primary_results=primary, negative_control_results=negative)
    assert result.kill_required is False
    assert result.negative_control_pass is False
    assert result.overall_pass is False


def test_evaluator_rejects_wrong_seed_set_and_wrong_control_kind():
    primary = tuple(_primary_seed(seed) for seed in _seeds())
    negative = tuple(_negative_seed(seed) for seed in _seeds())

    try:
        evaluate_gate1(primary_results=primary[:-1], negative_control_results=negative)
    except ValueError as exc:
        assert "8" in str(exc)
    else:
        raise AssertionError("incomplete primary seed set was accepted")

    bad_negative = list(negative)
    bad_negative[0] = _primary_seed(101)
    try:
        evaluate_gate1(primary_results=primary, negative_control_results=tuple(bad_negative))
    except ValueError as exc:
        assert "negative-control" in str(exc)
    else:
        raise AssertionError("wrong control kind was accepted")


def test_evaluator_rejects_mixed_plan_commitments():
    primary = list(_primary_seed(seed) for seed in _seeds())
    negative = tuple(_negative_seed(seed) for seed in _seeds())
    original = primary[0]
    primary[0] = SVF0SeedResult(
        seed=original.seed,
        negative_control=False,
        logical_subject_id=original.logical_subject_id,
        plan_commitment="b" * 64,
        steps=original.steps,
    )
    try:
        evaluate_gate1(primary_results=tuple(primary), negative_control_results=negative)
    except ValueError as exc:
        assert "plan commitment" in str(exc)
    else:
        raise AssertionError("mixed plan commitments were accepted")
