# Noema Architecture Candidate A — Persistent Predictive Control Organism

Status: **BRAINSTORMING / SYNTHESIS CANDIDATE / NOT AN APPROVED IMPLEMENTATION**

Date: 2026-09-06

## Purpose

This document is the first attempt to bind the current Noema capability contract, developmental/evidential constraints, hostile research findings, interface boundaries, and first-falsification program into one coherent architecture candidate.

It is intentionally stronger than a list of requirements and weaker than an implementation specification.

The candidate must be replaceable. Passing this paper design does not validate Noema empirically. Failing a requirement or falsifier should cause revision or rejection rather than retroactive reinterpretation of the requirement.

## Architecture thesis

Noema Candidate A is a **persistent predictive control organism** built around a small set of interacting processes rather than a catalog of human cognitive nouns.

Its central loop is:

`experience -> belief-state update -> prediction -> valuation -> resource allocation -> action / inquiry -> consequence -> learning -> persistence`

Language is an ordinary learned signal stream entering and leaving this loop. It is not the substrate of cognition.

The candidate separates:

- what happened from what Noema infers;
- what Noema predicts from what it wants;
- persistent learned state from temporary task configuration;
- raw/episodic history from consolidated generalization;
- Noema-visible signals from operator-only diagnostics and controls;
- evaluator equivalence classes from any one preferred internal representation.

## Candidate anatomy

### 1. Provenanced event boundary

Every learner-visible event enters through a minimal provenance-bearing envelope.

The envelope may identify computational source classes such as:

- external observation;
- internally issued action/efference;
- later sensed action consequence;
- communication signal;
- retrieved memory;
- internal simulation.

The source class is not a semantic interpretation of the event. The architecture does not receive privileged object IDs, agent IDs, causal labels, truth labels, stable world coordinates, hidden simulator handles, or evaluator semantic answers.

Transducers are allowed to solve lower-level transformation problems, but their contribution must be declared in the supplied-capability ledger.

This boundary is Candidate A's F0 leakage-control surface.

### 2. Fast predictive belief substrate

The immediate cognitive substrate is a **continuous recurrent probabilistic state model**.

At time `t`, it maintains an internal belief state over current latent conditions rather than a single asserted world description.

Conceptually:

`B_t = Update(B_{t-1}, E_t, R_t)`

where:

- `E_t` is the current provenanced event;
- `R_t` is any retrieved memory context admitted by the memory controller;
- `B_t` is a predictive belief state sufficient to generate distributions over expected future learner-visible experience.

The model must support both passive predictions and action-conditioned predictions.

The first candidate should not hard-code human concepts such as object, cause, self, agent, goal, sentence, or skill into this state.

#### Uncertainty realization

Candidate A uses a **bounded population of continuous model states** rather than one point model or exhaustive discrete structure enumeration.

Each live model state contains:

- continuous latent state;
- learned predictive parameters;
- uncertainty over its own predictions/parameters where the chosen implementation supports it;
- evidence weight / credibility;
- resource cost;
- provenance sufficient to understand what evidence materially changed its standing.

The population is not required to correspond to human-readable hypotheses and is not required to enumerate graph structures.

Multiple members may be behaviorally equivalent. They should not be forced apart merely to make the internals interpretable.

Population size, proposal budget, and retention limits are bounded implementation parameters to be preregistered later.

#### Representation-equivalence rule

No evaluator may demand recovery of one arbitrary latent representation when multiple internal representations are observationally/interventionally equivalent for the task.

Validation therefore operates on prediction, intervention response, transfer, calibration, and downstream control behavior, plus any stronger identifiability guarantee actually justified by the environment.

### 3. Model inadequacy and structural expansion

Candidate A never assumes that the least-bad current model is adequate.

The predictive substrate tracks absolute predictive adequacy in addition to relative competition among live model states.

Persistent unexplained structure, failed intervention prediction, transfer failure, calibration failure, or systematic residual dependence may trigger **evidence-guided structural expansion**.

Structural expansion is generic. Candidate operations may include adding/removing/reorienting dependencies, introducing latent mediators, changing temporal scope, splitting or merging learned processes, or falling back to a more distributed representation.

No specific operation earns architectural necessity until ablation shows it matters.

A structural proposal is only a candidate explanation. Evidence controls retention.

### 4. Episodic experience store

Candidate A retains a bounded episodic store of selected experience with provenance and temporal context.

Its purpose is not perfect archival recall. It supplies detailed experience that the current predictive model may need when compressed/generalized state is insufficient.

Encoding and retrieval are selective and resource-bounded.

