# Noema implementation-family comparison

Status: **BRAINSTORMING / ARCHITECTURE COMPARISON / NOT AN APPROVED IMPLEMENTATION**

## Requirements being compared

Any candidate core must plausibly support:

- open-ended latent structure without privileged object/agent/self labels;
- dynamic relational binding and compositionality;
- persistent uncertain belief state and competing hypotheses;
- epistemic source/mode separation;
- multi-horizon and counterfactual simulation;
- intervention-sensitive causal learning;
- continual local learning and metaplasticity;
- multi-timescale memory, consolidation, decay, and forgetting;
- learned valuation and finite-resource allocation;
- contestable intracommunication/integration;
- developmental acquisition that survives ablation, intervention, and transfer tests.

No family gets credit merely because it can approximate a behavior with enough parameters.

## Family A — monolithic neural latent world model

Examples in spirit: recurrent neural world models, state-space models, transformer-like latent dynamics, large end-to-end predictive networks.

### Strengths

- scalable continuous representation;
- strong pattern learning;
- differentiable end-to-end training;
- can learn action-conditioned prediction and multi-horizon dynamics;
- can absorb high-dimensional sensory streams.

### Failures / risks

- latent state can become entangled and hard to factor;
- uncertainty is often approximate or collapsed;
- dynamic role binding and nested agent-specific state are weak unless specifically engineered;
- continual online learning risks catastrophic interference;
- causal locality/provenance of a prediction is hard to recover;
- internally simulated and observed states can share opaque representations without reliable epistemic separation;
- excellent prediction can coexist with poor transfer/compositionality.

### Verdict

**Useful substrate component, poor whole architecture by itself.**

A monolithic latent model is likely valuable for continuous perception/dynamics, but it fails too many of Noema's persistence, compositionality, uncertainty, provenance, and local-revision requirements if treated as the complete mind.

## Family B — explicit probabilistic graphical model / factor graph

Examples in spirit: dynamic Bayesian networks, factor graphs, structured probabilistic world models.

### Strengths

- explicit uncertainty and competing hypotheses;
- natural provenance and conditional dependence structure;
- intervention/counterfactual reasoning is conceptually clean;
- local belief updates and causal traceability are easier;
- persistent identity hypotheses can exist without certainty.

### Failures / risks

- graph variables and factor types are often hand-designed, which would smuggle ontology into Noema;
- structure discovery can be computationally expensive;
- continuous 3D perception and rich learned features are awkward without neural representation learning;
- fixed graphical structure does not provide open-ended concept formation;
- scaling exact inference is difficult.

### Verdict

**Excellent epistemic skeleton, too hand-authored if used conventionally.**

Noema should borrow the idea of explicit uncertain factors and local dependencies, but not a predefined ontology or fixed graph schema.

## Family C — probabilistic program induction / learned world programs

Examples in spirit: systems that infer compact generative programs or reusable procedures that explain observed data.

### Strengths

- very strong compositionality and abstraction potential;
- natural counterfactual simulation;
- reusable relations can generalize across different surface forms;
- program structure can support causal traceability and local revision;
- compression/reuse pressure is explicit.

### Failures / risks

- search over program space is difficult and often brittle;
- continuous noisy dynamics can be hard to represent efficiently;
- useful primitive operations are often supplied by the designer, which can quietly encode the ontology;
- online continual revision of large learned programs is difficult;
- bootstrapping from minimally interpreted sensorimotor streams is an unsolved challenge.

### Verdict

**Very attractive for higher-order abstraction, unlikely to be sufficient as the first developmental substrate.**

Program-like structure may be something Noema learns or consolidates into rather than the only representation available from birth.

## Family D — predictive coding / active-inference-like architecture

### Strengths

- prediction, uncertainty, action, and interoceptive/homeostatic signals naturally interact;
- hierarchical prediction errors can support allocation and learning;
- embodied sensorimotor development fits the framing well;
- actions can function as experiments as well as control.

### Failures / risks

- active-inference formulations can presuppose too much generative structure;
- minimizing prediction/free-energy-like objectives can reward predictable or self-confirming states;
- compositional binding and open-ended concept formation are not automatically solved;
- learned values/commitments can collapse back into prior/preferences chosen by the designer;
- a theoretical description does not itself provide scalable memory, continual learning, or provenance.

### Verdict

**Useful principles, not enough architecture.**

Noema may use predictive-coding-like local learning dynamics, but adopting active inference wholesale would prematurely commit to assumptions the developmental contract is explicitly trying to test.

## Family E — LLM/agent stack as cognitive core

### Strengths

- excellent language, abstraction, planning-like behavior, and broad prior knowledge;
- mature tooling and fast prototyping.

