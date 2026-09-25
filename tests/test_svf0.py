import math

from noema.svf0 import SVF0WorldConfig, gaussian_nll, svf0_point


def test_svf0_point_generation_is_deterministic_for_seed_and_step():
    config = SVF0WorldConfig(
        change_point=5,
        coefficient_before=0.75,
        coefficient_after=-0.25,
        stable_coefficient=0.5,
        noise_half_width=0.1,
    )
    assert svf0_point(seed=17, step=3, config=config) == svf0_point(seed=17, step=3, config=config)


def test_svf0_regime_change_is_exactly_at_preregistered_step():
    config = SVF0WorldConfig(5, 0.75, -0.25, 0.5, 0.0)
    before = svf0_point(seed=11, step=4, config=config)
    after = svf0_point(seed=11, step=5, config=config)
    assert before.changed_coefficient == 0.75
    assert after.changed_coefficient == -0.25


def test_unrelated_dependency_coefficient_remains_stable_across_regime_change():
    config = SVF0WorldConfig(2, 0.8, -0.4, 0.3, 0.0)
    before = svf0_point(seed=23, step=1, config=config)
    after = svf0_point(seed=23, step=2, config=config)
    assert before.stable_coefficient == 0.3
    assert after.stable_coefficient == 0.3


def test_learner_visible_point_contains_only_opaque_numeric_channels():
    config = SVF0WorldConfig(2, 0.8, -0.4, 0.3, 0.0)
    point = svf0_point(seed=7, step=0, config=config)
    event = point.learner_event
    assert event.step == 0
    assert len(event.channels) == 3
    assert event.intervention is None
    assert not hasattr(event, "regime")
    assert not hasattr(event, "changed_coefficient")
    assert not hasattr(event, "stable_coefficient")


def test_gaussian_nll_matches_standard_unit_normal_at_mean():
    score = gaussian_nll(outcome=(0.0,), mean=(0.0,), variance=(1.0,))
    assert math.isclose(score, 0.5 * math.log(2.0 * math.pi), rel_tol=0.0, abs_tol=1e-12)


def test_gaussian_nll_rejects_dimension_mismatch():
    try:
        gaussian_nll(outcome=(0.0, 1.0), mean=(0.0,), variance=(1.0,))
    except ValueError as exc:
        assert "dimension" in str(exc).lower()
    else:
        raise AssertionError("dimension mismatch accepted")


def test_negative_control_has_no_regime_change_and_is_deterministic():
    from noema.svf0 import SVF0NegativeControlConfig, svf0_negative_control_point
    config = SVF0NegativeControlConfig(coefficient=0.4, stable_coefficient=-0.2, noise_half_width=0.05)
    early = svf0_negative_control_point(seed=31, step=1, config=config)
    late = svf0_negative_control_point(seed=31, step=99, config=config)
    assert early.changed_coefficient == 0.4
    assert late.changed_coefficient == 0.4
    assert svf0_negative_control_point(seed=31, step=99, config=config) == late


def test_svf0_dependencies_are_one_step_lagged_and_preoutcome_predictable():
    config = SVF0WorldConfig(5, 0.75, -0.25, 0.5, 0.0)
    previous = svf0_point(seed=19, step=2, config=config)
    current = svf0_point(seed=19, step=3, config=config)
    previous_driver = previous.learner_event.channels[0]
    assert current.learner_event.channels[1] == 0.75 * previous_driver
    assert current.learner_event.channels[2] == 0.5 * previous_driver


def test_svf0_changed_dependency_switches_on_outcome_step_without_changing_stable_dependency():
    config = SVF0WorldConfig(5, 0.75, -0.25, 0.5, 0.0)
    previous = svf0_point(seed=29, step=4, config=config)
    current = svf0_point(seed=29, step=5, config=config)
    previous_driver = previous.learner_event.channels[0]
    assert current.learner_event.channels[1] == -0.25 * previous_driver
    assert current.learner_event.channels[2] == 0.5 * previous_driver
