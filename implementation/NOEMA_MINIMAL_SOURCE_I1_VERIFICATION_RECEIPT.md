# Noema Minimal Source — I1 Deterministic Verification Receipt

Classification: **IP_CONFIDENTIAL**

Status: **I0 SOURCE FROZEN / I1 DETERMINISTIC VERIFICATION PASS / NO E0 OR P0 AUTHORITY**

Date: 2026-09-18

Research parent: `be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33`

Implementation branch: `impl/noema-minimal-source-i0-20260913`

Frozen implementation source/test commit: `0fc57c1d8023e0bc1cd4d48e63002f7131e2c563`

Implementation subject manifest:
- `implementation/NOEMA_MINIMAL_SUBJECT_V1.json`
- binds `source_commit=0fc57c1d8023e0bc1cd4d48e63002f7131e2c563`

## Verification evidence

Verification mode: **COMPOSITE_EXACT_BLOB_I1**

- 55 deterministic test cases are covered.
- 22 validator-facing cases were executed against the exact persisted validator bytes after full-V2 closure hardening.
- 22/22 changed-surface cases passed.
- The remaining 33 cases and their production dependencies are byte-identical to the previously verified 50/50 source subject; their prior deterministic PASS therefore remains applicable to those unchanged bytes.
- 0 known deterministic failures remain.
- 17/17 implementation source/test Git blob identities are accounted for; 0 mismatches.
- current validator blob: `1ed559616db8d964c62d40cb454e2959527eb0e0`
- current hostile-test blob: `f3719280c710cabb60acd34a02007341d616d9c5`

The changed-surface verification includes exact research-tuple binding, SVF-0/SVF-1 stage closure, closed learner/evaluator transport schemas, C1/C2 replay-isolation identity, resource-meter fail-closed semantics, operational rule decidability, commitment/source binding, and the earlier hostile validator cases.

No learner trajectory, training loop, developmental experiment, or hosted compute was executed to obtain this receipt.

## Authority ceiling

This receipt is source-verification evidence only. It does **not** authorize or claim learning/training, developmental trajectories, experiment execution, paid/hosted compute, deployment, merge, publication, repository-visibility change, provider/credential/ruleset mutation, protected-system connection, empirical architecture advantage, or BT2 R1 remediation/requalification.

Any implementation source/test change after `0fc57c1d8023e0bc1cd4d48e63002f7131e2c563` creates a new source subject and requires fresh I1 verification before inheriting this PASS.
