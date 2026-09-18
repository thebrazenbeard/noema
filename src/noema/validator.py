from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import json
import re
from typing import Any, Iterable, Mapping

from jsonschema import Draft202012Validator

from .provenance import ArtifactRef, DictArtifactResolver, ImplementationSubjectManifest, sha256_hex


class ValidationStatus(str, Enum):
    PASS_FROZEN_VALID = "PASS_FROZEN_VALID"
    FAIL_SCHEMA = "FAIL_SCHEMA"
    FAIL_STAGE_SEMANTICS = "FAIL_STAGE_SEMANTICS"
    FAIL_CROSS_FIELD_INVARIANT = "FAIL_CROSS_FIELD_INVARIANT"
    FAIL_SOURCE_BINDING = "FAIL_SOURCE_BINDING"
    FAIL_INFORMATION_BOUNDARY = "FAIL_INFORMATION_BOUNDARY"
    FAIL_WORLD_SCHEDULE_INTEGRITY = "FAIL_WORLD_SCHEDULE_INTEGRITY"
    FAIL_COMPARATOR_FAIRNESS = "FAIL_COMPARATOR_FAIRNESS"
    FAIL_RESOURCE_ACCOUNTING = "FAIL_RESOURCE_ACCOUNTING"
    FAIL_SUPPORT_AUDITION_CONTRACT = "FAIL_SUPPORT_AUDITION_CONTRACT"
    FAIL_LINEAGE_TRANSFER_CONTRACT = "FAIL_LINEAGE_TRANSFER_CONTRACT"
    FAIL_SCORING_CONTRACT = "FAIL_SCORING_CONTRACT"
    FAIL_RESTART_INTEGRITY = "FAIL_RESTART_INTEGRITY"
    FAIL_FREEZE_INTEGRITY = "FAIL_FREEZE_INTEGRITY"
    BLOCKED_UNAVAILABLE_EVIDENCE = "BLOCKED_UNAVAILABLE_EVIDENCE"


@dataclass(frozen=True, slots=True)
class ValidationFinding:
    code: str
    detail: str


@dataclass(frozen=True, slots=True)
class ValidationResult:
    status: ValidationStatus
    findings: tuple[ValidationFinding, ...] = ()


def _result(status: ValidationStatus, code: str, detail: str) -> ValidationResult:
    return ValidationResult(status, (ValidationFinding(code, detail),))


def _to_ref(value: Mapping[str, Any]) -> ArtifactRef:
    return ArtifactRef(
        repository=str(value["repository"]),
        commit=str(value["commit"]),
        path=str(value["path"]),
        git_blob=str(value["git_blob"]) if value.get("git_blob") is not None else None,
        sha256=str(value["sha256"]) if value.get("sha256") is not None else None,
    )


def _iter_known_artifact_values(manifest: Mapping[str, Any]) -> Iterable[Mapping[str, Any]]:
    subject = manifest.get("subject", {})
    for key in (
        "implementation_subject_manifest",
        "schema_artifact",
        "validator_artifact",
        "comparator_fairness_artifact",
        "resource_addendum_artifact",
        "decidability_addendum_artifact",
        "comparator_matrix_addendum_artifact",
        "comparator_interface_artifact",
        "supersedes_manifest",
    ):
        value = subject.get(key)
        if isinstance(value, Mapping):
            yield value

    fairness = manifest.get("comparator_fairness_contract")
    if isinstance(fairness, Mapping):
        yield fairness

    info = manifest.get("information_boundary", {})
    for key in ("learner_visible_schema", "evaluator_only_schema"):
        value = info.get(key)
        if isinstance(value, Mapping):
            yield value

    resource = manifest.get("resource_contract", {})
    measurement = resource.get("measurement_artifact")
    if isinstance(measurement, Mapping):
        yield measurement

    lineage = manifest.get("lineage_transfer_contract", {})
    policy = lineage.get("policy_artifact")
    if isinstance(policy, Mapping):
        yield policy
    for value in lineage.get("state_scope_manifest_artifacts", ()):
        if isinstance(value, Mapping):
            yield value

    world = manifest.get("world", {})
    for key in (
        "generator",
        "parameter_distribution_artifact",
        "seed_manifest_artifact",
        "negative_control_generator",
        "intervention_schedule_artifact",
    ):
        value = world.get(key)
        if isinstance(value, Mapping):
            yield value

    for candidate in manifest.get("candidates", ()):
        if isinstance(candidate, Mapping):
            for value in candidate.get("source_artifacts", ()):
                if isinstance(value, Mapping):
                    yield value


