# Noema latent-process representation

Status: **BRAINSTORMING / REPRESENTATION HYPOTHESIS / NOT AN APPROVED IMPLEMENTATION**

## Why representation is now the critical problem

Residual-Guided Structure Search (RGSS) and the two-timescale search hypothesis only help if the candidate structures they create are expressive enough to support persistence, compositionality, uncertainty, local revision, counterfactual simulation, and abstraction without quietly hard-coding objecthood or other target concepts.

The representation therefore has to satisfy two competing demands:

- remain generic enough that objects, agents, selves, causes, relations, goals, and abstractions can be learned rather than supplied;
- remain structured enough that learned hypotheses can be individually revised, bound, tested, ablated, reused, and traced.

A single opaque vector is too entangled. Fixed object slots are too semantic. A fully symbolic graph with pre-authored predicates is too prescriptive.

## Three candidate representation families

### A. Fixed slot / object-centric representation

A fixed set of latent slots each tracks a candidate entity and its state.

**Advantages**

- strong locality;
- easy persistence tracking;
- efficient relational reasoning over a bounded number of slots;
- easy intervention and ablation.

**Fatal risk**

The slot itself strongly suggests that experience is naturally divided into discrete persistent entities. Even if the slot has no human-readable label, a fixed slot architecture heavily biases the learner toward objecthood and may fail on fields, fluids, distributed processes, crowds, or abstract relational structure.

**Verdict:** reject as the universal substrate. Object-like slots may be a learned specialization later, but not the representation assumed from birth.

### B. Fully distributed continuous latent field

All experience and learned structure remain in one or more high-dimensional continuous representations with no explicit factors.

**Advantages**

- very flexible;
- well suited to continuous dynamics;
- can represent phenomena that do not decompose cleanly;
- scalable with neural learning methods.

**Fatal risk**

Local revision, explicit competing hypotheses, dynamic variable binding, source/provenance separation, selective ablation, and long-term persistence become difficult. A distributed model can also memorize correlations without creating reusable compositional structure.

**Verdict:** retain as a first-class lower layer, but reject as the only representation.

### C. Dynamic latent-process hypotheses over a continuous substrate

The continuous layer remains available, but RGSS may create explicit **latent-process hypotheses** when doing so earns predictive, intervention, transfer, or credit-assignment value.

A latent-process hypothesis is not defined as an object or entity. It is a provisional model of a recurring dependency or process that spans some temporal support and contributes to future predictions.

**Verdict:** strongest current option.

## Why process-first is safer than object-first

The word `factor` can accidentally suggest a static thing. A more neutral abstraction is a **latent process hypothesis**.

A learned process can eventually behave like:

- a persistent object whose state changes slowly;
- a motion pattern;
- a location-like regularity;
- an interaction;
- a body-related contingency;
- another agent's hidden state trajectory;
- a recurring strategy;
- a relation among other learned structures;
- an abstract transformation;
- a distributed phenomenon that never becomes object-like.

Objecthood then becomes one possible stable pattern of process organization rather than the primitive representation format.

This is consistent with chronoception being available from birth while persistent identity remains learned.

## Minimal conceptual contents of one latent-process hypothesis

The representation should expose only computational structure, not semantic type labels.

A candidate hypothesis provisionally needs:

### 1. Internal hypothesis handle

An internal address allows working memory, provenance, local update, and ablation to refer back to the same **hypothesis**.

This is not a world-object ID.

Important distinction:

> **hypothesis continuity is not referent identity.**

Noema may keep one internal hypothesis alive while remaining uncertain about whether it corresponds to one external entity, several entities, a relation, or no real persistent thing at all.

### 2. Latent state / state belief

The hypothesis carries a learned internal state sufficient to contribute to prediction.

The exact encoding may be continuous, discrete, multimodal, or hybrid. The architecture should not force every learned process into one semantic family.

### 3. Uncertainty / competing state possibilities

A hypothesis cannot collapse every ambiguous situation to one point estimate. It must be possible to preserve multiple plausible states or confidence structure when evidence does not discriminate them.

Exact Bayesian representation is not required at the design level, but uncertainty must be behaviorally meaningful and calibratable.

### 4. Temporal support and dynamics

A hypothesis has some learned temporal extent and transition behavior.

Its persistence is therefore evidential, not assumed. A hypothesis can:

- last milliseconds;
- recur intermittently;
- persist for long periods;
- split into different regimes;
- decay or disappear;
- be reactivated from memory.

### 5. Generative grounding

The hypothesis must be accountable to experience by affecting predicted future sensory/internal state or the predicted consequences of action.

A latent symbol that cannot change any prediction, intervention expectation, transfer behavior, valuation, or credit assignment has no demonstrated cognitive meaning.

### 6. Evidence/provenance trace

The system needs enough approximate traceability to know what observations, memories, simulations, interventions, or other hypotheses support the candidate and which predictions it materially influenced.

This need not be a human-readable audit log. It must be sufficient for selective revision, confidence change, ablation, and evaluation.

### 7. Learned bindings / dependencies

A hypothesis may participate in dynamically learned dependencies with other hypotheses.

Bindings cannot use innate semantic roles such as `AGENT`, `PATIENT`, `OWNER`, `INSIDE`, or `BELIEVER`.

