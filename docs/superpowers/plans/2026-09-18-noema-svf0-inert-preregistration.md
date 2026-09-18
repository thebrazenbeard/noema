# Noema SVF-0 Inert Preregistration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a fully artifact-bound, mechanically validated, inert SVF-0 preregistration subject without executing any learning/training trajectory.

**Architecture:** Extend the existing minimal Python source only where the V2 validator and deterministic evaluator/world definition are incomplete. Freeze exact source, support artifacts, manifest, and receipt in separate commits so provenance is non-circular. All verification is deterministic local I1 work; E0 remains closed.

**Tech Stack:** Python 3.13.5, jsonschema 4.26.0, pytest 9.0.2, standard library only beyond the existing jsonschema dependency.

**Spec:** `docs/working-design/MINIMAL_STRUCTURAL_VALUE_FALSIFICATION_FAMILY.md`, `EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V2.json`, V2 validator contract and normative addenda at research subject `be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33`.

## Global Constraints

- I0 implementation source and I1 deterministic non-learning verification are authorized.
- E0 learning/training/experiment execution is NOT authorized.
- P0 protected effects, merge, deploy, publication, paid/hosted compute, provider/credential/ruleset/visibility mutation are NOT authorized.
- Frozen BT2 R1 remains separate and untouched.
- Exact-head provenance is mandatory; any source change requires fresh I1 verification.
- C0 remains optional; SVF-0 requires C1 and C2.
- Primary V2 fixed-envelope SVF-0 subjects use `checkpointing_used=false`.
- All primary adjudication rules must be mechanically decidable before execution.

---

### Task 1: Close V2 validator decidability/resource gaps

**Files:**
- Modify: `tests/test_hostile_contracts.py`
- Modify: `src/noema/validator.py`

**Interfaces:**
- Consumes: `validate_manifest(manifest, schema, resolver)`
- Produces: fail-closed `FAIL_RESOURCE_ACCOUNTING` and `FAIL_SCORING_CONTRACT` paths.

- [ ] Add RED hostile tests for checkpointed primary V2, vague primary threshold, and vague negative-control rule.
- [ ] Run the three tests and confirm they fail for missing validator behavior.
- [ ] Add the missing result class and minimal deterministic rule checks.
- [ ] Run hostile and full deterministic suites; require all green.
- [ ] Commit.

### Task 2: Add inert SVF-0 world/evaluator source

**Files:**
- Create: `src/noema/svf0.py`
- Create: `tests/test_svf0.py`

**Interfaces:**
- Produces deterministic world specification/generator and single-observation Gaussian NLL evaluator helpers.
- Must not call learner transitions across an experiment trajectory.

- [ ] Add RED tests for deterministic seeded generation, exact regime-change boundary, stable unrelated dependency, opaque learner event shape, and scoring formula.
- [ ] Confirm RED.
- [ ] Implement the smallest standard-library-only pure functions.
- [ ] Run tests and full suite.
- [ ] Commit.

### Task 3: Freeze the new source subject

**Files:**
- Update: `implementation/NOEMA_MINIMAL_SUBJECT_V1.json`
- Update: `implementation/NOEMA_MINIMAL_SOURCE_I1_VERIFICATION_RECEIPT.md`
- Update: `governance/IMPLEMENTATION_CURRENTNESS.json`

- [ ] Reconstruct exact GitHub source/test bytes locally.
- [ ] Run the complete I1 suite.
- [ ] Recompute Git blob IDs and compare to GitHub.
- [ ] Bind the new exact source commit and counts.
- [ ] Commit subject/currentness/receipt updates after source is frozen.

### Task 4: Freeze SVF-0 support artifacts

**Files:**
- Create under `implementation/svf0/`: learner/evaluator schemas, parameter distribution, seed manifest, resource measurement contract, state-scope manifest, negative-control spec, scoring/decision rules.

- [ ] Define explicit implementation-choice constants and mechanically decidable rules.
- [ ] Validate JSON syntax and required invariants deterministically.
- [ ] Commit all support artifacts together.
- [ ] Compute their Git blob and SHA-256 identities.

### Task 5: Create inert V2 manifest and freeze receipt

**Files:**
- Create: `implementation/svf0/SVF0_PREREGISTRATION_V2.json`
- Create later: `implementation/svf0/SVF0_FREEZE_RECEIPT_V1.json`

- [ ] Build a schema-valid SVF-0 manifest with C1/C2 on one base substrate and fixed conditions.
- [ ] Bind exact research, implementation, support, world, resource, lineage, scoring, and schema/validator artifacts.
- [ ] Freeze manifest in its own commit.
- [ ] Validate exact manifest bytes using the frozen V2 schema and implementation validator with an exact artifact resolver.
- [ ] Create a later receipt binding manifest commit/path/blob and normative source tuples.
- [ ] Revalidate receipt/source bindings without executing learners.
- [ ] Commit receipt.

### Task 6: Hostile qualification and coordination

**Files:**
- Add exact-head qualification record under `implementation/svf0/`.
- Update PR #36 metadata.
- Add sanitized Bus status + PR mirror.

- [ ] Hostile-test mutations: vague rules, checkpointing, source drift, digest/blob drift, candidate condition mismatch, missing evidence.
- [ ] Require expected failure classes.
- [ ] Record exact-head I1 qualification ceiling.
- [ ] Fresh-read PR #32/#35/#36 and Bus before writes.
- [ ] Mirror only sanitized provenance/status to Bus.
- [ ] Stop at E0: no learning/training/trajectory execution.
