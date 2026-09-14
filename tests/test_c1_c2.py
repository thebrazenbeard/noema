from noema.candidates import GaussianState, C1Config, ReplayBuffer, ReplayConfig, predict_gaussian, transition_c1


def test_c1_prediction_reads_only_committed_state():
    state = GaussianState(mean=(1.0, -1.0), variance=(2.0, 3.0), count=5)
    prediction = predict_gaussian(state)
    assert prediction.mean == state.mean
    assert prediction.variance == state.variance


def test_c1_one_step_transition_is_pure_and_bounded():
    state = GaussianState(mean=(0.0,), variance=(1.0,), count=0)
    updated = transition_c1(state, (2.0,), C1Config(alpha=0.25, variance_floor=0.01))
    assert state.mean == (0.0,)
    assert updated.mean == (0.5,)
    assert updated.count == 1
    assert updated.variance[0] >= 0.01


def test_replay_buffer_never_exceeds_capacity():
    buf = ReplayBuffer.empty(ReplayConfig(capacity=2, max_replay_updates_per_event=1))
    buf = buf.append((1.0,)).append((2.0,)).append((3.0,))
    assert buf.items == ((2.0,), (3.0,))


def test_c2_one_step_uses_same_c1_kernel_and_appends_raw_replay():
    from noema.candidates import C2State, transition_c2_once
    c1 = C1Config(alpha=0.25, variance_floor=0.01)
    replay = ReplayConfig(capacity=2, max_replay_updates_per_event=1)
    state = C2State(
        base=GaussianState(mean=(0.0,), variance=(1.0,), count=0),
        replay=ReplayBuffer.empty(replay),
    )
    updated = transition_c2_once(state, (2.0,), c1, replay)
    assert updated.base.mean == (0.5,)
    assert updated.replay.items == ((2.0,),)


def test_c2_replay_update_is_explicit_and_bounded_by_preregistered_indices():
    from noema.candidates import C2State, transition_c2_replay
    c1 = C1Config(alpha=0.5, variance_floor=0.01)
    replay = ReplayConfig(capacity=3, max_replay_updates_per_event=1)
    state = C2State(
        base=GaussianState(mean=(0.0,), variance=(1.0,), count=0),
        replay=ReplayBuffer.empty(replay).append((2.0,)).append((4.0,)),
    )
    updated = transition_c2_replay(state, replay_indices=(1,), c1_config=c1, replay_config=replay)
    assert updated.base.mean == (2.0,)
    try:
        transition_c2_replay(state, replay_indices=(0, 1), c1_config=c1, replay_config=replay)
    except ValueError as exc:
        assert "max_replay_updates_per_event" in str(exc)
    else:
        raise AssertionError("replay update limit bypassed")
