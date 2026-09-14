# Noema Minimal Implementation-Source Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the smallest private implementation subject that realizes the Noema C1/C2/C4 research contracts, exact V2 preregistration validation boundary, comparator/resource/support instrumentation, and hostile deterministic source tests without running training or an experiment.

**Architecture:** Use a small Python package with immutable dataclass state and pure transition/prediction functions. Keep learner-visible data types, evaluator-only provenance, candidate kernels, accounting, and manifest validation in separate modules. Deterministic I1 tests may exercise pure functions over fixed unit fixtures, but may not run developmental trajectories, persist learned state, estimate empirical performance, or execute SVF-0/SVF-1.

**Tech Stack:** CPython 3.13.5; `jsonschema==4.26.0`; `pytest==9.0.2`; Python standard library (`dataclasses`, `hashlib`, `json`, `math`, `pathlib`, `typing`). No NumPy, ML framework, pretrained component, hosted service, network dependency, or semantic embedding.

**Spec:** `docs/working-design/IMPLEMENTATION_SOURCE_HANDOFF_AND_AUTHORITY_BOUNDARY.md` plus `docs/working-design/IMPLEMENTATION_SOURCE_HANDOFF_NORMATIVE_INPUTS_ADDENDUM.md` at research parent `be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33`.

## Global Constraints

- Authority is I0 + I1 only. No E0 learning/training/experiment execution and no P0 merge/deploy/publish/spend/provider/credential/visibility/protected-system effect.
- Implementation branch is `impl/noema-minimal-source-i0-20260913`, rooted exactly at research parent `be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33`.
- PR #32 remains research provenance and is not modified by implementation work.
- C1/C2/C4 share one declared base substrate. C2 differs from C1 only by bounded replay. C4 adds only bounded generic structural machinery and accounting.
- Learner-visible values and evaluator-only provenance must be different source types and must not share arbitrary metadata bags.
- Unit tests may call pure one-step kernels on fixed synthetic fixtures; they must not loop a curriculum, retain learned output as a developmental checkpoint, score performance across worlds, or execute the frozen experiment family.
- Historical V1 preregistration artifacts are non-normative. V2 and its normative addenda control.
- `PASS_FROZEN_VALID` is impossible until a real immutable implementation-source commit and implementation-subject manifest exist and are resolved by the validator.
- All source review is exact-head-bound.

---

### Task 1: Runtime decision and package boundary

**Files:**
- Create: `docs/implementation/IMPLEMENTATION_DECISION_RECORD_V1.md`
- Create: `pyproject.toml`
- Create: `src/noema/__init__.py`
- Test: `tests/test_package_boundary.py`

**Interfaces:**
- Consumes: approved research parent and I0/I1 authority.
- Produces: importable `noema` package and an explicit runtime/dependency decision record.

- [ ] **Step 1: Write the failing package-boundary test**

```python
from importlib.metadata import version


def test_runtime_dependencies_are_exactly_supported():
    assert version("jsonschema") == "4.26.0"
    assert version("pytest") == "9.0.2"


def test_noema_package_imports():
    import noema
    assert noema.__all__ == []
```

- [ ] **Step 2: Run the test and verify RED**

Run: `PYTHONPATH=src pytest -q tests/test_package_boundary.py`
Expected: dependency assertions pass and `import noema` fails because `src/noema` does not exist.

- [ ] **Step 3: Add the minimal package/config and decision record**

`pyproject.toml` must declare Python `>=3.13,<3.14`, runtime dependency `jsonschema==4.26.0`, test dependency `pytest==9.0.2`, and no other third-party dependencies. `src/noema/__init__.py` contains only `__all__: list[str] = []`.

The decision record must classify Python/jsonschema/pytest as implementation choices, state that no framework choice is research evidence, record canonical JSON as UTF-8 JSON with sorted keys and compact separators, and prohibit network/runtime services.

- [ ] **Step 4: Run GREEN**

Run: `PYTHONPATH=src pytest -q tests/test_package_boundary.py`
Expected: `2 passed`.

- [ ] **Step 5: Commit**

Commit message: `Initialize minimal Noema implementation runtime`.

---

### Task 2: Immutable provenance and implementation-subject admissibility

