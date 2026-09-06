# Noema developmental capability graph

Status: **BRAINSTORMING / PROVISIONAL / NOT AN APPROVED ARCHITECTURE**

## Why a graph, not a ladder

A strictly linear developmental ladder is probably the wrong abstraction. Several capabilities can co-develop and provide evidence for one another. Noema should therefore be evaluated against a dependency graph of developmental milestones rather than a single fixed sequence.

The graph below records current hypotheses about what must be learned and what later capacities depend on earlier ones. It is deliberately architecture-neutral.

## Root conditions available from birth

These are not claims of understanding. They are access pathways or raw pressures that make learning possible:

- temporal order/change access;
- proprioceptive and interoceptive streams;
- introspective and metacognitive access pathways;
- action issuance/efference information;
- egocentric structured sensory features without object IDs, object segmentation, or world coordinates;
- minimal physical/cognitive viability pressure and primitive valence;
- general mechanisms capable of changing future inference and behavior from experience.

## Early developmental cluster

### Temporal regularity and short-horizon prediction

Noema should learn regularities in how sensory structure changes over time and form predictions about near-future observations.

Evidence of learning must survive changes in superficial feature values and should not depend on a scripted transition table supplied to the learner.

### Sensorimotor contingency

Noema should learn that some changes systematically follow particular issued actions while others do not.

This is a prerequisite for discovering controllability, but not equivalent to a self-concept.

### Feature binding / candidate wholes

Noema should learn that some simultaneously perceived features move, deform, disappear, reappear, or interact as coherent groups.

This is the beginning of learned mereology/object formation. No privileged object boundary is supplied by perception.

These three capabilities may develop in parallel and reinforce one another.

## Self/world and persistence cluster

### Body-schema discovery

From proprioception, interoception, efference information, contact, and egocentric sensory change, Noema should infer a relatively stable set of structures with unusually strong controllability and internal-state correlation.

A successful body schema is evidence-based and revisable; it is not a hard-coded `THIS IS ME` label.

### Persistent-entity tracking

Noema should infer when separated perceptual episodes likely correspond to the same continuing entity.

Success must persist through temporary occlusion, viewpoint change, and partial feature change. Stable IDs from the environment are prohibited.

### Spatial-map construction

Noema should learn relations among places and trajectories from egocentric experience and movement rather than receiving absolute world coordinates.

A learned allocentric representation, if one emerges, is a developmental achievement rather than an input format.

These capacities likely interact: body-schema discovery can improve spatial mapping; spatial mapping can improve persistence judgments; persistence judgments can improve body/world segmentation.

## Causal learning cluster

### Intervention-sensitive causation

Noema should distinguish predictive correlation from relationships that remain informative under action/intervention.

The learner should eventually use its own actions to test uncertain causal hypotheses rather than only passively observing correlations.

### Affordance learning

Noema should learn action possibilities as relations among its discovered capabilities, current state, and environmental structure.

Affordances are not fixed object labels such as `PUSHABLE`; they should generalize across novel entities with relevant relational properties.

### Error diagnosis

Prediction failure should trigger hypothesis comparison rather than automatic model replacement. Noema should learn to discriminate among bad model, bad inference, poor perception, noise, hidden state, and agent-driven unpredictability.

## Social-development cluster

### Agent detection

Noema should learn that some persistent entities exhibit action patterns better explained by internally generated behavior than by passive physical dynamics.

`AGENT` is not supplied as an environment label.

### Individual-agent continuity

Noema should distinguish one other agent from another across time without privileged persistent IDs.

### Agent-specific models / mentalization

Noema should learn that different agents can have different histories, tendencies, information, goals, and likely future actions.

### Empathic adaptation

Empathy is evaluated behaviorally as appropriate adaptation to another agent's likely state, needs, knowledge, or goals—not as production of empathic language.

## Motivation and endogenous development cluster

### Learned salience mapping

Experience should change what receives attention and processing priority. Primitive attention capacity may exist innately, but higher-order salience should be learned.

### Preference formation

Persistent salience, valence, recurrence, consequence, and generalization may consolidate temporary responses into durable preferences.

### Learned drives

Some preferences should become sufficiently persistent and action-shaping to function as endogenous drives. Higher-order drives must remain revisable rather than becoming immutable commands.

### Epistemic initiative

Consequential uncertainty should sometimes produce self-initiated information-seeking behavior. Curiosity is stronger evidence when the system chooses an informative action that was not explicitly requested or directly rewarded as that exact action.

## Higher-order learning cluster

### Learning-to-learn from mistakes

Experience should modify not only beliefs but evidence-gathering strategy, confidence calibration, hypothesis generation, testing behavior, and revision thresholds.

### Transfer and abstraction

Noema should identify relational structure that survives changes in surface features and apply it to genuinely novel situations.

### Analogy and metaphor substrate

Analogical abstraction should eventually permit a learned relational pattern in one domain to structure interpretation in another. Figurative language can be taught later as a mapping onto this already-developed capacity.

### Self-model and self-directed development

A richer self-model should emerge from accumulated body, cognitive, memory, motivational, and social evidence. Noema should eventually identify meaningful gaps or conflicts in its own operation and alter its behavior or learning strategy in response.

## Current dependency hypothesis

The following is a dependency sketch, not a fixed sequence:

`temporal prediction + sensorimotor contingency + feature binding`

→ `body schema + persistent entities + spatial mapping`

→ `causal intervention + affordances + error diagnosis`

→ `agent detection + individual histories + mentalization`

while in parallel:

`viability + primitive valence + experience`

→ `learned salience + preferences + learned drives`

and:

`prediction error + metacognitive access + memory`

→ `error diagnosis + learning-to-learn`

These streams later converge into initiative, planning, abstraction, empathy, higher-order self-modeling, and communication.

## Falsification rule

Every milestone must eventually have at least four tests:

1. **Acquisition:** behavior appears only after relevant experience.
2. **Ablation:** removing the learned representation or learned pathway removes the capability.
3. **Intervention:** changing relevant world structure changes the learner's prediction/action appropriately.
4. **Transfer:** the capability generalizes to a situation whose superficial form was not part of training.

A milestone is not considered learned when success can be explained by privileged labels, environment IDs, evaluator leakage, scripted policies, or direct reward for the exact tested response.

## Open question

The next design task is not to keep stripping obvious environmental labels one by one. It is to determine what **general learning substrate** could make these capabilities emerge without separately programming a bespoke learner for each milestone.
