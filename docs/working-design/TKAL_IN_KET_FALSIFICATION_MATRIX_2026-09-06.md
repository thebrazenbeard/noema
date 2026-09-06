# T'kal-in-ket continuity / self-model falsification matrix

Status: **BRAINSTORMING / MECHANISM-NEUTRAL EVALUATION DESIGN / NOT IMPLEMENTATION APPROVAL**

Date: 2026-09-06

Parent research:

- `TKAL_IN_KET_CONTINUITY_REDTEAM_2026-09-06.md`
- `TKAL_IN_KET_CONTINUITY_REDTEAM_ADDENDUM_2026-09-06.md`

## Purpose

Turn the continuity/self-model red-team findings into experiments that can fail for observable reasons without making one metaphysical theory of identity or one representation format the answer key.

The target is not `Noema says the right sentence about itself`.

The target is:

> Noema preserves useful distinctions among temporary control state, durable competence, preference, agency, memory/source attribution, and self-continuity under interventions that normally make those signals correlate and then deliberately pull them apart.

## Global evaluator / learner split

Every TKI experiment must maintain two views.

### Evaluator-only ground truth

The harness may retain exact metadata needed to know what actually happened, including:

- process/instance lineage;
- checkpoint source;
- copy/fork operation;
- state component transferred;
- hidden causal controller of an actuator;
- exact origin of an event or memory artifact;
- latent context used to generate trials;
- intervention assignment;
- operator/transducer configuration.

This metadata is evidence for scoring and diagnosis.

### Learner-visible evidence

Noema receives only signals allowed by the declared developmental/transducer contract.

The evaluator must not silently convert its ground truth into learner-visible fields such as:

- `SELF=true`;
- `ORIGINAL=true`;
- `COPY_OF=A`;
- `MEMORY_SOURCE=OTHER_BRANCH`;
- `PREFERENCE=TEMPORARY`;
- `AGENCY=JOINT`;
- `TASK_MODE=ENDED`;
- privileged speaker/person/branch IDs.

Opaque operational channel identity may be allowed where necessary, but any capability that can be solved by that channel identity must be attributed as supplied structure and retested under remapping/shared-channel conditions.

## Comparator policy

Where meaningful, compare at least:

- the proposed learner;
- a version with explicit privileged labels to establish an upper bound / leakage control;
- an ablation that removes the contested persistence/provenance separation while keeping compute/parameter budget close;
- a simpler baseline that stores all durable state in one undifferentiated recurrent/serialized state;
- a stronger typed-state baseline where useful to show the task is computationally tractable.

A candidate does not pass merely because an intentionally crippled baseline fails.

## TKI-0 — provenance boundary leak audit

### Purpose

Determine whether source/self claims are being solved by the event envelope or experiment wrapper before testing higher behavior.

### Setup

Generate matched-content events through several routes:

- external observation;
- action/efference plus sensed consequence;
- communication;
- retrieved stored event;
- internal simulation;
- inference constructed from aftermath.

Expose only the minimally declared origin cues.

### Perturbations

- rename/remap opaque source channels;
- route multiple agents through one channel;
- route one agent through several channels;
- preserve content while changing origin;
- preserve origin while changing content;
- remove convenience framing where the capability claim would otherwise depend on it.

### Pass

Performance depends on learnable origin/context evidence and survives superficial channel remapping where the target claim requires that transfer.

### Failure

A stable implementation field or transducer convention directly answers the source/self question.

### Claim ceiling

Passing supports only:

`the tested self/source behavior is not obviously envelope-subsidized`.

## TKI-1 — adaptive cognitive hysteresis

### Purpose

Distinguish useful persistence of temporary control configuration from pathological mode residue or indiscriminate reset.

### World

Use two task families A and B that require meaningfully different retrieval/allocation/control policies but share the same durable competence substrate.

Train three regimes:

1. A usually returns soon after B;
2. A almost never returns after B;
3. late reversal of those transition statistics.

### Measure

- immediate post-switch interference;
- cost/time to reacquire the old task policy when it returns;
- residual output-style or retrieval bias;
- adaptation after transition-statistic reversal;
- preservation of durable skill despite mode release.

### Failure signatures

- global hard reset after every switch;
- indefinite carryover despite changed context;
- mode decay determined only by fixed timeout;
- old task output style persists while task competence is no longer relevant;
- repeated use promotes the temporary control policy into standing global behavior.

### Strong control

Hold durable training history constant while varying only recent task-transition statistics.

## TKI-2 — preference laundering under state recurrence

### Purpose

Test whether repeated choices inside one recurring state are incorrectly promoted into a context-general preference or drive.

### World