**Files:**
- Create: `src/noema/provenance.py`
- Test: `tests/test_provenance.py`

**Interfaces:**
- Produces: `canonical_json_bytes(value) -> bytes`, `sha256_hex(data) -> str`, immutable `ArtifactRef`, `ArtifactRecord`, `ImplementationSubjectManifest`, and `DictArtifactResolver.resolve(ref)`.

- [ ] **Step 1: Write failing provenance tests**

```python
from noema.provenance import ArtifactRef, ArtifactRecord, DictArtifactResolver, canonical_json_bytes, sha256_hex


def test_canonical_json_is_order_independent():
    assert canonical_json_bytes({"b": 2, "a": 1}) == b'{"a":1,"b":2}'


def test_resolver_rejects_digest_mismatch():
    data = b"abc"
    ref = ArtifactRef(repository="thebrazenbeard/noema", commit="a" * 40, path="src/x.py", sha256="0" * 64)
    resolver = DictArtifactResolver({(ref.repository, ref.commit, ref.path): ArtifactRecord(data=data)})
    try:
        resolver.resolve(ref)
    except ValueError as exc:
        assert "sha256" in str(exc)
    else:
        raise AssertionError("digest mismatch accepted")


def test_design_only_subject_is_not_implementation():
    from noema.provenance import ImplementationSubjectManifest
    subject = ImplementationSubjectManifest(source_paths=("docs/working-design/x.md",), test_paths=("tests/test_x.py",), instrumentation_paths=())
    assert subject.is_implementation_subject() is False
```

- [ ] **Step 2: Run RED**

Run: `PYTHONPATH=src pytest -q tests/test_provenance.py`
Expected: collection fails because `noema.provenance` does not exist.

- [ ] **Step 3: Implement minimal provenance types**

Use frozen dataclasses, strict 40-hex commit validation, optional 64-hex SHA-256 validation, exact repository/commit/path lookup, and digest verification when declared. `ImplementationSubjectManifest.is_implementation_subject()` is true only when at least one path begins `src/`, at least one begins `tests/`, and at least one instrumentation path is present.

- [ ] **Step 4: Run GREEN**

Run: `PYTHONPATH=src pytest -q tests/test_provenance.py`
Expected: all provenance tests pass.

- [ ] **Step 5: Commit**

Commit message: `Add immutable implementation provenance boundary`.

---

### Task 3: Learner/evaluator boundary and pre-outcome tickets

**Files:**
- Create: `src/noema/boundary.py`
- Test: `tests/test_boundary.py`

**Interfaces:**
- Produces: `LearnerEvent`, `InterventionPacket`, `EvaluatorRecord`, `Prediction`, `PredictionTicket`, `ScopeTicket`, and deterministic `commit_prediction(...)` / `commit_scope(...)`.

- [ ] **Step 1: Write failing boundary tests**

```python
from noema.boundary import LearnerEvent, EvaluatorRecord, Prediction, commit_prediction


def test_learner_event_has_no_evaluator_truth_fields():
    event = LearnerEvent(step=3, channels=(1.0, 2.0), intervention=None)
    assert not hasattr(event, "hidden_family")
    assert not hasattr(event, "score")


def test_prediction_ticket_commitment_is_stable():
    pred = Prediction(mean=(0.0, 1.0), variance=(1.0, 2.0))
    a = commit_prediction("c2", 7, pred)
    b = commit_prediction("c2", 7, pred)
    assert a.commitment == b.commitment
    assert len(a.commitment) == 64


def test_evaluator_record_is_separate_type():
    record = EvaluatorRecord(step=3, hidden_family="F", realized_score=None)
    assert record.hidden_family == "F"
```

- [ ] **Step 2: Run RED**

Run: `PYTHONPATH=src pytest -q tests/test_boundary.py`
Expected: module missing.

- [ ] **Step 3: Implement immutable boundary types**

No learner-visible dataclass may expose a free-form metadata mapping. Commitments use canonical JSON and SHA-256. Variances must be finite and strictly positive; channel values must be finite.

- [ ] **Step 4: Run GREEN**

Run: `PYTHONPATH=src pytest -q tests/test_boundary.py`
Expected: all boundary tests pass.

- [ ] **Step 5: Commit**

Commit message: `Separate learner and evaluator source boundaries`.

