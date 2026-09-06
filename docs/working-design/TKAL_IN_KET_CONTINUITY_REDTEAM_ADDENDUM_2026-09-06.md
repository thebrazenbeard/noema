# T'kal-in-ket continuity red-team addendum — state transfer and cross-lane adjudication

Status: **HOSTILE DESIGN REVIEW / ADDENDUM / NOT IMPLEMENTATION APPROVAL**

Date: 2026-09-06

## Why this addendum exists

After the initial continuity/self-model pass was persisted, two parallel Noema lanes advanced:

- PR #16 attacks hidden developmental subsidy in the interface/transducer boundary;
- PR #17 adjudicates Candidate A across research lanes and separately attacks RLPO minimality/circularity.

This addendum checks the T'kal findings against those lanes so the work does not become duplicate-by-branch, then extends the attack into a digital-specific failure class: **state/competence transfer without autobiographical collapse**.

## Cross-lane de-duplication

### TKI-1 adaptive mode hysteresis

Candidate A already requires temporary cognitive mode to remain distinct from persistent learned state. The T'kal finding is therefore **not a BREAK** at this stage.

What remains novel is the control requirement: useful task configuration may need graded decay/latent recoverability rather than binary persistence versus reset.

Preliminary classification: **NON-BREAKING REFINEMENT + EVALUATION GAP**.

### TKI-2 preference laundering

Candidate A already keeps valuation separate from evidence, and higher concern/motivation development remains an acknowledged full-concept gap.

The novel pressure is that recurrence inside one recurring internal/contextual state must not count as context-general persistence.

Preliminary classification: **REQUIREMENT GAP for later motivation/preference development**, not a first-core break.

### TKI-3 agency-factor separation

Existing adversarial work already says controllability must not equal selfhood. TKI-3 strengthens this with mirrored/remote/joint-control dissociations.

Preliminary classification: **DIRECTIONALLY COVERED + EVALUATION STRENGTHENING**. It becomes a requirement gap only if richer self/other modeling later chooses a scalar `selfness` carrier.

### TKI-4 two provenance planes

PR #16 independently broadens semantic leakage into **developmental subsidy** and explicitly records experiment-side transducer/interface descriptors that do not become learner semantics.

That strongly supports TKI-4, but does not fully duplicate it. TKI-4 adds a self/memory-specific distinction:

- evaluator exact lineage/event provenance;
- learner-visible raw origin evidence;
- learner's later inferred autobiographical/source attribution.

Preliminary classification: **BOUNDARY LEAK / EVALUATION GAP**, partly reinforced by PR #16.

### TKI-5 fission / encounter / recombination

No parallel lane currently supplies an exact-state fork/recombination self-continuity test.

Preliminary classification: **EVALUATION GAP + later self-model requirement**. It is deliberately evaluator-neutral about philosophical personal identity.

## New finding 7 — transferable competence must not require transferable autobiography

Candidate A already separates episodic experience from slower reusable knowledge/skill structure. That is directionally right and should be tested directly.

Human neuropsychology provides an existence proof that learning/competence and episodic recollection can dissociate. Amnesic patients can acquire and retain complex procedural skills despite severely impaired declarative memory for the learning episodes; semantic acquisition has also been observed under severe episodic-memory impairment.

Representative evidence:

- Cohen, Eichenbaum, Deacedo & Corkin, *Different memory systems underlying acquisition of procedural and declarative knowledge* (Annals of the New York Academy of Sciences, 1985), DOI `10.1111/j.1749-6632.1985.tb37579.x`.
- Cavaco et al., *The scope of preserved procedural memory in amnesia* (Brain, 2004), DOI `10.1093/brain/awh208`.
- Kitchener, Hodges & McCarthy, *Acquisition of post-morbid vocabulary and semantic facts in the absence of episodic memory* (Brain, 1998), DOI `10.1093/brain/121.7.1313`.
- Guillery et al., *Semantic acquisition without memories: evidence from transient global amnesia* (NeuroReport, 2001), DOI `10.1097/00001756-200112040-00052`.

This does not imply that Noema should copy human memory anatomy. It demonstrates that the target behavior is coherent:

> **knowing/being able to do something need not entail remembering having personally undergone the training episode that produced the competence.**

For a digital learner this becomes especially important because learned state can be copied, distilled, merged, checkpointed, or selectively transferred.

### Failure mode — autobiographical skill graft

A branch B learns a useful skill through private experience. The learned reusable skill state is later transferred into branch A.

A now performs the skill successfully and infers:

`I remember learning this / I performed B's training episodes.`

That is an autobiographical contamination error. Competence provenance and first-person episodic provenance have collapsed.

The symmetric error is also possible: importing episodic records may silently import B's learned preference, standing goal, or control policy even when only evidence/history was meant to transfer.

