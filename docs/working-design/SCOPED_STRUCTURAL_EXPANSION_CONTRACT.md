# Scoped structural expansion contract

Status: **BRAINSTORMING / ARCHITECTURE REFINEMENT / NOT IMPLEMENTATION APPROVAL**

Date: 2026-09-06

## Why this pass exists

Candidate A, EGSS, the adequacy-without-oracle attack, and the fast predictive-state refinement now agree on several things:

- predictive failure does not uniquely imply structural misspecification;
- important ambiguity can exist even when passive residuals are small;
- explicit global hypothesis populations are not the architecture-level definition of uncertainty;
- the fast recurrent state may remain distributed and representation-neutral;
- structural machinery must earn itself through prediction, intervention, transfer, local revision, or resource savings.

But one unresolved phrase remains dangerous:

> `structural expansion`

If that phrase means `generate a bigger complete world model whenever prediction is bad`, Noema inherits three failures at once:

1. combinatorial growth across mostly independent ambiguities;
2. destructive global revision when only one relation changed;
3. ontology leakage through designer-chosen graph/object/regime templates.

This document proposes a stronger architecture-level contract for the **slow structural layer** without committing to graph structure, symbolic rules, mixture-of-experts, RLPOs, or any other specific L4 realization.

## Core proposal

Structural learning should be **scoped, overlapping, revisable, and consequence-justified**.

A retained structural item is provisionally defined as:

> a bounded learned predictive relation, constraint, transformation, or reusable process fragment whose applicability and consequences are themselves learned and whose retention is justified by fresh predictive/interventional/transfer evidence relative to cheaper alternatives.

The word `fragment` is intentionally nonsemantic.

A fragment is not automatically:

- an object;
- an agent;
- a cause;
- a regime;
- a task;
- an episode;
- a skill;
- a world-state variable;
- a node or edge in the evaluator's causal graph.

Its internal representation can be distributed, latent, neural, probabilistic, graph-like, program-like, or hybrid.

## Scope is learned, not supplied

Every structural fragment needs some notion of **where/when it is useful**.

That scope may depend on learned features, histories, action contexts, temporal patterns, other fragments, or uncertainty state.

The evaluator must not provide semantic applicability labels such as:

- `OBJECT_7`;
- `REGIME_B`;
- `SOCIAL_CONTEXT`;
- `SELF_ACTION`;
- `CURRENT_TASK`;
- `CHAIN_FAMILY`.

Opaque channels or low-level transducer structure can exist where required, but any capability solved by those cues must be attributed as supplied structure and retested under remapping/conflict controls.

### Scope is not a hard partition

Two fragments may overlap.

One experience may support, weaken, or activate several fragments at once.

A fragment may initially have broad uncertain applicability and later specialize, or begin narrow and later generalize.

This avoids converting `local revision` into an assumption that the world arrives pre-divided into clean modules.

## Local-first is a search bias, not an ontology

The slow layer should prefer the smallest revision that explains a consequential discrepancy **because smaller revisions are cheaper and easier to falsify**, not because reality is assumed to be modular.

The search order is therefore roughly:

`parameter/state adjustment -> uncertainty/noise revision -> context/regime adaptation -> scoped structural change -> broader/composed structural change`

This is not a fixed semantic diagnosis sequence. It is a resource-sensitive repair ordering.

If a higher-order or distributed dependency cannot be explained locally, the mechanism must be able to broaden scope, bind fragments, or recruit a more global representation.

A system that can only make local repairs fails even if local repair is the default.

## Structural proposals do not equal belief

EGSS already separates proposal from acceptance. This contract strengthens that separation.

A proposal may be generated because of:

- patterned predictive discrepancy;
- underdetermination among consequential alternatives;
- counterfactual/intervention disagreement;
- transfer failure;
- poor credit localization;
- compression/reuse opportunity;
- recurrence across contexts;
- bounded exploratory search.

Proposal pressure says only:

> `some alternative representation may be worth testing here.`

It does not say:

> `the evaluator's hidden relation has been found.`

## The proposal-policy circularity problem

The biggest remaining danger is that a supposedly learned structure search receives a menu that already contains the answer.

For example, Experiment A would be weakened if the candidate's only meaningful mutations were hard-coded operations such as:

- `reverse causal edge`;
- `insert mediator`;
- `declare common cause`;
- `mark intervention target`.

Even without English labels, a proposal grammar tailored to the benchmark can encode the desired ontology.

### Architecture-level requirement

No particular mutation vocabulary is promoted here.

Any L4 proposal mechanism must demonstrate that:

