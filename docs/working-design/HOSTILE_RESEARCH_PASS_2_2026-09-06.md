# Noema hostile research pass 2 — 2026-09-06

Status: **EXTERNAL EVIDENCE REVIEW / DESIGN ATTACK / NOT AN IMPLEMENTATION APPROVAL**

## Purpose

This is an independent second hostile pass over Noema. The first research memo focused primarily on continual plasticity, consolidation, epistemic-vs-aleatoric uncertainty, intervention-based causal learning/model misspecification, and grounded communication.

This pass deliberately attacks different weak points:

- whether Noema's latent representations can ever be uniquely validated;
- whether temporal abstraction and skill structure can be learned rather than smuggled in;
- whether delayed credit can distinguish causal influence from mere temporal precedence;
- whether metacognitive confidence can itself be trusted;
- whether memory/replay can quietly distort later belief;
- whether developmental scaffolding can become a hidden answer key;
- whether homeostatic motivation is evidence for, or merely one candidate way of supplying, persistent concern.

The objective remains adversarial:

> What published results should make us narrow, alter, or add falsifiers to the current Noema concept before we commit to a concrete architecture?

## 1. Causal representation learning has an identifiability ceiling

A major risk in Noema's later embodied tests is requiring the learner to recover the evaluator's preferred latent variables as though there were always one uniquely correct decomposition of experience.

Recent causal-representation work gives a direct warning.

Jin & Syrgkanis, *Learning Causal Representations from General Environments: Identifiability and Intrinsic Ambiguity* (2023), prove that even with multiple environments, latent variables can remain identifiable only up to an intrinsic ambiguity class in their setting. Bing et al., *Invariance & Causal Representation Learning: Prospects and Limitations* (2023), provide impossibility results showing that invariance alone is insufficient to identify latent causal variables. von Kügelgen et al., *Nonparametric Identifiability of Causal Representations from Unknown Interventions* (2023), likewise characterize irreducible ambiguity even while giving stronger identifiability results under specific interventional assumptions.

Representative sources:

- https://doi.org/10.48550/arxiv.2311.12267
- https://doi.org/10.48550/arxiv.2312.03580
- https://doi.org/10.48550/arxiv.2306.00542

### Consequence for Noema

Noema should add an explicit **identifiability ceiling** to its evidence discipline:

> When multiple internal representations are observationally and interventionally equivalent under the available evidence, the evaluator must not require recovery of an arbitrary privileged latent coordinate system in order to call learning successful.

Later representation tests should therefore distinguish:

- recovery of task-relevant predictive/interventional structure;
- recovery up to an equivalence class;
- genuinely identifiable variables under declared assumptions;
- arbitrary agreement with evaluator naming/decomposition.

This strengthens the project's existing representation-neutral stance. It also means some future `ground-truth latent recovery` metrics would be scientifically invalid unless the benchmark first proves the target is identifiable.

## 2. Temporal abstraction is necessary, but predefining the abstraction can fake the capability

Hutsebaut-Buysse, Mets & Latré, *Hierarchical Reinforcement Learning: A Survey and Open Research Challenges* (2022), review how hierarchical RL can improve exploration, reuse, and interpretability through temporal/state abstraction, while emphasizing that many approaches begin with handcrafted abstractions or only semi-automatically discovered sub-behaviors.

Source:
https://consensus.app/papers/hierarchical-reinforcement-learning-a-survey-and-open-hutsebaut-buysse-mets/87b57dafa4075f7ab6093992c1b7d5fd/?utm_source=chatgpt

Machado, Barreto & Precup, *Temporal Abstraction in Reinforcement Learning with the Successor Representation* (2021), explicitly note that option-based approaches often assume a useful option set and that there is no definitive answer for which options should exist when they are not given.

A 2024 Scientific Reports study, *Exploring the limits of hierarchical world models in reinforcement learning*, further reports that a hierarchical model-based approach did not outperform traditional methods in final return and identified abstract-level model exploitation as a central failure mode.

Representative sources:

