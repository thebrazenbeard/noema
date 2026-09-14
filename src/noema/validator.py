from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import json
from typing import Any, Iterable, Mapping

from jsonschema import Draft202012Validator

from .provenance import ArtifactRef, DictArtifactResolver, ImplementationSubjectManifest


class ValidationStatus(str, Enum):
    PASS_FROZEN_VALID = "PASS_FROZEN_VALID"
    FAIL_SCHEMA = "FAIL_SCHEMA"
    FAIL_CROSS_FIELD_INVARIANT = "FAIL_CROSS_FIELD_INVARIANT"
    FAIL_SOURCE_BINDING = "FAIL_SOURCE_BINDING"
    FAIL_INFORMATION_BOUNDARY = "FAIL_INFORMATION_BOUNDARY"
    FAIL_RESOURCE_ACCOUNTING = "FAIL_RESOURCE_ACCOUNTING"
    FAIL_SUPPORT_AUDITION_CONTRACT = "FAIL_SUPPORT_AUDITION_CONTRACT"
    FAIL_LINEAGE_TRANSFER_CONTRACT = "FAIL_LINEAGE_TRANSFER_CONTRACT"
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
            return (_result(ValidationStatus.BLOCKED_UNAVAILABLE_EVIDENCE, "artifact_unavailable", str(exc)), resolved)
        except (KeyError, TypeError, ValueError) as exc:
            return (_result(ValidationStatus.FAIL_SOURCE_BINDING, "artifact_binding_invalid", str(exc)), resolved)
        resolved[(ref.repository, ref.commit, ref.path)] = record.data
    return None, resolved