---

### Task 4: C1/C2 recurrent probabilistic substrate and bounded replay

**Files:**
- Create: `src/noema/candidates.py`
- Test: `tests/test_c1_c2.py`

**Interfaces:**
- Produces: immutable `GaussianState(mean, variance, count)`, `C1Config(alpha, variance_floor)`, `ReplayConfig(capacity, max_replay_updates_per_event)`, `predict_gaussian(state)`, `transition_c1(state, observation, config)`, `ReplayBuffer`, and `transition_c2_once(...)`.

- [ ] **Step 1: Write failing pure-kernel tests**

```python
from noema.candidates import GaussianState, C1Config, ReplayBuffer, ReplayConfig, predict_gaussian, transition_c1


def test_c1_prediction_reads_only_committed_state():
    state = GaussianState(mean=(1.0, -1.0), variance=(2.0, 3.0), count=5)
    prediction = predict_gaussian(state)
    assert prediction.mean == state.mean
    assert prediction.variance == state.variance


def test_c1_one_step_transition_is_pure_and_bounded():
    state = GaussianState(mean=(0.0,), variance=(1.0,), count=0)
    updated = transition_c1(state, (2.0,), C1Config(alpha=0.25, variance_floor=0.01))
    assert state.mean == (0.0,)
    assert updated.mean == (0.5,)
    assert updated.count == 1
    assert updated.variance[0] >= 0.01


def test_replay_buffer_never_exceeds_capacity():
    buf = ReplayBuffer.empty(ReplayConfig(capacity=2, max_replay_updates_per_event=1))
    buf = buf.append((1.0,)).append((2.0,)).append((3.0,))
    assert buf.items == ((2.0,), (3.0,))
```

- [ ] **Step 2: Run RED**

Run: `PYTHONPATH=src pytest -q tests/test_c1_c2.py`
Expected: module/classes missing.

- [ ] **Step 3: Implement minimal C1/C2 kernel**

C1 is an exponentially weighted diagonal-Gaussian recurrent state. One-step transition updates mean and residual variance with fixed alpha and no external labels. C2 reuses the exact C1 kernel and adds a FIFO bounded raw-observation replay buffer; no priority metadata or evaluator annotations are accepted.

- [ ] **Step 4: Run GREEN**

Run: `PYTHONPATH=src pytest -q tests/test_c1_c2.py`
Expected: all tests pass. This verifies pure one-step mechanics only; do not run a sequence benchmark.

- [ ] **Step 5: Commit**

Commit message: `Implement minimal C1 and bounded-replay C2 kernels`.

---

### Task 5: C4 bounded generic structural candidate

**Files:**
- Modify: `src/noema/candidates.py`
- Test: `tests/test_c4.py`

**Interfaces:**
- Produces: `Dependency`, `StructuralHypothesis`, `C4Config`, `C4State`, `structural_predict(...)`, and `apply_structural_proposal(...)` with proposal enum limited to generic add/remove/replace-orientation/change-scope/split/merge-retire operations.

- [ ] **Step 1: Write failing C4 tests**

```python
from noema.candidates import C4Config, C4State, Dependency, GaussianState, StructuralHypothesis, structural_predict


def test_c4_rejects_semantic_relation_names():
    try:
        Dependency(source=0, target=1, weight=0.5, scope="cause")
    except ValueError as exc:
        assert "semantic" in str(exc).lower()
    else:
        raise AssertionError("semantic structural label accepted")


def test_structural_prediction_is_base_plus_bounded_generic_adjustment():
    base = GaussianState(mean=(1.0, 2.0), variance=(1.0, 1.0), count=0)
    hyp = StructuralHypothesis(handle="h1", dependencies=(Dependency(0, 1, 0.5, "current"),), confidence=1.0)
    state = C4State(base=base, hypotheses=(hyp,))
    pred = structural_predict(state, observation_context=(4.0, 0.0), config=C4Config(max_active_hypotheses=2, max_abs_weight=1.0))
    assert pred.mean == (1.0, 4.0)
```

- [ ] **Step 2: Run RED**

Run: `PYTHONPATH=src pytest -q tests/test_c4.py`
Expected: missing C4 classes/functions.