- https://consensus.app/papers/hierarchical-reinforcement-learning-a-survey-and-open-hutsebaut-buysse-mets/87b57dafa4075f7ab6093992c1b7d5fd/?utm_source=chatgpt
- https://consensus.app/papers/details/854ba5f0b07a55b19202720e9603180b/?utm_source=chatgpt
- https://consensus.app/papers/details/f06562618aac56468d24e526224dcdbc/?utm_source=chatgpt

### Consequence for Noema

The existing `temporal abstraction` and `reusable skill learning` capabilities survive, but their evidence standard needs to be harder.

Noema should not receive evaluator-defined episode, milestone, subgoal, or skill boundaries and then receive credit for discovering temporal structure.

A future temporal-abstraction falsifier should include:

- no privileged subgoal labels;
- boundary perturbation: shift where an evaluator would naturally segment the task and see whether the learned competence still works;
- decomposition: a learned skill must be revisable when only one subpart changes;
- composition: useful subskills should recombine in novel orders/context;
- anti-script transfer: the same action sequence should fail when context changes, forcing contextual skill invocation rather than cached trajectory replay;
- early-chunk poisoning: a once-useful routine later becomes wrong and must be reopened rather than protected merely because it is compressed/efficient.

This argues against making a fixed hierarchy part of Noema's mature anatomy before the learner has earned it.

## 3. Delayed credit is not solved by remembering what happened before the outcome

Pignatelli et al., *A Survey of Temporal Credit Assignment in Deep Reinforcement Learning* (2023), frame temporal credit assignment as learning the **influence** of an action over an outcome from finite experience. They emphasize difficulties from delayed effects, transpositions, and cases where actions have little or no actual influence.

Source:
https://consensus.app/papers/a-survey-of-temporal-credit-assignment-in-deep-pignatelli-ferret/adb24c887be955959b436003c24c194f/?utm_source=chatgpt

This directly attacks a possible weakness in Noema's current `provenance/influence trace` intuition. Provenance can preserve sequence and dependency candidates, but chronology alone does not establish credit.

### Consequence for Noema

A future delayed-credit test should force Noema to distinguish at least:

- an early action that actually changes a delayed outcome;
- an early action that merely precedes the same delayed outcome;
- two different early actions that jointly contribute;
- an apparent contributor whose effect is screened off by another variable;
- delayed negative consequences after many irrelevant intervening events;
- identical temporal statistics under different intervention/control conditions.

The evidence target should be **selective intervention-sensitive credit**, not merely an eligibility trace that reaches far enough backward.

This is important enough to remain its own capability/falsification track rather than being treated as automatically solved by memory, temporal abstraction, or causal discovery.

## 4. Metacognitive confidence is an inference, not privileged introspection

Fleming, *Metacognition and Confidence: A Review and Synthesis* (Annual Review of Psychology, 2023), emphasizes that confidence can be understood as an inference informed by an observer's models of the world and of its own cognitive system. Those self-models can be inaccurate, which explains why metacognitive judgments can diverge from actual performance.

Source:
https://consensus.app/papers/metacognition-and-confidence-a-review-and-synthesis-fleming/7b12a7740f4e510bbce666400fde1ac6/?utm_source=chatgpt

Bénon et al., *The online metacognitive control of decisions* (Communications Psychology, 2024), model mental effort allocation as a resource-control problem balancing expected cognitive benefit against cost, with confidence participating in that control rather than serving merely as a reportable number.

Source:
https://consensus.app/papers/the-online-metacognitive-control-of-decisions-bénon-lee/1a859a84e1cb5178bfce2ed6ba73caf9/?utm_source=chatgpt

### Consequence for Noema

This supports Noema's current move away from a universal certainty threshold, but it adds a stronger warning:

> **Noema's estimate of its own uncertainty/confidence must itself remain fallible and calibratable.**

The architecture should not contain a magical self-readout that is treated as ground truth merely because it is internal.

Future metacognitive tests should separate:

- task accuracy;
- uncertainty/calibration about the world;
- calibration about Noema's own likely performance;
- whether that self-estimate appropriately changes cognitive effort, asking, testing, acting, or deferring.

A useful adversarial case is a regime where Noema's old confidence policy becomes miscalibrated while first-order task competence remains partly intact. The system should be able to learn that **its confidence estimator/controller is wrong**.

