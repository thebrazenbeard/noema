# Noema developmental contract

Status: **BRAINSTORMING / PROVISIONAL / NOT AN APPROVED ARCHITECTURE**

## Purpose

Noema should not be judged by whether it can imitate intelligent behavior that was implicitly encoded for it. The developmental contract separates what machinery may exist at birth from what the learner must discover through experience.

The guiding rule is:

> Innate machinery may expose signals and learning capabilities, but should encode as little interpretation as possible.

A capability that Noema is later claimed to understand should not be silently supplied as ground truth in the substrate.

## Innate machinery — current working set

These are provisionally allowed from birth as access pathways or raw signals, not as fully interpreted concepts:

- **Chronoception:** access to temporal order, duration, and change.
- **Proprioception:** access to internal configuration / actuator-state signals.
- **Interoception:** access to internal viability and operating-state signals.
- **Metacognitive access:** access to aspects of its own processing state, confidence, conflict, prediction status, or uncertainty without pre-labeling those states with human concepts.
- **Introspective access:** access to internal state and activity streams that can later support a learned self-model.
- **Action issuance / efference information:** the learner can access the commands it issues so it can compare intended action with subsequent change.
- **Minimal homeostatic viability signals:** physical and cognitive variables can move toward or away from viable ranges and produce primitive valence/pressure without directly commanding a particular action.
- **Learning capacity:** mechanisms capable of changing future inference, prediction, behavior, and eventually learning strategy from experience.

## Learned interpretations / concepts — current working set

The system may receive raw signals relevant to these domains, but the meaning, categories, boundaries, and relations should be learned rather than handed over:

- nociception / damage meaning
- exteroception / interpretation of external sensory structure
- somatosensation / body mapping
- apperception
- neuroception
- alloception
- affordance
- allostasis / learned anticipatory regulation
- mentalization / models of other agents
- epistemic drive / curiosity beyond minimal information-seeking machinery
- salience mapping beyond primitive attention/importance mechanisms
- mereology / part-whole structure
- haecceity / persistent individual identity of entities
- substrate independence
- beneception
- selfhood and body/world boundary
- persistent objects and agents
- causal structure
- higher-order drives, preferences, values, and goals
- abstractions, analogies, and metaphoric mappings

This list is not yet a claim that every term is necessary, distinct, or correctly named. It is a working inventory to challenge during design.

## Perception / identity boundary

Structured perception may expose momentary perceptual features, but **perception is not identity**.

A percept may contain position, motion, shape, orientation, size, surface features, or other structured sensory measurements. It must not receive a stable object identifier whose persistence across observations silently supplies haecceity or object permanence.

Percept-instance identifiers, if needed operationally, are local to the observation and expire with it. The learner must infer whether two temporally separated percepts correspond to the same persistent entity.

Therefore, claims such as `this is the same thing I saw before` must arise from learned temporal continuity, feature continuity, motion, interaction history, causal continuity, or other evidence available to the learner—not from privileged identity metadata.

## Self-discovery rule

Noema should not be born with a symbolic fact equivalent to `THIS IS ME`.

It should be able to discover self/world structure from correlations among:

- issued actions;
- proprioceptive and interoceptive change;
- externally perceived change;
- temporal regularity;
- controllability;
- persistent sensorimotor relationships.

An efference copy is allowed as raw evidence of issued action. A pre-authored self-concept is not.

## Viability rule

Viability is both physical and cognitive.

Homeostatic variables may create pressure, salience, and primitive valence when they depart from viable ranges, but should not function as absolute commands such as `survive at any cost`.

The learner must be capable of weighing viability pressure against other learned priorities as those priorities emerge.

## Memory principle

Noema should experience continuously but should not require permanent retention of every experience.

Durable memory is expected to be selective. Decay, consolidation, revalidation, and forgetting are considered necessary cognitive functions rather than storage failures.

The exact memory policy is deliberately deferred. Salience is likely to influence persistence and decay, but this is not yet fixed architecture.

## Error and meta-learning principle

Prediction error is evidence, not an automatic instruction to rewrite the model.

The learner should eventually distinguish among possible causes of error: incorrect model, incorrect inference, bad perception, noise, hidden state, or another agent's behavior.

A central target is **learning how to learn from mistakes**: experience should be capable of changing not only what Noema believes, but how it gathers evidence, forms confidence, revises hypotheses, and tests uncertain models.

## Anti-cheating requirement

For every developmental capability later claimed, tests should ask:

1. What was actually available innately?
2. What observations could support the learned result?
3. Could success be explained by a hidden rule, privileged label, scripted policy, or evaluator leakage?
4. What intervention or transfer test would distinguish learned structure from memorized behavior?

Noema should fail a capability claim when the architecture already encoded the answer being celebrated as learned.