- [ ] **Step 3: Implement bounded generic structural state**

Reject scope/relation strings containing `cause`, `parent`, `child`, `chain`, `fork`, or `common cause`. Enforce finite bounded weights, no self-edge, hypothesis population cap, confidence in `[0,1]`, and deterministic weighted adjustment. Do not implement exhaustive DAG enumeration.

- [ ] **Step 4: Run GREEN**

Run: `PYTHONPATH=src pytest -q tests/test_c4.py`
Expected: all C4 tests pass.

- [ ] **Step 5: Commit**

Commit message: `Implement bounded generic C4 structural state`.

---

### Task 6: Resource/support ledger and comparator instrumentation

**Files:**
- Create: `src/noema/accounting.py`
- Create: `src/noema/comparator.py`
- Test: `tests/test_accounting_comparator.py`

**Interfaces:**
- Produces: `ResourceLedger`, `SupportClass`, `SupportRecord`, `ComparatorRecord`, `compare_committed_predictions(...)`.

- [ ] **Step 1: Write failing accounting/comparator tests**

```python
from noema.accounting import ResourceLedger, SupportClass, SupportRecord


def test_consumed_unmeasured_resource_is_not_zero():
    ledger = ResourceLedger()
    ledger = ledger.consume("structural_compute", amount=None)
    assert "structural_compute" in ledger.unmeasured_classes


def test_zero_support_cannot_claim_strong_confidence():
    try:
        SupportRecord(SupportClass.ZERO_OR_UNKNOWN_SUPPORT, confidence=0.9)
    except ValueError:
        pass
    else:
        raise AssertionError("zero support accepted strong confidence")
```

- [ ] **Step 2: Run RED**

Run: `PYTHONPATH=src pytest -q tests/test_accounting_comparator.py`
Expected: missing module/classes.

- [ ] **Step 3: Implement accounting and comparator records**

Resource classes are explicit strings from a closed enum: resident memory, durable state, update, query, replay, structural, scope, audition, base-shadow, checkpoint/restart. Missing measurement is retained as unknown, never converted to zero. Comparator records bind candidate IDs, prediction-ticket commitments, resource-condition ID, information-condition ID, opportunity-condition ID, and representation version.

- [ ] **Step 4: Run GREEN**

Run: `PYTHONPATH=src pytest -q tests/test_accounting_comparator.py`
Expected: all tests pass.

- [ ] **Step 5: Commit**

Commit message: `Add auditable resource support and comparator records`.

---

### Task 7: V2 schema plus semantic validator

**Files:**
- Create: `src/noema/validator.py`
- Test: `tests/test_validator.py`

**Interfaces:**
- Produces: `ValidationStatus`, `ValidationFinding`, `ValidationResult`, `validate_manifest(manifest, schema, resolver)`.

- [ ] **Step 1: Write failing validator tests**

```python
from noema.validator import ValidationStatus, validate_manifest


def test_design_only_implementation_subject_cannot_pass(valid_shape_manifest, v2_schema, resolver_with_design_only_subject):
    result = validate_manifest(valid_shape_manifest, v2_schema, resolver_with_design_only_subject)
    assert result.status is ValidationStatus.FAIL_SOURCE_BINDING


def test_missing_bound_artifact_blocks_instead_of_guessing(valid_shape_manifest, v2_schema, empty_resolver):
    result = validate_manifest(valid_shape_manifest, v2_schema, empty_resolver)
    assert result.status is ValidationStatus.BLOCKED_UNAVAILABLE_EVIDENCE


def test_svf1_zero_audition_probability_fails_schema(svf1_manifest_with_zero_audition, v2_schema, empty_resolver):
    result = validate_manifest(svf1_manifest_with_zero_audition, v2_schema, empty_resolver)
    assert result.status is ValidationStatus.FAIL_SCHEMA
```

- [ ] **Step 2: Run RED**

Run: `PYTHONPATH=src pytest -q tests/test_validator.py`
Expected: missing validator.

- [ ] **Step 3: Implement fail-closed validator order**

Validation order: schema; exact artifact availability/digests; implementation-subject admissibility; learner/evaluator information boundary; candidate/comparator condition closure; resource-measurement binding; support/audition checks; lineage state-scope binding; freeze/provenance consistency. First impossible authoritative lookup returns `BLOCKED_UNAVAILABLE_EVIDENCE`; contradictory evidence returns the relevant FAIL status. The validator never returns execution authority.

