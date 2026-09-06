# Noema compositional-temporal substrate options

Status: **BRAINSTORMING / L4 MECHANISM FORK / NOT AN APPROVED IMPLEMENTATION**

Date: 2026-09-06

Parent: `NOEMA_ARCHITECTURE_CANDIDATE_A_HOSTILE_VALIDATION.md`

## Problem

Candidate A's hostile validation exposed one architecture frontier that cuts across more capabilities than any other current gap:

> Noema needs a learned way to discover, retain, bind, reuse, and compose structure across time without being handed objects, semantic roles, episode boundaries, subgoals, skills, predicates, or task decompositions.

This substrate would eventually support at least:

- reusable abstraction;
- temporal chunking;
- skill formation;
- planning;
- delayed credit locality;
- grounded communication composition;
- analogy/transfer;
- later self/other process modeling.

The goal is not to reproduce a familiar cognitive vocabulary. The goal is to find the weakest generic computational structure that makes these capabilities possible.

## Research pressure

Relevant research supports several pieces but does not deliver a ready Noema architecture:

- Options / option-critic research demonstrates that initiation, policy, and termination can be learned as temporally extended behavior, but option discovery remains strongly action/reward/task framed and can inherit poor abstractions.
- Interest-function work shows that **where** a temporal abstraction applies is itself learnable, which is important for context-sensitive reuse.
- Work on temporal abstraction across both action and perception argues that abstraction should not be confined to motor policy.
- Autonomous temporal-abstraction work shows recurring successful trajectories can yield useful reusable macros, but success/failure filtering can quietly encode current task objectives into the abstraction system.
- Structured-representation and relational-learning research shows that explicit reusable structure can improve compositional generalization, but object slots, predicates, trees, graph nodes, and symbolic roles can become strong ontology priors.
- Recent OOD work warns that even strong held-out performance does not prove the learner discovered the intended compositional features.
- Work on composing representation transformations suggests a more general target: learn reusable transformations and how to compose them, rather than beginning from hand-named symbolic relations.

Representative sources consulted in this pass include:

- Hutsebaut-Buysse, Mets & Latré (2022), *Hierarchical Reinforcement Learning: A Survey and Open Research Challenges*, DOI `10.3390/make4010009`.
- Bacon & Precup (2018), *Constructing Temporal Abstractions Autonomously in Reinforcement Learning*, DOI `10.1609/AIMAG.V39I1.2780`.
- Khetarpal et al. (2020), *Options of Interest: Temporal Abstraction with Interest Functions*, DOI `10.1609/AAAI.V34I04.5871`.
- Khetarpal (2019), *Learning Generalized Temporal Abstractions across Both Action and Perception*, DOI `10.1609/AAAI.V33I01.33019890`.
- Bagaria & Konidaris (2020), *Option Discovery using Deep Skill Chaining*.
- Doumas, Puebla & Martin (2017), *How we learn things we don't know already: A theory of learning structured representations from experience*, DOI `10.1101/198804`.
- Martin & Doumas (2019), *Predicate learning in neural systems: Using oscillations to discover latent structure*, DOI `10.1016/J.COBEHA.2019.04.008`.
- Chang, Gupta, Levine & Griffiths (2019), *Automatically Composing Representation Transformations as a Means for Generalization*.
- Dittadi (2023), *On the Generalization of Learned Structured Representations*, DOI `10.48550/arXiv.2304.13001`.

These are hostile evidence and design inspirations, not authority for a mechanism choice.

## Family A — option / skill hierarchy

### Core idea

Learn temporally extended actions with some equivalent of:

- initiation/applicability condition;
- internal policy;
- termination condition;
- expected outcome/value.

Skills can compose into longer skills.

### Strengths

- directly addresses temporal abstraction and execution efficiency;
- mature research literature;
- clean relationship to action-conditioned prediction and delayed credit;
- initiation/termination can be learned rather than hand-coded;
- straightforward ablations against flat control.

### Weaknesses for Noema

- action-centric by default;
- often assumes an external task/reward signal already tells the system what counts as useful;
- can turn discovered bottlenecks into a hidden ontology of `subgoals`;
- does not by itself solve relational composition or communication structure;
- skill termination can become benchmark-specific segmentation;
- may encourage a separate hierarchy module when Noema's target is a more general reusable process substrate.

