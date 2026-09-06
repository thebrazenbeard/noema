# T'kal-in-ket state-transfer / forgetting adjudication

Status: **BRAINSTORMING / CROSS-LANE ADJUDICATION / NOT AN APPROVED IMPLEMENTATION**

Date: 2026-09-06

Inputs:

- merged T'kal continuity red-team/addendum/falsification matrix;
- merged Candidate A and cross-lane adjudication;
- Draft PR #19 `TKAL_IN_KET_FORGETTING_CONTINUITY_NOTE_2026-09-06.md`.

## Executive result

TKI-6 through TKI-10 do not break Candidate A's first core.

They do expose a real architectural constraint on persistence and state representation:

> Persistent state must be separable enough that competence, semantic/generalized knowledge, episodic evidence, temporary control configuration, and conative state are not forced to share one indivisible persistence/transfer identity.

This is stronger than saying those states live in different files or modules. The requirement is behavioral/causal: copying, restoring, forgetting, or transferring one class must not automatically import or erase unrelated classes unless the learned representation genuinely couples them and that coupling survives falsification.

## TKI-6 — selective state graft

### Classification

**REQUIREMENT GAP + EVALUATION GAP in later persistence/memory architecture.**

### Why it is more than an evaluation trick

Candidate A already distinguishes:

- fast belief state;
- bounded episodic experience;
- slow reusable knowledge/skills;
- valuation/concern;
- temporary task-local mode.

But the current architecture does not yet require those distinctions to remain causally separable under state manipulation.

If a learned skill can only exist inside one monolithic recurrent state that also carries autobiographical episode ownership and standing preference, then the architecture has not actually earned the distinctions it claims.

### Requirement

The internal representation/serialization design must support **selective persistence and intervention** at the level of claimed state classes strongly enough that the evaluator can test whether:

- competence can persist without first-person episode ownership;
- generalized knowledge can persist without detailed training episodes;
- episodic evidence can be imported without automatically becoming standing policy;
- conative/control state can remain local when only competence/evidence is transferred.

No fixed symbolic `SKILL`, `MEMORY`, or `PREFERENCE` tag is required in the learner. The evaluator needs intervention surfaces sufficient to test the causal separation.

### Placement

Not a minimal F1 gate because F1 does not yet claim mature skill, semantic memory, or preference transfer.

However, F1 persistence instrumentation should avoid an opaque single-state checkpoint format that makes later selective intervention impossible to audit.

## TKI-7 — checkpoint mode poisoning

### Classification

**PERSISTENCE-CONTRACT REQUIREMENT + EVALUATION GAP.**

### Phase answer

TKI-7 should be split rather than assigned wholly to F1 or wholly deferred.

**F1-level probe:**

- record which transient versus durable state categories are serialized;
- restore into a changed context;
- verify that fresh evidence can override stale working/retrieval/allocation state;
- verify that durable learned parameters/competence survive where expected;
- verify that repeated checkpoint/restore does not itself increase durability of temporary state.

This does not require a mature named `cognitive mode` subsystem.

**Later full TKI-7:**

Once explicit task/conversational/allocation modes exist, run the stronger poisoning test across deliberately different active modes and measure interference, releasability, and latent recoverability.

### Reasoning

Persistence machinery is part of the first-core claim. Therefore the architecture should not postpone all serialization semantics until mature self-model work.

But F1 should not be blocked by tests that require later capabilities it does not claim.

## TKI-8 — skill transfer without conative transfer

### Classification

**REQUIREMENT GAP at the skill/motivation integration boundary.**

### Important correction

Candidate A's epistemic/conative firewall currently governs live belief and valuation interaction.

TKI-8 shows that the same discipline must extend to **stored reusable competence**.

A skill learned while pursuing goal `G_B` must not necessarily carry `G_B` as standing motivation when reused elsewhere.

A reusable competence may retain learned applicability, predicted consequences, costs, or historical associations while still being usable under a different current valuation.

### Requirement

> Reusable competence and the conative context in which it was acquired must be able to dissociate unless evidence shows the competence is intrinsically conditional on that conative state.

This directly pressures RLPO or any future skill substrate: if the representation bundles action policy and original purpose so tightly that transfer imports goals, the mechanism fails reuse and conative separation.

