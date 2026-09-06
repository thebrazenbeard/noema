# Noema actuation-boundary hostile attack

Status: **BRAINSTORMING / SUCCESSOR-CUT SELF-RED-TEAM / NOT IMPLEMENTED / NOT PART OF FROZEN BT2 R1**

Date: 2026-09-06

Target: `ACTUATION_AND_ACTION_SEMANTICS_CONTRACT.md`

## Verdict

The actuation contract closes the obvious semantic-action leaks, but a clean-looking `CognitiveAction { actuator_port_id, command_payload }` is still not sufficient.

The strongest attack is:

> **Action semantics can leak or be supplied downstream of the cognitive action object through synchronous call semantics, controller state, hidden targeting, command acknowledgments, safety substitution, scheduler behavior, or checkpoint mismatch.**

The outbound side therefore needs the same whole-path noninterference discipline as the inbound event path.

## H1 — synchronous API return can become a success/completion oracle

A cognitive action call can reveal semantic information even if its arguments are clean.

Examples:

```text
result = actuator.send(command)
```

where `result` exposes:

- accepted/rejected;
- completed;
- target reached;
- collision;
- infeasible;
- success/failure;
- exception type tied to hidden target state.

Even blocking until the command finishes supplies a temporal completion boundary.

Correction:

- the cognitive action interface should not synchronously return evaluator-level success or semantic completion;
- command admission should be mechanically bounded and predictable from the declared actuator contract where possible;
- direct operational feedback that a physical actuator would expose should return later through ordinary learner-visible sensory/proprioceptive evidence;
- semantic completion remains learned unless deliberately supplied and claim-limiting.

## H2 — hidden controller state is part of the experienced world dynamics

A PID integrator, trajectory generator, adaptive controller, low-pass command filter, motor mixer, or learned stabilizer may retain state across commands.

Then identical `CognitiveAction` sequences can produce different consequences depending on controller history.

That is not automatically a problem. But if controller state is omitted from checkpoint/replay lineage, the experiment is not reproducible and Noema may appear nonstationary for reasons the evaluator forgot to record.

Correction:

The actuator manifest must classify controller state as one of:

- stateless deterministic transformation;
- evaluator/world state that is checkpointed and replayed;
- deliberately stochastic state with isolated RNG and reproducible seed/state;
- external uncontrolled state whose uncertainty is explicitly part of the experiment.

Learner checkpoint/restore cannot claim faithful continuation if the actuator/controller state relevant to future consequences is silently reset or retained inconsistently.

## H3 — a low-level-looking command may hide semantic targeting downstream

A command payload can appear continuous while an upstream UI/controller has already selected the object or target.

Example:

```text
CognitiveAction { port=manipulator, payload=[0.2, -0.1] }
```

looks innocent if the actuator implementation has secretly bound that vector to `currently_selected_object_id` maintained in evaluator/UI state.

Correction:

F0 audits the **complete cognitive-action-to-world-effect dependency graph**, not only the serialized command.

No actuator/controller path may read evaluator object IDs, hidden target handles, semantic affordance tables, task labels, or answer-bearing state unless that capability is explicitly declared as supplied and claim-limiting.

## H4 — safety intervention can become an unmodeled hidden agent

Collision avoidance, workspace clamping, force limiting, emergency stops, automatic recovery, and constraint solvers may rewrite or veto learner commands.

If this happens silently, Noema experiences a hidden causal process. That may make some learning problems underdetermined or appear to be actuator unreliability.

Correction:

- record safety intervention exactly evaluator-side;
- preserve it in checkpoint/replay state;
- decide per experiment whether its physically available consequences become ordinary sensory evidence;
- do not expose semantic `safety_override=true` by default;
- do not claim Noema learned unconstrained motor competence if the safety layer solved avoidance/control.

## H5 — action-port topology is itself a morphology prior

Opaque port IDs are not semantics, but a port decomposition can reveal substantial body/action structure.

Examples:

- one port per joint;
- separate left/right limb ports;
- a dedicated gaze actuator;
- a dedicated communication actuator;
- a dedicated intervention actuator.

This can be legitimate innate topology. It still changes the developmental problem.

Correction:

- record the actuator-port decomposition as supplied morphology/topology;
- do not claim Noema discovered the existence or independence of actuator channels from scratch;
- where a later claim depends on cross-effector generalization, test port remapping or changed morphology rather than relying on permanent port identity.

## H6 — normalization and control coordinates can supply geometry

A command range such as `[-1,1]` may hide substantial engineering assumptions:

- exact joint limits;
- symmetric action scale;
- body axes;
- global/world axes;
- normalized reach distance;
- object-relative coordinates;
- inverse-dynamics compensation.

Correction:

Every command coordinate system belongs in the actuator manifest.

Body-relative coordinates may be a reasonable supplied interface. Global object/world-relative coordinates are a stronger spatial subsidy and must be treated consistently with the spatial-interface contract.

## H7 — action scheduling can leak hidden world phase

A runtime may only accept actions at particular simulator ticks, after particular observations, or at scenario-defined decision points.

If the learner can infer these admission windows from timing, blocking, errors, or queue behavior, the scheduler can reveal event boundaries, regime transitions, or task phase.

Correction:

- declare action scheduling policy;
- keep it independent of evaluator semantic phase unless phase is intentionally observable;
- avoid answer-bearing `your turn now` gates in formal tests;
- if decision opportunities are externally scheduled, count that structure as supplied and test whether the capability survives altered schedules where appropriate.

