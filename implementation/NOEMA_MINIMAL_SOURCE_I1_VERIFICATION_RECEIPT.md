# Noema Minimal Source — I1 Deterministic Verification Receipt

Classification: **IP_CONFIDENTIAL**

Status: **I0 SOURCE FROZEN / I1 COMPOSITE DETERMINISTIC VERIFICATION PASS / NO E0 OR P0 AUTHORITY**

Date: 2026-09-18

Research parent: `be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33`

Corrected frozen implementation source/test/config commit: `8460f5e279c0178d6305e115cbb5ddcb29bebf03`

Corrected recurrent SVF-0 support commit: `d44bfb26764571aaf8ff8f3d156d3a449f65f120`

Implementation subject manifest:
- `implementation/NOEMA_MINIMAL_SUBJECT_V1.json`
- binds `source_commit=8460f5e279c0178d6305e115cbb5ddcb29bebf03`

## Verification evidence

Verification mode: **COMPOSITE_I1_WITH_EXACT_GITHUB_SOURCE_BINDING**

Exact source inventory:
- 10 deterministic test files;
- 69 `test_*` cases present at the corrected source commit;
- 0 known deterministic failures.

Executed deterministic slices:
- validator-facing V2 closure: 22/22 PASS before the subject-specific resource correction;
- recurrent C1/C2 mechanics: 5/5 PASS;
- lagged SVF-0 world mechanics: 2/2 PASS;
- meter/reset/replay-selector mechanics: 5/5 PASS;
- first-core metric-profile semantics: 1/1 PASS;
- corrected real process-resident-memory path: 2/2 PASS.

The resident-memory repair is material:
- the earlier subject incorrectly used `tracemalloc` Python allocation peak as the resident-memory measure;
- the corrected source measures process peak resident set / peak working set;
- Python allocation peak remains a separate diagnostic and is never substituted for resident memory;
- local deterministic measurement confirmed a real process peak well above the superseded 8 MiB envelope, so that old resource subject is not carried forward;
- support V3 freezes a 256 MiB resident-memory ceiling.

Scientific subject:
- recurrent linear-Gaussian C1 over the previous opaque observation;
- same-base C2 plus bounded opaque transition-pair replay;
- deterministic most-recent replay selector;
- stateless reset reference;
- one-step-lagged primary and negative-control worlds;
- fail-closed resource adjudication;
- subject-specific first-core metric profile.

Limitation:
- this sandbox cannot obtain a clean authenticated checkout of the private repository;
- no hosted CI, paid compute, learner trajectory, training loop, or experiment was used;
- therefore this is a composite I1 source-verification receipt, not a clean-checkout qualification claim.

## Authority ceiling

This receipt does **not** authorize or claim E0 learning/training/experiment execution, paid/hosted compute, deployment, merge, publication, repository-visibility change, provider/credential/ruleset mutation, protected-system connection, empirical architecture advantage, or BT2 R1 remediation/requalification.

Any source/test/config change after `8460f5e279c0178d6305e115cbb5ddcb29bebf03` creates a new source subject and requires fresh I1 verification before inheriting this PASS.
