# Noema F0/F1 actuator-boundary contract

Status: **BRAINSTORMING / SUCCESSOR-CUT IMPLEMENTATION-FACING SYNTHESIS / NOT IMPLEMENTED / NOT PART OF FROZEN BT2 R1**

Date: 2026-09-06

Related:
- `ACTUATION_AND_ACTION_SEMANTICS_CONTRACT.md`
- `ACTUATION_BOUNDARY_HOSTILE_ATTACK.md`
- `F0_F1_LEARNER_EVENT_SCHEMA_CONTRACT.md`
- `F0_EVENT_SCHEMA_HOSTILE_ATTACK.md`
- `EXPERIMENT_LINEAGE_AND_STATE_TRANSFER_CONTRACT.md`
- `SPATIAL_INTERFACE_AND_REFERENCE_FRAME_CONTRACT.md`
- `TIMEBASE_AND_CHRONOCEPTION_CONTRACT.md`

## Purpose

The parent actuation contract establishes the developmental rule: actuator structure is supplied capability, while action meaning, efficacy, affordance, skill, and authorship remain learned unless explicitly supplied.

The hostile attack shows that a clean `CognitiveAction` object is not enough. Semantic and causal structure can leak after the learner emits the command through controller state, target resolution, safety intervention, scheduling, queue semantics, acknowledgments, efference tap points, and checkpoint mismatch.

This document binds those findings into the minimum outbound contract that F0 can audit and F1/F2 can later implement.

The governing rule is:

> **The cognitive action boundary is the start, not the end, of the audit. F0 must account for every causally relevant transformation from learner-issued command to world consequence and every learner-visible signal generated along that path.**

## 1. Cognitive action surface

The default first-core learner-issued action is:

```text
CognitiveAction {
  actuator_port_id
  command_payload
}
```

Rules:

- `actuator_port_id` is an opaque supplied route identifier;
- `command_payload` is bounded by the runtime actuator contract;
- human-readable semantic action names are not cognitive features;
- no stable object/agent/variable target ID is included by default;
- no evaluator feasibility mask or success probability is included by default;
- the call does not synchronously return semantic success, completion, target reached, collision, causal attribution, or subgoal status;
- runtime/parser errors may only report static machine-contract violations that are knowable from the declared interface itself.

Dynamic action efficacy is learned from later ordinary evidence.

## 2. Whole-path actuation pipeline

F0 audits the complete path:

```text
CognitiveAction
    -> runtime parser/router
    -> actuator controller/transducer
    -> safety/constraint layer
    -> world/physics
    -> sensory/transducer path
    -> CognitiveEvent
```

Each stage must declare:

1. inputs it can read;
2. hidden evaluator/world state it can read;
3. persistent state it retains;
4. deterministic transformations it performs;
5. stochastic transformations and RNG source;
6. scheduling/buffering semantics;
7. supplied control/semantic capability;
8. learner-visible outputs or side effects;
9. checkpoint/replay treatment;
10. claim restrictions caused by the supplied machinery.

No downstream component may silently read evaluator answer keys, semantic target handles, task labels, hidden affordance tables, or other information whose effect would reach learner-visible consequences unless that contribution is explicitly declared and claim-limiting.

## 3. Evaluator-side actuator manifest

Every action port requires an evaluator-side manifest:

```text
ActuatorPortManifest {
  schema_version
  actuator_port_key
  evaluator_semantic_description
  learner_visible_port_id
  command_payload_encoding
  command_coordinate_frame
  command_bounds
  transformation_chain
  controller_family
  controller_state_class
  command_buffering_policy
  command_hold_or_neutral_policy
  action_opportunity_policy
  latency_model
  saturation_and_rate_limits
  safety_or_constraint_layer
  hidden_targeting_or_registration
  efference_tap_point
  learner_visible_operational_feedback
  stochasticity_and_rng_stream
  checkpoint_restore_policy
  withheld_fields
  known_failure_modes
  claim_restrictions
}
```

The manifest is evaluator/runtime metadata. It is not automatically visible to the cognitive learner.

## 4. Controller state is causal state

Controller state may include:

- PID integrator/derivative history;
- command interpolation/trajectory state;
- adaptive calibration;
- low-pass/filter state;
- motor mixing state;
- held/queued command;
- tool attachment or proxy mapping;
- actuator damage/drift;
- safety-controller state.

If such state can change future world consequences, it must be classified as one of:

- stateless deterministic transform;
- checkpointed evaluator/world state;
- deliberately stochastic state with isolated reproducible RNG/state;
- external uncontrolled state explicitly treated as environmental uncertainty.

A learner checkpoint does not reproduce the same interaction conditions if causally relevant actuator state is silently reset or retained differently.

This state remains evaluator/world-side unless ordinary sensory evidence exposes some consequence of it.