This strengthens the current epistemic-control concept without requiring a dedicated `metacognition module`.

## 5. Memory is constructive and selective; replay can improve learning while also distorting it

Memory research attacks any assumption that replay or consolidation simply copies truth into a safer store.

Lu et al., *A neural network model of when to retrieve and encode episodic memories* (eLife, 2022), model selective episodic retrieval/encoding and find advantages from retrieving when useful rather than indiscriminately, in part because irrelevant memories can induce confidently wrong predictions.

Spens & Burgess, *A generative model of memory construction and consolidation* (Nature Human Behaviour, 2024), model hippocampal replay training generative cortical representations and explicitly reproduce schema-based distortions that increase with consolidation.

Chen & Wilson, *Now and Then: How Our Understanding of Memory Replay Evolves* (Journal of Neurophysiology, 2023), review replay as implicated in consolidation, planning, spatial learning, and skill learning while also emphasizing unresolved analytic and functional questions.

Representative sources:

- https://doi.org/10.7554/eLife.74445
- https://doi.org/10.1038/s41562-023-01799-z
- https://doi.org/10.1152/jn.00454.2022

### Consequence for Noema

Noema should not treat `memory retrieved` as equivalent to `past observation replayed exactly`.

Later memory architecture/evaluation should distinguish:

- original learner-visible event record where retained;
- episodic reconstruction;
- semantic/generalized reconstruction;
- current inference about the past;
- confidence/provenance attached to each.

Replay/consolidation candidates should be tested not only for retention benefit but for **belief contamination and schema distortion**.

A strong negative control would deliberately create a frequently recurring schema with rare but important exceptions. An over-consolidating system should begin to misremember/reconstruct the exceptions toward the schema; a better system should preserve enough provenance/exception structure to avoid false certainty.

This does not imply copying hippocampus/neocortex biology. It strengthens the functional requirement that memory remain attributable, selective, revisable, and capable of expressing uncertainty about reconstruction.

## 6. Developmental scaffolding can accelerate learning and still manufacture shortcuts

Developmental science and machine-learning robustness point in opposite but complementary directions.

Tamis-LeMonda & Masek, *Embodied and Embedded Learning: Child, Caregiver, and Context* (Current Directions in Psychological Science, 2023), describe infant learning as emerging from varied, time-distributed self-generated activity plus contingent caregiver/environment feedback.

Source:
https://doi.org/10.1177/09637214231178731

Milano & Nolfi, *Automated curriculum learning for embodied agents: a neuroevolutionary approach* (Scientific Reports, 2021), show that automatically selected environmental difficulty can improve robustness across varying conditions.

Source:
https://doi.org/10.1038/S41598-021-88464-5

But Geirhos et al., *Shortcut Learning in Deep Neural Networks* (Nature Machine Intelligence, 2020), show the complementary danger: a learner may exploit simple correlations that perform well inside the training distribution but fail under more challenging transfer conditions.

Source:
https://doi.org/10.1038/S42256-020-00257-Z

### Consequence for Noema

The existing developmental scaffolding contract is strongly supported, but the hostile refinement is:

> **A good developmental curriculum should not merely increase success rate; it should create competence that survives withdrawal and violation of the scaffold.**

Therefore every strong scaffold should eventually face:

- withdrawal;
- surface remapping;
- reversal of an early regularity;
- ambiguous caregiver/teacher behavior;
- conditions where self-generated exploration reveals something the teacher never demonstrated;
- tests outside the difficulty schedule used during development.

The learner should also increasingly generate parts of its own curriculum through action, curiosity, competence gaps, and consequence—not remain dependent on an omniscient scheduler forever.

This is a direct guard against hiding intelligence in Patrick, the evaluator, or a curriculum generator.

## 7. Homeostatic motivation is a serious candidate model of persistent concern, not proof that Noema needs self-preservation

Yoshida, Sprekeler & Gutkin, *Linking homeostasis to reinforcement learning: internal state control of motivated behavior* (Current Opinion in Behavioral Sciences, 2025), discuss homeostatically regulated reinforcement learning as a framework in which learned behavior regulates internal variables and can yield anticipatory regulation, risk sensitivity, and adaptive behavior.

