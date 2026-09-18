import math
import noema.svf0_runner as runner
from noema.accounting import FixedEnvelope
from noema.boundary import LearnerEvent
from noema.candidates import (
    RecurrentC2State,
    RecurrentConfig,
    RecurrentGaussianState,
    RecurrentReplayBuffer,
    RecurrentReplayConfig,
)


def _initial_base() -> RecurrentGaussianState:
    return RecurrentGaussianState.zeros(dimension=3, initial_variance=1.0)


def _initial_c2(replay_config: RecurrentReplayConfig) -> RecurrentC2State:
    return RecurrentC2State(
        base=_initial_base(),
        replay=RecurrentReplayBuffer.empty(replay_config),
    )


def _config() -> runner.SVF0RunnerConfig:
    return runner.SVF0RunnerConfig(
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
    )


def test_all_prediction_tickets_commit_before_outcome_reveal(monkeypatch):
    order = []
    original_commit = runner.commit_prediction

    def recording_commit(candidate_id, step, prediction):
        order.append(("commit", candidate_id, step))
        return original_commit(candidate_id, step, prediction)

    monkeypatch.setattr(runner, "commit_prediction", recording_commit)

    def reveal():
        order.append(("reveal", None, 0))
        return LearnerEvent(step=0, channels=(0.25, -0.1, 0.05), intervention=None)

    result = runner.execute_svf0_step(
        sealed=runner.SealedLearnerEvent(step=0, reveal=reveal),
        state=runner.SVF0RuntimeState(c1=_initial_base(), c2=_initial_c2(_config().replay)),
        config=_config(),
    )

    assert order[:3] == [
        ("commit", "c1_recurrent", 0),
        ("commit", "c2_recurrent_replay", 0),
        ("commit", "reset_ref", 0),
    ]
    assert order[3] == ("reveal", None, 0)
    assert [record.ticket.candidate_id for record in result.candidate_records] == [
        "c1_recurrent",
        "c2_recurrent_replay",
        "reset_ref",
    ]


def test_c2_live_update_then_bounded_replay_without_stream_divergence():
    cfg = _config()
    seeded = RecurrentGaussianState(
        weights=((0.0, 0.0, 0.0),) * 3,
        variance=(1.0, 1.0, 1.0),
        previous=(1.0, 0.0, 0.0),
        count=1,
    )
    state = runner.SVF0RuntimeState(
        c1=seeded,
        c2=RecurrentC2State(
            base=seeded,
            replay=RecurrentReplayBuffer.empty(cfg.replay),
        ),
    )
    result = runner.execute_svf0_step(
        sealed=runner.SealedLearnerEvent(
            step=1,
            reveal=lambda: LearnerEvent(step=1, channels=(0.5, 0.4, -0.2), intervention=None),
        ),
        state=state,
        config=cfg,
    )
    c1_record, c2_record, _ = result.candidate_records
    assert c1_record.outcome == c2_record.outcome == (0.5, 0.4, -0.2)
    assert len(c1_record.channel_scores) == 3
    assert len(c2_record.channel_scores) == 3
    assert math.isclose(sum(c1_record.channel_scores), c1_record.score)
    assert math.isclose(sum(c2_record.channel_scores), c2_record.score)
    assert c2_record.replay_updates == 1
    assert result.state.c1.count == 2
    assert result.state.c2.base.count == 3
    assert result.state.c2.base.previous == result.state.c1.previous == (0.5, 0.4, -0.2)


def test_reset_reference_is_stateless_and_carries_zero_durable_state():
    result = runner.execute_svf0_step(
        sealed=runner.SealedLearnerEvent(
            step=0,
            reveal=lambda: LearnerEvent(step=0, channels=(0.1, 0.2, 0.3), intervention=None),
        ),
        state=runner.SVF0RuntimeState(c1=_initial_base(), c2=_initial_c2(_config().replay)),
        config=_config(),
    )
    reset = result.candidate_records[2]
    assert reset.ticket.candidate_id == "reset_ref"
    assert reset.resources.durable_state_bytes == 0
    assert reset.replay_updates == 0


def test_resource_envelope_failure_is_recorded_not_coerced_to_success():
    cfg = _config()
    tiny = runner.SVF0RunnerConfig(
        recurrent=cfg.recurrent,
        replay=cfg.replay,
        reset_variance=cfg.reset_variance,
        envelope=FixedEnvelope(
            max_resident_memory_bytes=1,
            max_durable_state_bytes=1,
            max_update_cpu_seconds_per_event=0.000000001,
            max_query_cpu_seconds_per_event=0.000000001,
            max_shadow_auditions_per_event=0,
        ),
    )
    result = runner.execute_svf0_step(
        sealed=runner.SealedLearnerEvent(
            step=0,
            reveal=lambda: LearnerEvent(step=0, channels=(0.0, 0.0, 0.0), intervention=None),
        ),
        state=runner.SVF0RuntimeState(c1=_initial_base(), c2=_initial_c2(tiny.replay)),
        config=tiny,
    )
    assert all(record.resources.envelope_valid is False for record in result.candidate_records)
    assert any(record.resources.violations for record in result.candidate_records)


def test_reveal_step_must_match_frozen_step():
    try:
        runner.execute_svf0_step(
            sealed=runner.SealedLearnerEvent(
                step=4,
                reveal=lambda: LearnerEvent(step=5, channels=(0.0, 0.0, 0.0), intervention=None),
            ),
            state=runner.SVF0RuntimeState(c1=_initial_base(), c2=_initial_c2(_config().replay)),
            config=_config(),
        )
    except ValueError as exc:
        assert "revealed event step" in str(exc)
    else:
        raise AssertionError("mismatched revealed step was accepted")


def test_svf0_runner_rejects_intervention_packets():
    from noema.boundary import InterventionPacket
    try:
        runner.execute_svf0_step(
            sealed=runner.SealedLearnerEvent(
                step=0,
                reveal=lambda: LearnerEvent(
                    step=0,
                    channels=(0.0, 0.0, 0.0),
                    intervention=InterventionPacket(target=0, commanded_value=1.0),
                ),
            ),
            state=runner.SVF0RuntimeState(c1=_initial_base(), c2=_initial_c2(_config().replay)),
            config=_config(),
        )
    except ValueError as exc:
        assert "intervention" in str(exc)
    else:
        raise AssertionError("SVF-0 intervention packet was accepted")


def test_any_resource_failure_invalidates_the_whole_point():
    cfg = _config()
    tiny = runner.SVF0RunnerConfig(
        recurrent=cfg.recurrent,
        replay=cfg.replay,
        reset_variance=cfg.reset_variance,
        envelope=FixedEnvelope(
            max_resident_memory_bytes=1,
            max_durable_state_bytes=1,
            max_update_cpu_seconds_per_event=0.000000001,
            max_query_cpu_seconds_per_event=0.000000001,
            max_shadow_auditions_per_event=0,
        ),
    )
    result = runner.execute_svf0_step(
        sealed=runner.SealedLearnerEvent(
            step=0,
            reveal=lambda: LearnerEvent(step=0, channels=(0.0, 0.0, 0.0), intervention=None),
        ),
        state=runner.SVF0RuntimeState(c1=_initial_base(), c2=_initial_c2(tiny.replay)),
        config=tiny,
    )
    assert result.point_valid is False
    assert result.invalid_candidate_ids
