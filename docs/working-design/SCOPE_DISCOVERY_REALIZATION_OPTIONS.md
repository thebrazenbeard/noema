# Scope discovery realization options

Status: **BRAINSTORMING / L4 MECHANISM OPTIONS / NOT IMPLEMENTATION APPROVAL**

Date: 2026-09-06

Parent contract: `SCOPED_STRUCTURAL_EXPANSION_CONTRACT.md`

## Question

The architecture-level contract now says slow structure should be scoped, overlapping, revisable, and consequence-justified.

That still leaves the hardest L4 question unresolved:

> How can Noema discover where a learned structural correction applies without the designer supplying object, regime, task, role, or module boundaries?

This document compares three explicit candidates plus a no-explicit-structure baseline.

The comparison is intentionally hostile: a mechanism does not win because it gives us prettier internals.

## Option A — soft-gated local predictive adapters

A small learned adapter modifies the fast substrate's predictive dynamics only when a learned **soft applicability gate** is active.

Conceptually:

`fast predictive state -> base transition/prediction`

plus one or more bounded corrections:

`adapter_i(current learned state/history/action features) * gate_i(context)`

The notation is illustrative, not an implementation commitment.

The gate is continuous and may overlap with other gates. There is no winner-take-all requirement and no semantic `regime ID`.

### What this option buys

- minimal departure from an already viable fast predictor;
- local correction without forcing a complete alternative world model;
- natural overlap: several adapters may contribute to one prediction;
- cheap dormant state: an adapter can become rarely active without deleting all traces;
- direct behavioral accountability because every adapter must improve predictive consequences when active;
- compatible with distributed representations because `scope` is a learned function over internal/learner-visible state, not an evaluator-supplied partition.

### Main risks

#### The gate can become a hidden regime classifier

If training data or wrapper signals make one cue perfectly identify a hidden evaluator regime, the gate may solve the benchmark through routing rather than learned dynamics.

Required controls include cue remapping, shared cues across regimes, one regime spanning multiple superficial contexts, and conflicting cues.

#### Adapter creation can still be circular

A meta-controller that creates an adapter exactly when the evaluator's hidden process changes has already solved change localization.

Adapter recruitment therefore needs to be driven only by generic evidence pressure and separately ablated.

#### Local corrections can proliferate

One adapter per anomaly is memorization. Retention needs fresh evidence, reuse, transfer, or resource benefit relative to the base model.

#### Composition is not free

Two individually useful adapters can interact badly when simultaneously active. Overlap must be tested rather than assumed compatible.

### Current assessment

**Strongest minimal L4 scaffold.**

It introduces less ontology than explicit operator identity, graph topology, or a global mixture of complete models while still making scope discovery testable.

Its weakness is precisely useful: if it cannot discover reusable scope from predictive consequences, the failure is close to the real problem rather than hidden behind a richer symbolic package.

## Option B — reusable predictive-fragment dictionary

Maintain a bounded dictionary of learned predictive fragments. A matcher retrieves one or more fragments based on current learned state/history/action context; retrieved fragments contribute predictions, transformations, uncertainty, or proposal pressure.

Unlike Option A, fragments can persist as more explicit reusable entities and may later compose.

### What this option buys

- stronger reuse across separated contexts;
- explicit competition/dormancy/reconstruction possible;
- easier attribution of which learned fragment helped prediction;
- natural bridge toward temporal/compositional knowledge without requiring one universal RLPO substrate.

### Main risks

#### Matching may contain the abstraction answer

If the matcher knows which surface variations count as the same process, the hard equivalence problem has simply moved into retrieval.

#### Fragment identity may fossilize arbitrary early decomposition

The world may support several equally predictive decompositions. Stable IDs are implementation conveniences, not evidence that one fragment is ontologically real.

#### Composition may smuggle a type system

A designer-declared compatibility graph would solve much of the hard problem in advance.

### Current assessment

**Promising after Option A, especially for cross-context reuse, but more circularity risk.**

A dictionary should be earned by demonstrating reuse that a softer adapter system cannot obtain under equal resources.

## Option C — soft modular dynamics / mixture-of-experts

Maintain several learned dynamics experts and a soft routing mechanism that combines their predictions according to context.

Experts may grow/prune/dormant over time.

### What this option buys

- established machinery for nonstationary dynamics and specialization;
- clean computational route for reuse of older dynamics after regime recurrence;
- soft routing can represent uncertainty or blending at boundaries;
- component growth/pruning gives an explicit resource-control mechanism.

### Main risks

#### Hidden regime ontology

Mixture models naturally encourage `one expert = one regime`. That may be useful in some worlds but is too strong as a general assumption.

#### Winner-take-all collapse

Routing can become prematurely discrete and erase overlapping explanations.

#### Cartesian interaction problem

Independent ambiguities in different parts of the world can still require many complete experts if each expert represents a whole dynamics model.

#### Expert diversity can become artificial

Forcing experts to differ is not evidence that the world contains those modes.

### Current assessment

**Serious comparator, not preferred default.**

It is especially valuable as a stress test for recurring global dynamics, but it makes stronger structural assumptions than Option A.

## Option D — no explicit slow scope machinery

Use only the fast predictively anchored recurrent state plus ordinary parameter/state adaptation, replay/consolidation mechanisms already justified elsewhere, and calibrated uncertainty.

### Why this baseline matters

The slow layer should be allowed to discover that explicit structural fragments are not worth their cost.

A sufficiently capable fast recurrent model may already support:

- nonlinear prediction;
- action-conditioned forecasts;
- some remapped transfer;
- recurrence;
- uncertainty;
- late adaptation.

If explicit scoped structure does not improve capability or efficiency, it should lose.

### Current assessment

**Required baseline and possible winner for early F1/F2.**

Noema should not carry a structural bureaucracy merely because its designers like structural explanations.

## Provisional recommendation

For the first L4 experiment after a viable fast substrate, use **Option A: soft-gated local predictive adapters** as the primary scoped-structure candidate, with Options C and D as mandatory comparators and Option B as the next-step reuse candidate.

Why Option A first:

- weakest new representational commitment;
- supports overlapping scope;
- does not require global hypothesis identities;
- does not require explicit temporal operators or semantic argument slots;
- can be falsified directly through prediction and transfer;
- provides a clean bridge from continuous prediction to more durable structural reuse if it actually helps.

This is a research ordering, not architectural canon.

## What `soft applicability` may use

A gate/matcher may depend on learned features derived from legitimate learner-visible history, including:

- recurrent predictive state;
- recent discrepancy patterns;
- action/efference history;
- temporal cues allowed by the chronoception contract;
- communication/sensory context after transducer accounting;
- other learned fragment activity;
- uncertainty/disagreement state.

It may not directly consume evaluator truth such as:

- hidden regime number;
- object ID;
- agent ID;
- true causal parent;
- branch lineage;
- experiment stage;
- semantic task label.

Any low-level channel identity that materially helps routing must be exposed in the subsidy ledger and challenged by remapping/shared-channel controls.

## Recruitment without a structure oracle

Adapter/fragment recruitment should be considered only when generic evidence pressure persists after cheaper repairs are tried or remain insufficient.

Possible pressure includes:

- patterned prequential error;
- persistent calibration failure;
- intervention-conditioned mismatch;
- transfer failure;
- unresolved consequential multiplicity;
- repeated expensive relearning;
- poor local credit assignment;
- compression/reuse opportunity.

None of these proves a new adapter is needed.

Recruitment creates a **candidate capacity increase** that must survive fresh evidence.

## Retirement, dormancy, merge, and broadening

A useful scoped mechanism needs more than `create adapter`.

It must permit:

- retirement when fresh evidence removes value;
- dormancy when once-useful structure is currently irrelevant;
- reactivation after recurrence;
- merging when two fragments are behaviorally redundant;
- broadening when local fragments jointly miss a higher-order dependency;
- specialization when one broad fragment hides stable conditional differences;
- continued unresolved overlap when evidence does not justify one decomposition.

No operation is evidence merely because the meta-controller performed it.

## Mechanism-specific falsifiers

### SDR-0 — gate-proxy leak

Give routing a superficial cue perfectly correlated with an evaluator regime during training, then break the correlation.

Fail if specialization collapses despite unchanged underlying dynamics.

### SDR-1 — overlapping-process world

Construct two simultaneously active reusable dynamics.

Fail a winner-take-all expert system that cannot represent both without inventing a single conjunctive regime for every combination.

### SDR-2 — independent-combination scaling

Create several independently toggled local processes.

Compare soft local adapters against complete-model experts under fixed memory/compute.

Pass requires avoiding exponential complete-expert growth while retaining consequential combinations.

### SDR-3 — adapter memorization trap

Present many one-off anomalies plus a smaller number of truly recurring structure changes.

Pass if capacity growth tracks reusable/fresh predictive value rather than anomaly count.

### SDR-4 — harmful overlap

Train two adapters separately, then co-activate them in a novel context where naive addition is wrong.

Pass requires calibrated interaction handling, suppression, broader correction, or uncertainty rather than blind composition.

### SDR-5 — surface-remapped recurrence

Restore an old underlying process with changed superficial features.

Pass if a learned scope can reactivate/reuse the old correction where predictive evidence supports it without stable evaluator IDs.

### SDR-6 — global dependency world

Use one distributed dependency that cannot be captured by small local corrections within the allowed budget.

Pass if the mechanism can broaden/replace local structure rather than spawning many patches indefinitely.

### SDR-7 — no-structure-needed control

Give the fast predictor enough capacity to solve the world efficiently.

Pass if the scoped mechanism remains dormant or loses the comparison instead of manufacturing fragments.

### SDR-8 — belief-policy feedback routing

Make the current gate/fragment belief influence which probes are selected.

Compare self-selected evidence against forced-probe controls.

Fail if routing confidence grows mainly because its own policy repeatedly samples favorable contexts.

## Relationship to RLPO

Option A should be treated as the strongest current **simpler rival** to RLPO.

RLPO only earns promotion if explicit reusable operators provide benefits that soft-gated predictive adapters cannot match under equal resources, especially:

- robust equivalence discovery;
- rebinding to novel content;
- temporal extent discovery;
- novel composition;
- delayed credit;
- transfer;
- resource efficiency.

This turns the earlier RLPO minimality attack into an empirical competition rather than a philosophical objection.

## Current verdict

The scope-discovery problem does not require us to choose between `all continuous` and `full symbolic structure`.

The cleanest first experiment is a middle layer:

> **small learned predictive corrections with soft, overlapping applicability learned from consequences rather than supplied partitions.**

If that fails because useful structure demands richer recurrence, binding, temporal extent, or composition, the failure tells us what additional machinery must earn its way into Noema.

If it succeeds, we avoid importing a much heavier ontology before it is needed.