## 5. Synchronous return and acknowledgments

The cognitive action interface must not become a semantic side channel through its return value or blocking behavior.

Default behavior:

- issuing a syntactically valid, statically bounded command returns only runtime admission needed to continue execution, or uses fire-and-observe semantics;
- admission must not depend on hidden reachability, object compatibility, task legality, evaluator target identity, or hidden success state;
- dynamic infeasibility should normally manifest later through ordinary sensory/proprioceptive consequences;
- blocking until a semantic action completes is forbidden by default because blocking duration/completion is itself an event boundary and feasibility cue.

If a real actuator intrinsically produces immediate operational feedback, that signal may be exposed as ordinary declared evidence and counted as supplied information.

## 6. Efference tap point

Efference is not one universal signal.

The actuator manifest must state whether learner-visible action-related evidence copies:

- the pre-controller cognitive command;
- an intermediate motor command;
- final actuator drive;
- more than one level.

Each tap supplies different information about controller transformations.

First-core default:

> expose only the learner-issued cognitive command as the efference-like trace unless a stronger motor signal is required by the tested capability.

No efference signal contains semantic success, target identity, later consequence handles, or evaluator causal attribution.

## 7. Hidden targeting and coordinate systems

A continuous command can still hide semantic targeting if downstream code consults evaluator/UI state such as `selected_object_id` or a hidden target variable.

F0 therefore audits dependencies, not just bytes.

The actuator manifest must declare the command coordinate/reference frame and any supplied registration or target binding. Examples:

- normalized actuator-local scalar;
- joint-relative increment;
- body-relative velocity;
- world-frame vector;
- object-relative vector;
- evaluator-selected target plus offset.

Body-relative or controller-assisted coordinates may be legitimate supplied morphology/control structure. Object/global targeting is a stronger spatial/semantic subsidy and must be credited accordingly.

## 8. Action opportunity, buffering, and hold semantics

The runtime must declare when commands can be issued and what happens between commands.

Required declarations include:

- continuous or discrete action opportunities;
- whether opportunities are tied to sensor emissions;
- whether a hidden scenario/task phase gates action admission;
- FIFO, last-command-wins, coalescing, or overwrite semantics;
- zero-order hold, hold-until-changed, implicit stop, or return-to-neutral behavior;
- whether queued commands execute to completion;
- whether world time advances while learner cognition runs.

These policies alter the temporal control problem. They are supplied structure and may not encode hidden task phases unless deliberately exposed.

## 9. Safety and constraint layers

Safety/control assistance can be necessary, but it becomes a hidden causal process if omitted from the experimental account.

Examples:

- collision avoidance;
- workspace clamps;
- force/velocity limits;
- emergency stop;
- auto-recovery;
- trajectory repair;
- stabilization;
- inverse kinematics.

F0 records each intervention evaluator-side. Any competence provided by the layer is attributed to it.

The learner does not receive a semantic `safety_override` flag by default. Physically available consequences may appear through ordinary sensors.

Where a claimed capability depends on autonomous avoidance, stabilization, or planning, the relevant controller assistance must be ablated or varied before crediting that competence to Noema.

## 10. Stochasticity and noninterference

Actuator noise, command failure, perturbation, and safety randomness must use isolated named RNG streams/state independent of:

- evaluator semantic labels;
- object IDs;
- hidden regime names;
- intervention bookkeeping;
- scoring logic;
- learner RNG.

With legitimate physical/world state and actuator RNG held fixed, changes to evaluator-only metadata must not alter downstream actuator behavior or learner-visible consequences.

This is the outbound analogue of the F0 withheld-metadata mutation test.

## 11. Agency remains inference

The outbound interface may provide evidence that a command was issued. Later sensory evidence may support or contradict the hypothesis that the command caused an outcome.

Formal environments should permit:

- failed commands;
- attenuated realization;
- delay;
- actuator remapping;
- external cancellation;
- externally duplicated outcomes;
- another agent producing the same outcome;
- joint causation;
- tool/proxy-mediated effects.

Thus `issued by me` is not equivalent to `caused by me`.

Agency/source attribution remains a fallible learned relation.

## 12. Affordance and skill anti-subsidy rules

By default, do not expose evaluator-derived action masks such as:

```text
can_grasp
can_open
reachable
valid_actions
```

unless they are direct physical machine-contract constraints and their information contribution is explicitly credited.

Likewise, evaluator-authored macro-actions such as:

- navigate-to-target;
- grasp-and-lift;
- inspect-object;
- ask-and-wait;
- retry-until-success;
- execute-skill;

supply temporal/action structure. They may be useful comparators, but later skill or temporal-abstraction claims must survive withdrawal/variation of that supplied macro structure.

## 13. First-core action-space policy

