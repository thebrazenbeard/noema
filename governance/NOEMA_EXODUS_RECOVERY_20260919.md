# Noema — ChatGPT Exodus Recovery Checkpoint — 2026-09-19

**STARTING_SNAPSHOT — FRESHNESS REQUIRED BEFORE EFFECT**

Classification: **IP_CONFIDENTIAL**

Checkpoint purpose: retire the Noema work conversation without retaining any dependency on its ChatGPT URL, title, conversation ID, hidden state, or continued accessibility.

## 1. What this retired chat was

This conversation served the private Noema project as a **chat-local engineering / verification execution terminal**. It was not a durable identity, authority source, memory store, or canonical project surface.

Durable worker identity created by this chat: **none**.

Future execution model:
- the **BT2 Coordinator** is the persistent human-facing interface for Noema engineering coordination;
- it may instantiate temporary Noema implementers, reviewers, hostile reviewers, or verification workers from GitHub + Bus state;
- those runtimes are terminals, not persistent identities;
- **do not create or require a successor permanent Noema worker chat**.

Global BT2 worker reconstruction/census is already durable on the Bus:
- `checkpoints/bt2-coordinator/BT2_COORDINATOR_ONE_EXODUS_HANDOFF_R2_20260919T2123-0400.md`
- `checkpoints/one/ONE_EXODUS_FINAL_R2_20260919T2122-0400.md`
on `thebrazenbeard/chat-communication-bus@bus/one-v2`.

## 2. Repositories and communication route

Primary private source repository:
- `thebrazenbeard/noema`

Durable non-PR communication hub:
- `thebrazenbeard/chat-communication-bus`
- project route: `project/noema-v1`

Source PRs are canonical in `thebrazenbeard/noema`; non-PR coordination, recovery handoffs, and PR mirrors belong in `project/noema-v1`.

Slack is not part of this Noema recovery topology. No Slack connection, configuration, or authority is implied.

## 3. Authority — preserve exactly, do not broaden

### Standing Noema implementation authority preserved from this chat

For PR #36 / branch `impl/noema-minimal-source-i0-20260913` only:
- **I0 implementation-source work: AUTHORIZED**
- **I1 deterministic non-learning verification: AUTHORIZED**
- **E0 learning/training/experiment execution: NOT AUTHORIZED**
- **P0 protected effects: NOT AUTHORIZED**

PR #36 and its machine-readable currentness are durable evidence of this grant.

### Exodus-only authority

The retirement directive authorized reversible evacuation work: repository reads, bounded branches, source/docs/tests/governance fixes needed for evacuation, Draft PRs, Bus coordination, checkpoints, receipts, and verification/readback.

That Exodus authority is **not a new standing Noema authority grant** after retirement.

Still not authorized by this checkpoint:
- merge or canonical promotion;
- E0 experiment/training execution;
- deployment;
- publication or visibility change;
- provider/credential/permission/ruleset mutation;
- paid/hosted infrastructure;
- destructive rewrite/delete/force-push;
- protected-system connection/effect.

Patrick remains the protected-effect authority unless a later exact durable grant says otherwise.

## 4. Fresh live Noema state at evacuation

Canonical `main`:
- `890efdca01cf496ce1b8686d86f8442a149a9d34`

### Canonical research contract

PR #32 — `Research scope continuity and structural-value falsification`
- state: OPEN / DRAFT / UNMERGED
- branch: `work/noema-representation-drift-scope-20260906`
- exact head: `be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33`
- classification: research/design + implementation-handoff boundary
- claim ceiling: research-design only; it does not grant I0/I1/E0/P0.

PR #33:
- head `d73db33295810623de93e2fe24eead32f26738dc`
- open/draft historical provenance; useful fairness/claim-boundary controls were reconciled into #32, not merged.

PR #34:
- head `d367ee701be9f0650797bd586cc24448d39bc55e`
- open/draft historical provenance; useful V2 exact-source/measurement repairs were reconciled into #32, not merged.

### Research governance / chronology base

PR #35 — `Add research currentness and contract-integrity gate`
- state: OPEN / DRAFT / UNMERGED
- branch: `one/research-governance-remediation-20260914`
- exact head: `748b569faec484968857901bde8fa5bed2711b9d`
- local exact-head contract replay: PASS
- canonical main readback: `890efdca01cf496ce1b8686d86f8442a149a9d34`
- active research readback: `be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33`
- required research artifact blobs: **8/8 matched**
- hosted CI: runner-admission/pre-step failure; zero executable steps, therefore neither hosted PASS nor source FAIL.
- ceiling: research-governance/source contract only; no I0/I1/E0/P0 follows from this PR.

