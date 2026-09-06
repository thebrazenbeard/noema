# Noema bounded hypothesis population

Status: **BRAINSTORMING / CANDIDATE UNCERTAINTY REALIZATION / NOT IMPLEMENTED**

## Problem

Experiment A needs uncertainty that can survive exact observational underdetermination without requiring exhaustive enumeration or collapsing mutually incompatible structures into one meaningless average.

Three broad options exist:

1. **single soft model** — cheapest, but can average incompatible explanations;
2. **full Bayesian structure posterior** — principled in tiny worlds, but combinatorial and unrealistic as Noema's general mechanism;
3. **bounded hypothesis population with continuous within-hypothesis uncertainty** — preserves material alternatives while keeping search finite.

The third is the strongest current candidate for the slow explicit layer.

## Core proposal

Maintain a resource-bounded set of live hypotheses.

Each hypothesis may contain:

- generic learned dependency/process structure;
- continuous learned parameters/state;
- uncertainty over those parameters/state;
- evidence/confidence weight;
- provenance/influence trace sufficient for local revision;
- estimated resource cost;
- predictions under ordinary and learned intervention-conditioned inputs.

The population is **not** a complete enumeration of possible worlds.

It is a working set of alternatives that have survived bounded proposal and evidence.

## Why not one soft adjacency

Suppose one plausible model predicts that an intervention on channel `a` will strongly change channel `b`, while another plausible model predicts no change.

Averaging their structure can produce a third prediction corresponding to neither hypothesis.

That is sometimes acceptable as a marginal predictive distribution, but it is dangerous if the averaged internal model is then treated as one coherent explanation for planning, intervention choice, credit assignment, or transfer.

Therefore:

- **mixture at the prediction level is legal**;
- **forced averaging at the explanatory-structure level is not required**.

## Why not exhaustive Bayesian enumeration

Experiment A is small enough that every three-channel DAG could be enumerated. The candidate learner must deliberately not rely on that convenience.

Enumeration is permitted for evaluator/reference baselines only.

The Noema candidate needs a mechanism that still makes conceptual sense when the space of possible learned processes, bindings, and operators is open-ended.

## Proposal routes

A new alternative can enter the population through evidence-guided structure search:

- persistent residual structure;
- underdetermination / several low-cost explanations fitting similarly well;
- sampled counterfactual disagreement;
- transfer failure;
- credit-assignment failure;
- compression/reuse opportunity;
- bounded exploratory structural mutation;
- learned proposal-policy suggestions based on prior analogous failures.

Proposal does not confer belief.

## Evidence update

Each live hypothesis earns or loses support from proper predictive evidence under the conditions actually observed.

Relevant evidence can include:

- passive predictive likelihood/score;
- intervention-conditioned predictive score;
- calibration;
- transfer/recombination performance;
- complexity/resource cost;
- consistency with other strongly supported learned structure.

Desirability/valence is excluded from epistemic weighting.

## Symmetry under observational equivalence

Experiment A intentionally uses structural alternatives with identical passive likelihood.

The candidate must not turn numerical tie-breaking, insertion order, random hash order, or arbitrary implementation details into epistemic certainty.

Where two live alternatives have equivalent evidence and comparable complexity, their support should remain unresolved until discriminating evidence appears.

A weak generic complexity prior may exist, but the benchmark should use matched-complexity alternatives so the result tests evidence rather than an arbitrary prior preference.

## Resource-bounded retention

The population cannot grow without limit.

Retention should consider:

- evidence quality;
- predictive/counterfactual distinctness from other live hypotheses;
- expected future usefulness;
- complexity/resource cost;
- provenance/reconstructability from episodic evidence;
- recency/nonstationarity where relevant.

Exact thresholds and population sizes belong in a pre-registered implementation plan.

## Deliberation must terminate

A bounded population alone is not enough. Without an explicit stopping policy, Noema could keep proposing, comparing, and revisiting alternatives indefinitely even when additional search is no longer worth the resources.

The design therefore needs a **bounded epistemic deliberation episode**.

A deliberation episode may end for any of three broad reasons:

1. **evidence sufficiency** — one hypothesis or coherent hypothesis family has enough calibrated support over its nearest live challengers for the current decision/context;
2. **low expected information value** — further proposal/search or currently available evidence is unlikely to change a consequential prediction or action enough to justify its cost;
3. **budget exhaustion** — a fixed step/iteration/time/compute budget is reached, forcing a bounded decision under residual uncertainty.

A literal loop/step counter is therefore appropriate as an engineering mechanism, but it should represent a **resource budget for the current reasoning episode**, not a global lifetime counter after which Noema stops reconsidering reality.

When the budget expires without sufficient evidence, the correct result is not fake certainty. Noema should retain a bounded unresolved state and act/predict under uncertainty.

## Confidence thresholds without epistemic lock-in

A certainty threshold is useful, but a single hard `confidence > X => truth` rule would create a new failure mode: early noisy evidence could permanently fossilize a bad hypothesis.

The stronger design is a staged confidence lifecycle:

- **provisional** — hypothesis is live but materially contested or weakly evidenced;
- **working belief** — sufficiently supported to guide ordinary prediction/action in the current scope while challengers remain representable;
- **consolidated** — repeatedly supported across time/context/intervention/transfer and therefore cheaper/default to use;
- **reopened** — new anomaly, contradiction, transfer failure, or challenger evidence exceeds a reopening threshold.