### Verdict

Useful later baseline and likely source of implementation ideas.

**Not recommended as the full common substrate.**

## Family B — explicit relational / object / predicate structure

### Core idea

Learn explicit entities, relations, argument bindings, trees, graphs, predicates, or object-centric slots and compose them structurally.

### Strengths

- strong path to systematic relational reuse;
- interpretable composition;
- natural fit for analogy, communication, and planning;
- locality can make revision and credit easier.

### Weaknesses for Noema

- risks pre-selecting `entity`, `relation`, `role`, `tree`, or `object` as the ontology of intelligence;
- object-centric or predicate-centric representations can perform well precisely because the world/benchmark shares those priors;
- explicit symbolic structure does not guarantee OOD compositional generalization;
- temporal process structure becomes secondary unless added separately;
- can easily violate the representation-equivalence principle by rewarding evaluator-readable structure.

### Verdict

Important comparator and possible later specialization.

**Too ontologically committed for Candidate A's general substrate.**

## Family C — reusable latent process operators

### Core idea

Learn **reusable transformations over selected latent state**, where the same learned operator can participate in perception, prediction, action, memory, and communication.

An operator is not born as an `object`, `relation`, `skill`, `word`, `cause`, or `subgoal`.

It is a learned reusable process hypothesis whose utility comes from improving prediction/control/compression/transfer across contexts.

Provisional name:

**RLPO — Reusable Latent Process Operator**

### Minimal operator state

A candidate operator contains:

- a learned applicability / routing function over current latent belief state;
- a learned transformation or transition model over a selected latent subspace;
- a continuation/termination hazard rather than a fixed externally supplied boundary;
- predictive uncertainty;
- optional action emission / action-conditioned dynamics;
- a resource cost;
- evidence/provenance for its formation and later revision.

The operator may be invoked for one step or persist across multiple steps.

### Binding without semantic role labels

Candidate A should avoid fixed human-named argument roles.

RLPO therefore uses **generic learned routing/binding**:

- current latent features/processes compete or are softly routed into an operator's active subspace;
- the binding is contextual and temporary;
- reuse is defined by the same transformation working across different bound latent content;
- evaluator identity labels are unnecessary.

This is still an inductive bias: reusable transformations plus dynamic routing are supplied architectural capacity.

The learning claim is only that the *content, applicability, bindings, and useful compositions* were acquired.

### Temporal abstraction

An operator earns temporal extent when maintaining the same reusable process across several steps predicts/compresses experience better than repeatedly re-solving each step independently.

Candidate boundary pressure can come from:

- predictive regime change;
- loss of transformation consistency;
- changed applicability;
- changed action/control policy;
- compression loss;
- counterfactual divergence;
- downstream transfer utility.

No single signal is treated as a semantic `event boundary` oracle.

### Skill formation

A skill is not a separate representational species.

It is an RLPO or composition of RLPOs whose learned transformation includes reliable action production and expected consequence under some applicability region.

This lets the same substrate represent both:

- a mostly perceptual/process regularity; and
- an action-bearing reusable competence.

### Planning

Planning can operate by composing candidate operators in simulated latent state:

`B_t -> O_a -> B' -> O_b -> B'' ...`

The planner need not know that the operators are `skills` or `relations`.

It only requires learned applicability, transformation, uncertainty, cost, and valuation of predicted consequences.

### Delayed credit

Operator invocation creates a compact influence trace:

- which operator/composition was active;
- which latent content was routed into it;
- what it predicted;
- what action it emitted if any.

Later outcomes can revise the implicated operator/binding/composition rather than an entire undifferentiated trajectory.

This does not solve causal credit automatically, but it gives the credit system a learned temporal/compositional unit finer than full-history chronology and coarser than one raw timestep.

### Communication

Recurring signal-context transformations can become RLPO structure without language-specific primitives.

Examples of what could eventually be learned rather than supplied:

- a signal pattern predicts attention to some latent content;
- a sequence transforms current discourse/world state in a reusable way;
- a compact directive changes expected action/context while a hedge alters only confidence/relevance scope;
- the same signal transformation transfers across different bound referents.

