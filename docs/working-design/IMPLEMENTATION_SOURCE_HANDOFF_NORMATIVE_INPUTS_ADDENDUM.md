# Implementation-Source Handoff — Normative Inputs Addendum

Classification: **IP_CONFIDENTIAL**

Status: **NORMATIVE COMPANION TO `IMPLEMENTATION_SOURCE_HANDOFF_AND_AUTHORITY_BOUNDARY.md` / INERT RESEARCH-SOURCE ARTIFACT / NO IMPLEMENTATION OR EXECUTION AUTHORITY**

Date: 2026-09-13

Parent handoff commit: `034674bb1cada677b7c2ff2216d18ad4abf68ccc`.

## 1. Purpose

The implementation-source handoff defines a future authority boundary. This addendum prevents that handoff from becoming an accidental mechanism for selecting stale research artifacts, reviving superseded V1 preregistration rules, or silently amending the research contract during source implementation.

## 2. Normative research input set

A future implementation-source lane must resolve its obligations from the exact immutable research parent it is authorized to use. At the current research line, the implementation-relevant normative set includes:

- `MINIMAL_STRUCTURAL_VALUE_FALSIFICATION_FAMILY.md`
- `C2_C4_COMPARATOR_INTERFACE_CONTRACT.md`
- `C0_C4_FAIR_COMPARISON_AND_CLAIM_BOUNDARY_MATRIX.md`
- `EXPERIMENT_SCOPE_SUPPORT_AND_AUDITION_LEDGER.md`
- `PREQUENTIAL_SCOPE_APPLICABILITY_CONTRACT.md`
- `REPRESENTATION_DRIFT_SCOPE_CONTINUITY_CONTRACT.md`
- `EXPERIMENT_LINEAGE_AND_STATE_TRANSFER_CONTRACT.md`
- `EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V2.json`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_CONTRACT_V2.md`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_RESOURCE_ADDENDUM.md`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_DECIDABILITY_ADDENDUM.md`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_COMPARATOR_MATRIX_ADDENDUM.md`
- `EXPERIMENT_RESOURCE_FRONTIER_SERIES_CONTRACT.md`
- `DEVELOPMENTAL_INTERFACE_VALIDATION_CONTRACT.md`
- `DIAGNOSTIC_INTERPRETER_BOUNDARY.md`
- `IMPLEMENTATION_SOURCE_HANDOFF_AND_AUTHORITY_BOUNDARY.md`
- this addendum.

The source lane must resolve these from the authorized exact parent commit, not from whichever branch happens to have the same filenames later.

This list identifies the minimum implementation-facing dependency set; it does not erase other private research artifacts that those files themselves normatively reference.

## 3. Supersession rule

`EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V1.json` and the V1 validator contract remain historical provenance only for future implementation work.

They must not be used to validate a new implementation subject where V2 applies. A source implementation may include migration or historical-compatibility tests only if they are clearly labeled non-normative and cannot produce a current `PASS_FROZEN_VALID` result.

No source lane may quietly combine permissive V1 behavior with V2 labels.

## 4. Precedence and contradiction rule

The handoff files describe how a future source lane is bounded. They do **not** amend the scientific or evidential meaning of the research contracts above.

If the handoff wording and a normative research contract can reasonably be read differently, the implementation lane must stop and obtain research adjudication rather than choosing the interpretation that is easiest to implement.

If two research artifacts appear contradictory, the lane must use exact-head provenance and the recorded adjudications to determine whether one is superseded. If the conflict remains unresolved, implementation is blocked until the research line resolves it.

An implementation convenience, framework limitation, test shortcut, or runtime default is never sufficient authority to weaken a research invariant.

## 5. No implicit implementation architecture

The normative input set constrains evidence, fairness, information boundaries, support, provenance, resources, scope, transfer, and validation semantics. It does not approve a language, framework, optimizer, package topology, numerical library, serialization library, or concrete learner realization beyond what the research contracts explicitly require.

A future implementation decision record must therefore distinguish:

- **research-required behavior**;
- **implementation choice**;
- **testing convenience**;
- **evaluator-only machinery**.

Only the first category may be presented as inherited project requirement.

## 6. Head-movement rule

Any research-head movement after an implementation lane is opened invalidates assumptions that the new head is interchangeable with the authorized parent.

The implementation lane may continue against its exact frozen parent unless fresher authority changes that parent. It must not silently rebase onto moving PR #32 and carry forward a prior review PASS.

Likewise, a new research artifact does not automatically apply retroactively to an already frozen implementation subject.

## 7. Authority ceiling

This addendum does not grant implementation-source authority, deterministic test authority, learning/training authority, experiment-execution authority, merge authority, or any other protected effect.

It exists only to make a future separately authorized implementation lane provenance-safe and semantically bounded.
