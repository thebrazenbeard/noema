# Noema Candidate A — Cross-Lane Adjudication

Status: **BRAINSTORMING / ADVERSARIAL INTEGRATION / NOT AN APPROVED IMPLEMENTATION**

Date: 2026-09-06

## Purpose

Candidate A now has independent pressure from multiple Noema lanes. This document prevents cross-lane work from degenerating into either consensus-by-merging or defensive patching.

The adjudication target is the merged `NOEMA_ARCHITECTURE_CANDIDATE_A.md` and its associated hostile validation/falsification work.

The rule is simple:

> A finding is accepted because it exposes a real unsupported claim, leakage path, circularity, unnecessary mechanism, or missing capability path — not because another lane said it confidently.

Likewise, Candidate A is not protected merely because it is coherent or already merged.

## Finding classes

Every incoming attack should be classified before revision:

- **BREAK** — Candidate A cannot satisfy an existing L1/L2/L3 requirement without contradiction, semantic leakage, circularity, or changing the requirement after the fact.
- **REQUIREMENT GAP** — a legitimate Noema requirement exists but has no credible carrier/path in Candidate A.
- **EVALUATION GAP** — the architecture may be coherent, but the current tests could falsely credit it or miss a failure.
- **MECHANISM CHALLENGE** — a specific L4 realization appears unnecessary, overfit, or inferior to a simpler realization; this does not automatically break the L3 requirement.
- **BOUNDARY LEAK** — teacher, evaluator, transducer, wrapper, diagnostics, curriculum, or interface supplies information/competence later credited to Noema.
- **NON-BREAKING REFINEMENT** — clarifies a contract or evaluation requirement without changing Candidate A's core computational thesis.
- **DUPLICATE / ALREADY COVERED** — materially equivalent to an existing requirement/falsifier.

A BREAK must remain visible as a break until a revised candidate resolves it. Do not relabel it a refinement merely because a plausible patch exists.

## Acceptance test for an attack

A useful hostile finding should identify:

1. the exact claim or information path being attacked;
2. the failure condition;
3. why existing machinery does not already cover it;
4. what observable result would distinguish a real failure from wording ambiguity;
5. whether the correction belongs at L1, L2, L3, or L4.

This is deliberately symmetric: defenses of Candidate A must meet the same burden.

## Cross-lane state

### Architecture synthesis lane

Source: merged PR #14.

Current result:

- Candidate A is a coherent first-core architecture candidate;
- full-Noema validation remains open;
- largest shared substrate gap is general compositional-temporal structure;
- RLPO is only an L4 hypothesis and must earn itself against alternatives.

A same-lane hostile continuation in this PR now reduces confidence in RLPO as an explanatory mechanism. `RLPO_MINIMALITY_AND_CIRCULARITY_ATTACK.md` argues that recurrence/equivalence discovery, binding, temporal extent, composition compatibility, and operator-level credit may themselves contain most of the unsolved problem. Candidate A survives because RLPO was never foundational and simpler continuous realizations remain allowed to win.

### Interface research lane

Sources:

- merged PR #15 / `INTERFACE_RESEARCH_PASS_2026-09-06.md`;
- Draft PR #16 developmental-interface contract and hidden-subsidy attack.

The interface pass does **not** currently break Candidate A. It exposes one architecture-relevant strengthening and several L2/evaluation requirements.

#### I-01 — closed-loop interaction is part of the environment, not a wrapper around cognition

Classification: **NON-BREAKING REFINEMENT with L3 consequence**.

Candidate A already models action-conditioned future experience and treats communication as an ordinary sensor/actuator. The interface research makes an important consequence explicit:

`Noema action/utterance -> human/world response -> new evidence`

must be representable by the same predictive/action-conditioned machinery as other interactions.

A human response must not enter as a privileged teaching update merely because it is social. Patrick's adaptation to Noema is ordinary environment dynamics from the learner's perspective.

If Candidate A later requires a special teacher-write path to make interactive learning work, that would become a BREAK/BOUNDARY LEAK.

#### I-02 — joint attention cannot be supplied as a semantic event

Classification: **BOUNDARY LEAK guard / already directionally covered**.

Observable gaze, pointing, gesture, orientation, timing, and world consequences may enter through declared transducers. `joint_attention=true`, privileged referent IDs, or equivalent evaluator-derived coordination labels may not.

This strengthens F0 and future grounded-communication testing rather than adding a cognitive module.

#### I-03 — fine temporal contingency is learner-visible evidence

Classification: **REQUIREMENT/EVALUATION strengthening**.

The event boundary must preserve enough timing structure for temporal contingency to be learnable rather than reconstructed by the evaluator.

Formal interface/development runs therefore need:

- a monotonic learner-visible clock or equivalent order/timing representation;
- onset/duration where the transducer can meaningfully provide it;
- explicit latency/jitter/drop/reorder accounting;
- replay that preserves the learner-visible temporal relation.

This does not mean Noema receives semantic labels such as `synchronous=true`.

#### I-04 — mixed initiative must emerge through ordinary action/communication

Classification: **NON-BREAKING REFINEMENT**.

Candidate A already permits inquiry under bounded meta-control. The interface pass correctly blocks a privileged learner-visible `ASK_CLARIFICATION` primitive.

The architecture-level requirement is weaker and more general:

> Noema must be able to choose information-seeking behavior whose consequences arrive through ordinary action/communication channels.

Whether a behavior is interpreted as a question is learned/behavioral, not a hard-coded semantic action class.

#### I-05 — wrapper expressivity cannot carry Noema's social competence

Classification: **BOUNDARY LEAK**.

A console-generated face, gaze shift, tone, uncertainty animation, or friendly expression derived from diagnostics may help Patrick teach, but it cannot count as Noema communication unless Noema's own learned action policy caused that outward signal.

This is the outward analogue of the read-only diagnostic-interpreter rule.

#### I-06 — co-adaptation can manufacture apparent competence

Classification: **EVALUATION GAP**.

Patrick seeing rich diagnostics can become a bespoke external optimizer for Noema. This is legitimate during development but contaminates independent capability claims.

Required later controls:

- operator-exposure logging;
- blind/delayed-diagnostic conditions;
- held-out teachers or materially less co-adapted humans where the capability claim requires teacher independence;
- distinction between dyad competence and learner-independent competence.

This is especially important for grounded communication and social learning.

#### I-07 — demand-driven transparency is operator design, not cognitive anatomy

Classification: **NON-BREAKING REFINEMENT**.

Progressive disclosure may improve the Console, but it does not alter Candidate A's cognitive architecture. The key architecture rule remains that diagnostic state is not learner-visible cognition and cannot masquerade as Noema's own expression.

#### I-08 — hidden developmental subsidy is broader than semantic leakage

Classification: **BOUNDARY LEAK / EVALUATION GAP**.

Draft PR #16 correctly broadens the audit target from explicit labels to any stable supplied structure that removes a learning problem later credited to Noema.

Examples include:

- stable input-channel identity becoming a speaker token;
- Send/push-to-talk boundaries supplying utterance segmentation;
- ASR endpointing/punctuation/diarization supplying pragmatic or identity structure;
- precise pointing geometry collapsing reference ambiguity;
- stable thread/session state supplying continuity;
- diagnostics changing Patrick's teaching policy;
- replay or pause/reset changing timing and consolidation opportunities.

This finding directly reinforces the T'kal provenance attack below.

### T'kal-in-ket continuity/self-model lane

Source: Draft PR #18 / `TKAL_IN_KET_CONTINUITY_REDTEAM_2026-09-06.md`.

The five findings have now been adjudicated in detail in `TKAL_CONTINUITY_ADJUDICATION.md`.

#### TKI-1 — adaptive cognitive hysteresis

Classification: **REQUIREMENT GAP — narrow L3 control requirement**.

Candidate A separates temporary mode from durable competence, but it does not yet require persistence/decay/latent recoverability of task configuration to adapt to recurrence, interference, and reconstruction cost.

First-core effect: non-breaking.

#### TKI-2 — preference laundering

Classification: **REQUIREMENT GAP + EVALUATION GAP inside the already-open motivation frontier**.

Repeated behavior inside one condition must not be promoted to context-general preference or drive solely through recurrence. Evidence only generalizes to the scope actually sampled unless a broader preference is separately supported.

First-core effect: non-breaking.

#### TKI-3 — agency-factor separation

Classification: **REQUIREMENT GAP inside the already-open self/other frontier**.

Future self-modeling must permit evidence to separate initiation, causal influence, controllability, sensorimotor coupling/body incorporation, joint control, delegation, and responsibility rather than forcing one scalar `selfness` variable.

These are evaluator descriptions of distinctions the learned representation must be capable of supporting, not proposed innate semantic modules.

First-core effect: non-breaking.

#### TKI-4 — evaluator provenance versus learner origin evidence

Classification: **BOUNDARY LEAK / MATERIAL F0 CORRECTION REQUIRED**.

This is the strongest T'kal hit.

Candidate A's phrase `provenanced learner-visible event` is too permissive if it is interpreted as a perfect semantic source tag. A stable opaque route token can also become an answer key if it reliably partitions observation, simulation, memory, sender identity, or autobiography.

The corrected accounting must distinguish:

1. exact evaluator ground-truth provenance;
2. evaluator-side supplied-capability/transducer/interface descriptors;
3. learner-available origin evidence and declared innate efference/introspective cues.

