# Experiment A — core realization options

Status: **BRAINSTORMING / ARCHITECTURE COMPARISON / NOT IMPLEMENTED**

## Purpose

Experiment A is now specific enough that implementation families can be judged against a concrete falsification target rather than by general appeal.

The goal here is not to choose the final Noema architecture. It is to identify the smallest epistemic realization that can honestly test the DGFW/RGSS claims without building the organism around them.

A pass in Experiment A will be evidence only for the narrow capabilities tested. It must not be treated as proof that the same representation scales to 3D objects, agents, selves, language, or abstraction.

## Option 1 — explicit Bayesian graph search

Represent the observed channels as variables in candidate directed graphs. Enumerate or locally search possible orientations, fit continuous conditional models, preserve multiple graph hypotheses, and update their evidence after intervention.

### Strengths

- clean uncertainty over competing structures;
- exact local ablation and revision;
- easy to verify whether passive Markov-equivalent structures remain ambiguous;
- intervention semantics are mathematically explicit;
- excellent diagnostic/oracle implementation for the first world.

### Weaknesses

- assumes from birth that the world should be represented as discrete variables connected by graph edges;
- candidate variables are already supplied by the observation channels;
- graph mutation can solve the chain/fork task while teaching us little about open-ended latent-process discovery;
- risks turning Experiment A into a causal-discovery benchmark rather than a Noema substrate test.

### Verdict

**Use as a reference/oracle and sanity-check implementation, not as sufficient evidence for DGFW.**

If even this family cannot solve A under the evaluation rules, the test harness or resource budget is probably wrong. If it succeeds, that only establishes that the world is identifiable under intervention and that the scoring/evaluation machinery works.

## Option 2 — differentiable soft-structure model

Use a continuous predictive model with learnable directed dependency gates/attention weights between opaque signal representations. Structure begins soft rather than as discrete graph commitment. Sparsity/complexity pressure and intervention evidence can drive some dependencies toward stronger or weaker directional organization.

### Strengths

- cheap relative to explicit combinatorial search;
- can preserve graded uncertainty over dependency strength;
- compatible with continuous values and online learning;
- does not require enumerating every candidate graph;
- useful bridge between distributed prediction and explicit structure.

### Weaknesses

- one soft matrix can collapse ambiguity into averaged edges rather than preserve genuinely distinct explanations;
- uncertainty over parameters is not the same as uncertainty over structures;
- local ablation is possible but may not isolate a coherent learned hypothesis;
- transfer may reflect parameter reuse rather than learned relational structure;
- still assumes pairwise directed dependency is a privileged representational form.

### Verdict

**Useful baseline and likely fast layer, but insufficient alone unless it can demonstrably preserve multimodal structural alternatives.**

## Option 3 — bounded latent-process hypothesis population

Use a continuous predictive substrate plus a small resource-bounded population of provisional latent-process hypotheses.

Each hypothesis contains only generic computational structure:

- opaque internal handle;
- local learned state/function parameters;
- dynamically learned dependencies/bindings to other active processes or raw channels;
- uncertainty/confidence;
- provenance/influence trace;
- resource status.

RGSS proposes local mutations from persistent residual structure. Candidate mutations are generic: add/remove/reverse dependency, split/fork, introduce mediator, change scope, merge, retire, or remain distributed.

Multiple candidates can stay live when passive evidence does not discriminate them.

### Strengths

- directly tests the DGFW/RGSS thesis rather than merely the benchmark;
- explicit alternatives can remain distinct under observational equivalence;
- local ablation and revision are natural;
- proposal-versus-acceptance separation is testable;
- can later generalize beyond observed-channel graph nodes by introducing latent processes and learned operators;
- provides direct data about tractability under a bounded hypothesis budget.

### Weaknesses

- more machinery than Option 2;
- local search may still hide graph/object biases if mutation grammar is too narrow;
- maintaining several parameterized candidate models may be expensive;
- success on a three-channel graph-like world can still overstate generality;
- search/scoring choices can quietly encode the answer.

### Verdict

**Recommended experimental Noema candidate.**

It is the smallest realization that actually puts the distinctive DGFW/RGSS claims at risk.

## Recommended Experiment A stack

Do not choose only one model and call success validation.

Use three levels:

1. **reference graph learner** — validates the world/evaluation and gives an oracle-like structural benchmark;
2. **continuous soft-structure baseline** — tests how much can be achieved without explicit competing latent-process hypotheses;
3. **bounded latent-process RGSS learner** — the actual candidate under falsification.

The decisive comparison is between levels 2 and 3.

If the RGSS learner does not produce measurable gains in ambiguity preservation, intervention-conditioned prediction, local revision, transfer, or sample efficiency relative to the soft continuous baseline, its added explicit structure is not earning its complexity.

## Important restriction

The observed channels in Experiment A are intentionally simple. That means a graph-like slow layer is acceptable **as an experimental specialization**, but it cannot be promoted to Noema's universal ontology from an A pass.

A later Experiment A-family test must include hidden mediators, higher-order dependencies, and worlds where useful structure does not map one-to-one onto observed channels. Otherwise the system may simply be learning graph orientation among designer-supplied variables.

## Narrow implementation recommendation when the design gate eventually opens

For the first implementation plan, keep the continuous substrate deliberately small and CPU-feasible. The RGSS layer should use a tiny bounded candidate population rather than exhaustive enumeration.

Candidate generation should be residual-localized, but acceptance should be based on held-out predictive/intervention evidence and resource cost.

No LLM, pretrained embedding model, hosted service, or cloud runner is necessary.

## What A can legitimately establish

If the recommended stack passes the pre-registered tests, we can claim evidence that:

- explicit competing learned structure can improve over a distributed baseline under observational ambiguity;
- intervention evidence can drive selective structural revision;
- the learned structural machinery can transfer across surface remapping;
- proposal-generation learning may improve later hypothesis search.

We still cannot claim that Noema has learned objecthood, causality as a human concept, selfhood, agency, abstraction in general, or intelligence in the broad sense.

The purpose of this restraint is to keep each later developmental claim independently falsifiable.
