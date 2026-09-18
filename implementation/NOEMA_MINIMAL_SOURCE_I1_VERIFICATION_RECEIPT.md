# Noema Minimal Source — I1 Deterministic Verification Receipt

Classification: **IP_CONFIDENTIAL**

Status: **I0 SOURCE FROZEN / I1 DETERMINISTIC VERIFICATION PASS / NO E0 OR P0 AUTHORITY**

Date: 2026-09-18

Research parent: `be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33`

Implementation branch: `impl/noema-minimal-source-i0-20260913`

Frozen implementation source commit: `22d280a65dfae772a9651213392cabafd374d07b`

Implementation subject manifest:
- `implementation/NOEMA_MINIMAL_SUBJECT_V1.json`
- binds `source_commit=22d280a65dfae772a9651213392cabafd374d07b`

## Verification evidence

A clean local reconstruction was made from the exact GitHub branch bytes for the source/test surfaces.

Runtime:
- Python 3.13.5
- jsonschema 4.26.0
- pytest 9.0.2

Deterministic suite:
- 32 tests collected
- 32 passed
- 0 failed

Independent Git-object identity check:
- 15 source/test files used by the suite were rehashed with the Git blob preimage rule `sha1("blob " + len + NUL + bytes)`
- 15/15 local blob IDs matched the exact GitHub blob IDs
- 0 mismatches

The passing suite includes:
- C1 immutable one-step prediction/update behavior;
- C2 bounded raw replay storage and explicit bounded replay updates;
- C4 generic structural proposal semantics, semantic-label rejection, population caps, C2/C4 base/replay parity, and structural-state preservation across replay;
- learner/evaluator boundary separation and pre-outcome commitments;
- resource/support accounting;
- immutable SHA-256 and Git-blob provenance checks;
- V2 source-subject binding;
- world commitment/preimage checks;
- primary-metric comparator referential closure;
- fail-closed unavailable evidence handling.

## Authority ceiling

This receipt is source-verification evidence only.

It does **not** authorize or claim:
- learning/training;
- developmental trajectories;
- experiment execution;
- paid/hosted compute;
- deployment;
- merge;
- publication;
- repository-visibility change;
- provider/credential/ruleset mutation;
- protected-system connection;
- empirical architecture advantage;
- BT2 R1 remediation or requalification.

Any source change after `22d280a65dfae772a9651213392cabafd374d07b` creates a new implementation source subject and requires fresh I1 verification before inheriting this PASS.
