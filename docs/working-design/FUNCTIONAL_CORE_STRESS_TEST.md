# Noema functional core stress test

Status: **BRAINSTORMING / ADVERSARIAL DESIGN REVIEW / NOT AN APPROVED ARCHITECTURE**

## Context

The predictive-substrate review weakened the original idea of a single recurrent predictive state and replaced it with a stronger requirement: uncertain belief over possible world states/explanations, multi-horizon prediction, intervention-sensitive learning, plasticity/metaplasticity, persistence across timescales, and viability/valence.

The current question is whether the resulting functional decomposition is missing any primitive operation.

## Current candidate functions

1. **Modeling / simulation** — maintain uncertain beliefs, predict future experience, preserve competing explanations, and support counterfactual rollouts.
2. **Action / intervention** — issue actions, compare predicted futures, and use interventions as evidence.
3. **Learning / plasticity** — assign error and credit, revise representations and strategies, consolidate useful structure, and support metaplasticity.
4. **Valuation / motivation** — begin from primitive physical/cognitive viability and valence, then allow learned preferences, drives, and higher-order values to shape future choices.

Cross-cutting requirements already identified:

- persistence/memory across multiple timescales;
- uncertainty and provenance;
- egocentric sensory grounding;
- interoceptive/proprioceptive/metacognitive/introspective access;
- finite computational resources;
- internal communication/integration.

## Attack: is allocation a fifth fundamental function?

A finite learner cannot process every sensory feature, prediction, memory, hypothesis, counterfactual, and internal state at equal resolution.

If allocation is omitted, the design silently assumes one of two impossible or misleading conditions:

1. effectively unlimited compute; or
2. a hidden scheduler whose priorities are already hand-authored.

Therefore some process must determine **what receives scarce cognitive resources now**.

This is broader than human-language notions of attention. It includes:

- which sensory streams receive resolution;
- which hypotheses remain active;
- which memories are retrieved;
- which prediction errors receive diagnosis;
- which counterfactual futures are simulated;
- which internal conflicts receive metacognitive review;
- which experiences are candidates for consolidation;
- which action opportunities receive planning effort.

### Verdict

**Allocation is functionally fundamental.**

However, the content of salience should not be heavily innate. The architecture may need an innate capacity to allocate limited resources, but **what becomes salient should largely be learned** from experience.

Candidate inputs to learned allocation include:

- primitive valence / viability pressure;
- uncertainty;
- prediction error;
- novelty;
- expected consequence;
- learned relevance;
- recurrence;
- social significance;
- memory activation;
- expected information gain or learning progress.

The allocation mechanism should remain revisable through metaplasticity rather than becoming a fixed executive policy.

## Attack: can allocation be derived entirely from the other functions?

In principle, action selection and modeling could compete internally and appear to produce attention without an explicit allocation module.

That does not remove the functional requirement. Competition for finite representational and computational resources **is itself allocation**, whether implemented explicitly or emergently.

Therefore allocation should be present in the functional contract while remaining implementation-neutral.

## Attack: raw novelty as salience creates pathology

A system that allocates heavily toward raw surprise can become trapped by irreducible noise or stochastic stimuli (the classic "noisy TV" problem).

Therefore novelty/prediction error cannot alone determine salience.

A better eventual signal is likely **reducible uncertainty / learning progress / consequential uncertainty**, tempered by viability and learned relevance. This remains a hypothesis, not an innate reward specification.

## Attack: valuation is broader than homeostasis

Calling the fourth loop `homeostatic` becomes too narrow once Noema develops learned preferences and values that can compete with immediate viability.

### Revision

Use **valuation / motivation** as the functional category.

Innate homeostatic viability and primitive valence seed valuation, but higher-order preferences, commitments, drives, and value-like structures are learned and revisable.

This avoids silently treating every future choice as a survival optimization problem.

## Attack: is memory a sixth function rather than a cross-cutting property?

Learning without retention is not learning, and persistence is central to the project's purpose.

However, memory participates in every function:

- modeling needs working and episodic state;
- action needs prior outcomes and current plans;
- learning needs retained evidence and consolidation;
- valuation needs persistent preference history;
- allocation needs learned relevance and retrieval.

### Verdict

Treat **persistence/memory as a cross-cutting substrate requirement**, not a separate loop, unless later implementation evidence shows that an independent memory system is necessary.

## Attack: is coordination/integration a separate function?