def _resolve_all(
    manifest: Mapping[str, Any],
    resolver: DictArtifactResolver,
) -> tuple[ValidationResult | None, dict[tuple[str, str, str], bytes]]:
    resolved: dict[tuple[str, str, str], bytes] = {}
    for value in _iter_known_artifact_values(manifest):
        try:
            ref = _to_ref(value)
            record = resolver.resolve(ref)
        except FileNotFoundError as exc:
            return (
                _result(
                    ValidationStatus.BLOCKED_UNAVAILABLE_EVIDENCE,
                    "artifact_unavailable",
                    str(exc),
                ),
                resolved,
            )
        except (KeyError, TypeError, ValueError) as exc:
            return (
                _result(
                    ValidationStatus.FAIL_SOURCE_BINDING,
                    "artifact_binding_invalid",
                    str(exc),
                ),
                resolved,
            )
        resolved[(ref.repository, ref.commit, ref.path)] = record.data
    return None, resolved


def _implementation_subject_result(
    manifest: Mapping[str, Any],
    resolved: Mapping[tuple[str, str, str], bytes],
) -> ValidationResult | None:
    subject = manifest.get("subject", {})
    value = subject.get("implementation_subject_manifest")
    if not isinstance(value, Mapping):
        return _result(
            ValidationStatus.FAIL_SOURCE_BINDING,
            "implementation_subject_manifest_missing",
            "implementation subject manifest must be an immutable artifact reference",
        )
    try:
        ref = _to_ref(value)
        payload = json.loads(resolved[(ref.repository, ref.commit, ref.path)].decode("utf-8"))
        implementation = ImplementationSubjectManifest(
            source_paths=tuple(payload["source_paths"]),
            test_paths=tuple(payload["test_paths"]),
            instrumentation_paths=tuple(payload["instrumentation_paths"]),
        )
    except (KeyError, TypeError, ValueError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return _result(
            ValidationStatus.FAIL_SOURCE_BINDING,
            "implementation_subject_manifest_invalid",
            str(exc),
        )
    if not implementation.is_implementation_subject():
        return _result(
            ValidationStatus.FAIL_SOURCE_BINDING,
            "design_only_subject",
            "implementation subject must bind source, tests, and instrumentation",
        )
    source_commit = subject.get("implementation_subject_commit")
    if not isinstance(source_commit, str) or len(source_commit) != 40:
        return _result(
            ValidationStatus.FAIL_SOURCE_BINDING,
            "implementation_subject_commit_invalid",
            "implementation subject commit is not exact immutable provenance",
        )
    return None


_FULL_V2 = "NOEMA_EXPERIMENT_PREREGISTRATION_MANIFEST_V2"
_RESEARCH_SUBJECT = "be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33"
_RESEARCH_REPOSITORY = "thebrazenbeard/noema"
_NORMATIVE_SUBJECT_PATHS = {
    "schema_artifact": "docs/working-design/EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V2.json",
    "validator_artifact": "docs/working-design/EXPERIMENT_PREREGISTRATION_VALIDATOR_CONTRACT_V2.md",
    "comparator_fairness_artifact": "docs/working-design/C0_C4_FAIR_COMPARISON_AND_CLAIM_BOUNDARY_MATRIX.md",
    "resource_addendum_artifact": "docs/working-design/EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_RESOURCE_ADDENDUM.md",
    "decidability_addendum_artifact": "docs/working-design/EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_DECIDABILITY_ADDENDUM.md",
    "comparator_matrix_addendum_artifact": "docs/working-design/EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_COMPARATOR_MATRIX_ADDENDUM.md",
    "comparator_interface_artifact": "docs/working-design/C2_C4_COMPARATOR_INTERFACE_CONTRACT.md",
}


def _is_full_v2(manifest: Mapping[str, Any]) -> bool:
    return manifest.get("schema_version") == _FULL_V2


def _normative_contract_binding_result(manifest: Mapping[str, Any]) -> ValidationResult | None:
    if not _is_full_v2(manifest):
        return None
    subject = manifest.get("subject")
    if not isinstance(subject, Mapping) or subject.get("design_base_commit") != _RESEARCH_SUBJECT:
        return _result(
            ValidationStatus.FAIL_SOURCE_BINDING,
            "research_subject_mismatch",
            "V2 design_base_commit must bind the reviewed PR #32 research subject",
        )
    for key, path in _NORMATIVE_SUBJECT_PATHS.items():
        value = subject.get(key)
        if not isinstance(value, Mapping):
            return _result(
                ValidationStatus.FAIL_SOURCE_BINDING,
                "normative_artifact_missing",
                f"{key} must bind the exact reviewed V2 artifact",
            )
        if (
            value.get("repository") != _RESEARCH_REPOSITORY
            or value.get("commit") != _RESEARCH_SUBJECT
            or value.get("path") != path
        ):
            return _result(
                ValidationStatus.FAIL_SOURCE_BINDING,
                "normative_artifact_tuple_mismatch",
                f"{key} does not bind the reviewed V2 artifact tuple",
            )
    fairness = manifest.get("comparator_fairness_contract")
    expected_fairness = _NORMATIVE_SUBJECT_PATHS["comparator_fairness_artifact"]
    if not isinstance(fairness, Mapping) or (
        fairness.get("repository") != _RESEARCH_REPOSITORY
        or fairness.get("commit") != _RESEARCH_SUBJECT
        or fairness.get("path") != expected_fairness
    ):
        return _result(
            ValidationStatus.FAIL_SOURCE_BINDING,
            "comparator_fairness_tuple_mismatch",
            "top-level comparator fairness contract must bind the reviewed research tuple",
        )
    return None


def _stage_semantics_result(manifest: Mapping[str, Any]) -> ValidationResult | None:
    if not _is_full_v2(manifest):
        return None
    subject = manifest.get("subject", {})
    stage = subject.get("stage")
    roles = {
        str(candidate.get("role"))
        for candidate in manifest.get("candidates", ())
        if isinstance(candidate, Mapping)
    }
    world = manifest.get("world", {})
    audition = manifest.get("audition_scope_contract", {})
    scoring = manifest.get("scoring_contract", {})
    primary_claims = tuple(scoring.get("primary_claims", ()))

    if stage == "SVF-0":
        if not {"C1", "C2"}.issubset(roles):
            return _result(
                ValidationStatus.FAIL_STAGE_SEMANTICS,
                "svf0_candidate_roles",
                "SVF-0 requires C1 and C2 candidates",
            )
        if primary_claims != ("P",):
            return _result(
                ValidationStatus.FAIL_STAGE_SEMANTICS,
                "svf0_primary_claims",
                "SVF-0 primary claims must be exactly P",
            )
        conditions = (
            scoring.get("c2_vs_c4_external_comparison_required") is False,
            world.get("intervention_mode") == "NONE",
            world.get("intervention_schedule_artifact") is None,
            world.get("intervention_schedule_commitment") is None,
            audition.get("learned_scope_primary_claim_allowed") is False,
            audition.get("simple_audition_rival_required") is False,
        )
        if not all(conditions):
            return _result(
                ValidationStatus.FAIL_STAGE_SEMANTICS,
                "svf0_stage_shape",
                "SVF-0 stage semantics do not match the frozen Gate-1 contract",
            )
        return None

    if stage == "SVF-1":
        if not {"C2", "C4"}.issubset(roles):
            return _result(
                ValidationStatus.FAIL_STAGE_SEMANTICS,
                "svf1_candidate_roles",
                "SVF-1 requires C2 and C4 candidates",
            )
        if not primary_claims or any(claim not in {"S", "T", "L", "G"} for claim in primary_claims):
            return _result(
                ValidationStatus.FAIL_STAGE_SEMANTICS,
                "svf1_primary_claims",
                "SVF-1 primary claims must be nonempty and drawn from S/T/L/G",
            )
        probability = audition.get("simple_audition_probability")
        verification = world.get("observational_equivalence_verification")
        flags = (
            "schedule_may_adapt_to_hidden_family",
            "schedule_may_adapt_to_candidate_predictions",
            "schedule_may_adapt_to_scored_outcomes",
            "schedule_may_adapt_to_evaluator_diagnostics",
        )
        conditions = (
            scoring.get("c2_vs_c4_external_comparison_required") is True,
            world.get("intervention_mode") == "EXTERNALLY_SCHEDULED",
            isinstance(world.get("intervention_schedule_artifact"), Mapping),
            isinstance(world.get("intervention_schedule_commitment"), str),
            isinstance(verification, Mapping),
            audition.get("simple_audition_rival_required") is True,
            isinstance(probability, (int, float)) and not isinstance(probability, bool) and probability > 0,
            all(world.get(flag) is False for flag in flags),
        )
        if not all(conditions):
            return _result(
                ValidationStatus.FAIL_STAGE_SEMANTICS,
                "svf1_stage_shape",
                "SVF-1 stage semantics do not match the frozen structural-value contract",
            )
        return None

    return _result(
        ValidationStatus.FAIL_STAGE_SEMANTICS,
        "unknown_stage",
        "experiment stage must be SVF-0 or SVF-1",
    )


def _resolved_json_artifact(
    value: Mapping[str, Any],
    resolved: Mapping[tuple[str, str, str], bytes],
) -> Mapping[str, Any]:
    ref = _to_ref(value)
    payload = json.loads(resolved[(ref.repository, ref.commit, ref.path)].decode("utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError("resolved artifact is not a JSON object")
    return payload


def _information_schema_closure_result(
    manifest: Mapping[str, Any],
    resolved: Mapping[tuple[str, str, str], bytes],
) -> ValidationResult | None:
    if not _is_full_v2(manifest):
        return None
    info = manifest.get("information_boundary")
    if not isinstance(info, Mapping):
        return None
    for ref_key, field_key in (
        ("learner_visible_schema", "learner_visible_field_names"),
        ("evaluator_only_schema", "evaluator_only_field_names"),
    ):
        value = info.get(ref_key)
        if not isinstance(value, Mapping):
            return _result(
                ValidationStatus.FAIL_INFORMATION_BOUNDARY,
                "transport_schema_missing",
                f"{ref_key} must be an immutable schema artifact",
            )
        try:
            schema = _resolved_json_artifact(value, resolved)
        except (KeyError, TypeError, ValueError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            return _result(
                ValidationStatus.FAIL_INFORMATION_BOUNDARY,
                "transport_schema_invalid",
                str(exc),
            )
        properties = schema.get("properties")
        if (
            schema.get("type") != "object"
            or schema.get("additionalProperties") is not False
            or not isinstance(properties, Mapping)
            or schema.get("patternProperties")
            or schema.get("unevaluatedProperties") not in (None, False)
        ):
            return _result(
                ValidationStatus.FAIL_INFORMATION_BOUNDARY,
                "transport_schema_open",
                f"{ref_key} must be a closed object schema",
            )
        declared = set(info.get(field_key, ()))
        if declared != set(properties):
            return _result(
                ValidationStatus.FAIL_INFORMATION_BOUNDARY,
                "transport_field_set_mismatch",
                f"{field_key} must exactly match the resolved schema properties",
            )
    return None


def _c1_c2_replay_isolation_result(manifest: Mapping[str, Any]) -> ValidationResult | None:
    if not _is_full_v2(manifest) or manifest.get("subject", {}).get("stage") != "SVF-0":
        return None
    candidates = {
        candidate.get("candidate_id"): candidate
        for candidate in manifest.get("candidates", ())
        if isinstance(candidate, Mapping)
    }
    c2s = [candidate for candidate in candidates.values() if candidate.get("role") == "C2"]
    for c2 in c2s:
        parent_id = c2.get("variant_of_candidate_id")
        parent = candidates.get(parent_id)
        if (
            not isinstance(parent, Mapping)
            or parent.get("role") != "C1"
            or c2.get("variant_dimension") != "REPLAY"
            or c2.get("base_substrate_id") != parent.get("base_substrate_id")
            or c2.get("source_commit") != parent.get("source_commit")
        ):
            return _result(
                ValidationStatus.FAIL_COMPARATOR_FAIRNESS,
                "c1_c2_replay_isolation",
                "SVF-0 C2 must be an explicit REPLAY variant of a C1 sharing one frozen base/source",
            )
    return None


def _resource_measurement_artifact_result(
    manifest: Mapping[str, Any],
    resolved: Mapping[tuple[str, str, str], bytes],
) -> ValidationResult | None:
    if not _is_full_v2(manifest):
        return None
    resource = manifest.get("resource_contract")
    if not isinstance(resource, Mapping):
        return None
    value = resource.get("measurement_artifact")
    if not isinstance(value, Mapping):
        return None
    try:
        artifact = _resolved_json_artifact(value, resolved)
    except (KeyError, TypeError, ValueError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return _result(
            ValidationStatus.FAIL_RESOURCE_ACCOUNTING,
            "resource_measurement_artifact_invalid",
            str(exc),
        )
    rules = artifact.get("rules")
    required_rules = {
        "cpu_clock",
        "resident_memory",
        "durable_state",
        "update_cpu",
        "query_cpu",
        "replay",
        "shared_overhead",
        "absent_feature_zero",
        "missing_measurement",
        "over_budget",
    }
    if (
        not isinstance(artifact.get("measurement_method_id"), str)
        or not artifact.get("measurement_method_id")
        or not isinstance(rules, Mapping)
        or not required_rules.issubset(rules)
    ):
        return _result(
            ValidationStatus.FAIL_RESOURCE_ACCOUNTING,
            "resource_measurement_artifact_incomplete",
            "resource measurement artifact does not close all required accounting routes",
        )
    if (
        rules.get("missing_measurement") != "INVALIDATE_FIXED_ENVELOPE_POINT"
        or rules.get("over_budget") != "INVALIDATE_FIXED_ENVELOPE_POINT"
    ):
        return _result(
            ValidationStatus.FAIL_RESOURCE_ACCOUNTING,
            "resource_measurement_fail_open",
            "missing measurements and overruns must invalidate the fixed-envelope point",
        )
    if artifact.get("envelope") != resource.get("fixed_total_envelope"):
        return _result(
            ValidationStatus.FAIL_RESOURCE_ACCOUNTING,
            "resource_envelope_mismatch",
            "measurement artifact envelope differs from the manifest fixed_total_envelope",
        )
    replay = artifact.get("replay")
    manifest_replay = resource.get("replay_limits", {})
    if not isinstance(replay, Mapping) or (
        replay.get("raw_buffer_capacity_events") != manifest_replay.get("raw_buffer_capacity_events")
        or replay.get("max_replay_updates_per_event") != manifest_replay.get("max_replay_updates_per_event")
    ):
        return _result(
            ValidationStatus.FAIL_RESOURCE_ACCOUNTING,
            "resource_replay_meter_mismatch",
            "measurement artifact replay limits differ from the manifest replay contract",
        )
    return None


def _information_boundary_result(manifest: Mapping[str, Any]) -> ValidationResult | None:
    info = manifest.get("information_boundary")
    if not isinstance(info, Mapping):
        return None
    learner = set(info.get("learner_visible_field_names", ()))
    evaluator = set(info.get("evaluator_only_field_names", ()))
    overlap = learner & evaluator
    if overlap:
        return _result(
            ValidationStatus.FAIL_INFORMATION_BOUNDARY,
            "learner_evaluator_field_overlap",
            f"learner/evaluator field sets overlap: {sorted(overlap)!r}",
        )
    forbidden = info.get("forbidden_learner_ingress", {})
    if isinstance(forbidden, Mapping) and any(value is not False for value in forbidden.values()):
        return _result(
            ValidationStatus.FAIL_INFORMATION_BOUNDARY,
            "forbidden_learner_ingress",
            "forbidden evaluator-derived learner ingress must remain false",
        )
    return None


def _world_schedule_result(manifest: Mapping[str, Any]) -> ValidationResult | None:
    world = manifest.get("world")
    if not isinstance(world, Mapping):
        return None
    if "hidden_family_randomization_rule" in world and not _is_algorithm_rule(
        world.get("hidden_family_randomization_rule")
    ):
        return _result(
            ValidationStatus.FAIL_WORLD_SCHEDULE_INTEGRITY,
            "undecidable_hidden_family_randomization",
            "hidden_family_randomization_rule is not a frozen algorithm identifier",
        )
    return None


def _cross_field_result(manifest: Mapping[str, Any]) -> ValidationResult | None:
    candidates = [c for c in manifest.get("candidates", ()) if isinstance(c, Mapping)]
    ids = [c.get("candidate_id") for c in candidates]
    if len(ids) != len(set(ids)):
        return _result(
            ValidationStatus.FAIL_CROSS_FIELD_INVARIANT,
            "duplicate_candidate_id",
            "candidate_id values must be unique",
        )

    info_id = manifest.get("information_boundary", {}).get("information_condition_id")
    opp_id = manifest.get("stream_contract", {}).get("opportunity_condition_id")
    resource = manifest.get("resource_contract", {})
    resource_id = resource.get("resource_condition_id")
    replay_id = resource.get("replay_limits", {}).get("replay_policy_id")
    scope_ids = set(manifest.get("audition_scope_contract", {}).get("scope_policy_ids", ()))

    for candidate in candidates:
        expected_pairs = (
            ("information_condition_id", info_id),
            ("opportunity_condition_id", opp_id),
            ("resource_condition_id", resource_id),
            ("replay_policy_id", replay_id),
        )
        for key, expected in expected_pairs:
            if expected is not None and candidate.get(key) != expected:
                return _result(
                    ValidationStatus.FAIL_CROSS_FIELD_INVARIANT,
                    "candidate_condition_mismatch",
                    f"candidate {candidate.get('candidate_id')!r} {key} does not resolve to top-level condition",
                )
        if scope_ids and candidate.get("scope_policy_id") not in scope_ids:
            return _result(
                ValidationStatus.FAIL_CROSS_FIELD_INVARIANT,
                "candidate_scope_policy_unresolved",
                f"candidate {candidate.get('candidate_id')!r} scope_policy_id is not frozen",
            )
        parent_id = candidate.get("variant_of_candidate_id")
        if parent_id is not None:
            if parent_id == candidate.get("candidate_id"):
                return _result(
                    ValidationStatus.FAIL_CROSS_FIELD_INVARIANT,
                    "candidate_variant_self_reference",
                    f"candidate {candidate.get('candidate_id')!r} cannot be its own variant parent",
                )
            if parent_id not in set(ids):
                return _result(
                    ValidationStatus.FAIL_CROSS_FIELD_INVARIANT,
                    "candidate_variant_parent_unresolved",
                    f"candidate {candidate.get('candidate_id')!r} variant parent does not resolve",
                )

    scoring = manifest.get("scoring_contract")
    if isinstance(scoring, Mapping):
        primary_claims = set(scoring.get("primary_claims", ()))
        metrics = [m for m in scoring.get("primary_metrics", ()) if isinstance(m, Mapping)]
        metric_ids = [m.get("metric_id") for m in metrics]
        if len(metric_ids) != len(set(metric_ids)):
            return _result(
                ValidationStatus.FAIL_CROSS_FIELD_INVARIANT,
                "duplicate_metric_id",
                "metric_id values must be unique",
            )
        candidate_ids = set(ids)
        for metric in metrics:
            if metric.get("claim") not in primary_claims:
                return _result(
                    ValidationStatus.FAIL_CROSS_FIELD_INVARIANT,
                    "metric_claim_not_primary",
                    f"metric {metric.get('metric_id')!r} claim is not in primary_claims",
                )
            if metric.get("comparator_candidate_id") not in candidate_ids:
                return _result(
                    ValidationStatus.FAIL_CROSS_FIELD_INVARIANT,
                    "metric_comparator_unresolved",
                    f"metric {metric.get('metric_id')!r} comparator does not resolve to a frozen candidate",
                )

    stage = manifest.get("subject", {}).get("stage")
    by_role: dict[str, list[Mapping[str, Any]]] = {}
    for candidate in candidates:
        by_role.setdefault(str(candidate.get("role")), []).append(candidate)
    if stage == "SVF-1" and by_role.get("C2") and by_role.get("C4"):
        c2 = by_role["C2"][0]
        c4 = by_role["C4"][0]
        if c2.get("base_substrate_id") != c4.get("base_substrate_id"):
            return _result(
                ValidationStatus.FAIL_CROSS_FIELD_INVARIANT,
                "c2_c4_base_substrate_mismatch",
                "primary C2/C4 comparison must share one declared base substrate",
            )
    return None


_FIRST_CORE_SVF0_ID = "NOEMA_SVF0_RECURRENT_GATE1_V3"
_FIRST_CORE_SVF0_METRICS = {
    "P_C1_VS_RESET_LATE_POST": {
        "claim": "P",
        "direction": "LOWER_IS_BETTER",
        "comparator_candidate_id": "reset_ref",
        "aggregation_rule": "algo:mean_seed_window_delta@v1",
        "threshold_rule": "expr:mean_nll_delta<=-0.02&&upper_ci_delta<0",
        "support_requirement": "expr:scored_count==expected_count&&worlds_completed==maximum_worlds&&resource_accounting_complete==true",
    },
    "P_C2_VS_RESET_LATE_POST": {
        "claim": "P",
        "direction": "LOWER_IS_BETTER",
        "comparator_candidate_id": "reset_ref",
        "aggregation_rule": "algo:mean_seed_window_delta@v1",
        "threshold_rule": "expr:mean_nll_delta<=-0.02&&upper_ci_delta<0",
        "support_requirement": "expr:scored_count==expected_count&&worlds_completed==maximum_worlds&&resource_accounting_complete==true",
    },
}


def _first_core_svf0_metric_result(manifest: Mapping[str, Any]) -> ValidationResult | None:
    subject = manifest.get("subject", {})
    if subject.get("manifest_logical_id") != _FIRST_CORE_SVF0_ID:
        return None
    if subject.get("stage") != "SVF-0":
        return _result(
            ValidationStatus.FAIL_SCORING_CONTRACT,
            "first_core_profile_wrong_stage",
            "first-core recurrent Gate-1 profile is defined only for SVF-0",
        )
    candidates = {
        candidate.get("candidate_id"): candidate
        for candidate in manifest.get("candidates", ())
        if isinstance(candidate, Mapping)
    }
    required_roles = {
        "c1_recurrent": ("C1", True),
        "c2_recurrent_replay": ("C2", True),
        "reset_ref": ("REFERENCE", False),
    }
    for candidate_id, (role, eligible) in required_roles.items():
        candidate = candidates.get(candidate_id)
        if (
            not isinstance(candidate, Mapping)
            or candidate.get("role") != role
            or candidate.get("developmental_evidence_eligible") is not eligible
        ):
            return _result(
                ValidationStatus.FAIL_SCORING_CONTRACT,
                "first_core_candidate_profile",
                f"{candidate_id} does not match the frozen first-core candidate role",
            )
    scoring = manifest.get("scoring_contract", {})
    metrics = scoring.get("primary_metrics", ())
    by_id = {
        metric.get("metric_id"): metric
        for metric in metrics
        if isinstance(metric, Mapping)
    }
    if set(by_id) != set(_FIRST_CORE_SVF0_METRICS):
        return _result(
            ValidationStatus.FAIL_SCORING_CONTRACT,
            "first_core_metric_set",
            "first-core SVF-0 primary metric set differs from the frozen profile",
        )
    for metric_id, expected in _FIRST_CORE_SVF0_METRICS.items():
        metric = by_id[metric_id]
        if any(metric.get(key) != value for key, value in expected.items()):
            return _result(
                ValidationStatus.FAIL_SCORING_CONTRACT,
                "first_core_metric_semantics",
                f"{metric_id} differs from the frozen first-core metric semantics",
            )
    return None


def _resource_result(manifest: Mapping[str, Any]) -> ValidationResult | None:
    resource = manifest.get("resource_contract")
    if not isinstance(resource, Mapping):
        return None
    if not isinstance(resource.get("measurement_artifact"), Mapping):
        return _result(
            ValidationStatus.FAIL_RESOURCE_ACCOUNTING,
            "resource_measurement_unbound",
            "resource measurement must be an immutable artifact",
        )
    if "measurement_method" in resource and not _is_algorithm_rule(resource.get("measurement_method")):
        return _result(
            ValidationStatus.FAIL_RESOURCE_ACCOUNTING,
            "undecidable_resource_measurement_method",
            "resource measurement_method is not a frozen algorithm identifier",
        )
    restart = manifest.get("restart_contract")
    scoring = manifest.get("scoring_contract")
    has_primary_claim = isinstance(scoring, Mapping) and bool(scoring.get("primary_claims"))
    if isinstance(restart, Mapping) and restart.get("checkpointing_used") is True and has_primary_claim:
        return _result(
            ValidationStatus.FAIL_RESOURCE_ACCOUNTING,
            "checkpointed_primary_v2",
            "V2 primary fixed-envelope evidence cannot use checkpointing without an explicit checkpoint resource axis",
        )
    return None


_EXPR_TERM = re.compile(
    r"^[a-z][a-z0-9_]*(?:<=|>=|==|!=|<|>)(?:-?\d+(?:\.\d+)?|true|false|[a-z][a-z0-9_]*)$"
)
_ALGO_RULE = re.compile(r"^algo:[a-z][a-z0-9_]*@v[1-9][0-9]*(?::[a-z0-9_.=,-]+)?$")


def _normalized_rule(value: object) -> str:
    return " ".join(str(value).strip().lower().split())


def _is_expression_rule(value: object) -> bool:
    rule = _normalized_rule(value)
    if not rule.startswith("expr:"):
        return False
    terms = rule[5:].replace(" ", "").split("&&")
    return bool(terms) and all(_EXPR_TERM.fullmatch(term) for term in terms)


def _is_algorithm_rule(value: object) -> bool:
    return bool(_ALGO_RULE.fullmatch(_normalized_rule(value).replace(" ", "")))


def _scoring_decidability_result(manifest: Mapping[str, Any]) -> ValidationResult | None:
    scoring = manifest.get("scoring_contract")
    if isinstance(scoring, Mapping):
        if "proper_scoring_rule" in scoring and not _is_algorithm_rule(scoring.get("proper_scoring_rule")):
            return _result(
                ValidationStatus.FAIL_SCORING_CONTRACT,
                "undecidable_proper_scoring_rule",
                "proper_scoring_rule is not a frozen algorithm identifier",
            )
        for metric in scoring.get("primary_metrics", ()):
            if not isinstance(metric, Mapping):
                continue
            metric_id = metric.get("metric_id")
            aggregation = metric.get("aggregation_rule")
            if aggregation is not None and not _is_algorithm_rule(aggregation):
                return _result(
                    ValidationStatus.FAIL_SCORING_CONTRACT,
                    "undecidable_primary_aggregation",
                    f"primary metric {metric_id!r} aggregation_rule is not a frozen algorithm identifier",
                )
            for key in ("threshold_rule", "support_requirement"):
                if key in metric and not _is_expression_rule(metric.get(key)):
                    return _result(
                        ValidationStatus.FAIL_SCORING_CONTRACT,
                        "undecidable_primary_rule",
                        f"primary metric {metric_id!r} {key} is not a mechanically decidable expression",
                    )

    world = manifest.get("world")
    if isinstance(world, Mapping) and "negative_control_acceptance_rule" in world:
        if not _is_expression_rule(world.get("negative_control_acceptance_rule")):
            return _result(
                ValidationStatus.FAIL_SCORING_CONTRACT,
                "undecidable_negative_control_rule",
                "negative-control acceptance rule is not a mechanically decidable expression",
            )

    statistics = manifest.get("statistics_contract")
    if isinstance(statistics, Mapping):
        for key in ("uncertainty_method", "multiple_comparison_rule"):
            if key in statistics and not _is_algorithm_rule(statistics.get(key)):
                return _result(
                    ValidationStatus.FAIL_SCORING_CONTRACT,
                    "undecidable_statistics_algorithm",
                    f"{key} is not a frozen algorithm identifier",
                )
        if "stopping_rule" in statistics and not _is_expression_rule(statistics.get("stopping_rule")):
            return _result(
                ValidationStatus.FAIL_SCORING_CONTRACT,
                "undecidable_stopping_rule",
                "stopping_rule is not a mechanically decidable expression",
            )
        for criterion in statistics.get("kill_criteria", ()):
            if not _is_expression_rule(criterion):
                return _result(
                    ValidationStatus.FAIL_SCORING_CONTRACT,
                    "undecidable_kill_criterion",
                    "kill criteria must be mechanically decidable expressions",
                )
    return None


def _lineage_result(manifest: Mapping[str, Any]) -> ValidationResult | None:
    lineage = manifest.get("lineage_transfer_contract")
    if not isinstance(lineage, Mapping):
        return None
    artifacts = lineage.get("state_scope_manifest_artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        return _result(
            ValidationStatus.FAIL_LINEAGE_TRANSFER_CONTRACT,
            "state_scope_manifest_unbound",
            "lineage state scope must be bound by at least one immutable artifact",
        )
    return None


def _candidate_source_binding_result(
    manifest: Mapping[str, Any],
    resolved: Mapping[tuple[str, str, str], bytes],
) -> ValidationResult | None:
    subject = manifest.get("subject", {})
    ref_value = subject.get("implementation_subject_manifest")
    if not isinstance(ref_value, Mapping):
        return None
    try:
        ref = _to_ref(ref_value)
        payload = json.loads(resolved[(ref.repository, ref.commit, ref.path)].decode("utf-8"))
        bound_commit = payload["source_commit"]
        source_paths = set(payload["source_paths"])
    except (KeyError, TypeError, ValueError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return _result(
            ValidationStatus.FAIL_SOURCE_BINDING,
            "implementation_source_manifest_binding_invalid",
            str(exc),
        )
    subject_commit = subject.get("implementation_subject_commit")
    if bound_commit != subject_commit:
        return _result(
            ValidationStatus.FAIL_SOURCE_BINDING,
            "implementation_subject_commit_mismatch",
            "implementation-subject manifest source_commit must equal subject implementation_subject_commit",
        )
    for candidate in manifest.get("candidates", ()):
        if not isinstance(candidate, Mapping):
            continue
        role = candidate.get("role")
        developmental = role in {"C0", "C1", "C2", "C3", "C4"} or candidate.get("developmental_evidence_eligible") is True
        if not developmental:
            continue
        if candidate.get("source_commit") != subject_commit:
            return _result(
                ValidationStatus.FAIL_SOURCE_BINDING,
                "candidate_source_commit_mismatch",
                f"candidate {candidate.get('candidate_id')!r} source_commit differs from implementation subject",
            )
        for artifact in candidate.get("source_artifacts", ()):
            if not isinstance(artifact, Mapping):
                continue
            if artifact.get("commit") != subject_commit or artifact.get("path") not in source_paths:
                return _result(
                    ValidationStatus.FAIL_SOURCE_BINDING,
                    "candidate_source_artifact_outside_subject",
                    f"candidate {candidate.get('candidate_id')!r} source artifact is outside frozen implementation subject",
                )
    return None


def _commitment_integrity_result(
    manifest: Mapping[str, Any],
    resolved: Mapping[tuple[str, str, str], bytes],
) -> ValidationResult | None:
    world = manifest.get("world")
    if not isinstance(world, Mapping):
        return None
    pairs = (
        ("parameter_distribution_artifact", "parameter_distribution_commitment"),
        ("seed_manifest_artifact", "seed_commitment"),
        ("intervention_schedule_artifact", "intervention_schedule_commitment"),
    )
    for artifact_key, commitment_key in pairs:
        artifact = world.get(artifact_key)
        commitment = world.get(commitment_key)
        if commitment is None:
            continue
        if not isinstance(artifact, Mapping):
            return _result(
                ValidationStatus.FAIL_FREEZE_INTEGRITY,
                "commitment_without_artifact",
                f"{commitment_key} exists without immutable {artifact_key}",
            )
        try:
            ref = _to_ref(artifact)
            actual = sha256_hex(resolved[(ref.repository, ref.commit, ref.path)])
        except (KeyError, TypeError, ValueError) as exc:
            return _result(ValidationStatus.FAIL_FREEZE_INTEGRITY, "commitment_artifact_invalid", str(exc))
        if actual != commitment:
            return _result(
                ValidationStatus.FAIL_FREEZE_INTEGRITY,
                "commitment_preimage_mismatch",
                f"{commitment_key} does not match resolved {artifact_key} bytes",
            )
    return None


def validate_manifest(
    manifest: Mapping[str, Any],
    schema: Mapping[str, Any],
    resolver: DictArtifactResolver,
) -> ValidationResult:
    schema_errors = sorted(
        Draft202012Validator(schema).iter_errors(manifest),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    if schema_errors:
        return _result(
            ValidationStatus.FAIL_SCHEMA,
            "schema",
            schema_errors[0].message,
        )

    resolution_result, resolved = _resolve_all(manifest, resolver)
    if resolution_result is not None:
        return resolution_result

    for check in (
        lambda: _implementation_subject_result(manifest, resolved),
        lambda: _normative_contract_binding_result(manifest),
        lambda: _stage_semantics_result(manifest),
        lambda: _candidate_source_binding_result(manifest, resolved),
        lambda: _commitment_integrity_result(manifest, resolved),
        lambda: _information_boundary_result(manifest),
        lambda: _information_schema_closure_result(manifest, resolved),
        lambda: _world_schedule_result(manifest),
        lambda: _cross_field_result(manifest),
        lambda: _c1_c2_replay_isolation_result(manifest),
        lambda: _first_core_svf0_metric_result(manifest),
        lambda: _scoring_decidability_result(manifest),
        lambda: _resource_result(manifest),
        lambda: _resource_measurement_artifact_result(manifest, resolved),
        lambda: _lineage_result(manifest),
    ):
        result = check()
        if result is not None:
            return result

    return ValidationResult(ValidationStatus.PASS_FROZEN_VALID)