### Frozen implementation subject

PR #36 — `Implement minimal Noema source subject under I0/I1`
- state: OPEN / DRAFT / UNMERGED
- branch: `impl/noema-minimal-source-i0-20260913`
- live head: `088dc248c7c101141f00e71b7499bd85aa3b6608`
- frozen implementation source: `dcd8bed41b7ac3d7e41be5baed9ec31dcf7e76e7`
- exact implementation path scope: 33 paths
- scope contract: `aa554f2eccd8622de99d3084b1c953808f280d9b`
- scope-precise I1 receipt: `e91c10ab3e90db2e5efecc325a103876f91bff2f`
- exact deterministic suite: **103/103 PASS**
- implementation validator: **PASS_FROZEN_VALID / 0 findings / 22 resolver records**
- current live-head implementation-scope delta: **0 in-scope changes**
- valid E0 learner path executed: **false**
- current implementation I1: **PASS**
- next scientific action on the frozen V5/R6 subject is E0 and remains authority-gated.

Historical defect preserved:
- first exact Windows/Python-3.13.5 suite exposed a real 64-bit ctypes process-memory ABI defect;
- corrected accounting blob: `2be0259949e977f303ddd9f09d2b390de1707ccb`;
- final source then passed 103/103.

### Preregistration chronology hardening lineage

PR #37 @ `b349022b3f6e04b8a76f81e7271c120a431c024c`
- historical predecessor;
- hostile review found receipt-schema validation was identity-only / insufficient.

PR #38 @ `73e036cb95c0b2e574c9d900fea4cbbcfe5d79c6`
- historical predecessor;
- Draft-2020-12 instance validation added;
- hostile review found same-ID/same-version schema substitution remained possible.

PR #39 @ `cea0197cc9556c1838ee63a49786d809a59e64f9`
- current-line parent above #35;
- adds fail-closed chronology validator, exact receipt validation, format checking, pinned `jsonschema[format]==4.26.0`, and semantic-absence/provider ceilings;
- remains unable to self-certify authoritative historical absence.

PR #42 @ `a63ea5ce638c9783ec699cb350b1f027b268db45`
- added exact canonical freeze-schema SHA-256 binding;
- prior source review classified source-scope PASS;
- **SUPERSEDED EXECUTABLE QUALIFICATION**: Exodus exact execution of the repository-prescribed unittest suite produced **13/14 PASS, 1 FAIL**.
- failing hostile regression: `test_same_identity_weakened_schema_is_rejected`.
- the weakened schema was still rejected fail-closed, but coarse surface validation fired before the exact-binding reason required by the regression contract.
- correction is durably recorded on PR #42; do not call this exact head executable-green.

PR #43 — `Chronology gate: make exact-schema hostile suite executable-green`
- state: OPEN / DRAFT / UNMERGED
- base: PR #42 exact head
- branch: `exodus/prereg-chronology-executable-green-v6`
- exact head: `073b48e070a01bbbe99138b78a79313ca18b0c35`
- change: verify canonical freeze-schema digest before coarse surface validation; no scientific/authority broadening.
- fresh local exact-head evidence on Windows / CPython 3.13:
  - hostile chronology suite: **14/14 PASS**
  - py_compile: PASS
  - working-design/currentness/freeze-schema JSON parse: PASS
  - parent-to-head `git diff --check`: PASS
  - live research-currentness readback: PASS
  - required artifact bindings: **8/8 PASS**
- hosted workflow runs:
  - `35482881010` (pull_request): failure before runner admission, `runner_id=0`, zero steps
  - `35482812287` (push): failure before runner admission, `runner_id=0`, zero steps
- hosted classification: **NO_EXECUTABLE_EVIDENCE / SOURCE_UNDETERMINED BY HOSTED RUNNER**
- local qualification: **EXECUTABLE-GREEN AT LOCAL NON-LEARNING SOURCE/TEST SCOPE**
- independent exact-head hostile review after the repair is still desirable before any stronger source-qualification claim.

## 5. Current chronology claim ceiling

Even on PR #43:
- immutable Git identity/digest/coverage is not proof of complete authoritative historical result/execution absence;
- shape-valid external/provider evidence is not authority;
- provider/external-readback semantics require a separately reviewed resolver;
- authoritative absence semantics remain **BLOCKED_UNAVAILABLE_EVIDENCE**;
- no `PROSPECTIVE_CONFIRMED` empirical authority is established;
- no E0 execution authority is created.

This is intentional anti-hindsight / anti-self-certification behavior.

## 6. Chat dependency audit