Selection pressure may include novelty, prediction error, uncertainty, rare consequential events, unresolved contradiction, event/episode boundaries, and expected future retrieval value.

Raw historical evidence and present interpretation remain distinguishable.

Retrieval is contestable: a retrieved episode can help prediction, but irrelevant retrieval can also cause confident error.

### 5. Slow consolidation / reusable knowledge store

Durable learning is not identical to the fast belief state.

Candidate A therefore has a slower learning path that extracts reusable predictive/control structure from accumulated experience while remaining reopenable.

Slow learning may alter:

- predictive parameters;
- reusable latent operators/bindings;
- retrieval/index structure;
- learned temporal abstractions;
- reusable policies/skills;
- meta-learning policy.

Consolidation is selective and must earn itself through improved future competence, transfer, efficiency, or calibration rather than durability alone.

The evaluator must test for schema distortion, false generalization, rigidity, and late-life plasticity.

Replay is a candidate mechanism, not an architectural requirement.

### 6. Temporal abstraction and skill formation

Candidate A must be able to stop treating all cognition/action as one-step transitions.

Temporal abstractions are **learned**, not handed over as evaluator-defined milestones.

A candidate chunk/skill becomes useful when a recurring sequence or policy:

- compresses repeated predictive/control structure;
- improves planning or execution efficiency;
- transfers across contexts where its preconditions still hold;
- remains interruptible/revisable when context changes;
- does not merely memorize a benchmark trajectory.

The architecture may retain learned temporally extended policies in the slow store, with activation controlled by current belief state and valuation.

No evaluator-provided subgoal boundary may later be claimed as discovered temporal abstraction.

### 7. Credit / influence learning

Delayed credit is treated as learning **influence**, not temporal proximity.

Candidate A retains enough event/action traces to test whether earlier state, action, skill invocation, prediction, or information-gathering choice materially changed later outcomes.

The candidate should prefer intervention-sensitive or counterfactual evidence where obtainable and avoid assigning causal credit solely because an event came first.

Credit must be local enough to prevent one delayed failure from indiscriminately rewriting unrelated competence.

### 8. Valuation / concern process

Noema requires action-relevant valuation, but valuation is not evidence.

Candidate A maintains a learned/partly primitive **concern state** separate from predictive confidence.

Initial experiments may use minimal viability variables to create consequences that matter. However, operational conditions required for the software to keep functioning are not automatically motivational self-preservation drives.

The architecture must eventually permit multiple simultaneous, potentially conflicting concerns without collapsing them into one permanently fixed scalar designer reward if a richer representation proves necessary.

Homeostatic or modular multi-need mechanisms remain candidate realizations, not settled anatomy.

### 9. Epistemic/conative firewall

Belief update and action preference interact but are not interchangeable.

Valuation may influence:

- what receives attention;
- what uncertainty is investigated;
- what action is chosen;
- which memory is worth retrieving;
- how much cognition is worth spending.

Valuation may not directly write predictive confidence.

Conversely, high predictive confidence does not itself imply strong action commitment.

### 10. Meta-control / finite-resource allocator

Candidate A has a contestable resource-allocation process that chooses among available cognitive operations under finite budgets.

Possible operations include:

- continue inference;
- observe/wait;
- retrieve memory;
- simulate;
- test/intervene;
- ask another agent;
- clarify a signal;
- invoke a learned skill;
- act robustly under unresolved uncertainty;
- defer.

The stopping principle is not a universal certainty threshold or bare loop counter.

Further cognition should continue only while its expected value exceeds its expected cost within current risk/resource constraints.

Engineering safeguards may still impose hard per-episode compute and step budgets.

#### Evidence maturity

Repeated processing of unchanged evidence does not manufacture certainty.

Maturation/consolidation should depend on meaningful evidence opportunity, diversity, calibration, contradiction exposure, scope, and consequence—not simply a raw number of hypothesis cycles.

A minimum-cycle guard may be used experimentally, but it is not the epistemic principle.

### 11. Fallible self-monitoring

Meta-control cannot assume privileged access to its own correctness.

Noema's estimates of:

- confidence;
- competence;
- likely value of more cognition;
- expected reliability of a skill;
- expected usefulness of a source;

are themselves learned predictions that can be wrong.

They must therefore be calibrated against later outcomes and able to update when self-assessment proves unreliable.

The evaluator should distinguish task performance from metacognitive calibration.

### 12. Temporary cognitive mode versus persistent learned self

Candidate A separates task-local working configuration from durable learned state.

Temporary mode state may include:

- currently active task/goal context;
- temporary retrieval set;
- current cognitive strategy;
- short-term allocation bias;
- local conversational/pragmatic context.