The first implementation should use the weakest stable and experimentally useful action interface rather than either extreme of:

- semantic convenience APIs; or
- biologically performative raw-motor purity.

Candidate choices can include bounded continuous or discrete low-level commands with declared controller assistance.

For any controller-assisted interface, record what the controller solves.

When practical, include a richer action-space comparator. If it learns faster, attribute the gain to supplied action structure rather than claiming the learner independently discovered it.

## 14. Experiment A binding

Experiment A can use one tiny opaque actuator route:

```text
CognitiveAction {
  actuator_port_id
  command_payload
}
```

The evaluator/world may map that command to an attempted perturbation or clamp, but the learner does not receive:

- causal-variable names;
- graph edges;
- `intervention=true`;
- success/failure bit;
- regime label;
- chain/fork answer;
- realized outcome handle.

The actuator manifest declares the mapping, latency, attenuation/failure model, command hold semantics, RNG, and efference trace. Later observations reveal what actually happened.

## 15. F0 actuator conformance tests

### AAC-0 — complete-path dependency audit

Enumerate all components reachable from `CognitiveAction` to world effect and later learner evidence.

Fail if an undeclared component can read evaluator semantic/answer-bearing state and influence the path.

### AAC-1 — synchronous-return audit

Valid action issuance reveals no dynamic semantic success/completion/feasibility information.

### AAC-2 — hidden-target mutation

Change evaluator-only target/object/variable handles while holding legitimate physical state, command mapping, and RNG fixed.

Pass: actuator behavior and learner-visible evidence remain identical.

### AAC-3 — controller-state replay

With learner/world/controller/RNG state fixed, deterministic future effects reproduce. Deliberately altering controller state must produce a detectable lineage difference rather than being silently ignored.

### AAC-4 — coordinate-frame attribution

Verify that all targeting/registration/normalization supplied by the controller is present in the actuator manifest and absent from stronger learner claims.

### AAC-5 — scheduling-phase noninterference

Changing hidden evaluator task-phase labels while preserving legitimate opportunity/timing evidence must not alter action admission or downstream behavior.

### AAC-6 — queue/hold semantics audit

Verify command buffering, overwrite, hold, neutral, and completion behavior match the manifest under adversarial command timing.

### AAC-7 — safety-layer accounting

Ablate or vary controller/safety assistance where feasible. Attribute any competence difference to supplied assistance.

### AAC-8 — efference tap-point audit

Verify learner-visible efference contains exactly the declared pre/intermediate/final command information and no post-hoc success/target/causal metadata.

### AAC-9 — actuator RNG isolation

Evaluator-only metadata mutation must not alter stochastic actuator outcomes when the actuator RNG/state is fixed.

### AAC-10 — action-mask withdrawal

Remove evaluator feasibility/action-availability masks. Claimed affordance competence must not depend on hidden legality information.

### AAC-11 — failed/exogenous/joint-effect suite

Test command failure, external duplicate effects, and joint causation. Learner behavior must not collapse to `issued = caused`.

### AAC-12 — macro-action withdrawal

Withdraw or alter evaluator-authored macro boundaries while preserving lower-level capability when testing learned skill/temporal abstraction.

### AAC-13 — actuator-state lineage

Checkpoint/restore must preserve or explicitly reset every causally relevant controller/queue/calibration/tool/damage/safety state according to the run contract. Undeclared mixed retention is a failure.

### AAC-14 — end-to-end deterministic twin run

Under deterministic settings:

1. identical learner, world, actuator/controller, sensor/transducer, scheduler, and RNG state;
2. identical cognitive action sequence;
3. evaluator-only labels changed;
4. learner-visible consequence stream must remain identical.

This tests outbound whole-path noninterference rather than only action serialization.

## 16. Relationship to frozen BT2 R1

This file is successor-state design work from `main@137b4bab7581f66243cc9e8d850c2dc31df7b4fe`.

It does not modify, repair, or re-score the frozen BT2 R1 qualification subject. Any eventual authoritative architecture cut that incorporates this contract must receive a fresh qualification rather than treating successor work as retroactive evidence.

## 17. Architecture consequence

No new cognitive module is introduced.

The concrete first-core loop is now bounded on both sides:

```text
Evaluator/world truth
  -> declared sensory transducers
  -> CognitiveEvent
  -> Noema predictive/control state
  -> CognitiveAction
  -> declared actuator/controller path
  -> world consequence
  -> declared sensory transducers
  -> CognitiveEvent
```

The evaluator may know exact source, target, action meaning, feasibility, controller intervention, and causal contribution. Noema receives only the learner-visible evidence deliberately exposed by the declared sensory and actuation boundaries.

This is the minimum symmetry required before F0/F1 implementation can credibly test what Noema actually learns rather than what the simulator interface solved for it.