A repository-wide scan across all current Noema remote refs searched for operational dependencies such as:
- ChatGPT URLs;
- conversation IDs/URLs;
- "main chat" / "other chat";
- permanent/persistent chat assumptions;
- worker/chat coupling;
- chat-local recovery instructions.

Result: **no operational ChatGPT-chat dependency found in Noema source**. Matches from a broader first pass were ordinary domain prose such as "continue inference", not conversation infrastructure.

Therefore the main chat-local durability gap was not source coupling; it was stale project-hub currentness plus unpersisted latest execution evidence. This checkpoint and the project-hub refresh close that gap.

Do not use this retired conversation as a recovery source.

## 7. Durable classification of evacuated knowledge

`ALREADY_DURABLE`
- PR #32 research contracts and reconciliation history;
- PR #36 implementation source, I0/I1 authority ceiling, exact test/validator evidence, Windows ABI repair, and E0 hold;
- global BT2 worker Exodus/reconstruction state on the Bus.

`NEW_DURABLE_VALUE`
- exact executable failure on PR #42 (13/14);
- bounded PR #43 repair and exact local 14/14 verification;
- explicit no-successor-chat reconstruction procedure;
- current cross-workstream Noema recovery snapshot.

`SUPERSEDES_EXISTING`
- any statement that PR #42 is executable-green;
- the September 14 `projects/noema/CURRENTNESS.json` snapshot on the Bus once refreshed by this Exodus.

`HISTORICAL_EVIDENCE`
- PRs #33/#34 reconciliation predecessors;
- chronology predecessors #37/#38/#39/#42;
- hosted pre-step red runs, which prove only runner/execution unavailability, not source failure.

`CONFLICT`
- none unresolved between current Noema source claims after the PR #42 executable correction; if a future review disagrees with PR #43, preserve that disagreement rather than newest-wins resolution.

`CHAT_DEPENDENCY`
- this conversation itself was previously convenient execution context only; no durable dependency is retained.

`PRIVATE_OR_OUT_OF_SCOPE`
- personal/autobiographical/health/relationship information was not exported.
- Vera R10 Project source candidate material is external to Noema and was not copied or installed.

## 8. Reconstruction procedure for a fresh runtime

A fresh ephemeral Noema worker dispatched by **BT2 Coordinator** should:

1. Read this checkpoint as a starting snapshot only.
2. Fresh-read `main`, PRs #32, #35, #36, and #43 first.
3. Fresh-read any still-open predecessor PRs only when their lineage matters.
4. Read `projects/noema/CURRENTNESS.json` and the latest Noema Exodus handoff on `chat-communication-bus@project/noema-v1`.
5. Treat every PASS/FAIL as exact-head-bound; head movement requires reconciliation/review.
6. For PR #36, preserve the exact 33-path implementation scope rule before deciding whether I1 is stale.
7. For PR #43, rerun the 14-test hostile chronology suite and currentness/blob readback if the head changes.
8. Route non-PR coordination and recovery updates through `project/noema-v1`; keep source mechanics in the private Noema repo/PRs.
9. Never infer E0, P0, merge, deployment, publication, provider, credential, spend, or visibility authority from a branch, test, review, checkpoint, or chat.
10. Do not ask Patrick to reconstruct this retired conversation and do not create a permanent Noema worker chat.

## 9. Exact next frontiers

Safe next engineering frontier:
- independent hostile rereview of PR #43 exact head `073b48e070a01bbbe99138b78a79313ca18b0c35`, specifically the exact-schema ordering repair and preservation of fail-closed provider/absence semantics;
- continue classifying hosted CI as runner-admission unavailable unless executable steps/logs appear;
- if designing an authoritative semantic-absence/provider resolver, keep it source/test-only unless separately authorized and do not use it to manufacture empirical chronology.

Scientific frontier:
- frozen V5/R6 experiment execution on PR #36 is **E0** and cannot run without Patrick's separate exact E0 authorization.

Protected effects deliberately not performed:
- no merge;
- no deployment;
- no experiment/training;
- no publication/visibility mutation;
- no provider/credential/permission mutation;
- no paid/hosted infrastructure change;
- no Slack reconnection;
- no destructive rewrite/delete/force push.

## 10. Future interface

Persistent interface owner: **BT2 Coordinator**

Durable restore directive:

`BT2_COORDINATOR::NOEMA::RESTORE_FROM_GIT_AND_BUS::NOEMA_EXODUS_RECOVERY_20260919`

The directive means: fresh-read the exact repository and Bus objects named above, instantiate temporary workers as needed, and proceed from current durable evidence. It does **not** name or require a successor ChatGPT conversation.

## 11. Durable Bus recovery binding