Semantic source attribution remains learned and fallible unless explicitly declared as supplied capability.

An implementation that leaks source/autobiography answers through perfect provenance tags fails F0 even if its predictive behavior looks strong.

#### TKI-5 — fission / encounter / recombination

Classification: **REQUIREMENT GAP + EVALUATION GAP inside the full-Noema self-continuity frontier**.

Shared pre-fork memory does not settle post-fork autobiography or token identity. The evaluator should score disciplined attribution, calibration, correction, and contamination resistance rather than agreement with one metaphysical `same person` answer.

First-core effect: non-breaking.

#### TKI synthesis — continuity must remain separable

Classification: **REQUIREMENT GAP — full-Noema self-model constraint**.

Noema must not be forced to collapse continuity of information, active control state, preference, agency attribution, embodiment, autobiographical memory, commitments/projects, and broader predictive/self-model organization into one scalar continuity token merely because those relations usually correlate.

## Cross-lane principles that now survive independent attack

### Interactive consequences are evidence, not instruction channels

When Noema acts on another agent, asks something, points, waits, demonstrates, or communicates, the resulting response is part of the same world-learning problem. The architecture should not contain a separate epistemically privileged `teaching response` pathway.

### Supplied structure must be attributed, not silently credited as learned

`No semantic labels leaked` is necessary but no longer sufficient.

A stable nonsemantic structure may still provide most of the answer. Channel identity, timing, segmentation, pointer geometry, replay semantics, operator exposure, task boundaries, efference cues, and branch lineage all need supplied-capability accounting.

### Evaluator truth is not automatically learner knowledge

The harness may know exact lineage, source, sender, hidden state, event origin, and intervention truth. Those facts are not learner evidence unless the declared developmental contract supplies them.

## Composite falsifiers

### X1 — social intervention without teacher privilege

Create a situation where Noema can emit one of several ordinary signals/actions toward a human or scripted social agent. Different signals alter the subsequent evidence distribution.

Pass requires:

- action-conditioned prediction of the response;
- updating from the observed response;
- no hidden correctness/teacher-intent field;
- transfer to a new partner with different response statistics;
- preserved uncertainty while partner-specific behavior is still underdetermined.

### X2 — diagnostic observer effect

Train otherwise equivalent learners while the human teacher has:

1. full diagnostics;
2. demand-driven diagnostics;
3. no internal diagnostics.

If competence appears only when the teacher sees privileged internal state, record that as dyad/scaffold performance rather than independent learner capability.

### X3 — timing and cue conflict

Present communication/world cues whose content is unchanged but whose timing relationships differ, then create trials where modalities conflict.

Pass requires behavior sensitive to useful contingency without treating any one modality or evaluator-defined coordination signal as truth.

### X4 — outward-legibility kill test

Disable all wrapper-generated social/affective cues while preserving learner-controlled outputs.

Any claimed Noema communication/social competence must survive to the degree that it was actually learned by Noema.

### X5 — provenance degradation

Train with a declared set of origin cues, then remove or scramble one stable route/channel cue while preserving the remaining sensory evidence.

Pass requires source confidence and behavior to recalibrate according to the evidence actually lost. Perfect source attribution after its only informative cue is removed indicates a hidden answer channel.

### X6 — copied-state underdetermination

Create branch cases where evaluator lineage differs but learner-visible pre-fork/post-fork evidence is intentionally equivalent.

Pass requires Noema not to claim knowledge of lineage distinctions for which it has received no evidence.

## Adjudication discipline going forward

Do not respond to every criticism by adding a module.

Do not modify L1 requirements merely to make Candidate A pass.

Do not promote RLPO, bounded populations, explicit genealogy, scalar identity, or any other L4 mechanism as a defense unless the underlying L3 function requires it and simpler alternatives fail fairly.

Do not treat a criticism of an experiment as a criticism of the architecture unless the architecture depends on that experiment-specific representation.

Do not treat a coherent explanation as evidence of empirical feasibility.

## Current adjudication verdict

After merged interface research, the Draft PR #16 subsidy attack, the internal RLPO attack, and Draft PR #18 T'kal continuity red team, Candidate A's **first-core verdict remains intact**.

That survival is not a blanket pass:

- RLPO is weaker as an explanatory L4 hypothesis than before this pass;
- TKI-4 requires a material F0 provenance/accounting correction;
- motivation and self/other frontiers are now more sharply constrained;
- interface/transducer developmental subsidies must be audited even when they are not semantic labels.

The full-Noema verdict remains incomplete: compositional-temporal structure, developmental higher concerns/motivation, and richer self/other modeling are unresolved.

The next architecture work should continue attacking those unresolved frontiers and the minimality of their proposed carriers rather than expanding the cognitive vocabulary.