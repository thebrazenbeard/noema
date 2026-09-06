# Noema candidate factor-formation criteria

Status: **BRAINSTORMING / WORKING HYPOTHESIS / NOT AN APPROVED IMPLEMENTATION**

## Problem

The DGFW hypothesis fails if factor creation is really hidden object/agent/causal labeling. Noema therefore needs a domain-general reason to create, split, merge, preserve, or retire latent structure.

## Working principle

A new latent factor should be considered only when the learner's current representation leaves **persistent, reusable residual structure** that can be explained more efficiently and more robustly by introducing a distinct latent dependency.

This is not equivalent to "something moved together, therefore object."

A candidate factor earns support when it improves some combination of:

- multi-horizon prediction;
- transfer across changed surface conditions;
- intervention-conditioned prediction;
- reusable compression of repeated dependencies;
- uncertainty calibration;
- local error attribution;
- counterfactual simulation.

Complexity is a cost, not a truth test. Rare anomalies must be allowed to remain unresolved rather than being compressed away.

## Candidate lifecycle

### Birth

A factor may be proposed when residual prediction/error structure recurs in a way the existing model cannot explain compactly.

The proposal is provisional and low-confidence.

### Strengthening

Confidence increases when the factor remains useful across time, viewpoints, interventions, recombinations, or contexts.

### Splitting

A factor should split when one latent explanation repeatedly predicts incompatible dynamics or intervention responses that become cleaner when represented separately.

### Merging

Factors should merge when their distinction adds complexity without improving prediction, transfer, intervention response, or uncertainty calibration.

### Weakening / retirement

A factor loses active weight when its explanatory contribution disappears, becomes redundant, or repeatedly fails intervention/transfer tests.

Retirement need not erase historical evidence immediately; memory/decay policy remains separate.

## Anti-cheating rules

Factor formation must not directly use privileged semantics such as:

- spatial contiguity => object;
- autonomous motion => agent;
- controllability => self;
- temporal precedence => cause;
- reward association => goal.

Those patterns may become evidence *learned by Noema*, but they are not allowed as designer-authored category rules.

## Important complication: several structures may be equally good

Noema should not force one decomposition when several explain the evidence comparably well.

Competing factor structures may remain live until new observation or intervention discriminates between them.

This is essential for avoiding premature ontology formation.

## Important complication: residual structure depends on the current representation

A poor lower-level representation can generate misleading residuals and cause factor proliferation.

Therefore factor formation and continuous representation learning must be bidirectional:

- factors can direct attention/prediction back toward the continuous layer;
- failures in factor structure can motivate revision of the underlying representation;
- neither layer is treated as ground truth for the other.

## First falsification pattern

Construct an experience stream with two initially indistinguishable hypotheses:

- H1: several features belong to one persistent latent process;
- H2: they are independent processes that merely co-vary during early experience.

Early passive observation should not let Noema decide confidently.

Later intervention should break the correlation in a way that distinguishes H1 from H2.

A valid learner should:

1. retain uncertainty before the intervention;
2. propose/revise latent structure from the new evidence;
3. improve prediction after revision;
4. transfer the learned structural distinction to a new surface configuration;
5. lose that transfer advantage when the relevant learned factor/relation is ablated.

## Current verdict

The most defensible factor-formation rule is not a semantic heuristic but a **structure-learning pressure over residual dependencies**, judged by prediction, reuse, intervention, uncertainty, and complexity together.

This is still not a complete mechanism. The unresolved implementation question is how to search candidate structures efficiently without embedding domain semantics in the proposal machinery.