### Failures / risks

- language becomes the substrate before Noema has learned a world;
- persistent belief, selfhood, memory, source separation, and causal structure are usually reconstructed from context rather than developmental achievements;
- much apparent intelligence is inherited from training rather than acquired in the experimental world;
- impossible to tell whether target concepts emerged or were imported from pretraining.

### Verdict

**Reject as the developmental core.**

An LLM may later become a language interface or teacher, but using one as the original cognitive substrate would invalidate much of the experiment.

## Strongest current synthesis — dynamic generative factor workspace

No existing family cleanly satisfies the contract. The strongest current direction is a hybrid working hypothesis provisionally called a **Dynamic Generative Factor Workspace (DGFW)**.

This is not a fixed object graph and not a single opaque latent vector.

### Layer 1 — continuous sensorimotor field

Momentary egocentric external features plus proprioceptive/interoceptive/introspective/efference streams remain available in continuous or distributed form.

No stable object IDs, agent labels, world coordinates, or object segmentation are supplied.

### Layer 2 — dynamic latent hypotheses

The learner can create, split, merge, weaken, strengthen, and retire **latent factors** when doing so improves predictive reuse and intervention/transfer performance.

A factor is deliberately not defined as an object. It might eventually represent:

- a candidate whole;
- a recurring motion relation;
- a location-like structure;
- a body-related contingency;
- another agent's hidden state;
- an abstract relation;
- a learned value or strategy.

The substrate supplies the capacity to form factors, not their semantics.

### Layer 3 — learned relations / bindings

Factors can participate in learned, dynamically instantiated relations. Relations may themselves be learned latent structures rather than a fixed human-authored vocabulary.

This supplies a route toward compositionality without giving Noema concepts such as `OBJECT`, `AGENT`, `CAUSE`, `BELIEF`, or `SELF`.

### Layer 4 — belief workspace

Active factors/relations can maintain competing hypotheses, uncertainty, temporal span, source/provenance, and epistemic mode.

Internally simulated possibilities remain distinguishable from observation, memory, inference, intention, and desire by raw origin/provenance even before Noema learns human concepts for those distinctions.

### Layer 5 — action-conditioned generative simulation

The active belief structure can be projected forward under candidate actions.

Prediction occurs across multiple horizons. Interventions provide evidence that can change factor structure and relations.

### Layer 6 — allocation and contestable integration

Finite cognitive resources are assigned among sensory streams, hypotheses, memories, simulations, and error investigations.

Internal proposals need not collapse immediately into consensus. Competing hypotheses can retain confidence/provenance and later be credited or blamed based on outcome.

### Layer 7 — multi-timescale persistence

- active/working belief state;
- episodic traces;
- consolidated reusable factors/relations/policies;
- selective decay, forgetting, and revalidation.

The exact storage mechanisms remain open.

### Layer 8 — valuation and learned drives

Primitive physical/cognitive viability and valence are available from birth. Higher-order valuation is learned from experience and can bind to modeled future states, permitting derived goals rather than only cached rewards.

### Layer 9 — local plasticity and metaplasticity

Learning updates the implicated factor, relation, policy, valuation, or allocation rule when evidence supports revision. Later, Noema can learn context-sensitive changes to how it learns.

## Why this synthesis is attractive

It combines:

- neural-style continuous representation where continuous representation is useful;
- probabilistic/factor-graph-like uncertainty and local dependence without a fixed ontology;
- program-like compositional reuse without requiring explicit programs from birth;
- predictive/action-conditioned learning without treating prediction as the sole objective;
- workspace-like intracommunication without assuming language is internal thought.

## Why this synthesis may still be wrong

1. Dynamic factor formation may itself smuggle in an assumption that the world is cleanly factorizable.
2. Learned relation formation may be as hard as the original intelligence problem.
3. Maintaining distributions over dynamic structures may be computationally intractable.
4. A hybrid system can become a pile of bespoke mechanisms disguised by one name.
5. The continuous layer and factor layer may learn incompatible representations and require a hand-authored translation layer.
6. Local plasticity may fail to coordinate globally when representations are deeply shared.
7. The design may overvalue inspectability at the expense of learning efficiency.

## Current recommendation

Do **not** choose a conventional architecture family wholesale.

Use the DGFW only as the current architecture hypothesis to attack next. Its decisive question is:

> Can a system discover and maintain useful latent factors and relations from minimally interpreted sensorimotor experience, while preserving uncertainty and compositional reuse, without the factor machinery silently handing it the ontology we claim it learned?

If the answer is no, the project should retreat rather than paper over the failure with object slots, agent labels, symbolic predicates, or an LLM.