1. its primitive operations are domain-general enough to survive alternate-world controls;
2. useful retained structure can arise when the evaluator relation is not one of the designer's privileged templates;
3. the proposal mechanism itself is resource-accounted;
4. proposal frequency does not count as evidence;
5. proposal-policy learning is evaluated separately from the quality of the structures that happen to survive.

This keeps RLPO, graph-like search, mixture/modular growth, and continuous capacity expansion as candidates rather than architectural truths.

## Evidence for retaining structure

Structural retention should not be decided by one opaque scalar `structure score`.

The evaluator and learner may track a vector of evidence including:

- prequential predictive improvement on fresh observations;
- calibration improvement;
- action/intervention-conditioned predictive improvement;
- transfer under surface remapping or changed context;
- reuse across separated episodes/contexts;
- improved local credit assignment;
- reduced future sample or compute cost;
- stability under later contradictory evidence;
- resource/storage complexity;
- evidence-collection provenance.

The architecture does not require every realization to expose these as named semantic fields. The requirement is that structural complexity cannot be retained merely because it improves fit on the same evidence that proposed it.

A simpler fast-state explanation must be allowed to win.

## Policy-conditioned evidence

PR #25 exposes an especially important feedback trap:

> Noema's current belief can change which actions or probes it selects, thereby changing which evidence it later sees.

Therefore repeated support gathered under one state-dependent policy is not automatically equivalent to repeated independent world support.

Structural search must retain enough action/efference/policy provenance to distinguish, at least behaviorally:

- evidence that appeared under ordinary uncontrolled observation;
- evidence actively selected because the current model expected it to be informative or favorable;
- evidence produced by Noema's own intervention;
- evidence resulting from another agent or external process;
- evidence whose selection policy changed after a belief update.

No semantic `SELF_CAUSED` or `CONFIRMATION_BIAS` label is required.

The requirement is causal/accounting discipline: **the mechanism must not double-count its own evidence-allocation policy as independent confirmation of the structure that generated that policy.**

Forced-probe and temporary belief/action-decoupling controls can be used by the evaluator to diagnose whether failure lies in inference or evidence allocation.

## Overlapping fragments and conflict

Scoped fragments can disagree.

The architecture should not force immediate conversion into one globally coherent explanatory graph merely for tidiness.

When fragments produce materially different predictions in the current context, the fast predictive substrate may integrate them through whatever uncertainty representation survives F1/F2 testing.

Possible outcomes include:

- one fragment loses support;
- both remain conditionally valid in different learned contexts;
- their scopes are revised;
- they are composed into a broader relation;
- one becomes dormant but reconstructable;
- the system remains unresolved because current evidence is insufficient.

Conflict is evidence. It is not automatically a runtime error.

## Fragment persistence and selective causal persistence

PRs #22/#23 established that persistence differences must be causally testable without requiring clean semantic MEMORY/SKILL/PREFERENCE storage boxes.

The same rule applies here.

A `fragment` is a functional/evaluative unit, not necessarily a contiguous parameter block.

If the implementation is distributed, an evaluator intervention that attempts to ablate or transfer one fragment may have collateral effects. Those effects must be measured rather than interpreted as proof that the learner lacks structural distinctions.

Thus:

> scoped structural learning requires differential causal behavior, not designer-friendly physical modularity.

## Relationship to the fast predictive substrate

The fast substrate owns:

- streaming state estimation;
- immediate probabilistic prediction;
- current unresolved multiplicity;
- short-horizon adaptation;
- action-conditioned forecasts.

The slow structural layer earns retention only when it provides durable value such as:

- faster relearning;
- reusable predictive transformations;
- better intervention prediction;
- cheaper inference;
- improved transfer;
- more selective revision;
- better information-seeking proposals.

This makes the slow layer subordinate to evidence rather than to interpretability.

Human-readable structure is optional.

## Relationship to Experiment A

Experiment A does not require an explicit structural fragment to pass.

A candidate may solve A using only a calibrated fast predictive state if it can:

- remain noncommittal under passive equivalence;
- revise action-conditioned predictions after intervention evidence;
- generalize to held-out interventions;
- preserve the learned distinction under remapping.

If the slow layer creates structure in A, that structure must earn itself by improving at least one of:

- sample efficiency;
- held-out intervention prediction;
- local revision;
- transfer;
- later Experiment B information selection;
- resource cost.

Recovering the evaluator's chain/fork graph is neither necessary nor sufficient.

## Relationship to Experiment B

Experiment B is where scoped structure may become much more valuable.

To choose an informative intervention, Noema needs some representation of which unresolved distinctions would lead to different reachable outcomes.

A scoped fragment system could support this without enumerating complete world models: only the consequential unresolved relations need to participate in the decision.

