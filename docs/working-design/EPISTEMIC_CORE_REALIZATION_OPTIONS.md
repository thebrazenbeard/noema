# Noema epistemic-core realization options

Status: **BRAINSTORMING / DESIGN SECTION / NOT IMPLEMENTED**

## Purpose

Experiment A now has a sufficiently sharp falsification world. The next question is how to realize the epistemic core without accidentally building the answer into the learner.

This document compares three realizations and assigns them distinct experimental roles rather than pretending one architecture should be trusted from the start.

## Design rule

The first implementation should separate three questions:

1. **Is the experimental task actually learnable under the resource budget?**
2. **How far can a continuous predictor get without explicit structural hypotheses?**
3. **Does bounded explicit structure provide a measurable advantage without semantic leakage?**

Those questions should not be answered by the same model.

---

## Approach 1 — explicit dependency-graph reference learner

A small population of evaluator-readable dependency graphs is fit to the observed channels.

Each graph represents generic conditional dependence among opaque signal channels. For the reference learner only, the evaluator may use stronger structural assumptions than Noema itself will eventually be allowed to use.

### Role

**Reference / learnability ceiling**, not developmental evidence.

### Strengths

- easy to verify that Experiment A contains enough information after intervention;
- easy to calculate expected posterior movement;
- easy to ablate individual dependencies;
- easy to detect a broken generator or impossible resource budget.

### Weaknesses

- graph structure is a strong inductive bias;
- hard-coded intervention semantics could trivially leak causal structure;
- success would not show that Noema discovered the representation.

### Rule

Any oracle knowledge used here is clearly marked evaluator-side and cannot be counted as evidence for DGFW/RGSS.

---

## Approach 2 — continuous soft-structure baseline

Use a small continuous predictor with no explicit persistent graph/factor/process records. It receives the same opaque signal channels and raw intervention-provenance packet as the candidate learner.

Uncertainty can be represented through an ensemble, probabilistic output, or another generic continuous mechanism, but the model has no selectively addressable explicit structural hypotheses.

### Role

**Primary baseline.**

### Why it matters

If a compact continuous model matches the candidate on intervention prediction, transfer, local correction, sample efficiency, and meta-learning, then explicit DGFW/RGSS structure has not earned its complexity.

### Required fairness

The continuous baseline should receive comparable parameter/compute budgets where practical and the same curriculum, observations, intervention packets, train/test splits, and evaluation metrics.

It must not be intentionally crippled merely to make explicit structure look useful.

---

## Approach 3 — bounded RGSS latent-process learner

This is the candidate Noema epistemic-core realization for Experiment A.

It combines:

- a cheap continuous predictive substrate;
- a small population of explicit, provisional **latent-process hypotheses**;
- generic local structural mutations triggered by persistent residual structure;
- learned intervention-sensitive modulation acquired from the curriculum rather than a built-in `do()` operator;
- bounded competition among live alternatives;
- local revision and selective ablation;
- proposal-policy meta-learning across worlds.

### Recommended role

**Candidate architecture under test.**

The experiment does not assume it wins.

---

# Recommended first candidate realization

For Experiment A, use a deliberately small hybrid rather than jumping straight to a maximally expressive neural or program-synthesis system.

## Fast layer

A compact continuous predictor estimates the next/current observable distribution from:

- recent opaque signal history;
- current intervention-provenance packet when present;
- current active latent-process state.

It must be small enough that unlimited memorization is not the default solution.

No pretrained semantic embeddings or language models are used.

## Slow explicit layer

Maintain a resource-bounded population of live structural hypotheses.

Each hypothesis contains only generic computational structure:

- internal hypothesis handle;
- uncertain state/parameters;
- sparse learned dependencies among opaque process/channel representations;
- learned conditional dynamics;
- intervention-sensitive behavior learned from prior curriculum;
- evidence/confidence;
- influence trace sufficient for local revision and ablation.

A dependency edge does **not** mean `CAUSE`. It means only that the current hypothesis uses one learned process in predicting another under some conditions.

## Why a population rather than one soft average

Experiment A deliberately creates incompatible explanations that are observationally equivalent before intervention.

A single averaged adjacency or averaged parameter state can invent a hybrid explanation that neither live hypothesis actually asserts.