It should decay, terminate, or be superseded when evidence/task context changes unless explicitly learned as a durable reusable competence.

Persistent memory, learned dispositions, skill, source models, and eventually self-model structure are not erased merely because the temporary mode ends.

This prevents specialized research/task configuration from silently hardening into personality or standing control state.

### 13. Communication as grounded sensor/actuator

Communication enters through the same architecture as other learned signals.

Typed symbols, speech-derived signals, gesture, pointing, correction, and demonstration may all be learner-visible events depending on the declared transducer contract.

No semantic embedding or teacher statement becomes truth merely by entering through the communication channel.

The learner develops situated signal use through prediction, shared context, correction, source reliability, pragmatic inference, and long-term interaction history.

Illocutionary/action force and uncertainty scope are separate learnable dimensions: a local hedge should not automatically turn a clear directive into non-action.

The diagnostic interpreter remains read-only and operator-facing.

## Information-flow sketch

The candidate's live cycle is:

1. A provenanced learner-visible event arrives.
2. The fast predictive population updates its continuous belief state.
3. Episodic retrieval may supply bounded historical context.
4. The predictive substrate emits passive and/or action-conditioned forecasts with uncertainty.
5. Absolute adequacy and disagreement are evaluated.
6. The concern/valuation process scores possible consequences without changing evidential confidence.
7. Meta-control allocates bounded compute among inference, memory, simulation, intervention, communication, skill invocation, robust action, or deferral.
8. An issued action is logged as efference but not assumed to have succeeded.
9. Later sensed consequence updates predictive state and influence/credit traces.
10. Fast learning changes immediate state/parameters.
11. Selective slow consolidation may update reusable knowledge, temporal abstraction, skills, retrieval policy, or meta-learning.
12. New evidence may reopen prior consolidation or expose whole-model inadequacy.

No single stage is allowed to turn operator diagnostics, desired outcomes, or evaluator labels into belief evidence.

## First implementation slice

Candidate A is broader than the first build.

The first implementation slice remains deliberately small:

### F0 — information-boundary audit

Instantiate only enough event plumbing to prove that source/provenance, transducer attribution, learner-visible inputs, operator controls, and diagnostics do not leak target answers.

### F1 — persistent streaming learner

Instantiate:

- the provenanced event boundary;
- fast predictive recurrent substrate;
- bounded uncertainty realization;
- persistent state across streaming observations;
- minimal episodic/trace retention as required by the test;
- online learning;
- late-within-run novelty/plasticity probe;
- regime-change correction;
- resource accounting.

No grounded language, social cognition, full motivation, 3D embodiment, or mature skill system is required for F1.

### F2 — Experiment A

Add externally scheduled intervention evidence and test:

- calibrated non-commitment under passive ambiguity;
- update from decisive intervention evidence;
- command-versus-realized-outcome separation;
- held-out intervention prediction;
- remapped transfer;
- model-family inadequacy;
- representation-mismatch controls;
- no destructive global reset;
- bounded compute/memory.

The structural-expansion machinery is an ablated candidate here, not an assumed winner.

## What Candidate A deliberately does not settle

This document does not yet choose:

- recurrent network family;
- latent dimensionality;
- optimizer / update rule;
- ensemble/population size;
- exact uncertainty parameterization;
- replay algorithm;
- memory indexing implementation;
- structural proposal language;
- planning algorithm;
- skill-learning algorithm;
- motivation representation;
- homeostatic versus alternative concern architecture;
- long-horizon self-model realization;
- full embodiment simulator;
- speech front-end;
- any LLM component.

Those are implementation or later-architecture forks that should be chosen only when a target capability/test requires them.

## Candidate kill conditions

Candidate A should be rejected or materially revised if hostile validation shows that it:

- requires hidden semantic labels to function;
- cannot represent meaningful uncertainty without exhaustive model enumeration;
- treats its current model family as necessarily adequate;
- cannot learn late without catastrophic overwrite or freezing;
- makes confidence a privileged self-truth channel;
- turns valuation into evidence;
- needs evaluator-provided temporal/subgoal boundaries for skills;
- assigns delayed credit mainly by chronology;
- cannot separate temporary mode from persistent learned state;
- depends on diagnostic interpreter output for cognition;
- requires one evaluator-preferred latent representation despite representational equivalence;
- cannot operate under bounded compute/memory;
- cannot survive F0/F1/F2 with simpler baselines treated fairly.

## Current assessment

Candidate A is now coherent enough to receive a hostile requirement-by-requirement design validation.

It is not yet an approved Noema architecture and it is not an implementation specification.
