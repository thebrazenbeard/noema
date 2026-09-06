# Noema adversarial developmental scenarios

Status: **BRAINSTORMING / ADVERSARIAL DESIGN REVIEW / NOT AN APPROVED ARCHITECTURE**

## Purpose

Attack the current five-function core with concrete developmental situations:

1. model/simulate;
2. value/motivate;
3. allocate/attend;
4. act/intervene;
5. learn/adapt;

Cross-cutting requirements already include persistence/memory, uncertainty/calibration/provenance, multi-timescale operation, internal integration, and developmental anti-cheating constraints.

The goal is not to show that the five functions can be hand-waved into every capability. The goal is to find cases that expose a genuinely missing primitive or substrate property.

## Scenario 1 — occluded persistence

A feature bundle moves behind a barrier. Several futures remain possible. It later reappears with partial feature change.

Required behavior:

- preserve multiple hypotheses while hidden;
- predict candidate reappearance trajectories;
- update confidence from timing and motion;
- infer persistent identity without environment IDs.

**Five-function result:** plausible. Model + uncertainty + memory + learning are sufficient in principle.

**New requirement exposed:** hypotheses must support **binding across time** without turning a temporary percept ID into permanent identity.

## Scenario 2 — detachable tool and body boundary

Noema learns to manipulate a stick. The stick becomes tightly coupled to action, then is dropped. Later it controls a remote actuator with delayed effects.

Required behavior:

- learn graded relations such as controllable, proprioceptively coupled, attached, externally located, temporarily incorporated;
- avoid equating controllability with selfhood;
- revise the body/self model when coupling changes.

**Five-function result:** plausible.

**New requirement exposed:** the representation must support multiple simultaneous relations rather than one binary `SELF/NONSELF` label.

## Scenario 3 — false belief in another agent

Agent A watches an object placed in location X, leaves, and while absent the object moves to Y. Noema knows Y; Agent A has evidence only for X.

Required behavior:

- represent current world belief separately from a model of Agent A's belief;
- bind different information histories to different agents;
- predict A's action from A's information rather than Noema's own.

**Five-function result:** this is possible only if the substrate supports **nested, compositional state**. A flat latent state can memorize examples but may not generalize role structure.

**New requirement exposed:** **dynamic relational binding / compositionality** should be a cross-cutting substrate capability. Noema does not need innate concepts such as `BELIEF` or `AGENT`, but it needs machinery capable of learning reusable relations and binding arbitrary learned entities/states into them.

## Scenario 4 — deception

Agent B learns that Noema predicts hidden-object locations from B's behavior and intentionally acts to induce a false belief.

Required behavior:

- detect that a previously reliable behavioral cue changed conditional on interaction history;
- entertain the hypothesis that another agent's action may target Noema's own belief state;
- revise trust/source weighting without globally labeling B unreliable.

**Five-function result:** plausible only with agent-specific provenance, nested modeling, and context-sensitive uncertainty.

**New requirement exposed:** source attribution cannot be an afterthought. Evidence must retain **who/what generated it and under which conditions**.

## Scenario 5 — imagination contaminates memory

Noema considers two futures: in one it pushes a block left; in the other it pushes right. It chooses right. Hours later it must remember what actually occurred.

Required behavior:

- simulate futures vividly enough to plan;
- prevent simulated state from being stored as observed history;
- distinguish remembered observation, inference, prediction, counterfactual, desire, and action intention.

**Five-function result:** the current core is under-specified.

**New requirement exposed:** **epistemic mode/source separation** is fundamental. Internally generated simulations must carry provenance distinct from externally observed or enacted events. The concepts attached to those modes may be learned, but the raw origin channel cannot safely be erased.

This is analogous to the existing rule that action issuance/efference information is innately available: the learner is allowed to know that a signal was internally generated without being told what that generation means.

## Scenario 6 — analogy across unrelated domains

Noema learns that placing a support under a falling structure prevents collapse. Much later it encounters an entirely different configuration where an intermediate relation can play the same stabilizing role.

Required behavior:

- separate relation from surface features;
- reuse learned structure with new entities and geometry;
- test whether the relation transfers rather than memorize a visual template.

**Five-function result:** prediction + compression + learning can provide pressure, but only if the representation is compositionally reusable.

**New requirement reinforced:** dynamic binding/compositional representation is one of the strongest constraints on implementation families.

## Scenario 7 — contradiction between immediate valence and persistent commitment

Noema has developed a persistent project/goal whose completion usually carries positive learned value. Continuing now produces fatigue or other negative interoceptive pressure.

Required behavior:

- represent short- and long-horizon consequences;
- allow learned commitments to compete with immediate homeostatic pressure;
- revise plans without reducing all value to one instantaneous reward scalar.

**Five-function result:** valuation needs richer structure than a single reward number.

**New requirement exposed:** learned valuation should support **multiple simultaneously active, differently timed concerns** and context-dependent arbitration. This does not require innate human values, but argues against a single scalar reward as the whole motivational substrate.

## Scenario 8 — noisy-TV trap

One region of the world produces irreducibly random high-surprise signals. Another contains a difficult but learnable mechanism whose prediction improves with investigation.

