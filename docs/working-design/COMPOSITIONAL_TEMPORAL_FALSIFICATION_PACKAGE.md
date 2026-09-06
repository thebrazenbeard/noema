# Noema compositional-temporal falsification package

Status: **BRAINSTORMING / MECHANISM-NEUTRAL EVALUATION DESIGN / NOT AN APPROVED IMPLEMENTATION**

Date: 2026-09-06

Parent frontier: `COMPOSITIONAL_TEMPORAL_SUBSTRATE_OPTIONS.md`

## Purpose

Test the common computational requirement exposed by Candidate A hostile validation without making RLPO, options, graphs, predicates, slots, or any other mechanism the answer key.

The target claim is intentionally behavioral:

> The learner can discover reusable structure in continuous experience, rebind it to novel content, compose it across time, use it to improve prediction/control, and revise it when the structure stops working — without evaluator-supplied semantic roles or temporal boundaries.

This package occurs **after** the first-core F0/F1/F2 sequence. It should not delay the first persistent predictive implementation slice.

## Entry conditions

A candidate enters this package only after demonstrating:

- persistent online learning;
- bounded resources;
- calibrated uncertainty;
- action/outcome source separation;
- non-destructive regime-change revision;
- no material F0 information leakage.

## Comparator policy

At minimum compare:

- a flat continuous recurrent predictor/controller with no explicit reusable temporal/compositional structure;
- Candidate A plus the proposed compositional-temporal mechanism;
- a deliberately stronger reference realization where useful for ceiling measurement;
- an ablation that keeps parameter count/compute close while destroying cross-context reuse.

The proposed mechanism does not pass merely by outperforming a crippled flat baseline.

## CT0 — boundary-leakage control

### World

Continuous streams contain repeated processes, but evaluator-known episode/subgoal boundaries are withheld.

Training presentation boundaries are jittered or absent.

### Required behavior

The candidate's reusable structure should not collapse when external logging/window boundaries shift.

### Failure

Learned chunks align primarily with evaluator/training-window boundaries rather than predictive/control structure.

### Claim ceiling

Passing CT0 supports only:

`temporal abstraction is not obviously boundary-subsidized`.

## CT1 — recurring transformation discovery

### World

Several latent transformations recur across different surface states/content.

Some frequent transitions are useless coincidences; some rarer transformations are predictively/control useful.

### Required behavior

The candidate identifies/reuses structure that improves held-out prediction or control relative to the flat baseline.

### Critical control

Frequency alone must not define usefulness.

### Failure

- memorized trajectory fragments;
- operator/chunk explosion;
- no efficiency or transfer gain;
- success only on exact repeats.

## CT2 — rebinding under surface substitution

### World

A learned transformation reappears with different perceptual channels, entities, locations, values, or opaque feature positions.

Evaluator labels remain hidden.

### Required behavior

The candidate reuses the learned transformation on novel bound content with less experience than cold-start learning.

### Failure

The reusable unit is actually tied to original surface identities.

### Claim ceiling

Supports limited **relational/process reuse**, not human-like symbolic reasoning.

## CT3 — novel composition

### World

The learner has separately experienced transformations `A` and `B` but not the target composition/order required in the held-out problem.

Test several variants:

- `A -> B`;
- `B -> A`;
- repeated `A -> A` where meaningful;
- a composition longer than seen during training;
- a composition with one familiar and one newly learned component.

### Required behavior

The candidate can use acquired components to improve prediction/control on the novel combination without training the whole trajectory from scratch.

### Failure

- only memorized known sequences work;
- composition depth is fixed by architecture/training;
- wrong order performs identically;
- surface similarity rather than learned transformation drives success.

## CT4 — applicability and termination learning

### World

The same learned process is useful in some contexts and harmful in others.

Its natural temporal duration varies with context.

### Required behavior

The candidate learns when reuse should begin, continue, terminate, or be suppressed.

### Adversarial cases

- tempting but invalid partial match;
- same start state, different hidden context;
- process interrupted by unexpected event;
- correct process must terminate earlier/later than training examples.

### Failure

Rigid macro invocation or externally supplied termination.

## CT5 — reusable skill emergence

### World

A recurring process becomes controllable through action.

The same competence is useful under several goals/valuations and surface variants.

