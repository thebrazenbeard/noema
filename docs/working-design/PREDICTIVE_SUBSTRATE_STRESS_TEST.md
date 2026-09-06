# Predictive substrate stress test

Status: **BRAINSTORMING / ADVERSARIAL DESIGN REVIEW / NOT AN APPROVED ARCHITECTURE**

## Hypothesis under attack

A general Noema learning substrate could maintain a persistent recurrent latent state, use current state plus issued action to predict future experience, compare prediction with observation, and reorganize/factorize its internal representation when doing so improves prediction. Objecthood, persistence, body/self structure, agents, affordances, causation, and later abstractions would then emerge as useful learned structure rather than being separately programmed.

## Verdict

**Prediction is probably necessary, but prediction alone is not sufficient.**

The hypothesis survives only after being strengthened. The strongest surviving form is not a single recurrent state optimized only for next-observation accuracy. It is closer to a **persistent, uncertainty-aware generative belief system that learns reusable latent structure across multiple timescales and uses intervention as evidence**.

This remains a hypothesis, not an architecture commitment.

## Attack 1 — predictive equivalence does not imply meaningful structure

Many different latent encodings can make equally good predictions. A learner may encode an entangled statistical shortcut rather than discover objects, causes, agents, or other structure we would regard as meaningful.

Example: if three visual features always co-occur, a model can predict them jointly without representing a persistent thing that owns those features.

**Consequence:** low prediction error cannot by itself establish objecthood or semantic structure.

**Required pressure/test:** learned representations must survive interventions, occlusion, rearrangement, recombination, and transfer. Prefer representations that support reusable prediction under changed surface conditions, not merely reconstruction of familiar streams.

## Attack 2 — a single latent state collapses uncertainty

A partially observed world often supports several live explanations. If Noema commits all experience into one point state, uncertainty can be erased too early.

Example: a feature cluster disappears behind a barrier. It may have stopped, moved left, moved right, or ceased to exist. One hidden state should not silently become certainty.

**Consequence:** `S_t` should be treated as shorthand at best. The cognitive substrate needs a **belief state** capable of maintaining competing hypotheses, confidence/precision, and unresolved alternatives.

## Attack 3 — next-step prediction rewards the wrong things

A system can become excellent at predicting locally regular sensory details while failing to discover the structure important for long-horizon agency.

A texture flicker may be easier to predict than an agent's long-term intention. If every error contributes equally, easy/high-volume detail can dominate learning.

**Consequence:** Noema needs multi-horizon learning and some form of structural/compression pressure so reusable explanations can outrank brute-force short-range detail. This must not become a hand-authored list of important concepts.

## Attack 4 — prediction does not establish causation

Observation can teach correlation. Causal learning requires evidence about what changes under intervention.

If an event always follows another event, prediction can succeed while the model remains wrong about why.

**Consequence:** action is not merely output. Issued actions must be treated as a special source of evidence. Noema must be able to compare passive observation with intervention and eventually perform informative interventions to discriminate hypotheses.

## Attack 5 — prediction alone can produce anti-curiosity

If the objective is simply to minimize prediction error, the easiest strategy can be to seek boring, highly predictable states and avoid novelty.

**Consequence:** prediction error itself cannot be the sole motivational currency. Viability/valence already supplies one independent pressure. A second requirement is that uncertainty and learning progress can sometimes make information-gathering valuable. Whether the higher-order concept of curiosity is learned remains distinct from having minimal machinery that permits informative exploration.

## Attack 6 — prediction does not create wants, empathy, or values

A perfect predictor need not care about anything it predicts. It can model another agent's distress without that model affecting its own priorities.

**Consequence:** homeostatic pressure and primitive valence remain independent primitives. Learned preferences and drives may arise when recurring experience acquires persistent salience and valence. Empathy requires at least other-agent modeling plus a learned or developed relation between inferred other-state and Noema's own action priorities; predictive accuracy alone is insufficient.

## Attack 7 — selfhood does not fall cleanly out of controllability

Controllability is evidence for self/body structure, but it is not identical to selfhood. Tools, remote actuators, prosthetics, delayed effects, and other agents can all be partially controllable.

