# Noema Minimal Source — I1 Deterministic Verification Receipt

Classification: **IP_CONFIDENTIAL**

Status: **I0 SOURCE FROZEN / I1 EXACT VERIFICATION PASS / PASS_FROZEN_VALID / NO E0 OR P0 AUTHORITY**

Date: 2026-09-18

Research parent: `be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33`

Final frozen source/test/config commit: `dcd8bed41b7ac3d7e41be5baed9ec31dcf7e76e7`

Implementation subject manifest:
- path: `implementation/NOEMA_MINIMAL_SUBJECT_V1.json`
- commit: `9b4797aa0bb664a1db17a3ef09288b6d2909b2d1`
- Git blob: `7892a2b9e1779fb5c31209bca0b9d1037bc9e2d2`

Support V6:
- commit: `45e6d6b42921e90e57be2ef4678836418e6bd295`
- bundle: `implementation/svf0/SUPPORT_BUNDLE_V6.json`
- bundle Git blob: `b2ae8995aa210363a4e88c96e06919610e6fce30`

Current inert preregistration:
- logical subject: `NOEMA_SVF0_RECURRENT_GATE1_V5`
- path: `implementation/svf0/SVF0_PREREGISTRATION_V2_R6.json`
- commit: `7975e3678939c6b0d04e9fa85997c3c244c900d6`
- Git blob: `785c481b1365ae88d965ee17b538173646c858ca`

Exact validator execution receipt:
- path: `implementation/svf0/SVF0_VALIDATOR_EXECUTION_RECEIPT_V1.json`
- commit: `c497d8b17acb64379884b33c21d0fceb2247e1c9`

## Exact full-suite verification

A detached worktree was checked out at the exact current source lineage on the user-controlled Windows machine and executed with the frozen runtime:
- Windows;
- CPython **3.13.5**;
- jsonschema **4.26.0**;
- pytest **9.0.2**.

At final frozen source `dcd8bed41b7ac3d7e41be5baed9ec31dcf7e76e7`:
- deterministic tests present: **103**;
- deterministic tests executed: **103**;
- passed: **103**;
- failed: **0**;
- exact tracked worktree: clean;
- valid E0 learner path executed: **false**.

Final run: **103/103 PASS**.

## Windows resident-memory defect found and repaired

The first exact Windows/Python-3.13.5 full-suite run exposed a real defect: the Windows `GetCurrentProcess` / `GetProcessMemoryInfo` ctypes calls relied on implicit signatures, causing the real-process resident-memory path to fail on 64-bit Python.

The source was repaired to use explicit Windows ABI types:
- `HANDLE` for the process handle;
- `DWORD` for size/count fields;
- `BOOL` return type;
- explicit `argtypes` / `restype`;
- last-error reporting enabled.

Corrected accounting source Git blob:
`2be0259949e977f303ddd9f09d2b390de1707ccb`

The complete exact suite then passed 103/103 at the final V5 source.

## Exact R6 qualification

Canonical V2 JSON Schema:
- **PASS / 0 errors**

Independent semantic/provenance mirror:
- **PASS / 0 findings**

Actual repository implementation validator:
- implementation: `src/noema/validator.py::validate_manifest`
- validator Git blob: `6a03912cf7160ece2f2b373a6a3dc379783697e6`
- immutable resolver records loaded: **22**
- artifact source: exact Git objects by immutable `commit:path`
- status: **PASS_FROZEN_VALID**
- findings: **0**

This is no longer a mirror-only or composite qualification claim.

## Frozen scientific/implementation properties

The current subject binds:
- recurrent one-step conditional prediction over previous opaque observation;
- one-step-lagged SVF-0 world dependency;
- matched C2 bounded replay with strictly-prior eligibility;
- no same-step replay of the just-observed transition;
- stateless reset reference;
- pre-outcome prediction commitments;
- real process peak RSS / working-set accounting;
- 256 MiB fixed resident-memory envelope;
- whole-point fail-closed resource invalidation;
- per-channel Gaussian NLL evidence;
- n=8 Student-t confidence intervals and exact df=7 two-sided p-values;
- Holm-Bonferroni correction;
- exact frozen-plan commitment;
- evaluator recomputation of prediction commitments and channel/total scores;
- logical-subject and plan-commitment integrity through top-level evaluation;
- E0 authority guard before world execution.

## Historical preregistration provenance

Historical R4 rejected schema attempt remains preserved:
- commit `8457f594ccd0e13890f7a91da47454fcd9188561`
- canonical schema: FAIL / 2 closed-schema errors
- schema was not weakened.

R5:
- commit `5d5db9a299cacd6f30766cee6b1de6d02f51586b`
- was schema-clean and semantically valid for the prior source;
- is now historical because the Windows ABI source correction created a new exact subject.

R6 is the current preregistration for the corrected V5 source.

## Implementation-subject staleness scope

Implementation I1 currentness is governed by the frozen machine-readable scope contract:

- path: `governance/IMPLEMENTATION_SUBJECT_SCOPE_V1.json`
- commit: `aa554f2eccd8622de99d3084b1c953808f280d9b`
- Git blob: `075e3d8e30b8827d3328874a8964cb80466f30c6`
- rule: `MANIFEST_ENUMERATED_IMPLEMENTATION_PATH_SET_V1`
- unique implementation qualification paths: **33**

The exact implementation qualification path set is the union of the bound subject manifest's `source_paths`, `test_paths`, and `instrumentation_paths`.

A post-freeze commit makes implementation I1 stale **only if it changes one or more paths in that frozen exact union**. Governance/currentness files, verification receipts, support bundles, preregistration manifests, freeze receipts, and validator-execution receipts are separate exact-bound qualification layers unless their paths are also members of the frozen implementation set.

This scope clarification does not alter the frozen source, test surface, scientific plan, or the 103/103 exact I1 result. It makes the previous generic phrase “source/test/config” mechanically precise.

## Authority ceiling

This receipt does **not** authorize or claim:
- E0 learning/training/experiment execution;
- empirical Gate-1 outcomes;
- merge or deployment;
- publication;
- paid/hosted compute;
- provider/credential/ruleset mutation;
- repository-visibility change;
- protected-system connection;
- BT2 R1 remediation/requalification.

No learner trajectory or frozen experiment was executed during I1 qualification.

Any post-freeze mutation to a path in the exact 33-path implementation qualification union defined by `governance/IMPLEMENTATION_SUBJECT_SCOPE_V1.json` creates a new implementation subject and requires fresh exact-head I1 qualification. Qualification-layer changes outside that path set are separately exact-bound and do not by themselves stale implementation I1.
