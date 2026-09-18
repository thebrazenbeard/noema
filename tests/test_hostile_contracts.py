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


def _full_v2_svf0_manifest():
    subject_bytes = real_subject_bytes()
    manifest, records = base_manifest(subject_bytes)
    research = "be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33"
    source = "b" * 40
    manifest["schema_version"] = "NOEMA_EXPERIMENT_PREREGISTRATION_MANIFEST_V2"
    manifest["subject"]["design_base_commit"] = research
    manifest["subject"]["implementation_subject_commit"] = source
    manifest["subject"].update({
        "schema_artifact": ref("docs/working-design/EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V2.json", research),
        "validator_artifact": ref("docs/working-design/EXPERIMENT_PREREGISTRATION_VALIDATOR_CONTRACT_V2.md", research),
        "comparator_fairness_artifact": ref("docs/working-design/C0_C4_FAIR_COMPARISON_AND_CLAIM_BOUNDARY_MATRIX.md", research),
        "resource_addendum_artifact": ref("docs/working-design/EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_RESOURCE_ADDENDUM.md", research),
        "decidability_addendum_artifact": ref("docs/working-design/EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_DECIDABILITY_ADDENDUM.md", research),
        "comparator_matrix_addendum_artifact": ref("docs/working-design/EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_COMPARATOR_MATRIX_ADDENDUM.md", research),
        "comparator_interface_artifact": ref("docs/working-design/C2_C4_COMPARATOR_INTERFACE_CONTRACT.md", research),
    })
    manifest["comparator_fairness_contract"] = ref(
        "docs/working-design/C0_C4_FAIR_COMPARISON_AND_CLAIM_BOUNDARY_MATRIX.md", research
    )
    c1 = _bound_c1_candidate()
    c2 = dict(c1)
    c2.update({
        "candidate_id": "c2",
        "role": "C2",
        "variant_of_candidate_id": "c1",
        "variant_dimension": "REPLAY",
    })
    manifest["candidates"] = [c1, c2]
    manifest["world"].update({
        "hidden_family_randomization_rule": "algo:fixed_none@v1",
        "intervention_mode": "NONE",
        "schedule_may_adapt_to_hidden_family": False,
        "schedule_may_adapt_to_candidate_predictions": False,
        "schedule_may_adapt_to_scored_outcomes": False,
        "schedule_may_adapt_to_evaluator_diagnostics": False,
        "passive_observational_equivalence_required": False,
        "observational_equivalence_verification": None,
        "negative_control_acceptance_rule": "expr:negative_control_mean_nll_delta<=0.02",
    })
    manifest["audition_scope_contract"].update({
        "learned_scope_primary_claim_allowed": False,
        "simple_audition_rival_required": False,
        "simple_audition_probability": None,
    })
    manifest["resource_contract"].update({
        "measurement_method": "algo:noema_svf0_python_fixed_envelope@v1",
        "fixed_total_envelope": {
            "max_resident_memory_bytes": 8388608,
            "max_durable_state_bytes": 1048576,
            "max_update_cpu_seconds_per_event": 0.05,
            "max_query_cpu_seconds_per_event": 0.01,
            "max_shadow_auditions_per_event": 0,
        },
        "replay_limits": {
            "replay_policy_id": "replay-1",
            "raw_buffer_capacity_events": 32,
            "max_replay_updates_per_event": 1,
            "replay_compute_charged": True,
            "priority_provenance_declared": True,
        },
    })
    manifest["scoring_contract"] = {
        "proper_scoring_rule": "algo:gaussian_nll_sum@v1",
        "primary_claims": ["P"],
        "primary_metrics": [{
            "metric_id": "p-c1-v-reset",
            "claim": "P",
            "comparator_candidate_id": "c1",
            "aggregation_rule": "algo:mean@v1",
            "threshold_rule": "expr:mean_nll_delta<=-0.02",
            "support_requirement": "expr:scored_count==expected_count",
        }],
        "c2_vs_c4_external_comparison_required": False,
    }
    manifest["restart_contract"] = {
        "checkpointing_used": False,
        "restart_equivalence_claimed": False,
    }
    learner_schema = canonical_json_bytes({
        "type": "object",
        "additionalProperties": False,
        "required": ["channels"],
        "properties": {"channels": {"type": "array"}},
    })
    evaluator_schema = canonical_json_bytes({
        "type": "object",
        "additionalProperties": False,
        "required": ["hidden_family"],
        "properties": {"hidden_family": {"type": "string"}},
    })
    resource_artifact = canonical_json_bytes({
        "schema_id": "NOEMA_SVF0_RESOURCE_MEASUREMENT_V1",
        "measurement_method_id": "NOEMA_SVF0_PYTHON_FIXED_ENVELOPE_V1",
        "rules": {
            "cpu_clock": "time.process_time_ns",
            "resident_memory": "tracemalloc",
            "durable_state": "pickle protocol 5",
            "update_cpu": "charged",
            "query_cpu": "charged",
            "replay": "charged",
            "shared_overhead": "candidate-specific",
            "absent_feature_zero": "only absent invoked paths",
            "missing_measurement": "INVALIDATE_FIXED_ENVELOPE_POINT",
            "over_budget": "INVALIDATE_FIXED_ENVELOPE_POINT",
        },
        "envelope": manifest["resource_contract"]["fixed_total_envelope"],
        "replay": {
            "raw_buffer_capacity_events": 32,
            "max_replay_updates_per_event": 1,
        },
    })
    for key, value in manifest["subject"].items():
        if (
            key != "implementation_subject_manifest"
            and isinstance(value, dict)
            and {"repository", "commit", "path"}.issubset(value)
        ):
            records[(value["repository"], value["commit"], value["path"])] = ArtifactRecord(b"bound")
    fair = manifest["comparator_fairness_contract"]
    records[(fair["repository"], fair["commit"], fair["path"])] = ArtifactRecord(b"bound")
    for candidate in manifest["candidates"]:
        for value in candidate["source_artifacts"]:
            records[(value["repository"], value["commit"], value["path"])] = ArtifactRecord(b"source")
    learner_ref = manifest["information_boundary"]["learner_visible_schema"]
    evaluator_ref = manifest["information_boundary"]["evaluator_only_schema"]
    records[(learner_ref["repository"], learner_ref["commit"], learner_ref["path"])] = ArtifactRecord(learner_schema)
    records[(evaluator_ref["repository"], evaluator_ref["commit"], evaluator_ref["path"])] = ArtifactRecord(evaluator_schema)
    measurement_ref = manifest["resource_contract"]["measurement_artifact"]
    records[(measurement_ref["repository"], measurement_ref["commit"], measurement_ref["path"])] = ArtifactRecord(resource_artifact)
    return manifest, records


