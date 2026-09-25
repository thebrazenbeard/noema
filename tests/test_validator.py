import json

from noema.provenance import ArtifactRecord, DictArtifactResolver, canonical_json_bytes, sha256_hex
from noema.validator import ValidationStatus, validate_manifest


def _ref(path: str, *, commit: str = "a" * 40, data: bytes | None = None):
    ref = {"repository": "thebrazenbeard/noema", "commit": commit, "path": path}
    if data is not None:
        ref["sha256"] = sha256_hex(data)
    return ref


def _schema():
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "required": ["subject", "resource_contract", "lineage_transfer_contract", "audition_scope_contract"],
        "properties": {
            "subject": {"type": "object", "required": ["stage", "implementation_subject_manifest"]},
            "resource_contract": {"type": "object", "required": ["measurement_artifact"]},
            "lineage_transfer_contract": {"type": "object", "required": ["state_scope_manifest_artifacts"]},
            "audition_scope_contract": {
                "type": "object",
                "required": ["simple_audition_probability"],
                "properties": {"simple_audition_probability": {"type": ["number", "null"]}},
            },
        },
        "allOf": [
            {
                "if": {"properties": {"subject": {"properties": {"stage": {"const": "SVF-1"}}}}},
                "then": {
                    "properties": {
                        "audition_scope_contract": {
                            "properties": {
                                "simple_audition_probability": {
                                    "type": "number",
                                    "exclusiveMinimum": 0,
                                    "maximum": 1,
                                }
                            }
                        }
                    }
                },
            }
        ],
    }


def _manifest(subject_manifest_ref):
    return {
        "subject": {
            "stage": "SVF-0",
            "implementation_subject_commit": "b" * 40,
            "implementation_subject_manifest": subject_manifest_ref,
            "schema_artifact": _ref("docs/schema.json"),
            "validator_artifact": _ref("docs/validator.md"),
            "comparator_fairness_artifact": _ref("docs/fairness.md"),
            "resource_addendum_artifact": _ref("docs/resource.md"),
            "decidability_addendum_artifact": _ref("docs/decidability.md"),
            "comparator_matrix_addendum_artifact": _ref("docs/matrix.md"),
            "comparator_interface_artifact": _ref("docs/interface.md"),
        },
        "comparator_fairness_contract": _ref("docs/fairness.md"),
        "information_boundary": {
            "information_condition_id": "info-1",
            "learner_visible_schema": _ref("schemas/learner.json"),
            "evaluator_only_schema": _ref("schemas/evaluator.json"),
            "learner_visible_field_names": ["channels"],
            "evaluator_only_field_names": ["hidden_family"],
        },
        "candidates": [],
        "stream_contract": {"opportunity_condition_id": "opp-1"},
        "resource_contract": {
            "resource_condition_id": "res-1",
            "measurement_artifact": _ref("instrumentation/resource.json"),
            "replay_limits": {"replay_policy_id": "replay-1"},
        },
        "lineage_transfer_contract": {
            "state_scope_manifest_artifacts": [_ref("implementation/state-scope.json")]
        },
        "audition_scope_contract": {
            "scope_policy_ids": ["scope-1"],
            "simple_audition_probability": None,
        },
        "world": {
            "generator": _ref("world/generator.py"),
            "parameter_distribution_artifact": _ref("world/params.json"),
            "seed_manifest_artifact": _ref("world/seeds.json"),
            "negative_control_generator": _ref("world/negative.py"),
            "intervention_schedule_artifact": None,
        },
    }


def _resolver_for_manifest(manifest, subject_manifest_bytes):
    records = {}
    def add(value):
        if isinstance(value, dict):
            if {"repository", "commit", "path"}.issubset(value):
                key = (value["repository"], value["commit"], value["path"])
                data = subject_manifest_bytes if value["path"] == "implementation/subject.json" else b"bound"
                records[key] = ArtifactRecord(data=data)
            for child in value.values():
                add(child)
        elif isinstance(value, list):
            for child in value:
                add(child)
    add(manifest)
    return DictArtifactResolver(records)


def test_design_only_implementation_subject_cannot_pass():
    subject_bytes = canonical_json_bytes({
        "source_paths": ["docs/working-design/x.md"],
        "test_paths": ["tests/test_x.py"],
        "instrumentation_paths": [],
    })
    subject_ref = _ref("implementation/subject.json", data=subject_bytes)
    manifest = _manifest(subject_ref)
    result = validate_manifest(manifest, _schema(), _resolver_for_manifest(manifest, subject_bytes))
    assert result.status is ValidationStatus.FAIL_SOURCE_BINDING


def test_missing_bound_artifact_blocks_instead_of_guessing():
    subject_ref = _ref("implementation/subject.json")
    manifest = _manifest(subject_ref)
    result = validate_manifest(manifest, _schema(), DictArtifactResolver({}))
    assert result.status is ValidationStatus.BLOCKED_UNAVAILABLE_EVIDENCE


def test_svf1_zero_audition_probability_fails_schema():
    subject_ref = _ref("implementation/subject.json")
    manifest = _manifest(subject_ref)
    manifest["subject"]["stage"] = "SVF-1"
    manifest["audition_scope_contract"]["simple_audition_probability"] = 0
    result = validate_manifest(manifest, _schema(), DictArtifactResolver({}))
    assert result.status is ValidationStatus.FAIL_SCHEMA