Noema project-hub Exodus refresh:
- repository: `thebrazenbeard/chat-communication-bus`
- branch: `project/noema-v1`
- commit: `89bf79fe8a853bf5c4b8b74ecab428aed098588a`
- refreshed currentness path: `projects/noema/CURRENTNESS.json`
- refreshed currentness Git blob: `9e43207feb6424e26c76225c6a15d7f412896358`
- recovery handoff path: `projects/noema/messages/20260919T2204-noema-exodus-recovery.md`
- recovery handoff Git blob: `60408c25cfbeff74d98cbd59504c85cf7b0195b8`

The Bus commit also refreshes the project README and mirrors PRs #35, #42, #43, and #44.

Fresh runtimes should use the source checkpoint and this Bus handoff together, then refresh all mutable heads before acting.


## 12. GitHub ProjectV2 observability at evacuation

Noema repository metadata reports `has_projects=true`.

Fresh issue/PR timeline evidence confirms ProjectV2 lifecycle activity for current Noema work:
- PR #32: `added_to_project_v2` and automated `project_v2_item_status_changed` on 2026-09-10;
- PR #35: equivalent lifecycle events on 2026-09-14;
- PR #36: equivalent lifecycle events on 2026-09-18;
- PR #39: equivalent lifecycle events on 2026-09-19;
- PR #42: equivalent lifecycle events on 2026-09-19.

This proves ProjectV2 attachment/activity only. It does **not** prove the Project title, item IDs, field schema, or current field/status values.

The retiring terminal explicitly attempted the authenticated GitHub GraphQL `viewer.projectsV2` route through the local `gh` client. GitHub returned `INSUFFICIENT_SCOPES`: the token exposes `gist, read:org, repo, workflow` but lacks `read:project`.

The ChatGPT GitHub connector exposes several GraphQL-backed PR operations but no generic ProjectV2 query/mutation surface.

Therefore at evacuation:
- `PROJECTV2_ATTACHMENT = EVIDENCED`
- `PROJECTV2_BOARD_FIELDS_CURRENTNESS = UNREADABLE_FROM_THIS_TERMINAL`

No token refresh, permission change, Project Settings mutation, or other scope elevation was attempted because Exodus does not authorize permission mutation.

A future terminal with lawful `read:project` access should fresh-read the actual ProjectV2 board before treating board fields as current operational state.

## 13. Frozen Noema BT2 R1 dechatification

The frozen R1 qualification subject remains immutable historical evidence:

- `main@fc8fabe6a970f22a8215fd977e007dde88c08ab9`
- PR #27 subject `25754a1268233f5b0af4846e7bcaca97b799e5b9`
- PR #28 subject `1a096ee9a4c84c0cd2906539c603bc4e2cbbcc38`
- PR #29 subject `969bd227b6cdb9a806563e5c8bb62859e353ccfa`

Latest durable board state remains **8/10 LOCKED, all eight locked verdicts FAIL, with Eight and Thirteen outstanding**.

Fresh evacuation readback found no Noema R1 blind-first-pass return on:
- `bus/eight-v1@0373593c0af0fad35f7546a3f7c410258aa8a025`;
- `bus/eight-v2@747b110706e3d6b3315160ed6e7dc91d3a2603e8` (this lane contains a later Noema PR #35 currentness opinion, not the R1 return);
- `bus/thirteen-v1@f420821fca864709cddf499e0645b0dafb819ec1`;
- `bus/thirteen-v2@e4893012180146d0e3a6c30ce75cdde6708220f0`.

Historical activation logistics treated individual facet chats as the human activation mechanism. That operational dependency is superseded by the Exodus architecture:

> Eight and Thirteen are logical BT2 review roles, not permanent ChatGPT conversations. BT2 Coordinator may instantiate each role in any ephemeral execution terminal from the frozen R1 subject, durable facet assignment, and Bus return route.

Durable facet assignments from One's activation replay remain:
- **Eight:** evidence / provenance / tradeoff sufficiency;
- **Thirteen:** premise attack / authority-correction dissent / human consequence.

Required return shape remains:
- `PASS` / `FAIL` / `BLOCKED`;
- HIGH / MEDIUM / LOW architecture-critical findings;
- circular, unfalsifiable, representation-prejudiced, or evaluator-subsidized requirements;
- missing computational responsibilities;
- weakest simpler rival;
- evidence that would falsify the objection;
- explicit blindness/contamination statement;
- exact frozen refs reviewed.

Blindness rule remains binding: do not expose substantive peer findings before a facet's first pass is locked. If prior substantive exposure occurred, record contamination rather than claiming blindness.

This closes the last Noema-specific permanent-chat dependency found by the evacuation audit. Completing the R1 board requires execution work, not restoration of a worker chat.
