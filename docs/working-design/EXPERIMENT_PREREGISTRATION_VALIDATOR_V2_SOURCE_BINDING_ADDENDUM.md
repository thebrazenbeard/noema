# Experiment Preregistration Validator V2 — Exact Source and Measurement Binding Addendum

Classification: **IP_CONFIDENTIAL**

Status: **NORMATIVE V2 VALIDATOR ADDENDUM / RESEARCH ONLY / NOT IMPLEMENTED / NOT EXECUTION AUTHORITY / NOT BT2 R1 REMEDIATION**

Date: 2026-09-13

Applies to:

- `EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V2.json`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_CONTRACT_V2.md`
- `C0_C4_FAIR_COMPARISON_AND_CLAIM_BOUNDARY_MATRIX.md`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_COMPARATOR_MATRIX_ADDENDUM.md`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_RESOURCE_ADDENDUM.md`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_DECIDABILITY_ADDENDUM.md`

## 1. Purpose

V2 already requires immutable implementation, world, schedule, scoring, support, and resource evidence in principle. This addendum closes the remaining provenance gap between those requirements and the machine-readable manifest:

- the exact schema/validator/addendum bytes must be bound;
- a design-only commit must not qualify as an implementation subject;
- lineage state scope must be locatable;
- resource measurement must be locatable;
- SVF-1 stage conditions must fail closed at both schema and validator layers.

A validator result is evidence-governance status only. It never authorizes implementation, training, execution, spend, merge, publication, deployment, or protected-system connection.

## 2. Exact normative-contract binding

For every future V2 manifest, resolve and verify all of these immutable references before any cross-field adjudication:

- `subject.schema_artifact`;
- `subject.validator_artifact`;
- `subject.comparator_fairness_artifact`;
- `subject.resource_addendum_artifact`;
- `subject.decidability_addendum_artifact`;
- `subject.comparator_matrix_addendum_artifact`;
- `subject.comparator_interface_artifact`;
- top-level `comparator_fairness_contract`.

Each reference must resolve to the declared repository, immutable commit, path, and any declared Git blob/SHA-256 digest. The resolved bytes must be the exact artifacts whose semantics the validator applies. An unavailable or mismatched artifact is `BLOCKED_UNAVAILABLE_EVIDENCE`, never an implicit current-path substitution.

The freeze receipt must bind these exact artifact tuples, not only the string `schema_version`. A later artifact at the same V2 logical/version label creates a new subject.

## 3. Implementation-subject admissibility

Resolve `subject.implementation_subject_manifest` at its immutable tuple before accepting any developmental candidate source.

The implementation-subject manifest must enumerate, at minimum:

- implementation source entrypoints or modules;
- the learner-visible/evaluator-only comparator boundary;
- resource-meter/instrumentation artifacts;
- hostile unit/contract-test artifacts;
- any derivation relation used by a candidate source commit.

The validator must verify that the enumerated artifacts exist at immutable commits and that developmental candidate source artifacts resolve under the frozen implementation subject or the declared frozen derivation relation.

A commit containing only working-design, schema, validator, review, or other documentation artifacts is not an implementation subject. It must return `FAIL_SOURCE_BINDING` or `BLOCKED_UNAVAILABLE_EVIDENCE`, depending on whether the evidence is contradictory or absent.

This rule does not require a particular programming language, optimizer, model family, or architecture. It only prevents documentation from being presented as executable implementation provenance.

## 4. Lineage state-scope binding

Resolve every artifact in `lineage_transfer_contract.state_scope_manifest_artifacts`.

For each carried, reset, copied, restored, or otherwise transferred condition declared by the manifest, the resolved state-scope evidence must identify:

- the operational state scope actually included;
- omitted/external state relevant to the claim;
- whether the state is complete, partial, transformed, or derived;
- learner-visible consequences of the operation;
- the evaluator-only lineage/operation record.

If the state-scope evidence cannot distinguish the C2 and C4 continuation/reset conditions required by claim `T`, return `FAIL_LINEAGE_TRANSFER_CONTRACT`. If the authoritative artifact is unavailable, return `BLOCKED_UNAVAILABLE_EVIDENCE`.

A boolean such as `state_scope_manifest_required=true` never substitutes for the artifact itself.

## 5. Resource-measurement binding

Resolve `resource_contract.measurement_artifact` before accepting any fixed-envelope or resource-frontier claim.

The measurement artifact must make independently decidable:

- every resource class relevant to the claimed comparison;
- resident and durable state accounting;
- update/query/replay/structural/scope/audition/base-shadow compute;
- checkpoint/restart cost when present;
- shared-overhead allocation;
- missing or unmeasured observations;
- over-budget and invalidation behavior.

The V2 resource and decidability addenda remain controlling: consumed-but-unmeasured is not zero, and an unverifiable meter cannot support `FIXED_TOTAL_ENVELOPE` or a one-dimensional frontier claim.

## 6. SVF-1 schema/validator closure

For `SVF-1`, the validator must reject:

- null or absent observational-equivalence verification;
- a nonpositive, null, or absent simple-audition probability when the simple-audition rival is required;
- a schedule artifact/commitment whose immutable preimage cannot be resolved;
- any stage shape that passes only because a general nullable definition was not narrowed by the SVF-1 conditional.

These checks remain required even though the repaired schema now narrows the two nullable fields. Schema PASS is not a substitute for validator PASS.

## 7. Exact freeze and mutation rule

A freeze receipt for a V2 subject must bind:

- the manifest repository, commit, path, and Git blob;
- the exact schema/validator/addendum tuples listed in Section 2;
- the implementation-subject commit and implementation-subject manifest;
- the resource measurement artifact;
- the lineage state-scope artifacts;
- the logical experiment ID and freeze time.

Changing any of these after freeze creates a new subject. Historical reviews and failed/blocked subjects remain immutable provenance and are not rewritten to simulate continuity.

## 8. Hostile validator additions

A future hostile suite must reject or block at least:

1. a manifest whose V2 schema version is unchanged but whose schema artifact points to different bytes;
2. a validator/addendum path that is mutable or unavailable;
3. an implementation subject containing only design documents;
4. a claim T manifest with only the boolean state-scope flag and no artifact;
5. a fixed-envelope manifest with a prose measurement method but no measurement artifact;
6. an SVF-1 manifest with null observational-equivalence verification;
7. an SVF-1 manifest with null or zero simple-audition probability;
8. a freeze receipt that binds only schema version text and not exact normative artifacts.

## 9. Authority boundary

This addendum does not authorize implementation, validator software, training, model execution, hosted/paid compute, merge, deployment, publication, provider/credential/ruleset mutation, repository-visibility change, or protected-system connection. It only makes the future boundary harder to misread.