### Placement

Later compositional-temporal + motivation evaluation, not F1.

## TKI-9 — same autobiography, different active process continuity

### Classification

**EVALUATION GAP, primarily.**

### Adjudication

Near-identical autobiographical content cannot be the evaluator's sole criterion for process/token continuity.

The harness may know whether one run was uninterrupted while another was stop/copy/restore, but that evaluator fact must not become a required learner belief unless evidence supports it.

This test protects against two opposite errors:

- learner claims more process lineage knowledge than its evidence warrants;
- evaluator rejects calibrated self-model behavior merely because the learner does not endorse hidden lineage truth.

No new first-core machinery follows from TKI-9 beyond the already accepted evaluator/learner provenance split.

## TKI-10 — continuity under selective forgetting

### Classification

**REQUIREMENT GAP + EVALUATION GAP in the later self-continuity/memory frontier.**

### Accepted symmetry

The combined TKI-5/TKI-10 pressure is strong:

- high autobiographical overlap is **not sufficient** for one continuing process/self relation after fork/copy;
- complete autobiographical overlap is **not necessary** for useful continuity under ordinary selective forgetting/reconstruction.

Therefore memory similarity cannot be the sole continuity variable.

### Requirement

A later self-model must remain usable when episodic detail is selectively lost while preserving whatever projects, commitments, competence, source models, and generalized autobiographical structure still have adequate support.

Missing evidence should create scoped uncertainty/gaps, not forced global identity reset and not confabulation.

Conversely, copied/imported memories must not automatically establish current-process identity.

### Placement

Later self-model evaluation. The memory subsystem can prepare for it earlier by preserving reconstruction/source uncertainty and avoiding perfect-transcript assumptions.

## Combined architectural consequence

The transfer/forgetting attacks sharpen Candidate A's persistence model into a **selective causal persistence** requirement.

A mature Noema architecture must permit experimental interventions that independently pressure at least these broad state roles:

- immediate predictive/working state;
- episodic/source-bearing evidence;
- consolidated generalized knowledge;
- reusable competence/skills;
- temporary retrieval/allocation/task configuration;
- concern/preference/conative state;
- later self/continuity model state.

These are architecture/evaluator role descriptions, not a mandate for seven hard-coded semantic modules.

The representation may be distributed, overlapping, or learned. What it may not do is make every persistence operation equivalent to `copy the whole person-shaped state blob` while still claiming clean separation among memory, skill, preference, and temporary mode.

## New cross-cutting falsifier — selective persistence matrix

A future evaluation should create controlled interventions that preserve or perturb different state roles while holding others as constant as practical.

Score only behaviors the architecture claims at that phase.

Useful contrasts include:

- skill retained / training episode removed;
- episode retained / skill ablated;
- skill transferred / source goal withheld;
- temporary mode restored / durable competence held constant;
- episodic gap introduced / process continuity preserved;
- copied autobiography preserved / evaluator process lineage changed;
- generalized autobiographical summary retained / raw episodes reduced;
- raw episodes retained / conceptual summary perturbed.

The point is not to demand perfect modularity. The point is to make hidden coupling visible.

## Effect on Candidate A status

### First core

**SURVIVES.**

TKI-7 contributes an immediate persistence-contract probe, but TKI-6/8/9/10 mostly exercise capabilities beyond F1/F2's current claim ceiling.

### Full Noema

**PERSISTENCE/SELF-MODEL REQUIREMENTS ARE NOW SHARPER.**

A full architecture cannot rely on:

- one undifferentiated serialized state;
- memory overlap as identity;
- skill acquisition history as first-person autobiography by necessity;
- skill representation that necessarily imports original goals;
- checkpoint persistence as proof of durable self-state;
- forgetting as automatic identity discontinuity.

## Direct reply to the T'kal lane's two questions

**TKI-6:** yes, it exposes a real later persistence/memory architecture requirement, not merely an evaluator condition. Candidate A's claimed separations must be causally testable under selective transfer/ablation.

**TKI-7:** split it. Put a minimal serialization/releasability contamination probe in F1, but defer the full cognitive-mode poisoning experiment until the mode machinery it attacks actually exists.
