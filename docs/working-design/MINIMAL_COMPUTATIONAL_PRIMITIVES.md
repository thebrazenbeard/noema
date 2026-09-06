# Noema minimal computational primitives

Status: **BRAINSTORMING / ARCHITECTURE REDUCTION REVIEW / NOT AN APPROVED IMPLEMENTATION**

## Purpose

The design has accumulated many useful descriptions: prediction, uncertainty, RGSS, latent-process hypotheses, operators/binding, allocation, action, valuation, memory, consolidation, reopening, source separation, and metaplasticity.

That creates a new risk: **architectural re-bespoking**. We could accidentally recreate a conventional hand-designed cognitive architecture by giving every desired capacity its own named subsystem, then call the integration emergent intelligence.

This review asks which distinctions are genuinely fundamental and which can be expressed as different operating regimes of a smaller set of generic mechanisms.

## Candidate reduction

The current design appears reducible to **five conceptual primitives** plus embodiment/environmental interface.

They are:

1. **provenanced signal flow**;
2. **generative structure**;
3. **valence / concern**;
4. **competition / selection**;
5. **plasticity across timescales**.

Everything else should be challenged as either an emergent capability, a derived operation, or an engineering optimization over these primitives.

## Primitive 1 — provenanced signal flow

Noema receives and emits temporally ordered signals.

Innate source channels may distinguish only raw origin where necessary for learning:

- external sensor streams;
- proprioceptive streams;
- interoceptive/viability streams;
- introspective/metacognitive-access streams;
- issued action/efference streams;
- internal simulation/replay streams when those mechanisms exist.

The channel says **where a signal came from computationally**, not what it means.

Chronoception is part of this primitive: signals have order/duration/change.

Motor output is the outward side of signal flow; efference copy makes issued action available internally.

### What this absorbs

- perception interface;
- action/efference interface;
- epistemic source/mode separation at the raw provenance level;
- chronoception;
- much of sensorimotor grounding.

## Primitive 2 — generative structure

Noema can maintain learned internal structure that represents uncertain regularities in experience and can generate/constrain predictions about current/future state.

The primitive must support both:

- continuous/distributed representation;
- optional explicit latent-process hypotheses and learned reusable operators/bindings.

The explicit structures are Noema's hypotheses, not a privileged map of the world.

A learned structure may represent anything its evidence supports: a transient pattern, persistent process, body contingency, agent-like hidden state, relation, strategy, abstraction, or nothing humans have named.

Generative structure may recursively refer to other learned structures.

### What this absorbs

- belief state;
- uncertainty representation;
- latent factors/processes;
- dynamic relational binding;
- counterfactual simulation substrate;
- object/self/agent/causal models once learned;
- workspace contents;
- planning model;
- abstractions/analogies once learned.

### Important caveat

`Generative structure` cannot become a magic box. It still needs implementable local state, learned dynamics, bindings, and uncertainty. This reduction is conceptual, not permission to hide complexity.

## Primitive 3 — valence / concern

Some predicted/internal states matter more than others.

Without directional pressure, a predictor has no intrinsic reason to preserve viability, choose one action over another, or develop wants.

At birth this primitive is intentionally sparse:

- physical/cognitive viability deviation produces primitive directional pressure/valence;
- possibly a minimal information/exploration pressure required to make learning possible.

Higher-order concerns, preferences, drives, commitments, and values are learned structures that acquire persistent valenced influence through development.

Crucially, valence does not determine truth.

### Why this appears irreducible

Attempts to encode desire as prediction/prior expectation collapse epistemic and conative status and risk making preferred states literally more believable.

The current design therefore treats **what is supported** and **what matters** as distinct.

### What this absorbs

- homeostatic pressure;
- primitive motivation;
- learned preference/drive substrate;
- multi-concern valuation;
- commitment influence.

## Primitive 4 — competition / selection

Noema has finite compute, memory, and action bandwidth. Several hypotheses, simulations, memories, concerns, and candidate actions can be simultaneously relevant.

A generic competition/selection mechanism decides what receives scarce resources and what output is selected when action is required.

Selection is influenced by different evidence depending on the domain:

- epistemic competition uses predictive/intervention/transfer/calibration evidence;
- allocation competition uses expected informational/conative/relevance benefit and resource cost;
- action competition uses predicted trajectories plus active concerns/valence.

The mechanism may be shared while the evidence channels remain separated enough to prevent desirability from directly manufacturing belief.

### What this absorbs

- attention;
- salience allocation;
- workspace access;
- hypothesis pruning;
- action arbitration;
- information-seeking priority;
- resource-bounded deliberation.

### Important caveat

Competition must not become a homunculus. Its scoring/arbitration policies are themselves learned/plastic except for minimal finite-resource and viability seeds.

## Primitive 5 — plasticity across timescales

Noema can change generative structure and selection behavior based on experience.

Plasticity includes generic operations such as:

- parameter update;
- strengthen/weaken;
- create/retire;
- split/merge;
- bind/unbind;
- change temporal span;
- consolidate;
- reopen;
- alter proposal policy;
- alter allocation/arbitration policy.

Plasticity occurs on multiple timescales and can eventually act on aspects of its own future plasticity (**metaplasticity**).

Residual prediction/intervention failure is evidence guiding plasticity, not a separate primitive.

RGSS is therefore a **strategy of plasticity**: use persistent unexplained residual structure to localize and test structural changes.

### What this absorbs

- ordinary learning;
- structure search;
- hypothesis-generation learning;
- memory consolidation;
- decay/forgetting;
- reopenable correction;
- stability/plasticity regulation;
- metaplasticity;
- much of self-development.

