from noema.provenance import ArtifactRecord, DictArtifactResolver, canonical_json_bytes
from noema.validator import ValidationStatus, validate_manifest


def ref(path: str, commit: str = "a" * 40):
    return {"repository": "thebrazenbeard/noema", "commit": commit, "path": path}


def schema():
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "required": ["subject", "resource_contract", "lineage_transfer_contract", "audition_scope_contract"],
        "properties": {
            "subject": {"type": "object", "required": ["stage", "implementation_subject_manifest"]},
            "resource_contract": {"type": "object", "required": ["measurement_artifact"]},
            "lineage_transfer_contract": {"type": "object", "required": ["state_scope_manifest_artifacts"]},
            "audition_scope_contract": {"type": "object"},
        },
    }


def base_manifest(subject_bytes: bytes):
    implementation_commit = "b" * 40
    subject_ref = ref("implementation/subject.json")
    manifest = {
        "subject": {
            "stage": "SVF-0",
            "implementation_subject_commit": implementation_commit,
            "implementation_subject_manifest": subject_ref,
            "schema_artifact": ref("docs/schema.json"),
            "validator_artifact": ref("docs/validator.md"),
            "comparator_fairness_artifact": ref("docs/fairness.md"),
            "resource_addendum_artifact": ref("docs/resource.md"),
            "decidability_addendum_artifact": ref("docs/decidability.md"),
            "comparator_matrix_addendum_artifact": ref("docs/matrix.md"),
            "comparator_interface_artifact": ref("docs/interface.md"),
        },
        "comparator_fairness_contract": ref("docs/fairness.md"),
        "information_boundary": {
            "information_condition_id": "info-1",
            "learner_visible_schema": ref("schemas/learner.json"),
            "evaluator_only_schema": ref("schemas/evaluator.json"),
            "learner_visible_field_names": ["channels"],
            "evaluator_only_field_names": ["hidden_family"],
        },
        "candidates": [],
        "stream_contract": {"opportunity_condition_id": "opp-1"},
        "resource_contract": {
            "resource_condition_id": "res-1",
            "measurement_artifact": ref("instrumentation/resource.json"),
            "replay_limits": {"replay_policy_id": "replay-1"},
        },
        "lineage_transfer_contract": {
            "state_scope_manifest_artifacts": [ref("implementation/state-scope.json")]
        },
        "audition_scope_contract": {"scope_policy_ids": ["scope-1"]},
        "world": {
            "generator": ref("world/generator.py"),
            "parameter_distribution_artifact": ref("world/params.json"),
            "parameter_distribution_commitment": None,
            "seed_manifest_artifact": ref("world/seeds.json"),
            "seed_commitment": None,
            "negative_control_generator": ref("world/negative.py"),
            "intervention_schedule_artifact": None,
            "intervention_schedule_commitment": None,
        },
    }
    records = {}
    def walk(value):
        if isinstance(value, dict):
            if {"repository", "commit", "path"}.issubset(value):
                data = subject_bytes if value["path"] == "implementation/subject.json" else b"bound"
                records[(value["repository"], value["commit"], value["path"])] = ArtifactRecord(data)
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)
    walk(manifest)
    return manifest, records


def real_subject_bytes():
    return canonical_json_bytes({
        "source_commit": "b" * 40,
        "source_paths": ["src/noema/candidates.py"],
        "test_paths": ["tests/test_c1_c2.py"],
        "instrumentation_paths": ["src/noema/comparator.py"],
    })


def test_candidate_source_commit_must_match_bound_implementation_subject():
    subject_bytes = real_subject_bytes()
    manifest, records = base_manifest(subject_bytes)
    candidate_ref = ref("src/noema/candidates.py", commit="c" * 40)
    manifest["candidates"] = [{
        "candidate_id": "c2",
        "role": "C2",
        "source_commit": "c" * 40,
        "source_artifacts": [candidate_ref],
        "base_substrate_id": "base-1",
        "information_condition_id": "info-1",
        "opportunity_condition_id": "opp-1",
        "resource_condition_id": "res-1",
        "replay_policy_id": "replay-1",
        "scope_policy_id": "scope-1",
    }]
    records[(candidate_ref["repository"], candidate_ref["commit"], candidate_ref["path"])] = ArtifactRecord(b"source")
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status is ValidationStatus.FAIL_SOURCE_BINDING


