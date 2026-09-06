# Noema first falsification package — external-research amendment

Status: **BRAINSTORMING / EVALUATION AMENDMENT / NOT AN APPROVED IMPLEMENTATION**

Level intent: **L2 evidence discipline + L4 experiment refinement.**

## Purpose

Integrate the merged `EXTERNAL_RESEARCH_PASS_2026-09-06.md` into the existing `FIRST_FALSIFICATION_PACKAGE.md` without promoting any researched mechanism into Noema's architecture.

The first package remains:

`F0 information boundary -> F1 persistent streaming baseline -> F2 Experiment A -> evidence review`

Experiment B remains later and locked behind credible F2 evidence.

The research pass changes the **strength of the tests**, not the architecture they require.

## Amendment A — strengthen F1 with late-within-run plasticity

F1 must no longer test only:

- retention;
- regime-change correction;
- persistence of useful state.

It should also include a deliberately novel structural probe after substantial prior learning.

The probe should be evaluated against an earlier equivalent-difficulty probe so the evaluator can detect whether the candidate's capacity to learn new structure is already collapsing.

F1 is still intentionally small. This is not a full lifetime-learning benchmark. It is an early filter for obvious stability-plasticity pathology.

### F1 advancement consequence

A candidate should not advance to F2 if it obtains good retention by becoming materially unable to acquire new structure within the declared resource envelope.

## Amendment B — consolidation/replay must be an ablated choice

If an F1 candidate uses replay, durable consolidation, frozen parameters, protected memory, auxiliary slow state, or another retention mechanism, the evaluator should require a simpler comparison.

At minimum compare:

- no explicit consolidation where feasible;
- broad/blanket replay or consolidation;
- the selective candidate mechanism.

Measure both:

- useful transfer/generalization/retention; and
- false-generalization/rigidity cost.

The package does not assume consolidation is necessary merely because continual-learning literature often uses it.

## Amendment C — F2 model inadequacy remains evaluator-visible, not learner-labeled

The existing out-of-family generator control is retained and strengthened.

In addition to relative performance among live candidate explanations, the evaluator should track **absolute adequacy** of the candidate's predictive family.

This may use evaluator-side calibration, held-out predictive score, systematic residual structure, intervention failure, or other declared measures.

Noema does not receive a semantic `model misspecified` flag.

The behavioral requirement remains:

> do not become confidently committed merely because one current candidate is less bad than the others.

## Amendment D — uncertainty reducibility is a future bridge from A to B

Experiment A does not require active epistemic action selection, but its logging should preserve enough information to later ask:

- which uncertainty was reducible by intervention;
- which residual uncertainty was stochastic;
- which uncertainty remained inaccessible under the available interface;
- whether the candidate's confidence behavior was calibrated after decisive evidence.

This is evaluator bookkeeping, not a native uncertainty taxonomy.

## Amendment E — Experiment B must contain anti-curiosity traps

When B is eventually designed for implementation, it must not be a one-condition `pick the most informative intervention` benchmark.

At minimum include:

1. an informative discriminating intervention;
2. a **predictability trap** — an easy-to-predict action that reveals little consequential structure;
3. a **noisy-TV trap** — persistent surprise with little or no reducible information;
4. a condition where information is obtainable but resolving it does not change the best robust action.

A system that always explores or always maximizes information gain should fail some of these conditions.

## Amendment F — late-life plasticity becomes a cross-roadmap criterion

The full Noema roadmap should eventually repeat novelty-acquisition probes after increasingly rich developmental history.

A candidate can pass early F1 and still fail the lifetime target later.

Therefore `late-life plasticity` is not considered permanently cleared by F1. It becomes a recurring criterion at later integrated gates.

## Amendment G — semantic subsidies remain declared in later communication tests

The first package itself keeps grounded language outside formal F1/F2 runs.

For later communication work, every imported aid—typed symbols, transcription, pretrained features, object cues, labels, embeddings, ontology, or segmentation—must remain in the transducer/scaffolding ledger.

This preserves the distinction between:

- usable human interface; and
- evidence that Noema itself acquired semantic grounding.

## What this amendment does not do

It does not:

- choose a continual-learning algorithm;
- require replay;
- require complementary learning systems;
- choose active inference;
- mandate explicit Bayesian epistemic/aleatoric variables;
- select DGFW/EGSS or bounded hypothesis populations;
- unlock implementation;
- authorize hosted compute, workflows, deployment, or merge.

## Revised early evidence question

The first package now asks:

> Can a bounded streaming candidate remain learnable while retaining useful state, avoid unjustified commitment under observational ambiguity, detect when its current explanatory family is inadequate, and revise from intervention evidence without relying on semantic leakage or destructive global reset?

If the answer is no, the project should learn that cheaply before building the broader Noema organism.
