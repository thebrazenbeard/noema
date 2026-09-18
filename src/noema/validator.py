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
    r"^[a-z][a-z0-9_]*(?:<=|>=|==|!=|<|>)(?:-?\\d+(?:\\.\\d+)?|true|false|[a-z][a-z0-9_]*)$"
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
        lambda: _candidate_source_binding_result(manifest, resolved),
        lambda: _commitment_integrity_result(manifest, resolved),
        lambda: _information_boundary_result(manifest),
        lambda: _cross_field_result(manifest),
        lambda: _scoring_decidability_result(manifest),
        lambda: _resource_result(manifest),
        lambda: _lineage_result(manifest),
    ):
        result = check()
        if result is not None:
            return result

    return ValidationResult(ValidationStatus.PASS_FROZEN_VALID)