Therefore the candidate should preserve a small number of materially distinct hypotheses when they imply materially different intervention-conditioned futures.

Within-hypothesis uncertainty may remain continuous. Structural ambiguity is represented by multiple live alternatives.

## Generic proposal operations

RGSS may propose only generic edits such as:

- add a dependency;
- remove a dependency;
- reverse/replace dependency orientation;
- change conditional/temporal scope;
- split one hypothesis into alternatives;
- merge/retire redundant alternatives;
- introduce a provisional latent mediator;
- leave a dependency distributed instead of making it explicit.

The proposal mechanism may not contain `chain`, `fork`, `cause`, `parent`, `child`, or task-family templates.

## Intervention semantics

The learner is not born knowing that a clamp severs incoming causes.

The raw intervention packet is an additional provenance-bearing signal. The simpler pre-A curriculum teaches, through experience, that such packets systematically change subsequent signal behavior.

If the learner develops a reusable intervention-sensitive operator, that operator is learned structure and can later be ablated/tested.

This is critical. Hard-coding Pearl-style `do()` semantics into the candidate would make Experiment A partly circular.

---

# Behavioral measurement without reading semantic labels from the learner

The evaluator should not require Noema to internally say `chain` or `fork`.

Instead, hidden-family uncertainty can be measured through predictions.

Across trials, the evaluator randomly selects the true hidden family while passive data remain observationally identical. Before decisive intervention, a well-calibrated learner should preserve predictive mass for both possible intervention outcomes.

After intervention evidence, the learner's predictive distribution should move toward the consequences generated by the actual family.

This gives a behavioral test of uncertainty preservation without requiring privileged access to a human-readable internal ontology.

## Key scores

Use proper probabilistic scores for:

- passive prediction;
- pre-evidence hypothetical/intervention-conditioned prediction;
- post-evidence intervention prediction;
- calibration across randomized hidden families;
- transfer sample/proposal efficiency;
- negative-control behavior.

Internal inspectability remains useful for ablation and locality tests, but semantic family labels are not required for the primary success claim.

---

# Locality test

After decisive evidence implicates the `x-y` relationship, the learner should revise that dependency without destroying unrelated predictive competence.

Measure:

- change in predictions for the implicated channels/conditions;
- change in unrelated passive relationships;
- amount of parameter/structure movement if inspectable;
- recovery time after revision.

A model that only succeeds by global retraining has weaker evidence for the locality claim.

---

# Transfer test refinement

Surface-remapped worlds should vary more than channel names.

Randomize:

- channel permutation;
- numeric scale and offset;
- dependency coefficients;
- noise levels;
- intervention magnitudes;
- irrelevant distractor channels;
- which member of the Markov-equivalent family is actually true.

Meta-learning counts only if the full learner becomes faster at proposing/evaluating useful alternatives while remaining calibrated on negative-control worlds.

If it merely learns `these experiments are usually chains`, it fails.

---

# Failure patterns that matter

The candidate direction weakens sharply if:

1. the continuous baseline matches the full learner on every claimed benefit;
2. ambiguity preservation requires manually enumerating the correct graph family;
3. intervention success depends on hard-coded causal intervention semantics rather than learned command consequences;
4. the hypothesis population explodes even in the three-channel world;
5. explicit structure improves interpretability but not prediction, transfer, locality, sample efficiency, or meta-learning;
6. meta-learning speeds later tasks only by becoming overconfident in the ontology of earlier tasks.

---

# Communication boundary

Grounded communication is a first-class developmental track in the broader Noema design, but **Experiment A remains language-free**.

This is deliberate isolation, not a reversal of the communication requirement. The communication track is tested later against the same anti-cheating and developmental standards once the epistemic substrate has earned survival.

---

# Current recommendation

Use all three approaches in the same experimental program:

1. **reference graph learner** to validate the task and estimate an upper bound;
2. **continuous soft-structure model** as the serious baseline;
3. **bounded RGSS latent-process learner** as the candidate architecture.

For the candidate, begin with graph-like sparse learned dependencies only as a **test realization of local explicit structure**, not as a claim that Noema's mature ontology is fundamentally a graph.

If the candidate cannot beat the continuous baseline in this tiny controlled case, do not scale the architecture outward.