def test_full_v2_svf0_stage_semantics_fail_closed():
    manifest, records = _full_v2_svf0_manifest()
    manifest["scoring_contract"]["primary_claims"] = ["S"]
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status is ValidationStatus.FAIL_STAGE_SEMANTICS


def test_full_v2_information_schemas_must_be_closed_and_match_declared_fields():
    manifest, records = _full_v2_svf0_manifest()
    learner_ref = manifest["information_boundary"]["learner_visible_schema"]
    records[(learner_ref["repository"], learner_ref["commit"], learner_ref["path"])] = ArtifactRecord(
        canonical_json_bytes({
            "type": "object",
            "additionalProperties": True,
            "properties": {"channels": {"type": "array"}},
        })
    )
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status is ValidationStatus.FAIL_INFORMATION_BOUNDARY


def test_full_v2_c1_c2_replay_isolation_requires_shared_base_and_replay_variant():
    manifest, records = _full_v2_svf0_manifest()
    manifest["candidates"][1]["base_substrate_id"] = "stronger-base"
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status is ValidationStatus.FAIL_COMPARATOR_FAIRNESS

    manifest, records = _full_v2_svf0_manifest()
    manifest["candidates"][1]["variant_dimension"] = "OTHER_PREREGISTERED"
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status is ValidationStatus.FAIL_COMPARATOR_FAIRNESS


