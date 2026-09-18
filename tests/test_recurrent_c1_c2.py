from noema.candidates import (
    RecurrentConfig,
    RecurrentGaussianState,
    RecurrentReplayBuffer,
    RecurrentReplayConfig,
    RecurrentC2State,
    predict_recurrent,
    transition_recurrent,
    transition_recurrent_c2_once,
    transition_recurrent_c2_replay,
)


def initial_state(dimension: int = 2) -> RecurrentGaussianState:
    return RecurrentGaussianState.zeros(
        dimension=dimension,
        initial_variance=1.0,
    )


def test_recurrent_prediction_uses_only_previous_committed_observation():
    state = RecurrentGaussianState(
        weights=((2.0, 0.0), (0.0, -1.0)),
        variance=(1.0, 1.0),
        previous=(3.0, 4.0),
        count=5,
    )
    pred = predict_recurrent(state)
    assert pred.mean == (6.0, -4.0)
    assert pred.variance == (1.0, 1.0)


def test_first_observation_only_establishes_recurrent_context():
    state = initial_state()
    updated = transition_recurrent(
        state,
        (1.0, 2.0),
        RecurrentConfig(learning_rate=0.5, variance_alpha=0.25, variance_floor=0.01),
    )
    assert updated.previous == (1.0, 2.0)
    assert updated.weights == state.weights
    assert updated.count == 1


def test_second_observation_updates_conditional_weights_from_prior_context():
    config = RecurrentConfig(learning_rate=0.5, variance_alpha=0.25, variance_floor=0.01)
    state = transition_recurrent(initial_state(), (1.0, 0.0), config)
    updated = transition_recurrent(state, (2.0, -1.0), config)
    assert updated.weights[0] == (1.0, 0.0)
    assert updated.weights[1] == (-0.5, 0.0)
    assert updated.previous == (2.0, -1.0)


def test_recurrent_c2_live_transition_matches_c1_and_stores_raw_transition_pair():
    config = RecurrentConfig(learning_rate=0.5, variance_alpha=0.25, variance_floor=0.01)
    replay_config = RecurrentReplayConfig(capacity=2, max_replay_updates_per_event=1)
    state = RecurrentC2State(
        base=initial_state(),
        replay=RecurrentReplayBuffer.empty(replay_config),
    )
    state = transition_recurrent_c2_once(state, (1.0, 0.0), config, replay_config)
    updated = transition_recurrent_c2_once(state, (2.0, -1.0), config, replay_config)
    c1_updated = transition_recurrent(state.base, (2.0, -1.0), config)
    assert updated.base == c1_updated
    assert len(updated.replay.items) == 1
    assert updated.replay.items[0].context == (1.0, 0.0)
    assert updated.replay.items[0].outcome == (2.0, -1.0)


def test_recurrent_replay_update_is_bounded_and_does_not_change_live_context():
    config = RecurrentConfig(learning_rate=0.5, variance_alpha=0.25, variance_floor=0.01)
    replay_config = RecurrentReplayConfig(capacity=2, max_replay_updates_per_event=1)
    state = RecurrentC2State(
        base=RecurrentGaussianState(
            weights=((0.0,),),
            variance=(1.0,),
            previous=(9.0,),
            count=2,
        ),
        replay=RecurrentReplayBuffer.empty(replay_config).append(
            context=(2.0,),
            outcome=(4.0,),
        ),
    )
    updated = transition_recurrent_c2_replay(
        state,
        replay_indices=(0,),
        config=config,
        replay_config=replay_config,
    )
    assert updated.base.weights == ((4.0,),)
    assert updated.base.previous == (9.0,)
    try:
        transition_recurrent_c2_replay(
            state,
            replay_indices=(0, 0),
            config=config,
            replay_config=replay_config,
        )
    except ValueError as exc:
        assert "max_replay_updates_per_event" in str(exc)
    else:
        raise AssertionError("recurrent replay limit bypassed")