Thresholds should be calibrated and scope-sensitive. A model may be highly certain for one context and unresolved outside it.

No state is metaphysically final. Consolidation changes resource allocation and default confidence, not the possibility of revision.

## Challenger margin

A useful stopping criterion should usually depend not only on absolute confidence but on the **margin over the strongest materially distinct challenger**.

This prevents a population from declaring resolution merely because all hypotheses are poorly calibrated but one happens to score slightly less badly than the others.

For example, a working belief may require all of the following:

- absolute predictive/calibration quality above a minimum floor;
- support margin over the strongest behaviorally distinct challenger;
- no unresolved challenger that predicts materially different consequences in the current reachable context;
- no anomaly debt above the reopening threshold.

Exact numerical values belong in the pre-registered implementation plan.

## Counterfactual diversity protection

A subtle pruning failure can occur when two hypotheses make the same predictions on all evidence seen so far but different predictions under an untested reachable intervention.

Purely passive scoring would view one as redundant and might delete it.

The candidate therefore needs a bounded **predictive-diversity check** before merging/pruning alternatives:

> Do these hypotheses remain behaviorally distinct under a small sampled set of admissible learned intervention/counterfactual inputs?

If yes, and evidence has not discriminated them, preserve some representation of that unresolved difference when resources permit.

This check uses predicted consequences, not semantic graph labels.

## Merge rule

Two hypotheses may be merged/treated as redundant when they are materially indistinguishable across:

- relevant observed conditions;
- a bounded sampled set of reachable counterfactual/intervention conditions;
- current transfer contexts;
- uncertainty within evaluator tolerance.

Structural difference alone is not enough reason to preserve two models if it never changes anything Noema can predict, test, transfer, or revise.

## Pruning, dormancy, and reconstructability

Discarding an explicit hypothesis need not erase all evidence that once supported it.

A pruned hypothesis may leave compressed provenance/episodic traces sufficient for later reconstruction if new anomalies make the old alternative relevant again.

Where storage permits, an intermediate **dormant** state is preferable to immediate deletion for once-serious alternatives: it consumes little active compute but can be reactivated cheaply when anomaly debt or new evidence makes it relevant.

This connects bounded structure search to reopenable consolidation rather than treating pruning as metaphysical deletion.

## Interaction with Experiment A

Experiment A does not require this population to contain two explicit alternatives before intervention.

If the candidate can remain calibrated in a distributed unresolved state and only creates explicit structure after decisive evidence, that remains legal.

The population earns its value only if explicit alternatives improve one or more of:

- calibration;
- intervention prediction;
- local revision;
- transfer;
- sample efficiency;
- later active epistemic selection in Experiment B.

## Interaction with Experiment B

Experiment B is where this representation becomes much more consequential.

Choosing an informative intervention requires Noema to represent that plausible models imply meaningfully different consequences.

A bounded hypothesis population is one strong mechanism for doing that without exhaustive Bayesian search.

If a simpler continuous representation can do the same job under the same resource constraints, the explicit population has not earned itself.

## Stress tests

### Population starvation

A low cap can prune the true alternative before evidence arrives.

**Test:** vary the resource cap and measure calibration/retention under ambiguity.

### Population explosion

A high cap can hide combinatorial failure.

**Test:** scale distractor channels and candidate mutations while holding compute fixed.

### Endless deliberation

A learner may keep cycling through alternatives without improving evidence.

**Test:** impose fixed deliberation budgets and measure whether additional cycles produce diminishing information/predictive gain. Budget expiry must preserve uncertainty rather than manufacture confidence.

### Threshold lock-in

A hard confidence threshold may consolidate an early wrong model and suppress challengers.

**Test:** deliberately create early misleading evidence followed by decisive contradictory intervention evidence. The system must reopen the consolidated belief without global reset.

### Cosmetic diversity

Many hypotheses may differ structurally while predicting the same thing.

**Test:** predictive-diversity merge/pruning should collapse behaviorally redundant alternatives.

### Early-ontology lock-in

A learned proposal policy may repeatedly generate familiar structures and crowd out novel ones.

**Test:** alternate-world negative controls plus a persistent exploratory proposal floor.

### Parameter uncertainty masquerading as structural uncertainty

A model may widen parameter variance rather than preserve a genuinely different dependency organization.

**Test:** compare predictions under interventions that distinguish topology/conditional structure but cannot be covered by reasonable parameter uncertainty in one structure.

## Current verdict

A **bounded hypothesis population with continuous within-hypothesis uncertainty** remains the strongest current realization for explicit epistemic ambiguity, but the bound must apply to both **population size and deliberation duration**.

The candidate therefore requires resource-limited hypothesis retention, a bounded reasoning episode, calibrated commitment thresholds, challenger-sensitive confidence, and a reopening path for later contradictory evidence.

It is not yet a commitment to Noema's mature architecture. It is a falsifiable candidate for the Experiment A/B program.

The benchmark remains representation-neutral: if a fair continuous model achieves the same calibration, intervention reasoning, local revision, and transfer under equal resources, explicit hypothesis population should be rejected as unnecessary overhead.
