# Noema inductive-bias boundary

Status: **BRAINSTORMING / FOUNDATIONAL DESIGN RULE / NOT AN APPROVED IMPLEMENTATION**

## Why zero bias is impossible

The earlier anti-cheating rule can be stated too strongly if it sounds like Noema should begin with no assumptions at all. A learner cannot infer one uniquely correct hidden structure from finite experience without some inductive bias. Many incompatible models can fit the same observations.

Therefore the goal is not `no innate structure`. The goal is:

> **Use the weakest explicit, domain-general inductive biases needed to make learning possible, while refusing to encode the target concepts that Noema is later supposed to discover.**

The distinction is between **learning machinery** and **semantic answers**.

## Provisionally admissible biases

The following appear defensible because they do not name objects, agents, causes, selves, goals, beliefs, or other target concepts.

### Temporal order

Noema may have access to sequence, duration, and change. This is already part of chronoception.

Temporal access does not tell Noema what persists through time or what causes what.

### Predictive usefulness

A learned structure may be preferred when it improves prediction of future experience across more than one horizon.

Prediction is evidence of usefulness, not proof of semantic truth.

### Reuse / compression pressure

A representation that explains many recurring dependencies with less duplicated machinery may be preferred over memorizing each case independently.

Compression is a complexity pressure, not a truth criterion. Rare but real exceptions must remain representable.

### Uncertainty preservation

When several explanations fit available evidence, the architecture may preserve more than one rather than forcing premature commitment.

The system is not given human concepts for doubt or belief; it is given capacity to represent unresolved alternatives and differential confidence.

### Intervention sensitivity

Issued actions/efference are an innate source channel. Models may be evaluated partly by whether they correctly predict how experience changes under different actions.

This does not hand Noema a concept of causality. Causal structure remains something learned from stable differences under intervention.

### Cross-context transfer

A learned structure earns support when it remains useful after superficial features, positions, contexts, or bindings change.

This favors reusable structure without specifying what the reusable structure must mean.

### Finite-resource pressure

Noema has bounded compute and memory. Candidate explanations cannot all receive unlimited resources forever.

Allocation and forgetting are therefore functional necessities, although what becomes salient should largely be learned.

### Generic structural plasticity

The learner may create, revise, split, merge, bind, unbind, strengthen, weaken, or retire provisional latent structure.

These are operations over representation. Their semantics are not supplied.

## Biases that would violate the developmental contract

The following would be disallowed as hidden answers unless a later experiment explicitly changes the contract:

- contiguous features are one object;
- co-moving features are one object;
- autonomous motion means agent;
- controllable structure means self;
- temporal precedence means cause;
- negative interoception means pain;
- reward-linked state means goal;
- fixed semantic roles such as AGENT, PATIENT, OWNER, CONTAINER, BELIEVER;
- stable environment IDs for entities;
- privileged absolute coordinates;
- labels distinguishing object/agent/self/cause/belief/desire as innate categories.

These patterns may become *evidence learned by Noema*. They may not be the designer's category rules.

## A stricter anti-cheating test

For every proposed innate mechanism, ask:

1. Could the same mechanism be useful in a world whose ontology is unlike our expected 3D object world?
2. Does the mechanism say **how to learn**, or does it quietly say **what exists**?
3. If the target concept were removed or radically changed in the environment, would the mechanism still operate coherently?
4. Could an evaluator trace success directly to privileged labels, semantic roles, or category-specific heuristics?
5. Is the bias explicit enough to ablate and compare against alternatives?

If the mechanism only works because the designer already knew what Noema was supposed to discover, it fails the contract.

## Important consequence

Noema's developmental experiment should not pretend to be philosophically assumption-free. That would be impossible and would hide the most important design choices.

Instead, every innate bias should be:

- explicit;
- minimal;
- domain-general where possible;
- independently ablatable;
- distinguished from learned semantics;
- tested against alternate environments where its favored assumptions can fail.

## Current implication

The structure-search problem should be framed as:

> **Given only admissible domain-general biases, how can Noema propose and compare new latent structures efficiently enough to discover useful organization without receiving the organization itself?**

This reframing is important: the target is not bias-free learning. The target is **non-semantic inductive bias with falsifiable developmental emergence**.