def test_parameter_commitment_must_match_resolved_artifact_bytes():
    subject_bytes = real_subject_bytes()
    manifest, records = base_manifest(subject_bytes)
    manifest["world"]["parameter_distribution_commitment"] = "0" * 64
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status is ValidationStatus.FAIL_FREEZE_INTEGRITY


def test_primary_metric_comparator_must_resolve_to_frozen_candidate():
    subject_bytes = real_subject_bytes()
    manifest, records = base_manifest(subject_bytes)
    manifest["scoring_contract"] = {
        "primary_claims": ["P"],
        "primary_metrics": [{
            "metric_id": "m1",
            "claim": "P",
            "comparator_candidate_id": "missing-candidate",
        }],
    }
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status is ValidationStatus.FAIL_CROSS_FIELD_INVARIANT


def test_primary_fixed_envelope_checkpointing_fails_resource_accounting():
    subject_bytes = real_subject_bytes()
    manifest, records = base_manifest(subject_bytes)
    manifest["restart_contract"] = {
        "checkpointing_used": True,
        "restart_equivalence_claimed": False,
    }
    manifest["scoring_contract"] = {"primary_claims": ["P"], "primary_metrics": []}
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status.value == "FAIL_RESOURCE_ACCOUNTING"


def test_vague_primary_threshold_rule_fails_scoring_contract():
    subject_bytes = real_subject_bytes()
    manifest, records = base_manifest(subject_bytes)
    manifest["candidates"] = [{
        "candidate_id": "c1",
        "role": "C1",
        "source_commit": "b" * 40,
        "source_artifacts": [ref("src/noema/candidates.py", commit="b" * 40)],
        "base_substrate_id": "base-1",
        "information_condition_id": "info-1",
        "opportunity_condition_id": "opp-1",
        "resource_condition_id": "res-1",
        "replay_policy_id": "replay-1",
        "scope_policy_id": "scope-1",
    }]
    records[("thebrazenbeard/noema", "b" * 40, "src/noema/candidates.py")] = ArtifactRecord(b"source")
    manifest["scoring_contract"] = {
        "primary_claims": ["P"],
        "primary_metrics": [{
            "metric_id": "m1",
            "claim": "P",
            "comparator_candidate_id": "c1",
            "aggregation_rule": "mean",
            "threshold_rule": "materially better",
            "support_requirement": "all scored observations present",
        }],
    }
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status.value == "FAIL_SCORING_CONTRACT"


def test_vague_negative_control_rule_fails_scoring_contract():
    subject_bytes = real_subject_bytes()
    manifest, records = base_manifest(subject_bytes)
    manifest["world"]["negative_control_acceptance_rule"] = "small overhead allowed"
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status.value == "FAIL_SCORING_CONTRACT"


def _bound_c1_candidate():
    return {
        "candidate_id": "c1",
        "role": "C1",
        "source_commit": "b" * 40,
        "source_artifacts": [ref("src/noema/candidates.py", commit="b" * 40)],
        "base_substrate_id": "base-1",
        "variant_of_candidate_id": None,
        "variant_dimension": "NONE",
        "information_condition_id": "info-1",
        "opportunity_condition_id": "opp-1",
        "resource_condition_id": "res-1",
        "replay_policy_id": "replay-1",
        "scope_policy_id": "scope-1",
        "developmental_evidence_eligible": True,
    }


def test_arbitrary_prose_primary_threshold_fails_decidability():
    subject_bytes = real_subject_bytes()
    manifest, records = base_manifest(subject_bytes)
    candidate = _bound_c1_candidate()
    manifest["candidates"] = [candidate]
    records[("thebrazenbeard/noema", "b" * 40, "src/noema/candidates.py")] = ArtifactRecord(b"source")
    manifest["scoring_contract"] = {
        "primary_claims": ["P"],
        "primary_metrics": [{
            "metric_id": "m1",
            "claim": "P",
            "comparator_candidate_id": "c1",
            "aggregation_rule": "algo:mean@v1",
            "threshold_rule": "bananas are better",
            "support_requirement": "expr:scored_count==expected_count",
        }],
    }
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status.value == "FAIL_SCORING_CONTRACT"


