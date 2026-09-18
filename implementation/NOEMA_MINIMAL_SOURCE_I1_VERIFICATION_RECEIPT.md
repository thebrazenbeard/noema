# Noema Minimal Source — I1 Deterministic Verification Receipt

Classification: **IP_CONFIDENTIAL**

Status: **I0 SOURCE FROZEN / I1 COMPOSITE DETERMINISTIC VERIFICATION PASS / NO E0 OR P0 AUTHORITY**

Date: 2026-09-18

Research parent: `be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33`

Execution-complete frozen source/test/config commit: `6d40befe2ee260586270610c4c9e864a8e84403e`

Support V4 commit: `7d1b3ff7c9c25cc56d16a4f2114e094da7dd5619`

Implementation subject manifest:
- `implementation/NOEMA_MINIMAL_SUBJECT_V1.json`
- binds `source_commit=6d40befe2ee260586270610c4c9e864a8e84403e`

## Exact source inventory

- 13 deterministic test files;
- **88** `test_*` cases present at the frozen source commit;
- **0 known failures**.

## Newly executed I1 verification

The new execution-layer source was verified without running a developmental learner trajectory:

- single-step runner contract: **7/7 PASS**;
- deterministic scoring/statistics primitives: **7/7 PASS**;
- E0 orchestration guard: **5/5 PASS**;
- combined new execution layer: **19/19 PASS**.

The E0 guard tests prove:
- missing E0 authority fails before world generation;
- authority for the wrong logical subject fails before world generation;
- an unfrozen seed fails before world generation;
- the valid subject+seed E0 path was **not executed**.

The single-step runner tests prove:
- C1, C2, and reset prediction tickets commit before outcome reveal;
- C1/C2 receive the same revealed outcome;
- C2 performs live update before at most one bounded replay update;
- reset carries zero durable state;
- SVF-0 intervention packets are rejected;
- resource violations remain fail-closed and invalidate the whole comparison point.

The deterministic statistics tests prove the frozen:
- score windows;
- target-minus-comparator window delta;
- n=8 Student-t interval with df=7 critical value 2.364624251;
- primary persistence effect + support-completeness gate;
- Holm-Bonferroni step-down rule;
- Gate-1 kill semantics.

## Existing source posture

The earlier recurrent, lagged-world, source-binding, resource-meter, and hostile-validator evidence remains applicable only where the exact underlying Git blobs are unchanged. The validator/profile identifier moved to `NOEMA_SVF0_RECURRENT_GATE1_V3`; a clean full-suite rerun was not available in this sandbox and is not claimed.

No learner trajectory, training loop, primary world run, negative-control run, hosted CI, or paid compute was executed.

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

Any source/test/config change after `6d40befe2ee260586270610c4c9e864a8e84403e` creates a new source subject and requires fresh I1 qualification.