def _implementation_subject_result(manifest: Mapping[str, Any], resolved: Mapping[tuple[str, str, str], bytes]) -> ValidationResult | None:
    subject = manifest.get("subject", {})
    value = subject.get("implementation_subject_manifest")
    if not isinstance(value, Mapping):
        return _result(ValidationStatus.FAIL_SOURCE_BINDING, "implementation_subject_manifest_missing", "implementation subject manifest must be an immutable artifact reference")
    try:
        ref = _to_ref(value)
        payload = json.loads(resolved[(ref.repository, ref.commit, ref.path)].decode("utf-8"))
        implementation = ImplementationSubjectManifest(
            source_paths=tuple(payload["source_paths"]),
            test_paths=tuple(payload["test_paths"]),
            instrumentation_paths=tuple(payload["instrumentation_paths"]),
        )
    except (KeyError, TypeError, ValueError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return _result(ValidationStatus.FAIL_SOURCE_BINDING, "implementation_subject_manifest_invalid", str(exc))
    if not implementation.is_implementation_subject():
        return _result(ValidationStatus.FAIL_SOURCE_BINDING, "design_only_subject", "implementation subject must bind source, tests, and instrumentation")
    source_commit = subject.get("implementation_subject_commit")
    if not isinstance(source_commit, str) or len(source_commit) != 40:
        return _result(ValidationStatus.FAIL_SOURCE_BINDING, "implementation_subject_commit_invalid", "implementation subject commit is not exact immutable provenance")
    return None


def _information_boundary_result(manifest: Mapping[str, Any]) -> ValidationResult | None:
    info = manifest.get("information_boundary")
    if not isinstance(info, Mapping):
        return None
    learner = set(info.get("learner_visible_field_names", ()))
    evaluator = set(info.get("evaluator_only_field_names", ()))
    overlap = learner & evaluator
    if overlap:
        return _result(ValidationStatus.FAIL_INFORMATION_BOUNDARY, "learner_evaluator_field_overlap", f"learner/evaluator field sets overlap: {sorted(overlap)!r}")
    forbidden = info.get("forbidden_learner_ingress", {})
    if isinstance(forbidden, Mapping) and any(value is not False for value in forbidden.values()):
        return _result(ValidationStatus.FAIL_INFORMATION_BOUNDARY, "forbidden_learner_ingress", "forbidden evaluator-derived learner ingress must remain false")
    return None


def _cross_field_result(manifest: Mapping[str, Any]) -> ValidationResult | None:
    candidates = [c for c in manifest.get("candidates", ()) if isinstance(c, Mapping)]
    ids = [c.get("candidate_id") for c in candidates]
    if len(ids) != len(set(ids)):
        return _result(ValidationStatus.FAIL_CROSS_FIELD_INVARIANT, "duplicate_candidate_id", "candidate_id values must be unique")
    info_id = manifest.get("information_boundary", {}).get("information_condition_id")
    opp_id = manifest.get("stream_contract", {}).get("opportunity_condition_id")
    resource = manifest.get("resource_contract", {})
    resource_id = resource.get("resource_condition_id")
    replay_id = resource.get("replay_limits", {}).get("replay_policy_id")
    scope_ids = set(manifest.get("audition_scope_contract", {}).get("scope_policy_ids", ()))
    for candidate in candidates:
        for key, expected in (("information_condition_id", info_id), ("opportunity_condition_id", opp_id), ("resource_condition_id", resource_id), ("replay_policy_id", replay_id)):
            if expected is not None and candidate.get(key) != expected:
                return _result(ValidationStatus.FAIL_CROSS_FIELD_INVARIANT, "candidate_condition_mismatch", f"candidate {candidate.get('candidate_id')!r} {key} does not resolve to top-level condition")
        if scope_ids and candidate.get("scope_policy_id") not in scope_ids:
            return _result(ValidationStatus.FAIL_CROSS_FIELD_INVARIANT, "candidate_scope_policy_unresolved", f"candidate {candidate.get('candidate_id')!r} scope_policy_id is not frozen")
    stage = manifest.get("subject", {}).get("stage")
    by_role: dict[str, list[Mapping[str, Any]]] = {}
    for candidate in candidates:
        by_role.setdefault(str(candidate.get("role")), []).append(candidate)
    if stage == "SVF-1" and by_role.get("C2") and by_role.get("C4"):
        if by_role["C2"][0].get("base_substrate_id") != by_role["C4"][0].get("base_substrate_id"):
            return _result(ValidationStatus.FAIL_CROSS_FIELD_INVARIANT, "c2_c4_base_substrate_mismatch", "primary C2/C4 comparison must share one declared base substrate")
    return None


def _resource_result(manifest: Mapping[str, Any]) -> ValidationResult | None:
    resource = manifest.get("resource_contract")
    if isinstance(resource, Mapping) and not isinstance(resource.get("measurement_artifact"), Mapping):
        return _result(ValidationStatus.FAIL_RESOURCE_ACCOUNTING, "resource_measurement_unbound", "resource measurement must be an immutable artifact")
    return None


def _lineage_result(manifest: Mapping[str, Any]) -> ValidationResult | None:
    lineage = manifest.get("lineage_transfer_contract")
    if not isinstance(lineage, Mapping):
        return None
    artifacts = lineage.get("state_scope_manifest_artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        return _result(ValidationStatus.FAIL_LINEAGE_TRANSFER_CONTRACT, "state_scope_manifest_unbound", "lineage state scope must be bound by at least one immutable artifact")
    return None


def validate_manifest(manifest: Mapping[str, Any], schema: Mapping[str, Any], resolver: DictArtifactResolver) -> ValidationResult:
    schema_errors = sorted(Draft202012Validator(schema).iter_errors(manifest), key=lambda error: tuple(str(part) for part in error.absolute_path))
    if schema_errors:
        return _result(ValidationStatus.FAIL_SCHEMA, "schema", schema_errors[0].message)
    resolution_result, resolved = _resolve_all(manifest, resolver)
    if resolution_result is not None:
        return resolution_result
    for check in (
        lambda: _implementation_subject_result(manifest, resolved),
        lambda: _information_boundary_result(manifest),
        lambda: _cross_field_result(manifest),
        lambda: _resource_result(manifest),
        lambda: _lineage_result(manifest),
    ):
        result = check()
        if result is not None:
            return result
    return ValidationResult(ValidationStatus.PASS_FROZEN_VALID)
