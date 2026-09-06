# Two-timescale structure search

Status: **BRAINSTORMING / TRACTABILITY HYPOTHESIS / NOT AN APPROVED IMPLEMENTATION**

## Problem

Residual-Guided Structure Search (RGSS) is conceptually attractive but can become combinatorial if Noema explicitly enumerates candidate factors, relations, bindings, and graph edits whenever a prediction fails.

The current tractability hypothesis is to separate **cheap soft discovery** from **expensive explicit structural commitment**.

## Core idea

Use two interacting timescales:

1. **Fast soft dependency learning** continuously tracks predictive relationships and unexplained residual structure without committing to discrete ontology.
2. **Slow structural search/consolidation** creates or branches explicit latent factors/relations only when persistent evidence indicates that the extra structure may earn its cost.

Neither layer is ground truth for the other.

## Fast layer — soft dependency field

The fast layer remains continuous/distributed and can be trained online to predict sensorimotor change.

It also preserves cheap approximate signals about where dependencies matter, such as:

- which latent/sensory channels jointly reduce prediction error;
- which action-conditioned changes repeatedly affect the same residual structure;
- which representations repeatedly co-vary across time;
- where predictive uncertainty remains multimodal or persistently high;
- which transformations recur across different contexts;
- approximate influence/eligibility traces showing which current representations contributed to a failed prediction.

These are not semantic labels and do not automatically become factors.

The fast layer's job is primarily **proposal localization**: identify regions of representational space where a more explicit hypothesis may be worth considering.

## Slow layer — explicit hypothesis construction

When residual/dependency evidence persists strongly enough to justify more compute, RGSS proposes bounded structural alternatives in the implicated region.

Examples:

- introduce a latent bottleneck mediating several dependencies;
- split one current representation into two regimes;
- merge two repeatedly redundant latent structures;
- create a reusable transformation/operator between latent arguments;
- branch two competing structural explanations;
- change temporal span;
- choose not to factorize and leave the phenomenon distributed.

The proposal is evaluated on held-out future experience, intervention-conditioned prediction, transfer/recombination, calibration, complexity/resource cost, and local credit-assignment value.

## Soft-to-structural bridge

A candidate factor should not be created because a pre-authored rule says `these features form a thing`.

Instead, the slow layer asks whether introducing an explicit latent dependency provides a measurable advantage over keeping the same structure distributed.

One generic form is a **predictive bottleneck test**:

> Can a lower-dimensional or reusable latent mediator explain/predict a recurring dependency across contexts better than independent memorization, while surviving intervention and transfer?

If yes, that mediator becomes a candidate factor. Its semantics remain learned/unknown.

This can produce object-like factors, motion-process factors, agent-state factors, relation factors, strategy factors, or nothing discrete at all depending on the evidence.

## Relation/operator discovery

The same principle can extend beyond factor formation.

Suppose different latent structures repeatedly undergo analogous transformations. Rather than memorizing each transformation independently, Noema can test whether one parameter-sharing operator predicts all cases when bound to different latent arguments.

A generic learned operator has:

- arity/addressable argument positions as computation;
- learned transformation/dynamics;
- no innate semantic role labels;
- evidence from reuse across bindings;
- transfer tests under argument permutation and novel surface features.

This is a candidate route to compositional relations and later analogy without a symbolic predicate vocabulary supplied from birth.

## Why the fast layer cannot be unlimited

A sufficiently powerful continuous predictor could memorize every local pattern and eliminate residual pressure before useful structure is ever consolidated.

Therefore the continuous substrate needs resource/complexity constraints. It should be easier or cheaper to reuse stable structure than to indefinitely absorb every recurring dependency into opaque distributed parameters.

This is not a demand for maximal compression. It is a pressure against unlimited memorization.

## Branching only when ambiguity matters

Explicit competing hypothesis branches are expensive. Noema should not fork models for every uncertain detail.

A branch is most justified when:

- the predictive distribution is meaningfully multimodal;
- competing structural explanations imply different future outcomes;
- available interventions could discriminate them;
- the unresolved difference affects current/future valuation, transfer, or error diagnosis;
- repeated anomalies indicate that one point estimate is causing systematic failure.

This ties structural uncertainty to finite-resource allocation rather than requiring exhaustive Bayesian enumeration.

