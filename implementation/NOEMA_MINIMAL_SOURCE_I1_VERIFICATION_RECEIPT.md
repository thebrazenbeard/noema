# Noema Minimal Source — I1 Deterministic Verification Receipt

Classification: **IP_CONFIDENTIAL**

Status: **I0 SOURCE FROZEN / I1 COMPOSITE DETERMINISTIC VERIFICATION PASS / NO E0 OR P0 AUTHORITY**

Date: 2026-09-18

Research parent: `be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33`

Final hardened source/test/config commit: `b376526e32945c6a7688b3ef7b0312881aede5de`

Implementation subject manifest:
- path: `implementation/NOEMA_MINIMAL_SUBJECT_V1.json`
- commit: `37f8f8f96018bf44e1daca9e987a8520d8ca12de`
- Git blob: `b43e32f9eeb40f42517cc19db6d675e2e5f80d6f`
- binds `source_commit=b376526e32945c6a7688b3ef7b0312881aede5de`

Support V5:
- commit: `ade4aa6eb84e2a7fc695fb85ee441fe1425506ac`
- bundle: `implementation/svf0/SUPPORT_BUNDLE_V5.json`
- bundle Git blob: `ca357087616c790b1087aecd484b98bc38dde757`

Current inert preregistration:
- logical subject: `NOEMA_SVF0_RECURRENT_GATE1_V4`
- path: `implementation/svf0/SVF0_PREREGISTRATION_V2_R5.json`
- commit: `5d5db9a299cacd6f30766cee6b1de6d02f51586b`
- Git blob: `afb0d9d5ce93afd2a95d6bc7a000c6da6f7d658b`

## Exact inventory

At the final source line:
- **14** deterministic test files;
- **103** `test_*` cases present;
- **0 known failures**.

The local exact reconstruction available in this runtime contains the hardened execution/evaluation slice, not every legacy private-repository module. Therefore this receipt does **not** claim a clean 103/103 full-suite rerun.

## Focused I1 execution/evaluation verification

The exact execution/evaluation slice was run without entering a valid E0 learner trajectory:

- runner: **8 tests**;
- deterministic statistics: **9 tests**;
- E0 experiment/plan guard: **8 tests**;
- Gate-1 evaluator/provenance integrity: **9 tests**;
- focused total: **34/34 PASS**.

The focused verification covers:
- prediction commitment before outcome reveal;
- identical learner-visible outcome for C1/C2;
- C2 live update followed by at most one **strictly prior** replay update;
- the just-stored current transition is not same-step replay eligible;
- reset-reference statelessness;
- SVF-0 intervention rejection;
- real process RSS / working-set resource accounting and whole-point fail-closed invalidation;
- per-channel Gaussian NLL persistence;
- exact frozen seeds, world parameters, learner parameters, replay limits, and resource envelope;
- deterministic experiment-plan commitment;
- E0 denial before world generation when authority is absent or mismatched;
- frozen score windows;
- n=8 Student-t confidence intervals and exact df=7 two-sided p-values;
- Holm-Bonferroni step-down decisions;
- persistence, adaptation, stable-retention, negative-control, six-flag kill, and overall Gate-1 evaluation;
- prediction-ticket commitment recomputation;
- per-channel and total Gaussian-NLL recomputation;
- candidate/outcome/resource evidence consistency;
- logical-subject and plan-commitment consistency through top-level experiment result evaluation.

The valid E0 subject+seed path was **not executed**.

## Manifest qualification

R4 historical rejected attempt:
- path: `implementation/svf0/SVF0_PREREGISTRATION_V2_R4.json`
- commit: `8457f594ccd0e13890f7a91da47454fcd9188561`
- Git blob: `e2b3d7788894be10a11d7da828d09bc654005254`
- canonical V2 schema result: **FAIL / 2 errors** because two redundant strict-prior fields were outside the closed schema.
- no schema weakening was performed; the extra detail remains immutably represented in support V5 / execution policy V3.

Current R5:
- canonical V2 JSON-Schema validation: **PASS / 0 errors**;
- independent semantic/provenance mirror: **PASS / 0 findings**;
- parameter-distribution SHA-256: `7f9975815d669f3312f45cba4d2020ce84e2eefd1567f5bf60310be42b5251f2`;
- seed-manifest SHA-256: `f68ee0307f9a7e9d735a0893c0c7c65bda938682e9d668bdd6bf5ccb2818dd5b`.

The Python implementation validator has **not** been directly executed against the exact R5 manifest in this runtime. Therefore this receipt does not claim `PASS_FROZEN_VALID`.

## Scientific hardening completed before freeze

The V4 subject closes defects found during hostile implementation review:
- real process resident-memory measurement replaces Python-allocation peak as the resident-memory axis;
- recurrent prediction uses one-step-lagged observable context;
- the world dependency is one-step lagged so pre-outcome prediction can actually test temporal dependency learning;
- C2 replay cannot reuse the just-observed current transition in the same step;
- the exact plan is content-addressed and seed results bind subject + plan commitment;
- required per-channel diagnostics are computable;
- Student-t p-values actually exist for Holm correction;
- evaluation recomputes commitments and scores rather than trusting stored evidence.

## Authority ceiling

This receipt does **not** authorize or claim:
- E0 learning/training/experiment execution;
- empirical Gate-1 results;
- merge or deployment;
- publication;
- paid/hosted compute;
- provider/credential/ruleset mutation;
- repository-visibility change;
- protected-system connection;
- BT2 R1 remediation/requalification.

Any source/test/config mutation after `b376526e32945c6a7688b3ef7b0312881aede5de` creates a new source subject and requires fresh I1 qualification.