Noema previously committed to first-class intracommunication, including direct subsystem exchange and a shared workspace. That decision presumes some coordination across processes.

At the functional level, however, coordination can be expressed as the requirement that information relevant to one function can causally affect others without collapsing all state into one opaque channel.

### Verdict

Treat **integration/routing as a cross-cutting requirement** for now, not a sixth cognitive function. If the implementation becomes modular, explicit routing/workspace machinery may be required.

## Attack: are we missing metacognition as its own loop?

Metacognition is central to error diagnosis and self-directed improvement, but it may not require a distinct mechanism if the modeling function can model internal as well as external state and the learner has introspective/metacognitive access from birth.

### Verdict

Do not create a separate metacognitive module yet. Require instead that internal cognitive states be modelable, uncertain, attributable, and available to learning/allocation/action.

## Provisional first-principles core

The cleanest surviving functional core is currently:

1. **Model / simulate** — form uncertain, multi-horizon, counterfactual beliefs about experience.
2. **Value / motivate** — make some possible states matter, beginning with viability/primitive valence and allowing learned drives/values.
3. **Allocate / attend** — direct scarce sensing, memory, modeling, learning, and planning resources.
4. **Act / intervene** — change the world/body and use consequences as evidence.
5. **Learn / adapt** — revise models, policies, allocation, valuation structure, and eventually learning strategy itself.

Cross-cutting properties:

- persistence/memory and selective forgetting;
- uncertainty/calibration/provenance;
- multi-timescale operation;
- internal communication/integration;
- developmental anti-cheating constraints.

This is a **functional contract**, not a software architecture. One mechanism may implement several functions; one function may require several mechanisms.

## Stress-test against target intelligence criteria

### Learning rather than parroting

Requires learning + persistence + transfer pressure. Covered in principle.

### Persistent attributable memory

Requires the cross-cutting persistence/provenance substrate. Covered in principle, mechanics unresolved.

### Causal understanding

Requires modeling + intervention + learning. Covered in principle.

### Prediction and surprise

Requires modeling + uncertainty + allocation. Covered in principle.

### Self-correction / learning from mistakes

Requires model provenance + learning + metacognitive access + allocation. Covered in principle.

### Other-agent modeling / empathy

Agent modeling can emerge inside the world model; empathic adaptation additionally requires valuation to become sensitive to inferred other-state. Covered in principle, emergence unproven.

### Wants / needs

Primitive needs arise from viability; learned preferences/drives require valuation + persistence + salience/allocation + learning. Covered in principle.

### Consistency without rigidity

Requires persistence plus controlled plasticity/metaplasticity. Covered in principle.

### Planning / counterfactual reasoning

Requires simulation + valuation + action selection + allocation. Covered in principle.

### Curiosity / initiative

Requires allocation and action to sometimes value informative futures, while avoiding raw-novelty traps. Mechanism remains unresolved.

### Transfer / abstraction / metaphor substrate

Requires reusable structural compression and transfer. Functional placement exists in model+learning, but this remains one of the strongest possible falsifiers.

### Self-development / self-actualization

Requires modeling internal state, learned valuation, metaplasticity, persistence, and action. Covered in principle, but safely changing one's own learning architecture is unresolved.

## Remaining red flags

The five-function core is not yet sufficient as a theory. Major unresolved risks include:

1. **Compositionality:** can learned representations be recombined productively, or does the system remain an entangled predictor?
2. **Open-ended concept formation:** can new latent structure be created without a fixed ontology?
3. **Epistemic action:** can information gathering arise without hand-authoring curiosity or information gain as a dominant drive?
4. **Stability/plasticity:** can the system learn continually without catastrophic drift?
5. **Goal/valuation integrity:** can learned drives evolve without wireheading or arbitrary self-modification?
6. **Scalability:** can uncertainty over many hypotheses remain computationally tractable?
7. **Internal coherence:** can independently learned subsystems/representations communicate without requiring a pre-authored symbolic language?
8. **Developmental bootstrapping:** can sufficiently rich structure emerge from minimal exploration before useful higher-order policies exist?

## Current frontier

The next useful step is to attack the **five-function core as a whole** with concrete adversarial developmental scenarios. The goal is to find a target capability that cannot plausibly emerge from these functions and cross-cutting requirements without adding a genuinely new primitive.

If no such missing primitive appears, the project can then compare implementation families against this functional contract instead of designing by analogy to existing AI systems.