## Learned proposal policy

Over time Noema may learn which residual patterns tend to justify which generic structural edits.

Important separation:

> **proposal policy suggests; evidence accepts.**

Accepted/rejected proposals become meta-learning data. The proposal policy can improve search efficiency without gaining authority to declare a structure true.

A small persistent exploration probability or equivalent diversity mechanism should remain so early-world ontology does not make future proposal space self-sealing.

## Stress test 1 — pairwise dependence misses synergy

Some dependencies are invisible to pairwise correlation or mutual information. XOR-like or higher-order interactions can matter even when every pair appears independent.

**Requirement:** proposal localization cannot rely only on pairwise statistics. The fast layer needs at least some capacity to detect higher-order predictive interactions, for example through learned nonlinear residual models, random/compositional probes, or unexplained multi-channel prediction gain.

## Stress test 2 — smooth latent bias misses regime changes

A low-dimensional continuous bottleneck may fit smooth dynamics well but fail discrete switching, branching, or hybrid processes.

**Requirement:** the structural search grammar must support more than one generic latent family or a sufficiently flexible representation that can express continuous, discrete, multimodal, and hybrid dynamics without semantic labels.

The choice among those forms should be evidence-driven.

## Stress test 3 — slow consolidation may fossilize stale structure

A once-useful explicit factor can become wrong in a nonstationary world.

**Requirement:** consolidated structure keeps confidence and recency/evidence dependence. It can weaken, fork, split, or retire when prediction/intervention/transfer evidence changes.

Consolidated does not mean immutable.

## Stress test 4 — the fast layer may dominate interpretation

If the soft layer is the only source of structural proposals, its biases can silently define what Noema is capable of discovering.

**Requirement:** preserve multiple proposal routes:

- residual-guided proposals from the fast layer;
- exploratory generic structural mutations;
- memory-driven proposals from analogous prior failures;
- intervention-driven proposals when live hypotheses disagree.

No single learned proposal channel becomes the sole ontology gatekeeper.

## Stress test 5 — resource allocation can create epistemic blind spots

If compute flows only toward current high-salience beliefs, neglected regions may never produce enough evidence to challenge the model.

**Requirement:** allocation needs an exploration/diversity floor and should treat persistent unexplained residuals as one source of priority even when they are not yet tied to current goals.

## Stress test 6 — discrete consolidation can be arbitrary

Turning a soft distributed pattern into an explicit factor may depend on a threshold chosen by the designer.

**Requirement:** threshold crossing should be viewed as a resource decision, not a declaration of truth. Different thresholds should change compute/storage cost more than the underlying evidential criterion, and sensitivity should be tested empirically.

## Working search pipeline

A concrete but still architecture-neutral pipeline is:

`experience`
→ `fast predictive update`
→ `residual + influence trace`
→ `soft dependency accumulation`
→ `proposal trigger when persistent/useful`
→ `bounded generic structural mutations`
→ `short-lived competing candidates`
→ `held-out/intervention/transfer evaluation`
→ `resource-bounded retention / consolidation / retirement`
→ `proposal-policy meta-learning`

## What this buys us

The two-timescale design answers the combinatorial objection without simply inserting object/agent detectors:

- most experience remains in cheap continuous representation;
- only persistent unexplained structure receives expensive explicit search;
- explicit factors are earned rather than ubiquitous;
- rejected proposals train future search efficiency;
- uncertainty can remain soft until structural branching has enough value to justify its cost.

## What could kill it

The hypothesis should be rejected or heavily revised if:

1. useful factors/relations only appear when proposal localization contains semantic heuristics;
2. the continuous predictor consistently absorbs structure before explicit reuse can emerge;
3. structural search remains computationally explosive even with residual localization and learned proposals;
4. learned proposal policies become so ontology-specific that transfer to radically different worlds collapses;
5. explicit consolidation produces no measurable transfer, intervention, or credit-assignment advantage over a purely continuous model.

## Current verdict

A two-timescale soft-to-structural search is the strongest current tractability strategy for RGSS.

The next decisive issue is **what kind of generic representation a candidate factor/operator actually has**. It must be expressive enough for open-ended learning but constrained enough to support local revision, uncertainty, dynamic binding, and efficient simulation.