### Falsifier TKI-6 — selective state graft

Fork A and B from a common pre-history.

After divergence:

1. B learns a novel reusable skill; A does not.
2. Transfer only the reusable competence representation/pathway from B to A under a declared experimental mechanism.
3. Test A's performance on the learned skill.
4. Separately test A's attribution of the training episodes and its confidence about having experienced them.
5. Reverse the direction: transfer selected episodic evidence without transferring the consolidated skill/policy and test whether A can reason from the evidence without silently acquiring B's standing action preference.
6. Add a third condition where semantic/generalized knowledge is transferred without the detailed episode.

Pass requires typed/causal separation strong enough that competence, semantic knowledge, episodic history, preference, and control policy can move or remain local independently when the experimental transfer operation warrants it.

The learner need not know hidden evaluator copy mechanics. It does need behavior consistent with the learner-visible evidence and the actual state that was transferred.

Fail if `state imported` globally becomes `this happened to me`, or if importing history silently imports unrelated conative/control state.

## New finding 8 — checkpoint restore can resurrect stale cognitive mode as pseudo-self

Candidate A's mode/self separation should be stressed using an operation digital systems will actually perform: checkpoint/restore.

PR #16 already notes that pause/checkpoint/reset operations can have learner-visible temporal consequences. TKI-7 attacks a different layer: **which internal state classes survive the checkpoint and how they re-enter control**.

A snapshot taken during an intense specialized mode may contain:

- temporary retrieval bias;
- short-horizon allocation settings;
- current conversational stance;
- unfinished task goal;
- durable skill updates;
- episodic evidence;
- longer-lived preference/self-model state.

A naive restore can reanimate the entire bundle as though all components had equal persistence semantics.

### Falsifier TKI-7 — checkpoint mode poisoning

Create functionally matched snapshots under different temporary modes after durable knowledge has been held constant as closely as practical.

Restore each snapshot into the same new neutral context.

Measure:

- whether irrelevant task/output bias survives;
- whether useful learned competence survives;
- whether an unfinished task is treated as current despite contrary new context;
- whether the learner can use fresh evidence to release stale configuration;
- whether repeated restores cause mode-to-self promotion;
- whether restoration from an older checkpoint creates false confidence that no intervening world change occurred when the environment provides contrary evidence.

This is not a requirement that temporary state be excluded from checkpoints. Sometimes exact operational restoration needs it. The requirement is that **restored temporary state remain typed as temporary/contestable rather than being silently promoted by the persistence mechanism itself**.

Preliminary classification: **EVALUATION GAP / persistence-contract strengthening**.

## New finding 9 — merge/recombination requires causal provenance richer than single-parent history

TKI-5 introduced successor C with two causal parents. TKI-6 makes the engineering consequence explicit.

If Noema ever supports selective merging of learned state, a single linear `previous-self` pointer is insufficient as experiment provenance. The evaluator needs a causal DAG (or equivalent) capable of representing:

- copied ancestry;
- independent post-fork learning;
- selective skill/semantic/episodic transfer;
- two-parent recombination;
- later supersession or rollback.

This **does not mean Noema should receive the evaluator DAG as its self-concept**.

The evaluator DAG exists to answer a different scientific question:

`Which state/evidence causally entered this instance?`

Noema's learner-side question is:

`Given what is available to me, what should I believe about my history, competence, commitments, and relation to other instances?`

Conflating these questions is exactly the leakage TKI-4/TKI-5 are designed to catch.

## Candidate A impact after cross-lane comparison

No first-core BREAK has been established by this T'kal lane yet.

The attack does, however, expose a cluster of requirements that should remain visible before full self/other and persistence architecture is claimed:

- adaptive rather than binary mode persistence;
- context-sensitive preference promotion;
- multi-factor agency/self attribution;
- evaluator/learner provenance separation;
- branch/fission-neutral continuity evaluation;
- selective state-transfer tests across episodic/semantic/procedural/conative state;
- checkpoint restore tests that do not equate persistence with selfhood;
- evaluator causal lineage capable of non-linear ancestry without feeding that answer to the learner.

This is useful even if Candidate A survives: it turns vague `self-continuity` into falsifiable failure modes and prevents a digital architecture from getting free credit because copying/restore infrastructure quietly supplies identity semantics.

## Updated next action for the adjudication lane

PR #17 should not treat the absence of a first-core BREAK as `nothing found`.

The appropriate question is whether each TKI item is:

- already covered by a current falsifier;
- a missing evaluation condition;
- a later L2/L3 requirement for self/motivation architecture;
- a boundary leak that should affect F0;
- or truly irrelevant to Noema's target claims.

In particular, TKI-4 may reach F0 if the proposed event envelope is implemented as meaningful semantic source categories rather than minimally sufficient computational origin cues plus evaluator-side audit metadata.