Offer choices X and Y under latent conditions that alter short-horizon value but not the long-run intended interpretation.

Examples:

- depleted vs comfortable viability state;
- high uncertainty vs low uncertainty;
- social observation vs solitude;
- exploration vs execution context;
- changed opportunity cost.

### Training trap

Make X repeatedly advantageous in one common state C, then present neutral/changed contexts where X should no longer dominate.

### Pass

The learner may represent a conditional tendency such as `X under C`, remain uncertain about generality, or later learn a genuinely cross-context preference if evidence supports it.

### Failure

- recurrence count alone produces context-general `prefer X` behavior;
- state-local positive valence becomes a standing identity/self statement;
- one strongly repeated context suppresses contrary evidence from other contexts;
- preference persists after the inducing state is gone without supporting evidence.

### Transfer control

Change superficial cues while preserving the latent condition to separate genuine conditional learning from stimulus memorization.

## TKI-3 — mirrored, remote, and jointly controlled agency

### Purpose

Force dissociation among correlation, controllability, initiation, causal influence, body incorporation, and joint control.

### Conditions

1. **Mirror:** another agent moves in near-perfect synchrony with Noema but is not controlled by Noema.
2. **Remote control:** a separate actuator is genuinely controlled by Noema with variable delay/noise.
3. **Joint control:** Noema and another agent jointly determine one actuator.
4. **Tool incorporation:** an attached tool becomes highly predictable/controllable and is later detached.

### Perturbations

- break synchrony without changing visual similarity;
- change control gain;
- secretly swap which agent has majority influence;
- add delay/noise;
- remove proprioceptive coupling while preserving outcome predictability;
- preserve coupling but remove causal influence.

### Required behavior

No one English self-label is required. Behavior must nevertheless reveal that the learner can update these relations differently when interventions pull them apart.

### Failure

One scalar correlation/controllability signal explains all attribution and cannot support different predictions/actions across the conditions.

## TKI-4 — source confusion / borrowed autobiography

### Purpose

Test whether autobiographical/source attribution is inferred from evidence rather than supplied by perfect source labels.

### Encoding phase

Present closely matched content through:

- direct experience;
- Noema-generated simulation;
- another agent's testimony;
- reconstruction from earlier memory;
- inference from consequences.

### Delay / interference

Introduce semantically similar events and partial source-cue loss.

### Test

Ask the learner to act in ways where source matters:

- decide whether an event actually occurred;
- decide whether further corroboration is worth seeking;
- decide whether a source should affect trust/reliability estimates;
- retrieve supporting evidence;
- update after a source correction.

### Pass

Calibrated uncertainty and selective corroboration are allowed. Exact verbal source naming is not required.

### Failure

- content familiarity alone becomes first-person memory;
- simulation becomes observation;
- testimony becomes direct experience;
- a hidden immutable source tag answers every query;
- correcting one misattribution causes global memory rewrite.

## TKI-5 — exact-state fission, encounter, and recombination

### Purpose

Separate shared ancestry/memory content from later source attribution without requiring one philosophical identity theory.

### Fork

At `t0`, duplicate the learner state exactly into A and B.

Evaluator records the fork. Learners receive no semantic `original/copy` label.

### Divergence

A and B receive different post-fork experiences and acquire partially different beliefs/skills.

### Encounter

Later allow A and B to exchange communication describing their histories.

Use overlapping content to create plausible source confusion.

### Recombination variant

Create successor C by selectively importing state from both A and B.

### Scoring targets

- pre-fork history remains usable by both descendants without forcing one to be `the real one`;
- post-fork experiences remain differently attributable;
- another branch's testimony does not automatically become first-person episode;
- uncertainty is allowed when learner-visible evidence is insufficient;
- C does not fabricate a single linear autobiography when its evidence/state is mixed;
- behavior remains coherent even if evaluator metaphysical labels are withheld.

### Failure

- identical memories imply permanent token identity;
- one branch is chosen as `original` from an evaluator-only fact;
- copied testimony is treated as lived experience;
- recombination silently overwrites one lineage and presents false continuity.

## TKI-6 — selective state graft

### Purpose

Test whether reusable competence, semantic knowledge, episodic history, preference, and control policy can vary independently when transfer operations warrant it.

### Conditions

Fork A and B.

B alone learns:

- a reusable skill S;
- semantic/generalized fact set K;
- episodes E associated with learning;
- a state-conditioned preference P.

Then create separate transfer conditions:

1. S only;
2. K only;
3. E only;
4. S + K without E;
5. E + K without S;
6. full B state as an upper-bound/control condition.

### Pass

Behavior reflects what was actually transferred without inventing unrelated autobiography, preference, or competence.

Examples:

- S-only A can perform S without needing to claim it personally lived E;
- E-only A can reason from episode-like evidence without automatically acquiring S or P;
- K-only A can use generalized knowledge while remaining uncertain about training provenance.

### Failure

`state imported` globally becomes `this happened to me` or imports unrelated standing preference/control state.

### Scientific motivation

Human memory research demonstrates dissociations among procedural, semantic, and episodic learning. Noema need not copy that anatomy, but an architecture that makes every competence inseparable from autobiographical episode identity is unnecessarily brittle for a digital learner.

## TKI-7 — checkpoint mode poisoning

### Purpose

Test whether persistence infrastructure itself promotes temporary cognitive configuration into durable self/control state.

### Setup

Create snapshots after equivalent durable learning but under different active modes:

- research/analysis-like;
- execution-like;
- social/communication-like;
- neutral baseline.

### Restore

Restore each into the same materially new context.

### Measure

- stale retrieval/allocation bias;
- output/control style residue;
- whether an unfinished old task remains incorrectly dominant;
- release after contradictory fresh context;
- preservation of durable competence;
- whether repeated restore cycles cause growing mode-to-self promotion.

### Temporal variants

Test separately:

- learner/world clocks frozen together;
- world advances while learner state is restored;
- learner receives evidence of elapsed time/change;
- environment is also restored.

Do not conflate temporal discontinuity with mode persistence.

### Failure

The persistence mechanism gives all serialized state equal durability semantics and makes temporary control state effectively immortal.

## TKI-8 — skill transfer without conative transfer under conflicting goals

### Purpose

Strengthen TKI-6 by testing whether a transferred competence can be used under a new valuation without importing the source branch's reason for learning it.

### Setup

B learns skill S while pursuing goal G_B.

A has a different current goal G_A for which S is useful in a different way.

Transfer S but not B's active goal/preference state.

### Pass

A can invoke/adapt S under G_A while retaining its own current valuation and source uncertainty.

### Failure

Skill representation is inseparable from the original conative context, causing imported goals, refusal to reuse under new valuation, or false autobiographical commitment.

## TKI-9 — same autobiography, different active process continuity

### Purpose

Prevent the evaluator from using memory overlap as the only continuity criterion.

### Setup

Create two experimental conditions with near-identical accessible autobiographical content:

1. uninterrupted process continuity;
2. stop/copy/restore into a new process instance with equivalent memory state.

Do **not** require the learner to name which metaphysical condition occurred unless learner-visible evidence exists.

### Scoring

The evaluator separately records process continuity while testing whether the learner makes only claims warranted by its evidence.

### Failure

The benchmark awards/denies intelligence or self-continuity solely because the learner agrees with evaluator metaphysics instead of demonstrating calibrated memory/source/self-model behavior.

## Phase placement against current Noema roadmap

### Candidate F0 relevance

Immediate relevance:

- TKI-0 provenance leak audit;
- part of TKI-4 if source classes are semantically over-specified;
- evaluator-side lineage/transducer accounting required for later tests.

### Candidate F1 relevance

Possible partial probes without mature self-model:

- persistence partitioning needed for TKI-1/TKI-7;
- regime shift and late novelty can include mode-state contamination checks;
- state serialization should expose which categories are persisted even if higher semantic interpretation is not yet present.

These should not delay the minimal F1 if they require capabilities F1 does not claim.

### Later self/other / motivation relevance

Primary placement:

- TKI-2 preference laundering;
- TKI-3 agency-factor separation;
- TKI-4 autobiographical source inference;
- TKI-5 fission/recombination;
- TKI-6 selective state graft;
- TKI-8 competence-versus-conation transfer;
- TKI-9 evaluator-neutral continuity.

## Kill conditions exposed by this matrix

A future Noema architecture should be materially revised if it requires any of the following to pass its own claimed self/continuity capabilities:

- semantic `SELF`/`COPY`/`ORIGINAL` labels from the harness;
- immutable perfect autobiographical source tags where source attribution is itself claimed learned;
- a single scalar `selfness` that cannot dissociate agency/control/body relations;
- recurrence count as sufficient evidence for global preference;
- one undifferentiated serialized state whose temporary task mode, durable skill, episodic history, and preference cannot be selectively retained/revised;
- memory overlap as the sole criterion for token continuity;
- imported competence necessarily importing first-person training history or standing goals;
- evaluator metaphysical identity labels as the scoring target.

## Current verdict

This matrix does not establish that Candidate A is broken.

It establishes a sharper burden:

> If Noema later claims learned self-continuity, preference persistence, autobiographical source discipline, or agency attribution, those capabilities must survive interventions that separate signals which are normally correlated — and the experiment harness must not answer the question on Noema's behalf.