## H8 — queue and command-overwrite policy changes action meaning

Suppose a continuous actuator consumes the latest command, but the runtime instead queues every command to completion. These create different temporal control problems.

Potential hidden structure includes:

- FIFO execution;
- last-command-wins;
- hold-until-changed;
- zero-order hold;
- implicit stop on no command;
- automatic return-to-neutral;
- command coalescing.

Correction:

The actuator manifest must specify command buffering, hold, overwrite, and neutral/default behavior. These are supplied temporal-control semantics.

## H9 — action acknowledgment timing can leak feasibility

Even a nonsemantic acknowledgment such as `accepted` can leak hidden state if acceptance depends on reachability, collision, object compatibility, or scenario legality.

Correction:

Command acceptance should depend only on learner-visible/static machine-contract constraints whenever possible. Dynamic feasibility should generally be learned from later consequences rather than an evaluator-derived immediate reject signal.

If dynamic rejection is physically intrinsic to the actuator, it should be modeled as ordinary operational feedback and its supplied information explicitly credited.

## H10 — learner-visible efference can be too rich

An efference trace copied after actuator transformation rather than before it might reveal controller-internal inverse kinematics, target resolution, or safety rewriting.

Conversely, copying only the pre-transform cognitive command may be insufficient for some embodiment studies where the organism has access to lower motor-command signals.

Correction:

The actuator manifest must identify the efference tap point:

- pre-controller cognitive command;
- intermediate motor command;
- final actuator drive;
- more than one of these.

Each tap is supplied internal access and changes what self-causation/control can be learned from.

First-core default should expose only the issued cognitive command unless a stronger signal is explicitly required.

## H11 — actuator RNG must be isolated from evaluator metadata

Stochastic failure, motor noise, or perturbation must not share random-number streams with evaluator labels, scenario IDs, or hidden intervention bookkeeping.

Otherwise hidden metadata can change action outcomes and become a learnable proxy.

Correction:

Use isolated actuator-noise RNG/state and include it in the same noninterference discipline already required for world/transducer randomness.

## H12 — checkpoint fidelity is bidirectional

The persistence contracts mostly discuss learner state, memory, and environment lineage. But actuation is part of the causal loop.

A checkpoint that restores learner state while restoring the actuator controller to a different integrator position, command queue, held command, tool attachment, calibration, damage state, or safety state does not restore the same future interaction conditions.

Correction:

Experiment lineage must include all causally relevant actuator/controller state needed for faithful continuation, even though that state is evaluator/world-side rather than autobiographical learner memory.

This does **not** make the controller state learner-visible.

## H13 — action-space convenience can mask missing skill learning

A rich action API may make long-horizon performance look like learned temporal abstraction when the environment is executing the difficult sequence.

Examples:

- navigation-to-target;
- grasp-and-lift;
- ask-and-wait-for-answer;
- inspect-object;
- retry-until-success;
- follow-agent.

Correction:

Whenever a later claim concerns acquired skills or temporal abstraction, identify the lowest-level executable sequence implemented by the environment/controller and test whether the claimed skill remains meaningful after removing or varying evaluator-authored macro structure.

## Revised whole-path rule

The outbound noninterference surface should be treated as:

```text
CognitiveAction
    -> runtime parser/router
    -> actuator port/controller
    -> safety/constraint layer
    -> world/physics
    -> ordinary learner-visible consequences
```

For every arrow, F0 asks:

1. What hidden evaluator/world state can this component read?
2. What state does it retain?
3. What semantic/control problem does it solve?
4. What learner-visible signal can its behavior create?
5. Is that contribution declared in the supplied-capability ledger?
6. Is it checkpointed/replayable when causally relevant?

A clean cognitive command object is insufficient if any downstream component can smuggle target identity, success, phase, affordance, or task semantics into behavior or feedback.

## Additional falsifiers

### AAS-14 — synchronous-return audit

Verify the cognitive action call returns no semantic success/completion/feasibility information.

### AAS-15 — controller-state replay

Restore identical learner/world state with identical actuator/controller state and verify deterministic future action effects under fixed RNG. Then deliberately change controller state and confirm the evaluator can detect the causal difference.

### AAS-16 — hidden-target reachability test

Mutate evaluator target/object handles that should be cognitively irrelevant while holding cognitive action and legitimate physical evidence fixed.

Pass: downstream control behavior is unchanged unless the physical world state itself legitimately changes.

### AAS-17 — scheduler-phase test

Change evaluator task-phase labels while preserving learner-visible timing/opportunity structure.

Pass: action admission and feedback remain unchanged.

### AAS-18 — safety-layer ablation/accounting

Compare safety/controller assistance conditions. Any competence supplied by automatic avoidance, recovery, stabilization, or trajectory generation is attributed to that layer.

### AAS-19 — efference tap-point test

Verify the learner receives exactly the declared efference representation and no post-controller target-resolution/success information.

### AAS-20 — actuator-state lineage test

Checkpoint/restore must preserve or explicitly reset all causally relevant actuator state according to the experiment contract. Undeclared mixed retention is a lineage failure.

## Result

The parent actuation contract survives, but only with these implementation-facing corrections.

The deeper architectural conclusion remains unchanged:

> **Noema can be given an engineered motor interface without pretending the interface is cognitively neutral. The scientific requirement is to make the motor substrate explicit enough that action semantics, affordance, agency, and skill are credited only for structure that the learner actually acquires.**