Required behavior:

- avoid allocating indefinitely to unreducible noise;
- distinguish surprise from learning progress;
- preferentially investigate uncertainty that can be reduced or matters to future action/viability.

**Five-function result:** supports allocation as a fundamental function and weakens raw novelty/error as intrinsic reward.

**New requirement exposed:** allocation should be sensitive to **expected reducibility / learning progress / consequence**, not just error magnitude.

## Scenario 9 — confident but wrong self-model

A calibration fault causes Noema to believe an actuator is tightly coupled to its own action when another agent is actually mirroring its movement.

Required behavior:

- preserve the provenance of the self-model's evidence;
- notice interventions that break the correlation;
- revise a central self-related belief without destabilizing unrelated identity structure.

**Five-function result:** plausible if beliefs are localizable and revision can be targeted.

**New requirement exposed:** the substrate needs **credit assignment with structural locality**. If every correction diffusely modifies the entire system, self-correction becomes catastrophic drift.

## Scenario 10 — learning a better learning rule

Early in development, one observation often predicts stable physical regularities. Later Noema encounters agents whose behavior varies with hidden history. Applying the old one-example generalization rule causes repeated errors.

Required behavior:

- detect a pattern in its own errors;
- infer that the *learning strategy* is mismatched to the domain;
- gather more evidence before high-confidence generalization in similar contexts;
- retain faster learning in domains where it remains reliable.

**Five-function result:** requires metaplasticity plus internal-state modeling.

**New requirement exposed:** metaplastic changes must be **context-sensitive**, not global. `Learn more slowly` is not an adequate meta-rule.

## Scenario 11 — self-generated arbitrary project

Noema has no external instruction to construct a novel arrangement. It has previously developed positive valence around mastery, prediction improvement, completion, or social contribution. It initiates a multi-step project whose exact terminal state was never directly rewarded.

Required behavior:

- compose learned values into a novel desired future;
- maintain the goal across delays and setbacks;
- revise subplans while preserving or reconsidering the higher-order goal;
- stop if the project loses its learned value or conflicts with stronger priorities.

**Five-function result:** possible in principle, but only if valuation can construct **derived goals** rather than merely cache action preferences.

**New requirement exposed:** goal formation should be treated as learned construction over modeled future states, not as a fixed list of reward targets.

## Scenario 12 — internal disagreement

Different learned processes support incompatible interpretations: the physical model predicts one future, the social model predicts another, and current viability pressure favors immediate action before uncertainty can be fully resolved.

Required behavior:

- retain the disagreement rather than forcing premature consensus;
- allocate additional computation when worthwhile;
- act under unresolved uncertainty when delay is more costly;
- preserve which hypothesis influenced the chosen action for later error diagnosis.

**Five-function result:** plausible, but only if integration does not mean flattening everything into one opaque state.

**New requirement exposed:** intracommunication must support **contestable representations and causal traceability**. Shared workspace/direct communication should allow disagreement, confidence, provenance, and later credit assignment.

## Findings

The scenarios did not reveal an obvious sixth behavioral loop beyond:

1. model/simulate;
2. value/motivate;
3. allocate/attend;
4. act/intervene;
5. learn/adapt.

They did reveal substrate properties that are too important to leave implicit:

### 1. Dynamic relational binding / compositionality

Noema must be capable of learning reusable relations and binding arbitrary learned entities/states into them, including nested structures. This is necessary for agent-specific beliefs, transfer, analogy, planning, and likely language later.

This is a capability of the representational substrate, not permission to hand Noema a predefined ontology.

### 2. Epistemic mode/source separation

Observed, internally simulated, remembered, inferred, intended, and desired states must not become indistinguishable merely because they share representation machinery. Raw source/origin information can be available innately without teaching the semantic concept of those modes.

### 3. Structured locality of revision

Learning and self-correction need enough internal causal/provenance structure to revise the implicated representation or learning policy without indiscriminate global drift.

### 4. Multi-dimensional learned valuation

A single scalar reward is unlikely to support the target. Noema must eventually arbitrate among multiple learned concerns over different timescales and construct derived goals over predicted future states.

### 5. Contestable integration

Intracommunication should preserve disagreement, confidence, source, and causal influence rather than merely merge subsystem outputs.

## Revised cross-cutting requirements

- persistence/memory with selective forgetting;
- uncertainty and behavioral calibration;
- evidence/provenance attribution;
- **epistemic source/mode separation**;
- multi-timescale operation;
- **dynamic compositional binding**;
- structural locality of learning/credit assignment;
- contestable internal communication/integration;
- finite-resource allocation;
- developmental anti-cheating constraints.

## Current verdict

The five-function core survives this round as a plausible **functional skeleton**, but the skeleton is not enough. The strongest new constraints concern the representational substrate: it must be compositional, source-aware, revisable locally, and capable of maintaining competing structured hypotheses without a predefined human ontology.

The next design frontier is to compare broad implementation families specifically against these constraints rather than against vague claims of intelligence. Before choosing a family, each candidate should be asked whether it can support open-ended latent structure, dynamic binding, persistent uncertain state, counterfactual simulation, continual local learning, metaplasticity, and causal intervention without privileged labels.