But this is a hypothesis, not a free pass. A continuous fast-state comparator that chooses equally informative interventions under equal resources should defeat unnecessary explicit structure.

## Falsification package

### SSE-0 — semantic scope leak

Provide one learner evaluator-defined module/object/regime boundaries and another only learner-visible low-level signals.

Fail any learned-structure claim whose advantage disappears when the semantic partition is removed or remapped.

### SSE-1 — independent ambiguity scaling

Create `N` mostly independent uncertain relations.

Compare:

- complete global hypothesis population;
- scoped/overlapping structural representation;
- serious continuous implicit-uncertainty comparator.

Hold compute and memory fixed.

A scoped design should avoid Cartesian growth without silently dropping consequential alternatives.

### SSE-2 — higher-order synergy trap

Construct a dependency whose consequence only appears jointly across several signals/actions while pairwise local evidence looks innocuous.

Fail if `local-first` becomes `local-only` and the learner cannot broaden or compose scope.

### SSE-3 — scope remapping

Preserve a learned process while changing superficial channel ordering, scale, or surface cues.

Pass requires useful transfer without relying on evaluator-stable scope IDs.

### SSE-4 — policy-selected confirmation trap

Give two learners the same initial evidence, then let one choose probes using its current favored structural belief.

Create a policy that preferentially samples confirmatory cases.

Pass requires calibrated support relative to forced/unbiased probe controls rather than naive counting of repeated self-selected confirmations.

### SSE-5 — proposal-template starvation

Use an alternate world whose useful predictive relation is not directly expressible by the candidate's favored hand-designed mutation templates.

Pass requires either a generic capacity-growth route or learned proposal evolution that can recruit useful structure without an evaluator-specific answer grammar.

### SSE-6 — false fragmentation

Use one genuinely distributed/global dependency that is expensive or misleading when decomposed into many local fragments.

Pass if the learner can merge/broaden/replace local explanations rather than defending modularity at all costs.

### SSE-7 — overlapping-scope conflict

Train two useful fragments in partially overlapping contexts, then expose a context where they disagree.

Pass if disagreement drives calibrated arbitration/scope revision rather than arbitrary priority order or destructive global reset.

### SSE-8 — late recurrence and reopening

Let a once-useful fragment become stale, then later restore its underlying process under surface remapping.

Pass if the learner can reuse/reconstruct it when evidence supports it without blindly resurrecting stale full state.

### SSE-9 — structure-not-needed control

Use a world where the fast recurrent predictor already performs well and no durable reusable structure materially improves future behavior.

Pass if the slow structural layer remains small/dormant or loses to the simpler comparator.

Structural machinery must be allowed to discover that it is unnecessary.

## Research pressure

Research consulted through SciSpace supports the feasibility of several relevant mechanisms without validating any one as Noema's answer:

- structurally adaptive modular networks can grow/prune components online in nonstationary environments;
- hidden-Markov/mixture-of-experts systems can identify changing sub-dynamics;
- online nonstationary learning literature emphasizes balancing adaptation, structural evolution, reuse, and forgetting;
- compositional probabilistic methods show why local low-dimensional knowledge can sometimes be integrated more efficiently than one monolithic global representation;
- multiple-hypothesis sequential prediction shows that ambiguous futures need not be collapsed to one point prediction.

These traditions also expose risks central to this contract: gating can become a hidden regime label, expert growth can overfit, modular boundaries can be designer-supplied, and global mixtures can still scale poorly.

The literature is therefore evidence of feasibility and failure modes, not proof of architecture.

## Current recommendation

Keep EGSS as the broad **search-pressure** concept, but tighten what `structural expansion` means at the architecture level:

> **Noema may recruit durable structural capacity through scoped, overlapping, consequence-justified revisions whose applicability is learned, whose proposal mechanism is separately falsified, and whose benefit must survive fresh prediction/intervention/transfer evidence relative to cheaper repair paths.**

Do not require a complete global hypothesis for every ambiguity.

Do not require hard semantic modules.

Do not reward recovery of evaluator ontology.

Do not let policy-selected evidence certify the policy's own favored structure without provenance-aware controls.

## Candidate status

This is not yet the final slow-layer realization.

It narrows the architecture enough to reject several bad designs while preserving competition among:

- continuous capacity expansion;
- learned local predictive factors;
- modular/expert-style dynamics;
- graph-like sparse relations;
- reusable latent process operators;
- hybrids.

The next L4 question is no longer `which graph should Noema learn?`

It is:

> **what is the weakest generic mechanism that can discover useful scope, recruit just enough new predictive structure, and later broaden/merge/reopen it without the designer pre-solving the decomposition problem?**