def test_machine_decidable_primary_rules_can_pass_scoring_check():
    subject_bytes = real_subject_bytes()
    manifest, records = base_manifest(subject_bytes)
    candidate = _bound_c1_candidate()
    manifest["candidates"] = [candidate]
    records[("thebrazenbeard/noema", "b" * 40, "src/noema/candidates.py")] = ArtifactRecord(b"source")
    manifest["scoring_contract"] = {
        "primary_claims": ["P"],
        "primary_metrics": [{
            "metric_id": "m1",
            "claim": "P",
            "comparator_candidate_id": "c1",
            "aggregation_rule": "algo:mean@v1",
            "threshold_rule": "expr:mean_nll_delta<=-0.02",
            "support_requirement": "expr:scored_count==expected_count",
        }],
    }
    manifest["world"]["negative_control_acceptance_rule"] = "expr:negative_control_mean_nll_delta<=0.02"
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status is ValidationStatus.PASS_FROZEN_VALID


def test_vague_stopping_rule_fails_scoring_contract():
    subject_bytes = real_subject_bytes()
    manifest, records = base_manifest(subject_bytes)
    manifest["statistics_contract"] = {
        "uncertainty_method": "algo:student_t_ci@v1",
        "multiple_comparison_rule": "algo:holm_bonferroni@v1",
        "stopping_rule": "stop when stable",
        "kill_criteria": ["expr:c1_persistence_pass==false"],
    }
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status.value == "FAIL_SCORING_CONTRACT"


def test_variant_parent_must_resolve_and_not_self_reference():
    subject_bytes = real_subject_bytes()
    manifest, records = base_manifest(subject_bytes)
    candidate = _bound_c1_candidate()
    candidate["variant_of_candidate_id"] = "missing"
    manifest["candidates"] = [candidate]
    records[("thebrazenbeard/noema", "b" * 40, "src/noema/candidates.py")] = ArtifactRecord(b"source")
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status is ValidationStatus.FAIL_CROSS_FIELD_INVARIANT

    candidate["variant_of_candidate_id"] = "c1"
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status is ValidationStatus.FAIL_CROSS_FIELD_INVARIANT


def test_validator_exposes_all_normative_v2_result_classes():
    expected = {
        "PASS_FROZEN_VALID",
        "FAIL_SCHEMA",
        "FAIL_STAGE_SEMANTICS",
        "FAIL_CROSS_FIELD_INVARIANT",
        "FAIL_SOURCE_BINDING",
        "FAIL_INFORMATION_BOUNDARY",
        "FAIL_WORLD_SCHEDULE_INTEGRITY",
        "FAIL_COMPARATOR_FAIRNESS",
        "FAIL_RESOURCE_ACCOUNTING",
        "FAIL_SUPPORT_AUDITION_CONTRACT",
        "FAIL_LINEAGE_TRANSFER_CONTRACT",
        "FAIL_SCORING_CONTRACT",
        "FAIL_RESTART_INTEGRITY",
        "FAIL_FREEZE_INTEGRITY",
        "BLOCKED_UNAVAILABLE_EVIDENCE",
    }
    assert {status.value for status in ValidationStatus} == expected


def test_prose_world_randomization_rule_fails_world_integrity():
    subject_bytes = real_subject_bytes()
    manifest, records = base_manifest(subject_bytes)
    manifest["world"]["hidden_family_randomization_rule"] = "balanced"
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status is ValidationStatus.FAIL_WORLD_SCHEDULE_INTEGRITY


def test_prose_resource_measurement_method_fails_resource_accounting():
    subject_bytes = real_subject_bytes()
    manifest, records = base_manifest(subject_bytes)
    manifest["resource_contract"]["measurement_method"] = "reasonable measurement"
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status is ValidationStatus.FAIL_RESOURCE_ACCOUNTING


def test_prose_proper_scoring_rule_fails_scoring_contract():
    subject_bytes = real_subject_bytes()
    manifest, records = base_manifest(subject_bytes)
    manifest["scoring_contract"] = {
        "proper_scoring_rule": "appropriate scoring",
        "primary_claims": [],
        "primary_metrics": [],
    }
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status is ValidationStatus.FAIL_SCORING_CONTRACT