def test_full_v2_resource_meter_must_match_frozen_envelope_and_fail_closed():
    manifest, records = _full_v2_svf0_manifest()
    measurement_ref = manifest["resource_contract"]["measurement_artifact"]
    artifact = {
        "schema_id": "NOEMA_SVF0_RESOURCE_MEASUREMENT_V1",
        "measurement_method_id": "NOEMA_SVF0_PYTHON_FIXED_ENVELOPE_V1",
        "rules": {
            "cpu_clock": "time.process_time_ns",
            "resident_memory": "tracemalloc",
            "durable_state": "pickle protocol 5",
            "update_cpu": "charged",
            "query_cpu": "charged",
            "replay": "charged",
            "shared_overhead": "candidate-specific",
            "absent_feature_zero": "only absent invoked paths",
            "missing_measurement": "TREAT_AS_ZERO",
            "over_budget": "INVALIDATE_FIXED_ENVELOPE_POINT",
        },
        "envelope": dict(manifest["resource_contract"]["fixed_total_envelope"]),
        "replay": {"raw_buffer_capacity_events": 32, "max_replay_updates_per_event": 1},
    }
    records[(measurement_ref["repository"], measurement_ref["commit"], measurement_ref["path"])] = ArtifactRecord(
        canonical_json_bytes(artifact)
    )
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status is ValidationStatus.FAIL_RESOURCE_ACCOUNTING


def test_full_v2_normative_research_tuple_must_match_reviewed_subject():
    manifest, records = _full_v2_svf0_manifest()
    manifest["subject"]["schema_artifact"]["commit"] = "c" * 40
    bad_ref = manifest["subject"]["schema_artifact"]
    records[(bad_ref["repository"], bad_ref["commit"], bad_ref["path"])] = ArtifactRecord(b"bound")
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status is ValidationStatus.FAIL_SOURCE_BINDING


def test_first_core_svf0_profile_requires_exact_primary_metric_semantics():
    manifest, records = _full_v2_svf0_manifest()
    manifest["subject"]["manifest_logical_id"] = "NOEMA_SVF0_RECURRENT_GATE1_V1"
    manifest["candidates"][0]["candidate_id"] = "c1_recurrent"
    manifest["candidates"][1]["candidate_id"] = "c2_recurrent_replay"
    manifest["candidates"][1]["variant_of_candidate_id"] = "c1_recurrent"
    manifest["candidates"].append({
        "candidate_id": "reset_ref",
        "role": "REFERENCE",
        "source_commit": "b" * 40,
        "source_artifacts": [ref("src/noema/candidates.py", commit="b" * 40)],
        "base_substrate_id": None,
        "variant_of_candidate_id": None,
        "variant_dimension": "RESET_REFIT",
        "information_condition_id": "info-1",
        "opportunity_condition_id": "opp-1",
        "resource_condition_id": "res-1",
        "replay_policy_id": "replay-1",
        "scope_policy_id": "scope-1",
        "developmental_evidence_eligible": False,
    })
    manifest["scoring_contract"]["primary_metrics"] = [
        {
            "metric_id": "P_C1_VS_RESET_LATE_POST",
            "claim": "P",
            "direction": "LOWER_IS_BETTER",
            "comparator_candidate_id": "reset_ref",
            "aggregation_rule": "algo:mean_seed_window_delta@v1",
            "threshold_rule": "expr:mean_nll_delta<=-0.02&&upper_ci_delta<0",
            "support_requirement": "expr:scored_count==expected_count&&worlds_completed==maximum_worlds&&resource_accounting_complete==true",
        },
        {
            "metric_id": "P_C2_VS_RESET_LATE_POST",
            "claim": "P",
            "direction": "LOWER_IS_BETTER",
            "comparator_candidate_id": "reset_ref",
            "aggregation_rule": "algo:mean_seed_window_delta@v1",
            "threshold_rule": "expr:mean_nll_delta<=-0.02&&upper_ci_delta<0",
            "support_requirement": "expr:scored_count==expected_count&&worlds_completed==maximum_worlds&&resource_accounting_complete==true",
        },
    ]
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status is ValidationStatus.PASS_FROZEN_VALID

    manifest["scoring_contract"]["primary_metrics"][0]["threshold_rule"] = "expr:mean_nll_delta<=0"
    result = validate_manifest(manifest, schema(), DictArtifactResolver(records))
    assert result.status is ValidationStatus.FAIL_SCORING_CONTRACT