- [ ] **Step 4: Run GREEN**

Run: `PYTHONPATH=src pytest -q tests/test_validator.py`
Expected: all tests pass.

- [ ] **Step 5: Commit**

Commit message: `Implement fail-closed V2 preregistration validator`.

---

### Task 8: Hostile suite, exact source subject, and source-readiness packet

**Files:**
- Create: `tests/test_hostile_contracts.py`
- Create after source commit is frozen: `implementation/NOEMA_MINIMAL_SUBJECT_V1.json`
- Create after verification: `docs/implementation/SOURCE_READINESS_PACKET_V1.md`

**Interfaces:**
- Produces: hostile deterministic I1 suite and immutable implementation-subject manifest that refers to the exact source commit preceding the manifest commit.

- [ ] **Step 1: Add hostile tests before any corresponding repair**

The hostile suite must exercise at least: evaluator truth injection rejected; semantic C4 labels rejected; replay capacity enforced; unmeasured consumed resource preserved; zero-support confidence rejected; design-only implementation subject rejected; missing normative artifact blocks; wrong digest fails; branch-like non-40-hex commit rejected; SVF-1 null/zero audition rejected by schema; and source manifest cannot claim docs-only source.

- [ ] **Step 2: Run the hostile suite and verify any new test is RED for the intended missing guard**

Run: `PYTHONPATH=src pytest -q tests/test_hostile_contracts.py`
Expected: each newly introduced guard must fail before its implementation repair; do not accept tests that pass on first introduction.

- [ ] **Step 3: Implement only the minimal guard needed for each RED case, rerunning to GREEN after each**

Run after each change: `PYTHONPATH=src pytest -q tests/test_hostile_contracts.py`.

- [ ] **Step 4: Run the full deterministic I1 suite**

Run: `PYTHONPATH=src pytest -q`
Expected: all tests pass, no warnings generated by Noema source, no network access, no developmental trajectory, no model training, no experiment execution.

- [ ] **Step 5: Freeze the source head and create implementation subject manifest in a subsequent commit**

The JSON manifest must bind:
- `research_parent_commit = be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33`;
- exact source commit SHA from Step 4;
- source paths under `src/noema/`;
- test paths under `tests/`;
- instrumentation paths for accounting/comparator/validator;
- runtime versions Python 3.13.5, jsonschema 4.26.0, pytest 9.0.2;
- explicit `training_executed=false`, `experiment_executed=false`, `hosted_compute_used=false`.

- [ ] **Step 6: Re-run full I1 suite against the manifest-bearing checkout**

Run: `PYTHONPATH=src pytest -q`
Expected: same passing count; manifest addition must not change behavior.

- [ ] **Step 7: Write source-readiness packet**

Record exact research parent, exact source commit, manifest commit, changed-file inventory, dependency versions, test command/count, explicit checks not run because E0 is withheld, and authority ceiling. Label only `SOURCE_IMPLEMENTATION_REVIEW`, never behavioral qualification.

- [ ] **Step 8: Open/update private Draft implementation PR and mirror sanitized provenance to Bus**

PR base: `work/noema-representation-drift-scope-20260906` so the implementation remains stacked on the canonical private research line. PR must remain Draft/unmerged. Bus receives only source/PR/head/status/authority pointers, not confidential mechanism detail.

---

## Plan Self-Review

- Spec coverage: runtime choice, learner/evaluator separation, C1/C2/C4, replay, generic structure, comparator tickets, resource/support ledger, V2 validator, implementation-subject manifest, hostile tests, source-readiness evidence, and authority separation are each assigned to a task.
- Placeholder scan: no `TBD`, `TODO`, or deferred implementation language is used for an authorized I0/I1 deliverable.
- Type consistency: `Prediction` originates in `noema.boundary`; provenance references are resolved in `noema.provenance`; validator consumes both without circular imports; candidate kernels do not import evaluator types.
- Execution ceiling: no task authorizes curriculum loops, empirical scoring, persistent developmental checkpoints, SVF execution, model training, merge, deployment, publication, or hosted/paid compute.
