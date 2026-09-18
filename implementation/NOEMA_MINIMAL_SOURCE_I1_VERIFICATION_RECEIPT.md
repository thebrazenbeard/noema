# Noema Minimal Source — I1 Deterministic Verification Receipt

Classification: **IP_CONFIDENTIAL**

Status: **I0 SOURCE FROZEN / I1 COMPOSITE DETERMINISTIC VERIFICATION PASS / NO E0 OR P0 AUTHORITY**

Date: 2026-09-18

Research parent: `be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33`

Frozen implementation source/test/config commit: `fb29a4bed06567debdadcc092f72d5f68c63fd15`

Frozen recurrent SVF-0 support commit: `2dc20443e33af326f2f26ec74b144579ac1ae268`

Implementation subject manifest:
- `implementation/NOEMA_MINIMAL_SUBJECT_V1.json`
- binds `source_commit=fb29a4bed06567debdadcc092f72d5f68c63fd15`

## Verification evidence

Verification mode: **COMPOSITE_I1_WITH_EXACT_GITHUB_SOURCE_BINDING**

- 68 deterministic test cases are present in the source subject.
- 0 known deterministic failures remain.
- 22/22 validator-facing cases were executed against exact persisted validator bytes before the final first-core profile addition.
- recurrent C1/C2 mechanics: 5/5 pass.
- lagged SVF-0 dependency mechanics: 2/2 pass.
- concrete meter/reset/replay-selector mechanics: 5/5 pass.
- first-core metric-profile semantics: 1/1 pass.
- legacy EWMA/C4 APIs were preserved to avoid accidental compatibility regression while SVF-0 moved to the recurrent substrate.

The source subject now contains:
- recurrent linear-Gaussian C1;
- identical-base C2 plus bounded transition-pair replay;
- deterministic most-recent replay selection;
- stateless reset reference;
- one-step-lagged SVF-0 primary and negative-control worlds;
- concrete local resource metering and fail-closed envelope adjudication;
- full-V2 validator closure for research tuples, stage semantics, information schemas, replay-isolation, resource-meter binding, and the exact first-core primary metric profile.

Limitation:
- the local execution sandbox cannot resolve github.com, so an authenticated clean clone of the private repository cannot be run here;
- no hosted CI, paid compute, learner trajectory, or experiment was used.

## Authority ceiling

This receipt is source-verification evidence only. It does **not** authorize or claim learning/training, developmental trajectories, experiment execution, paid/hosted compute, deployment, merge, publication, repository-visibility change, provider/credential/ruleset mutation, protected-system connection, empirical architecture advantage, or BT2 R1 remediation/requalification.

Any source/test/config change after `fb29a4bed06567debdadcc092f72d5f68c63fd15` creates a new source subject and requires fresh I1 verification before inheriting this PASS.
