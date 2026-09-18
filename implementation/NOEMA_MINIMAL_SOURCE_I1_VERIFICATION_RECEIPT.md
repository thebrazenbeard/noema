# Noema Minimal Source — I1 Deterministic Verification Receipt

Classification: **IP_CONFIDENTIAL**

Status: **I0 SOURCE FROZEN / I1 DETERMINISTIC VERIFICATION PASS / NO E0 OR P0 AUTHORITY**

Date: 2026-09-18

Research parent: `be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33`

Implementation branch: `impl/noema-minimal-source-i0-20260913`

Frozen implementation source commit: `3e4ffa49e7038f4326fb5cc74309ee57831347b5`

Implementation subject manifest:
- `implementation/NOEMA_MINIMAL_SUBJECT_V1.json`
- binds `source_commit=3e4ffa49e7038f4326fb5cc74309ee57831347b5`

## Verification evidence

A clean local reconstruction was verified against the exact GitHub source/test blob identities for the frozen source subject.

Runtime:
- Python 3.13.5
- jsonschema 4.26.0
- pytest 9.0.2

Deterministic suite:
- 47 tests collected
- 47 passed
- 0 failed

Exact Git-object identity check:
- 17 source/test files used by the suite were hashed with the Git blob preimage rule `sha1("blob " + len + NUL + bytes)`
- 17/17 local blob IDs match the exact GitHub blob IDs
- 0 mismatches
- exact validator blob: `63d1c884a6fe643d0ddf3a948a02252afd95335f`

The passing suite covers:
- C1 immutable one-step prediction/update behavior;
- C2 bounded raw replay storage and explicit bounded replay updates;
- C4 generic structural proposal semantics, semantic-label rejection, population caps, matched replay behavior, and structure preservation;
- learner/evaluator separation and pre-outcome commitments;
- resource/support accounting;
- immutable SHA-256 and Git-blob provenance;
- V2 implementation-source binding, commitment checks, comparator/reference closure, and variant-parent closure;
- fail-closed checkpointed-primary V2 resource accounting;
- mechanically decidable primary/negative-control/stopping/kill rule syntax;
- all normative V2 result classes;
- deterministic inert SVF-0 world, regime boundary, negative control, and single-observation Gaussian NLL scoring.

## Authority ceiling

This receipt is source-verification evidence only. It does **not** authorize or claim learning/training, developmental trajectories, experiment execution, paid/hosted compute, deployment, merge, publication, repository-visibility change, provider/credential/ruleset mutation, protected-system connection, empirical architecture advantage, or BT2 R1 remediation/requalification.

Any source/test change after `3e4ffa49e7038f4326fb5cc74309ee57831347b5` creates a new implementation source subject and requires fresh I1 verification before inheriting this PASS.
