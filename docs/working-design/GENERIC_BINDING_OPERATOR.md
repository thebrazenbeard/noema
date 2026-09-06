# Generic binding/operator hypothesis

Status: **BRAINSTORMING / COMPOSITIONALITY HYPOTHESIS / NOT AN APPROVED IMPLEMENTATION**

## Problem

The latent-process representation still has one major hole: saying that Noema can "learn relations" does not explain how a learned relation can be reused with different participants, nested inside other relations, revised locally, and simulated counterfactually without pre-authoring semantic predicates.

A compositional system needs some form of **variable binding**. The design challenge is to supply the computational ability to bind without supplying what the bindings mean.

## Candidate principle

A relation-like structure should be learned as a **reusable conditional operator** over dynamically bound latent-process hypotheses.

The operator is not born as `CAUSE`, `INSIDE`, `BELIEVES`, `SUPPORTS`, or any other human relation. It is a parameterized dependency that earns reuse because the same learned structure improves prediction or simulation across different bindings and contexts.

The general form is conceptually:

`bound latent states + context/action -> distribution over joint/current/future latent or sensory consequences`

The mapping may express a static constraint, temporal transformation, action-conditioned interaction, or higher-order relation.

## Three binding approaches under consideration

### Approach A — explicit graph/hypergraph edges

A learned operator instance connects explicit hypothesis handles through an edge or hyperedge.

**Strengths**

- excellent local revision and ablation;
- clear participant binding;
- straightforward influence/provenance tracing;
- naturally supports competing local hypotheses.

**Risks**

- explicit graph structure may over-discretize phenomena;
- searching edges and hyperedges is combinatorial;
- fixed edge types would leak semantics.

**Assessment:** strongest explicit slow-layer structure, provided edge/operator types themselves are learned rather than selected from a semantic vocabulary.

### Approach B — vector-symbolic / distributed binding

Participants and learned relation content are bound in a shared vector space using generic composition/unbinding or attention-like mechanisms.

**Strengths**

- scalable parallel computation;
- no need for a rigid graph schema;
- can support superposition and soft binding.

**Risks**

- provenance and selective revision become harder;
- unbinding/interference can degrade with depth;
- competing hypotheses may blur together;
- exact role permutation and recursive composition can become opaque.

**Assessment:** attractive inside the continuous/fast layer, but currently weak as the sole slow explicit hypothesis representation.

### Approach C — learned program/function application

A reusable learned function is applied to dynamically selected arguments.

**Strengths**

- powerful abstraction and counterfactual reasoning;
- clean parameter reuse;
- naturally supports recursive composition.

**Risks**

- program/operator search can become the entire intelligence problem;
- supplied primitive functions may leak ontology;
- continuous uncertain sensorimotor grounding is difficult.

**Assessment:** plausible as a later consolidation form for highly reusable abstractions, but risky as the birth substrate.

## Current synthesis

Use a **graph-like explicit binding structure at the slow hypothesis layer**, while allowing the content of hypotheses and operators to remain learned/continuous.

The graph is not a world graph. It is a graph of **Noema's current hypotheses**.

That distinction matters: the architecture is allowed to say `hypothesis A is currently bound into candidate dependency R with hypothesis B`; it is not allowed to say `object A is physically inside object B` unless that semantic relation has been learned.

## Generic learned operator contents

A provisional operator hypothesis needs only computational fields:

### Operator parameters

Learned parameters describing a reusable constraint/transformation/dependency.

These parameters carry no innate semantic label.

### Learned address positions

An operator may expose a bounded number of argument addresses or dynamically extensible participation positions.

The addresses are computationally distinguishable but semantically unnamed.

An asymmetric learned dependency is therefore possible without pre-labeling one slot `agent` and another `patient`.

### Optional learned position/role embeddings

Instead of permanent semantic roles, an operator may learn latent position embeddings jointly with its transformation.

Those embeddings initially mean only `the first/second/etc. functional place in this learned dependency`.

If later experience shows that a similar latent role recurs across many operators, RGSS may itself propose reusable higher-order role structure.

### Bound participant handles

An instantiated operator points to current latent-process hypotheses occupying its argument positions.

The handles refer to internal hypotheses, not privileged world entities.

### Applicability / uncertainty

The operator instance has confidence or competing applicability hypotheses. A relation need not be asserted merely because it was proposed.

### Temporal scope

The operator may constrain an instantaneous joint state, a transition over time, or a longer-horizon dependency.

Temporal scale is learned/revisable rather than tied to one relation class.

### Generative consequence

The operator must influence predictions, counterfactuals, action consequences, transfer, valuation, or credit assignment. Otherwise its meaning is not grounded enough to justify retention.

### Evidence / influence trace

Enough approximate provenance is retained to support selective revision and ablation.

## How a relation could be discovered without a relation detector

A plausible domain-general route is **parameter-sharing pressure over repeated transformations/dependencies**.