Source:
https://consensus.app/papers/linking-homeostasis-to-reinforcement-learning-internal-yoshida-sprekeler/e05fbf5effda50a18b36b94dc33f7b5c/?utm_source=chatgpt

Dulberg et al., *Having multiple selves helps learning agents explore and adapt in complex changing worlds* (PNAS, 2023), report simulations in which multiple need-specific subagents outperform a monolithic aggregate objective on multiobjective homeostatic tasks, with increased robustness and emergent exploration.

Source:
https://consensus.app/papers/having-multiple-selves-helps-learning-agents-explore-and-dulberg-dubey/9ffdaa30191b5fc786963a6c172f85ad/?utm_source=chatgpt

### Consequence for Noema

This research makes **multi-dimensional internal concerns** a credible candidate mechanism worth eventually comparing against one scalar reward/drive.

It does *not* establish that Noema should be born wanting its runtime, weights, process, or identity to survive.

The objective-review distinction should therefore remain firm:

- `operational integrity`: conditions the runtime requires to function;
- `motivational concern`: internal variables/states the learner is designed or learns to regulate;
- `self-preservation`: a specific concern that must not be smuggled in by conflating the first two.

If homeostatic variables are supplied, they are explicit motivational priors. Later claims should test what higher preferences/commitments develop from them rather than calling the supplied needs learned.

A useful future comparison would include:

- one scalar aggregate drive;
- multiple partly independent need signals;
- operational-integrity signals that are *not* motivational;
- conditions where needs conflict and priorities must be learned/contextualized.

## Strongest net changes from this pass

This second pass does not overturn the current Noema direction. It finds several places where the validation contract needs to become more precise before architecture synthesis.

The strongest additions are:

1. Add an **identifiability ceiling** so later benchmarks do not demand arbitrary evaluator-preferred latent representations where the evidence cannot uniquely identify them.
2. Treat temporal abstraction/skill boundaries as learned claims; add boundary perturbation, decomposition, composition, anti-script transfer, and early-chunk-poisoning tests.
3. Keep delayed credit distinct from memory/provenance; test intervention-sensitive influence rather than chronology.
4. Treat metacognitive confidence as a fallible self-inference; require calibration of the confidence/controller itself.
5. Treat replayed/consolidated memory as potentially constructive/distorting; measure false reconstruction and schema contamination, not just retention.
6. Require scaffold withdrawal and regularity violation; successful curriculum learning must survive outside the curriculum that produced it.
7. Keep homeostatic/multi-need motivation as a candidate architecture family while preserving the boundary between operational integrity and motivational self-preservation.

## Architecture-level implication

The current L3 list remains plausible, but this pass suggests two additions/strengthenings before a full architecture candidate is frozen:

### Representation equivalence / identifiability discipline

Noema needs evaluation semantics that can recognize multiple internally different but behaviorally/causally equivalent representations. This is primarily an evidence/validation requirement, not necessarily a learner module.

### Fallible self-monitoring

If Noema regulates its own cognition based on confidence, competence estimates, or expected value of further thought, those meta-estimates must be treated as learned/inferred state that can itself be wrong and corrected.

This appears stronger than merely saying `contextual bounded cognition`; it requires the controller's own calibration to be falsifiable.

## What this pass still does not establish

It does not establish:

- a unique architecture for temporal abstraction;
- that hierarchical RL or successor representations should be copied;
- that explicit options/subgoals are required;
- that Bayesian confidence is the right uncertainty substrate;
- that episodic and semantic memory require separate physical modules;
- that replay is necessary;
- that a homeostatic reward system is required;
- that multiple motivational subagents are Noema's correct design;
- that evaluator ground-truth latent variables should be recovered exactly;
- that any of these research systems satisfy the full Noema developmental target.

## Current recommendation

Do **not** respond to this pass by adding seven new named cognitive modules.

Instead, carry the findings into the upcoming architecture synthesis and hostile paper validation:

- constrain what the candidate architecture must make possible;
- add the new falsifiers to the capability/evidence roadmap;
- let the simplest architecture that survives those falsifiers win.

That is a stronger use of the literature than copying the mechanisms the papers happened to implement.