This provides a possible bridge from grounded signal learning to compositional language without making tokens the substrate of cognition.

### Memory / consolidation

Episodic traces provide candidate repeated transformations.

Slow consolidation may extract an RLPO when a transformation:

- recurs;
- improves compression/prediction;
- reduces control cost;
- transfers;
- survives perturbation;
- remains useful after accounting for its storage/compute cost.

An RLPO can later be weakened, split, merged, rebound, or retired when anomaly/transfer evidence changes.

## Why Family C is the current recommendation

RLPO is not recommended because it sounds elegant.

It is recommended because it potentially unifies the largest unresolved cluster with one generic bias:

> **experience may contain reusable transformations whose applicability and bindings can be learned and recomposed.**

That bias is weaker than assuming objects, predicates, skills, subgoals, sentences, or causal graphs while being stronger than an undifferentiated continuous state model.

It also fits Candidate A's process-first history better than a second dedicated hierarchy architecture.

## Hostile risks

### 1. Operator explosion

Every local pattern becomes an operator.

Counter-pressure:

- explicit resource cost;
- reuse/transfer/compression requirement;
- merge/retire pressure;
- compare against continuous baseline.

### 2. Operator fossilization

Early chunks become rigid and block later better structure.

Counter-pressure:

- late-life novelty tests;
- reopen/split/merge;
- curriculum violations;
- boundary perturbation.

### 3. Hidden semantic slots

Learned routing secretly becomes fixed object/role slots.

Counter-pressure:

- alternate worlds where object-like grouping is harmful;
- distributed constraint worlds;
- role permutation;
- variable arity/context;
- evaluator equivalence rather than slot readability.

### 4. Success-only abstraction

Only rewarded trajectories become reusable, making current goals the ontology.

Counter-pressure:

- predictive/compression/transfer discovery independent of external reward;
- learn useful processes observed in neutral/failure contexts;
- later reuse under different valuation.

### 5. Boundary leakage

Curriculum episode markers define operator termination.

Counter-pressure:

- continuous unsegmented streams;
- hidden evaluator boundaries;
- shifted boundaries;
- cross-boundary reusable patterns.

### 6. Compositionality theater

Operators exist but cannot combine systematically outside training distribution.

Counter-pressure:

- held-out recombinations;
- longer/deeper compositions than training;
- changed surface bindings;
- role permutation;
- novel operator sequences;
- compare with flat recurrent baseline.

### 7. Planner/model exploitation

Composed operators exploit predictive errors in latent simulation.

Counter-pressure:

- uncertainty-aware rollout;
- reality checks;
- held-out action consequences;
- penalize unsupported extrapolation;
- compare planned prediction with actual outcome.

## Candidate developmental progression

A minimal evidence path for RLPO would be:

1. discover a recurring transformation in a continuous stream without supplied boundaries;
2. reuse it on different latent content;
3. transfer it under surface remapping;
4. compose two learned transformations in a novel order;
5. learn context/applicability limits;
6. revise/split it after a regime change;
7. attach action production and demonstrate a reusable skill;
8. use the same substrate for a grounded signal transformation;
9. use operator-level traces to improve delayed credit assignment.

Failure at an early stage should prevent claims at later stages.

## Relation to F0/F1/F2

RLPO is **not required for F0**.

RLPO should probably be **absent from the first F1 baseline**. F1 should establish that the continuous persistent substrate itself can learn online without collapse.

For F2 / Experiment A, RLPO or another structural layer can appear as an **ablated candidate variant**, not the default winner.

The full compositional-temporal test program should come after the first-core F0/F1/F2 evidence establishes a viable persistent predictive substrate.

This protects Candidate A from letting the new mechanism redesign the first experiment around itself.

## Current recommendation

Carry **Reusable Latent Process Operators** forward as Candidate A's strongest L4 hypothesis for the compositional-temporal gap.

Do not promote it into L3 architecture yet.

The next useful design work is to define a mechanism-neutral **compositional-temporal falsification package** that could be passed by RLPO, an option hierarchy, a structured relational model, or an unforeseen better mechanism.