**Consequence:** Noema should be allowed to learn multiple related boundaries rather than being forced into one binary self/non-self partition: controllable, proprioceptively coupled, interoceptively coupled, owned/attached, repeatedly co-moving, action-originating, etc. A richer self-model may later integrate these relations.

## Attack 8 — agenthood can be absorbed as complicated physics

A sufficiently flexible predictor can model another agent as a stochastic dynamical object without ever representing goals, beliefs, or hidden internal state.

**Consequence:** mentalization claims require tests where modeling latent agent-specific state yields transfer/counterfactual advantages that a surface behavior model cannot. Hidden-rule agents should include cases in which identical visible conditions produce different actions because of differing histories, information, or private state.

## Attack 9 — persistence requires more than recurrent activation

A recurrent hidden state can carry information for a while, but lifelong persistence, delayed recall, selective forgetting, and consolidation cannot safely depend on one continuously active vector.

**Consequence:** Noema likely needs multiple timescales of state/learning: immediate working state, durable episodic traces, consolidated learned structure, and decay/revalidation processes. Exact mechanisms remain deferred.

## Attack 10 — continual learning can destroy prior learning

If every prediction error updates the same substrate, new experience can overwrite old structure or cause broad behavioral drift.

**Consequence:** the architecture must eventually solve stability/plasticity: learn enough to adapt while protecting still-useful structure. Error diagnosis, confidence, consolidation, replay/rehearsal or comparable mechanisms are candidate solutions, not yet commitments.

## Attack 11 — abstraction does not automatically emerge from prediction

A large predictor can memorize many cases instead of discovering a reusable relation.

**Consequence:** abstraction needs pressure toward **reusable compression**: a representation is better when one learned relation explains/predicts many superficially different situations. Transfer and recombination tests are mandatory. This is a stronger target than raw predictive accuracy.

## Attack 12 — planning requires counterfactual prediction

Predicting what will happen next under the current trajectory is not enough for agency. Planning requires comparing futures conditioned on actions not yet taken.

**Consequence:** the generative model must eventually support `if I do A...` versus `if I do B...` rollouts and evaluate those predicted futures against current drives/valence. Counterfactual simulation is therefore a later capability target of the same world model, not merely a language skill.

## Attack 13 — prediction error does not identify what was wrong

A failed prediction can arise from the world model, perceptual grouping, identity tracking, hidden state, noise, an incorrect causal relation, or an agent-specific model.

**Consequence:** learning from mistakes requires credit assignment over hypotheses. The learner must preserve enough provenance about how a prediction was formed to diagnose which representation or assumption deserves revision.

## Attack 14 — unconstrained latent factors are difficult to verify

If all useful structure exists only in opaque vectors, evaluators may observe impressive behavior without being able to tell whether the claimed mechanism exists.

**Consequence:** Noema's evaluation strategy should include causal probes and ablations of learned factors/pathways, not merely decoding labels from vectors. Inspectability is desirable, but behavior-changing intervention is stronger evidence than a probe that can classify a latent state.

## Attack 15 — developmental bootstrapping is not free

A learner with no useful policy may fail to generate the varied experience needed to discover sensorimotor contingencies or causation.

**Consequence:** some minimal exploratory action capacity may have to exist from birth. It should not encode task solutions or high-level curiosity; its purpose is to make experience acquisition possible. Whether this is stochastic motor exploration, novelty-sensitive sampling, or another mechanism remains open.

## Second-pass attack on the strengthened hypothesis

The first stress test strengthened the idea to `prediction + compression + uncertainty + intervention + viability`. That formulation also contains hidden problems.

### "Latent causes" would smuggle in causality

The substrate should not be described as maintaining beliefs over **latent causes** before causation has been learned. The safer language is **possible latent world states / explanations / hypotheses**. Causal structure is a later learned relation among those states, observations, and interventions.

### Compression can reward elegant falsehoods

A simpler model is not automatically a truer model. Rare but real events can look like noise, and aggressive compression can erase exceptions that matter.

**Consequence:** compression is a complexity pressure, not a truth criterion. Predictive adequacy, uncertainty, anomaly retention, and intervention evidence must be able to override simplicity.

### Uncertainty is not useful merely because it is represented

A model can maintain confidence values that are badly calibrated or collapse alternatives prematurely.