1. Separate local models initially explain several situations independently.
2. RGSS notices that similar residual structure or state transformation recurs across different bindings/context.
3. It proposes tying part of those models through one shared operator.
4. The shared operator is compared against independent memorization.
5. It earns support only if reuse improves held-out prediction, transfer, intervention response, counterfactual usefulness, or complexity/resource cost.
6. The learned operator remains revisable and semantically unnamed.

This gives abstraction a concrete developmental mechanism: **discover that one transformation is reusable across different things before knowing what humans call that transformation.**

## Arity problem

Pairwise relations are computationally convenient but insufficient. Some dependencies are genuinely higher-order and invisible in pairwise statistics.

The search mechanism therefore needs a way to grow/shrink participation generically:

- start with a small implicated set localized by residual/influence evidence;
- test whether adding another bound hypothesis explains additional residual structure;
- remove participants whose contribution is redundant;
- preserve a higher-order operator only when it earns enough predictive/transfer/intervention value to justify the added complexity.

This is a resource-bounded hyperedge search, not an exhaustive search over all subsets.

## Symmetry and role semantics

Some learned relations are symmetric; others are directional or role-sensitive.

The architecture should not encode which is which.

A candidate operator can be tested under participant permutation:

- if predictions remain unchanged, symmetry can be learned/compressed;
- if predictions change systematically, asymmetric position structure is supported;
- if the same asymmetric pattern transfers to new participants, the learned positions have acquired reusable functional meaning.

This is a route to learned role structure without semantic role labels.

## Recursive composition

Higher cognition requires relations among relations and hypotheses about hypotheses.

A rigid two-level system would fail here. Therefore an operator output or operator-instance hypothesis must be bindable into another learned operator when doing so proves useful.

Examples the architecture should eventually be capable of representing without pre-authored semantics include:

- one agent's state about another agent's state;
- a causal relation that holds only under another condition;
- an analogy between two learned relational patterns;
- a plan whose step depends on a predicted counterfactual relation.

Recursive composition is permitted computationally, but explicit nesting must remain resource-bounded and evidence-driven.

## Stress test 1 — address positions become hidden semantic roles

Even unlabeled slots can develop fixed meanings because training always presents the same physical categories in the same position.

**Requirement:** controlled permutation/rebinding tests must vary which surface entities occupy which addresses. Transfer should depend on the learned relation, not fixed surface-slot association.

## Stress test 2 — parameter sharing can merge superficially similar but distinct relations

Two dependencies may look alike in ordinary data but respond differently under intervention.

**Requirement:** operator consolidation must preserve competing alternatives when interventions or context reveal distinct dynamics. Reuse/compression does not override contradictory evidence.

## Stress test 3 — universal operators can memorize instead of abstract

An overpowered neural operator could condition on every participant detail and effectively memorize each case despite nominal parameter sharing.

**Requirement:** transfer/recombination tests must use novel participant features and bindings. Capacity/complexity controls should make reusable structure cheaper than participant-specific memorization without forcing one specific abstraction.

## Stress test 4 — graph structure can dominate the continuous substrate

If every useful interaction is forced into an explicit edge, distributed fields and diffuse dependencies will be misrepresented.

**Requirement:** explicit operators are optional. The distributed layer remains allowed to model phenomena whose explicit binding provides no measurable advantage.

## Stress test 5 — recursive composition becomes combinatorial

Allowing arbitrary operators over operators creates an enormous hypothesis space.

**Requirement:** higher-order composition should be proposed primarily from recurring residuals, analogy/reuse evidence, live prediction conflict, or goal-relevant simulation needs, with an exploration floor for unanticipated structure.

## Stress test 6 — abstract operators become ungrounded symbols

A high-level relation might become detached from sensorimotor evidence and continue circulating because internal modules agree with one another.

**Requirement:** grounding may be indirect but cannot disappear. A retained abstraction must eventually improve prediction, intervention, transfer, planning, valuation, compression, or error diagnosis in ways that can be causally tested.

## Strongest surviving hypothesis

The strongest current route to compositionality is:

> **dynamically learned operator hypotheses with semantically unnamed argument positions, bound to explicit internal hypothesis handles, earning reuse through parameter sharing across contexts and remaining accountable to generative/intervention evidence.**

Graph-like locality appears useful for the slow explicit layer; continuous/vector binding may still be used internally for fast representation and operator content.

## Important implication

The architecture does not need to be born knowing `relations`. It needs to be born capable of:

- representing several current hypotheses separately;
- conditionally coupling them;
- learning a transformation/constraint over their joint states;
- reusing that learned transformation with different bindings;
- evaluating whether reuse actually helps.

Human-like relational concepts can then be developmental interpretations of reusable learned dependency structure rather than primitive symbols.

## Next decisive attack

The next problem is **selection and objective conflict**.

Prediction, intervention value, transfer, compression, calibration, valuation, and resource cost can disagree. A Pareto frontier delays arbitrary scalarization, but an acting system eventually must choose what model to trust, what hypothesis to test, and what action to take.

The design must determine whether Noema needs one privileged global utility/arbitration function—which risks smuggling values—or whether arbitration itself can be a learned, multi-concern process grounded initially only in viability/valence and evidence quality.
