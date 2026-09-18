# Noema Minimal Source — I1 Deterministic Verification Receipt

Classification: **IP_CONFIDENTIAL**

Status: **I0 SOURCE FROZEN / I1 COMPOSITE DETERMINISTIC VERIFICATION PASS / NO E0 OR P0 AUTHORITY**

Date: 2026-09-18

Research parent: `be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33`

Implementation branch: `impl/noema-minimal-source-i0-20260913`

Frozen implementation source/test/config commit: `9eb234f07e85b20b7c801ed5c8f0bac55a1633a1`

Implementation subject manifest:
- `implementation/NOEMA_MINIMAL_SUBJECT_V1.json`
- binds `source_commit=9eb234f07e85b20b7c801ed5c8f0bac55a1633a1`

## Verification evidence

Verification mode: **COMPOSITE_I1_WITH_EXACT_GITHUB_SOURCE_BINDING**

Covered deterministic cases: **67**
Known deterministic failures: **0**

Evidence slices:
- 22/22 validator-facing cases passed against exact persisted validator bytes after V2 closure hardening.
- 5/5 recurrent C1/C2 mechanics checks passed for committed-state prediction, first-context establishment, conditional weight update, C1/C2 live-kernel parity, and bounded replay without live-context mutation.
- 2/2 lagged SVF-0 world checks passed for preregistered regime change and stable unrelated dependency.
- 5/5 newly added meter/reset/replay-selector mechanics checks passed.
- Previously verified compatibility surfaces remain structurally preserved; legacy EWMA/C4 APIs were retained rather than rewritten.

Scientific repair:
- C1 is no longer represented by the legacy per-channel EWMA for SVF-0.
- The SVF-0 base is now a recurrent linear-Gaussian predictor over the previous opaque observation.
- C2 is the same recurrent base plus bounded opaque transition-pair replay.
- The SVF-0 world now uses one-step-lagged dependencies, so the dependency target is predictable from information committed before the outcome is revealed.
- A stateless reset reference exists for the required cross-time persistence control.
- Resource measurement and replay selection are implemented source, not prose-only conventions.

Limitation:
- this sandbox cannot resolve github.com from its local execution environment, so a clean local clone of the private repository could not be run;
- hosted CI/paid compute was not used because E0/P0 remain closed;
- therefore this receipt is explicitly composite, not a clean-checkout qualification claim.

No learner trajectory, training loop, developmental experiment, or hosted compute was executed.

## Authority ceiling

This receipt is source-verification evidence only. It does **not** authorize or claim learning/training, developmental trajectories, experiment execution, paid/hosted compute, deployment, merge, publication, repository-visibility change, provider/credential/ruleset mutation, protected-system connection, empirical architecture advantage, or BT2 R1 remediation/requalification.

Any implementation source/test/config change after `9eb234f07e85b20b7c801ed5c8f0bac55a1633a1` creates a new source subject and requires fresh I1 verification before inheriting this PASS.
