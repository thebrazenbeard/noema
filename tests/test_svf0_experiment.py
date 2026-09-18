import noema.svf0_experiment as experiment
from noema.accounting import FixedEnvelope
from noema.candidates import RecurrentConfig, RecurrentReplayConfig
from noema.svf0 import SVF0NegativeControlConfig, SVF0WorldConfig
from noema.svf0_runner import SVF0RunnerConfig


SUBJECT = "NOEMA_SVF0_RECURRENT_GATE1_V3"


def _plan() -> experiment.SVF0ExperimentPlan:
    return experiment.SVF0ExperimentPlan(
        logical_subject_id=SUBJECT,
        seeds=(101, 202, 303, 404, 505, 606, 707, 808),
        max_events=128,
        world=SVF0WorldConfig(
            change_point=64,
            coefficient_before=0.8,
            coefficient_after=-0.4,
            stable_coefficient=0.3,
            noise_half_width=0.05,
        ),
        negative_control=SVF0NegativeControlConfig(
            coefficient=0.4,
            stable_coefficient=-0.2,
            noise_half_width=0.05,
        ),
        runner=SVF0RunnerConfig(
            recurrent=RecurrentConfig(
                learning_rate=0.1,
                variance_alpha=0.05,
                variance_floor=0.0025,
            ),
            replay=RecurrentReplayConfig(
                capacity=32,
                max_replay_updates_per_event=1,
            ),
            reset_variance=1.0,
            envelope=FixedEnvelope(
                max_resident_memory_bytes=268435456,
                max_durable_state_bytes=1048576,
                max_update_cpu_seconds_per_event=0.05,
                max_query_cpu_seconds_per_event=0.01,
                max_shadow_auditions_per_event=0,
            ),
        ),
    )


def test_plan_requires_exact_frozen_seed_count_and_event_count():
    plan = _plan()
    assert len(plan.seeds) == 8
    assert plan.max_events == 128
    try:
        experiment.SVF0ExperimentPlan(
            logical_subject_id=SUBJECT,
            seeds=(101, 202),
            max_events=128,
            world=plan.world,
            negative_control=plan.negative_control,
            runner=plan.runner,
        )
    except ValueError as exc:
        assert "8 seeds" in str(exc)
    else:
        raise AssertionError("non-frozen seed count was accepted")


def test_initial_runtime_state_is_reset_and_matched():
    state = experiment.initial_runtime_state(_plan())
    assert state.c1.count == 0
    assert state.c2.base.count == 0
    assert state.c1.previous is None
    assert state.c2.base.previous is None
    assert state.c1 == state.c2.base
    assert state.c2.replay.items == ()


def test_execute_seed_without_e0_authority_fails_before_world_generation(monkeypatch):
    called = False

    def forbidden_world(**kwargs):
        nonlocal called
        called = True
        raise AssertionError("world generation occurred before E0 authority")

    monkeypatch.setattr(experiment, "svf0_point", forbidden_world)
    try:
        experiment.execute_primary_seed(
            plan=_plan(),
            seed=101,
            authority=None,
        )
    except PermissionError as exc:
        assert "E0" in str(exc)
    else:
        raise AssertionError("seed execution proceeded without E0 authority")
    assert called is False


def test_wrong_subject_authority_fails_before_world_generation(monkeypatch):
    called = False

    def forbidden_world(**kwargs):
        nonlocal called
        called = True
        raise AssertionError("world generation occurred under wrong authority")

    monkeypatch.setattr(experiment, "svf0_point", forbidden_world)
    authority = experiment.E0ExecutionAuthority(
        authorization_id="test-only",
        logical_subject_id="WRONG_SUBJECT",
    )
    try:
        experiment.execute_primary_seed(
            plan=_plan(),
            seed=101,
            authority=authority,
        )
    except PermissionError as exc:
        assert "subject" in str(exc)
    else:
        raise AssertionError("wrong-subject authority was accepted")
    assert called is False


def test_unfrozen_seed_is_rejected_before_world_generation(monkeypatch):
    called = False

    def forbidden_world(**kwargs):
        nonlocal called
        called = True
        raise AssertionError("world generation occurred for unfrozen seed")

    monkeypatch.setattr(experiment, "svf0_point", forbidden_world)
    authority = experiment.E0ExecutionAuthority(
        authorization_id="test-only",
        logical_subject_id=SUBJECT,
    )
    try:
        experiment.execute_primary_seed(
            plan=_plan(),
            seed=999,
            authority=authority,
        )
    except ValueError as exc:
        assert "frozen seed" in str(exc)
    else:
        raise AssertionError("unfrozen seed was accepted")
    assert called is False


def test_full_experiment_without_e0_authority_fails_before_any_seed(monkeypatch):
    called = False

    def forbidden_seed(**kwargs):
        nonlocal called
        called = True
        raise AssertionError("seed executor ran before E0 authority")

    monkeypatch.setattr(experiment, "execute_primary_seed", forbidden_seed)
    try:
        experiment.execute_frozen_experiment(
            plan=_plan(),
            authority=None,
        )
    except PermissionError as exc:
        assert "E0" in str(exc)
    else:
        raise AssertionError("full experiment proceeded without E0 authority")
    assert called is False
