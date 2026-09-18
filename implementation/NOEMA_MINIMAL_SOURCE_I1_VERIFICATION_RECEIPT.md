# Noema Minimal Source — I1 Deterministic Verification Receipt

Classification: **IP_CONFIDENTIAL**

Status: **I0 SOURCE FROZEN / I1 DETERMINISTIC VERIFICATION PASS / NO E0 OR P0 AUTHORITY**

Date: 2026-09-18

Research parent: `be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33`

Implementation branch: `impl/noema-minimal-source-i0-20260913`

Frozen implementation source commit: `8ac5512c396c112f7a16ab86dcf63d5d3e6a0b46`

Implementation subject manifest:
- `implementation/NOEMA_MINIMAL_SUBJECT_V1.json`
- binds `source_commit=8ac5512c396c112f7a16ab86dcf63d5d3e6a0b46`

## Verification evidence

A clean local reconstruction was verified against exact GitHub source/test blob identities.

Runtime:
- Python 3.13.5
- jsonschema 4.26.0
- pytest 9.0.2

Deterministic suite:
- 50 tests collected
- 50 passed
- 0 failed

Exact Git-object identity check:
- 17 source/test files used by the suite were hashed with `sha1("blob " + len + NUL + bytes)`
- 17/17 local blob IDs match GitHub
- 0 mismatches
- exact validator blob: `6d521dd1b90806549b427148c8eb6d342e391625`

The suite covers C1/C2/C4 bounded source behavior; learner/evaluator separation; pre-outcome commitments; resource/support accounting; SHA-256 and Git-blob provenance; implementation-source and commitment binding; comparator and variant closure; checkpointed-primary V2 rejection; mechanically decidable primary, negative-control, stopping, kill, world-randomization, resource-measurement, and proper-scoring rules; all normative V2 result classes; and deterministic inert SVF-0 primary/negative-control world plus single-observation Gaussian NLL scoring.

## Authority ceiling

This receipt is source-verification evidence only. It does **not** authorize or claim learning/training, developmental trajectories, experiment execution, paid/hosted compute, deployment, merge, publication, repository-visibility change, provider/credential/ruleset mutation, protected-system connection, empirical architecture advantage, or BT2 R1 remediation/requalification.

Any source/test change after `8ac5512c396c112f7a16ab86dcf63d5d3e6a0b46` creates a new implementation source subject and requires fresh I1 verification before inheriting this PASS.
