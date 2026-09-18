import math

from noema.svf0_statistics import (
    FROZEN_WINDOWS,
    Gate1MetricResult,
    holm_bonferroni,
    mean_seed_window_delta,
    primary_persistence_result,
    student_t_ci_n8,
    student_t_two_sided_p_df7,
    student_t_two_sided_p_n8,
    gate1_kill_required,
)


def test_frozen_score_windows_match_preregistered_ranges():
    assert FROZEN_WINDOWS["warmup_excluded"] == (0, 15)
    assert FROZEN_WINDOWS["pre_change"] == (16, 63)
    assert FROZEN_WINDOWS["early_post_change"] == (64, 79)
    assert FROZEN_WINDOWS["late_post_change"] == (96, 127)
    assert FROZEN_WINDOWS["negative_control_score"] == (16, 127)


def test_mean_seed_window_delta_is_target_minus_comparator_and_complete():
    target = (1.0, 2.0, 3.0, 4.0)
    comparator = (2.0, 2.0, 4.0, 6.0)
    result = mean_seed_window_delta(target, comparator)
    assert result == -1.0


def test_mean_seed_window_delta_rejects_missing_or_mismatched_scores():
    for target, comparator in [
        ((), ()),
        ((1.0,), (1.0, 2.0)),
        ((1.0, math.nan), (1.0, 2.0)),
    ]:
        try:
            mean_seed_window_delta(target, comparator)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid score window was accepted")


def test_student_t_ci_n8_uses_frozen_df7_critical_value():
    values = (-0.08, -0.06, -0.05, -0.04, -0.03, -0.02, -0.01, 0.0)
    ci = student_t_ci_n8(values)
    mean = sum(values) / 8
    assert ci.mean == mean
    assert ci.lower < mean < ci.upper
    assert math.isclose(ci.critical_value, 2.364624251)


def test_primary_persistence_requires_effect_ci_and_support_completeness():
    passing = primary_persistence_result(
        seed_deltas=(-0.08, -0.07, -0.06, -0.05, -0.05, -0.04, -0.03, -0.03),
        scored_count=256,
        expected_count=256,
        worlds_completed=8,
        maximum_worlds=8,
        resource_accounting_complete=True,
    )
    assert passing.threshold_pass is True
    assert passing.support_pass is True
    assert passing.pass_gate is True

    incomplete = primary_persistence_result(
        seed_deltas=(-0.08, -0.07, -0.06, -0.05, -0.05, -0.04, -0.03, -0.03),
        scored_count=255,
        expected_count=256,
        worlds_completed=8,
        maximum_worlds=8,
        resource_accounting_complete=True,
    )
    assert incomplete.threshold_pass is True
    assert incomplete.support_pass is False
    assert incomplete.pass_gate is False


def test_holm_bonferroni_is_deterministic_and_monotone():
    decisions = holm_bonferroni(
        {"a": 0.001, "b": 0.02, "c": 0.2},
        alpha=0.05,
    )
    assert decisions == {"a": True, "b": True, "c": False}


def test_gate1_kill_triggers_if_any_required_pass_is_false():
    assert gate1_kill_required(
        c1_persistence_pass=True,
        c2_persistence_pass=True,
        c1_changed_dependency_adaptation_pass=True,
        c1_stable_dependency_retention_pass=True,
        c2_changed_dependency_adaptation_pass=True,
        c2_stable_dependency_retention_pass=True,
    ) is False
    assert gate1_kill_required(
        c1_persistence_pass=True,
        c2_persistence_pass=False,
        c1_changed_dependency_adaptation_pass=True,
        c1_stable_dependency_retention_pass=True,
        c2_changed_dependency_adaptation_pass=True,
        c2_stable_dependency_retention_pass=True,
    ) is True


def test_student_t_two_sided_df7_matches_frozen_reference_points():
    assert math.isclose(
        student_t_two_sided_p_df7(2.364624251),
        0.05,
        rel_tol=0.0,
        abs_tol=1e-9,
    )
    assert math.isclose(
        student_t_two_sided_p_df7(3.0),
        0.019942126131992536,
        rel_tol=0.0,
        abs_tol=1e-12,
    )


def test_student_t_two_sided_n8_matches_explicit_t_statistic():
    values = (-0.08, -0.07, -0.06, -0.05, -0.04, -0.03, -0.02, -0.01)
    mean = sum(values) / 8
    sample_sd = math.sqrt(sum((value - mean) ** 2 for value in values) / 7)
    t_statistic = mean / (sample_sd / math.sqrt(8.0))
    assert math.isclose(
        student_t_two_sided_p_n8(values),
        student_t_two_sided_p_df7(t_statistic),
        rel_tol=0.0,
        abs_tol=1e-15,
    )