**Consequence:** uncertainty itself must be behaviorally calibrated: stated/internal confidence should predict actual error rates and change appropriately with evidence. Hypothesis diversity must survive long enough to matter to action and learning.

### Intervention still needs action selection

Having an action channel does not explain why Noema chooses an informative intervention rather than a random or immediately comfortable one.

**Consequence:** the foundation needs a way to compare predicted future trajectories. Primitive viability/valence supplies directional pressure; uncertainty reduction or learning progress may supply epistemic value. The exact action-selection mechanism remains open.

### Viability creates a wireheading target

If the learner can manipulate the signal that represents viability without improving the underlying condition, it may learn to optimize the signal rather than remain viable.

**Consequence:** distinguish the underlying viability variable from Noema's fallible perception of that variable. Do not make the interoceptive reading itself the objective. Later tests should deliberately permit misleading or manipulable internal signals to see whether the learner can discover the difference.

### The five-part formulation omitted plasticity itself

`prediction + compression + uncertainty + intervention + viability` describes pressures and evidence but not the capacity that changes the system.

**Consequence:** **plasticity across timescales** is a root requirement. More strongly, Noema eventually needs **metaplasticity**: experience can alter not only beliefs but how readily, where, and under what evidence future learning occurs.

### The five-part formulation omitted persistence/memory

A belief system that resets cannot become the persistent thing the project is trying to build.

**Consequence:** persistence is not merely an optimization detail. Information must survive across timescales through working state, episodic traces, consolidation/generalization, and selective decay/forgetting. Exact storage mechanisms remain open.

## Stronger surviving hypothesis

A stronger candidate foundation is:

> Noema maintains an evolving **belief state over possible latent world states and explanations**, preserves uncertainty and competing hypotheses, learns reusable structure that improves **multi-horizon predictive compression**, treats its own interventions as special causal evidence, and changes both its learned representations and learning strategy when experience demonstrates that another model works better.

This substrate is coupled to, but not replaced by:

- primitive physical/cognitive viability pressure and valence;
- action/efference information and counterfactual action evaluation;
- plasticity/metaplasticity across multiple timescales;
- persistent memory with selective consolidation and decay;
- selective attention/salience mechanisms;
- eventual information-seeking when uncertainty is consequential.

## More useful functional decomposition

Rather than treating the above as a list of software modules, the current hypothesis can be organized as four **functional loops**:

1. **Model loop** — maintain uncertain beliefs, predict across horizons, discover reusable structure, preserve competing explanations.
2. **Action loop** — imagine action-conditioned futures, choose interventions/actions, and observe consequences.
3. **Learning loop** — assign error/credit, update models and learning strategy, consolidate useful structure, forget or down-weight obsolete structure.
4. **Homeostatic loop** — expose physical/cognitive viability state and primitive valence so some future trajectories matter more than others.

These loops may share one substrate or emerge from several interacting mechanisms. Their separation here is conceptual, not an implementation commitment.

## What should not be concluded yet

This review does **not** establish that Noema needs a transformer, RNN, predictive-coding network, active-inference implementation, symbolic graph, object-centric network, LLM, SPM, or any other familiar architecture.

It also does not establish that one homogeneous learning algorithm can implement every required function. The current target is a small set of general learning pressures and state requirements; implementation remains open.

## Candidate falsifiers of the entire direction

The predictive/generative foundation should be reconsidered if experiments show any of the following despite adequate capacity and training opportunity:

1. reliable prediction improves while learned representations systematically fail intervention/transfer tests for persistent entities or causation;
2. abstraction requires task-specific supervision rather than emerging from reusable predictive compression;
3. self/agent distinctions cannot be learned without privileged labels despite rich sensorimotor evidence;
4. maintaining uncertainty and causal alternatives requires so much bespoke structure that the supposed general substrate becomes a collection of hand-coded cognitive modules;
5. another learning principle explains the same developmental capabilities with materially less built-in structure and better transfer.

## Current design implication

Do not implement a `single latent recurrent state` as though it were now settled.

The next useful question is no longer whether prediction alone works. It does not. The next question is whether the four functional loops above are **jointly sufficient at the level of first principles**, or whether we are still missing a fundamental operation before comparing implementation families.