## Derived operation — prediction error / residual

Residuals are important but appear derived:

`predicted signal/state - observed signal/state -> discrepancy evidence`

The residual only exists because generative structure made a prediction and provenanced signal flow supplied new evidence.

Persistent structured residuals then influence competition and plasticity.

Therefore residual is not currently treated as a sixth primitive.

## Derived operation — memory

Memory may not need to be a conceptually separate system.

At the design level, memory can be expressed as **generative structure with persistence plus timescale-dependent plasticity and resource allocation**.

Different memory forms correspond to different regimes:

- active working state: high activation, rapid update;
- episodic trace: event-linked structure with source/time support;
- consolidated knowledge/operator: slower reusable structure;
- dormant memory: low active allocation but retained reconstructibility;
- forgetting: weakening/retirement under evidence/resource pressure.

An implementation may still use physically different storage systems for efficiency. The conceptual theory does not need a separate cognitive primitive called `MEMORY`.

## Derived operation — workspace / intracommunication

A workspace can be understood as the currently selected set of generative structures receiving enough allocation to interact and influence prediction/action.

Direct hypothesis/operator bindings provide local communication; competition/allocation determines which structures become globally influential.

No central interpreter is required.

Thus the `workspace` may be an emergent active regime rather than a distinct cognitive organ.

## Derived operation — RGSS

RGSS becomes:

- generative structure predicts;
- residuals reveal persistent unexplained dependencies;
- competition allocates search resources;
- plasticity proposes structural revisions;
- generative testing evaluates them;
- selection retains useful alternatives;
- metaplasticity improves proposal strategy.

This is useful because it suggests RGSS may be an emergent learning loop rather than a special module.

## Derived operation — planning

Planning becomes:

- generative structure simulates action-conditioned futures;
- active concerns/valence evaluate their consequences;
- competition selects simulations and candidate actions;
- action is emitted through signal flow;
- outcome drives plasticity.

No separate symbolic planner is required in the foundational theory.

## Derived operation — reopenable consolidation

Consolidation/reopening becomes a timescale regime of plasticity plus retained dependency/provenance structure and anomaly-driven competition.

Stable learned structures update slowly and receive default trust/low compute until contradictory residual evidence accumulates enough to reallocate search resources and raise plasticity.

Again, no dedicated `correction module` is theoretically necessary.

## Stress test 1 — five primitives may be too abstract to falsify

A theory that says `representation + motivation + selection + learning` risks explaining everything after the fact.

**Requirement:** each primitive must eventually receive a concrete computational contract, ablation, and measurable failure mode before implementation is approved.

## Stress test 2 — competition may actually contain several irreducible mechanisms

Epistemic model selection, attentional allocation, and motor action choice may require materially different algorithms.

**Requirement:** treat `competition/selection` as one computational family only if shared mechanisms genuinely work across those domains. If not, split it based on evidence rather than theoretical elegance.

## Stress test 3 — generative structure may hide both state and computation

A hypothesis and an operator are not obviously the same kind of thing.

**Requirement:** the representation experiment must test whether a unified recursive structure is useful or whether state-like and operator-like learned forms need distinct computational handling.

Distinct handling is acceptable if it is structural rather than semantic.

## Stress test 4 — valence might be derivable from viability prediction

A strong active-inference interpretation could argue that preferred viability states are simply prior predictions.

**Current objection:** that conflates expected and desired state. Noema needs to represent `I expect X and dislike X` without contradiction.

Until a design preserves that distinction without an independent valence signal, valence remains separate.

## Stress test 5 — memory may prove physically fundamental

Long-term episodic retention and fast working inference may be computationally incompatible in one representational substrate.

**Assessment:** that may force multiple implementation stores, but it does not yet establish multiple cognitive primitives. The same learned structure can still move among persistence regimes.

## Stress test 6 — metaplasticity creates regress

If plasticity itself is learned, what learns the learning rule that learns the learning rule?

**Requirement:** recursion must bottom out in minimal innate update capacity. Metaplasticity changes bounded parameters/policies of learning; it does not require infinite layers of explicit meta-learners.

## Stress test 7 — the theory could still smuggle semantics through initialization

Even generic primitives can be initialized with weights or proposal distributions that encode object/agent concepts.

**Requirement:** developmental experiments must control initialization/training provenance. A system cannot claim emergent concept discovery if the initial parameters were pretrained on data containing the target ontology.

This reinforces the rejection of pretrained LLMs or object-centric encoders as Noema's developmental core.

## Current minimal theory

The strongest reduced form is:

> **Noema is a temporally embodied system in which provenanced signals are modeled by revisable generative structures; primitive valence makes some states matter; finite-resource competition selects what is processed and acted upon; and multi-timescale plasticity changes both the model and the policies by which future learning/selection occur.**

Objects, selves, agents, causes, memories, plans, relations, abstractions, preferences, and even much of the workspace are not foundational modules in this theory. They are developmental structures/regimes the primitives must be capable of producing.

## Why this reduction matters

If this holds, Noema becomes substantially less bespoke than the growing list of design documents suggests.

The question stops being:

`How many cognitive modules do we need?`

and becomes:

`Can five generic computational capacities generate the developmental graph we require?`

That is a much cleaner falsifiable thesis.

## Next decisive work

Before implementation, each of the five primitives needs a **minimal computational contract** describing:

- what information it may receive;
- what state it may retain;
- what outputs/effects it may produce;
- what it is forbidden to semantically encode;
- how it can be ablated;
- which developmental capability should fail when it is absent.

Those contracts should then be checked against the developmental capability graph for coverage and against the anti-cheating rules for leakage.