### Required behavior

Repeated successful execution becomes cheaper/faster/more reliable than full replanning while remaining interruptible and revisable.

### Critical control

The skill must also be learnable from mixed successful/failed/neutral experience; reward-positive trajectories cannot be the only abstraction source.

### Failure

The learned unit is merely a current-goal macro or cannot transfer when valuation changes.

## CT6 — delayed influence localization

### World

Multiple earlier processes/actions occur before a delayed outcome.

Some are causally relevant, some correlated, some irrelevant.

Where feasible, interventions vary one earlier process while holding others stable.

### Required behavior

The candidate revises the implicated reusable structure more than unrelated structure and improves later prediction/control.

### Failure

- recency-only credit;
- global punishment of the whole trajectory;
- fixed human-defined step/milestone credit boundaries.

### Claim ceiling

Supports localized long-delay influence learning under the tested interventions, not unrestricted causal understanding.

## CT7 — grounded signal composition bridge

### World

Agent-produced signals are grounded in shared state/action contexts.

The learner acquires several reusable signal-context transformations separately, then encounters novel combinations.

No pretrained semantic embeddings or truth labels are supplied.

### Required behavior

The candidate uses shared learned structure to improve interpretation/production of a novel signal combination and transfers across changed referents/context.

### Adversarial cases

- same symbol with different pragmatic role;
- local hedge modifies uncertainty/relevance while directive force remains;
- changed speaker reliability;
- novel referent binding;
- word order/composition matters.

### Failure

Success requires a separate privileged language representation unrelated to the general substrate.

### Claim ceiling

Supports a bridge from general compositional-temporal structure to grounded communication; it does not establish fluent language competence.

## CT8 — regime change and deconsolidation

### World

A long-useful reusable transformation later becomes wrong, changes scope, or splits into two context-dependent processes.

### Required behavior

The candidate detects degraded utility, reopens the structure, and adapts without erasing unrelated competence.

### Failure

- frozen early ontology;
- global catastrophic rewrite;
- inability to learn a conflicting late-life transformation;
- hidden reset/retraining from scratch.

## CT9 — representation-mismatch controls

The package must include worlds where a favored representation is a poor fit.

Examples:

- distributed symmetric constraints with no natural directional macro;
- higher-order interactions where pairwise relation/chunk discovery is misleading;
- useful regularity that spans conventional object/episode boundaries;
- stochastic process where compression gain does not justify explicit structure;
- multiple behaviorally equivalent decompositions.

### Required behavior

The candidate may decline to form explicit reusable structure or may retain multiple equivalent decompositions.

### Failure

It forces every phenomenon into its favorite representation and interprets induced error as evidence about the world.

## CT10 — resource-value test

Reusable structure must earn its complexity.

Measure:

- prediction gain;
- sample efficiency;
- transfer speed;
- planning/deliberation reduction;
- memory cost;
- compute cost;
- false-generalization cost;
- late-life plasticity cost.

A more elaborate architecture that performs no better than the flat baseline under comparable resources fails the mechanism claim even if its internal structure looks attractive.

## Developmental order

The evaluator should not require every capability at once.

Suggested order:

`CT0 boundary integrity -> CT1 recurring transformation -> CT2 rebinding -> CT3 novel composition -> CT4 contextual initiation/termination -> CT5 skill emergence -> CT6 delayed influence -> CT7 communication bridge -> CT8 late revision -> CT9 mismatch -> CT10 resource-value review`

Later tests may reveal that earlier apparent success was shortcut learning. Such evidence reopens the earlier claim.

## Promotion rule

A specific mechanism such as RLPO should not be promoted from L4 toward the general L3 compositional/binding requirement merely for passing one world family.

Promotion requires:

- multiple world families;
- surface remapping;
- representation-mismatch survival;
- useful held-out recomposition;
- ablation showing the mechanism's structural contribution rather than capacity alone;
- resource-fair comparison;
- no semantic/boundary leakage.

## Current effect on Candidate A

This package closes a design-method gap: Candidate A now has a mechanism-neutral route to test its largest unresolved common-substrate hypothesis.

It does **not** close the architecture gap itself.

Until a candidate survives this package, compositional-temporal structure remains an L3 requirement with competing L4 realizations.