The primitive capacity is only to bind addressable arguments/participants to a reusable learned transformation or dependency.

### 8. Resource status

Because explicit structure is costly, a hypothesis needs some resource state: active, provisional, consolidated, low-priority, dormant, or eligible for retirement.

Those are operational states, not semantic categories about the world.

## Relations and operators

The hardest remaining representational requirement is reusable relation structure.

A relation should not begin as a named predicate. The current hypothesis is that Noema can learn **reusable transformations/operators** that take dynamically bound latent arguments and improve prediction across multiple contexts.

For example, if the same transformation predicts many different surface situations when attached to different learned processes, parameter sharing becomes useful. The learned transformation can then function as an abstract relation before Noema has any linguistic or human-readable concept for it.

### Generic operator requirements

A learned operator may have:

- variable or bounded arity;
- addressable argument positions as computation;
- learned transformation/dynamics;
- no innate semantic role names;
- uncertainty about applicability;
- reusable parameters across different bindings;
- recursive ability to operate over outputs of other learned operators/hypotheses;
- intervention and transfer accountability.

### Permutation test

If an operator only works when one physical feature always occupies one fixed position, it may be memorizing slot meaning.

A genuine reusable operator should survive controlled rebinding/permutation when the underlying learned relation is preserved.

## Three ways to realize binding later

No implementation family is selected, but three broad mechanisms remain plausible:

### Graph-backed dynamic binding

Explicit hypothesis records are connected through dynamically created dependency/operator edges.

**Strength:** locality, uncertainty, provenance, ablation.

**Risk:** graph structure itself can become too discrete or hand-authored.

### Vector-symbolic / distributed binding

Learned vectors are composed through generic binding/unbinding operations or attention-like addressing.

**Strength:** flexible, parallel, potentially scalable.

**Risk:** difficult local revision and uncertainty; unbinding can be noisy; semantic provenance may become opaque.

### Learned program/operator binding

Reusable learned functions are instantiated over dynamically selected arguments.

**Strength:** strong compositionality and counterfactual reuse.

**Risk:** proposal/search complexity and temptation to supply useful primitive operators by hand.

Current recommendation: treat **graph-like locality plus learned continuous content/operators** as the slow explicit layer, while leaving the exact binding implementation open until falsification experiments reveal what is actually needed.

## Stress test 1 — internal handles may be mistaken for external identity

A persistent internal handle is necessary for local revision but could become an implicit claim that the same external thing persists.

**Requirement:** evidence supporting `this hypothesis is still useful` must remain separate from evidence supporting `the external referent is the same individual`.

A hypothesis may change its referential interpretation, split, or be retired without corrupting internal bookkeeping.

## Stress test 2 — process-first still contains temporal bias

Representing learned structure as process assumes temporal change is fundamental.

**Assessment:** this bias appears admissible because chronoception and continuous experience are already explicit birth conditions. It does not specify what persists, how things group, or what categories exist.

It should still be tested in environments containing static/distributed structure where temporal evidence is weak.

## Stress test 3 — explicit hypotheses may over-fragment experience

RGSS could create too many local process hypotheses and lose global coherence.

**Requirement:** hypotheses can overlap, nest, merge, share parameters, and leave phenomena distributed when explicit decomposition adds no benefit.

## Stress test 4 — reusable operators may simply hide semantic predicates

A learned operator could be initialized or constrained so strongly that it effectively means `contains`, `causes`, or `agent-does` from birth.

**Requirement:** operator semantics must be earned through reuse. Generic initialization and alternate-world transfer tests must show that the same machinery can learn radically different transformations.

## Stress test 5 — recursion can explode

Allowing hypotheses and operators to reference other hypotheses/operators creates open-ended compositional power but also combinatorial growth.

**Requirement:** RGSS and allocation must make recursive composition demand-driven. Reuse, predictive benefit, intervention value, and resource cost determine which compositions receive explicit representation.

## Stress test 6 — local structure can become globally inconsistent

Several individually useful hypotheses may imply incompatible global predictions.

**Requirement:** the workspace must support joint simulation/consistency pressure without a privileged central interpreter. Conflicts remain explicit and may trigger hypothesis revision or branching.

## Stress test 7 — explicit structure may not beat the continuous layer

If the continuous substrate achieves the same transfer, intervention, planning, and local-credit performance with lower cost, explicit factor/process formation is unnecessary overhead.

**Requirement:** every explicit representation must earn itself against a distributed baseline.

This is a decisive falsifier of DGFW rather than a defect to paper over.

## Strongest current representation hypothesis

The current best representation is therefore not an object graph and not one recurrent vector.

It is:

> a **continuous predictive substrate** plus optional, dynamically created **latent-process hypotheses** with uncertain state, learned temporal dynamics, approximate provenance, generative grounding, and learned reusable bindings/operators.

Explicit structure exists only where it improves prediction, intervention, transfer, counterfactual simulation, persistence, or selective credit assignment enough to justify its cost.

## Immediate next attack

The next decisive design question is whether one generic operator/binding mechanism can support both low-level relational structure and high-level abstraction without becoming either:

1. too weak to represent compositional cognition; or
2. so expressive that search becomes computationally hopeless.

The falsification target should compare a small set of generic binding grammars on the same ambiguous developmental tasks, with all semantic role labels prohibited.
