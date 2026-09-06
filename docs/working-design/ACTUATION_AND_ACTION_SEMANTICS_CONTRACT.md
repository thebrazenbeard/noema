# Noema actuation and action-semantics contract

Status: **BRAINSTORMING / SUCCESSOR-CUT INTERFACE CONTRACT / NOT IMPLEMENTED / NOT PART OF FROZEN BT2 R1**

Date: 2026-09-06

Related:
- `NOEMA_ARCHITECTURE_CANDIDATE_A.md`
- `F0_F1_LEARNER_EVENT_SCHEMA_CONTRACT.md`
- `F0_EVENT_SCHEMA_HOSTILE_ATTACK.md`
- `ORIGIN_EVIDENCE_AND_PROVENANCE_CONTRACT.md`
- `SPATIAL_INTERFACE_AND_REFERENCE_FRAME_CONTRACT.md`
- `SENSORY_PACKETIZATION_AND_CHANNEL_IDENTITY_CONTRACT.md`
- `TIMEBASE_AND_CHRONOCEPTION_CONTRACT.md`
- `SKILL_TEMPORAL_CREDIT_FRONTIER.md`

## Purpose

The inbound information boundary is now explicit enough to audit what Noema is allowed to perceive. The outbound boundary needs the same treatment.

An action API is not neutral plumbing. The chosen action space can silently provide:

- object identity;
- target selection;
- affordance knowledge;
- inverse kinematics;
- collision avoidance;
- grasp/contact semantics;
- temporal chunking;
- subgoals;
- success conditions;
- causal attribution;
- skill libraries;
- task decomposition.

A command such as `pick_up(object_17)` gives a learner radically more developmental structure than a bounded continuous actuator command, even if both eventually move the same object.

The central rule is:

> **Actuator topology, control laws, action primitives, target-addressing conventions, safety controllers, and macro-action boundaries are supplied capability. Whatever they solve must be declared and must not be credited as learned action semantics, affordance, skill, agency, or causal understanding.**

This is not a demand for motor-control purity. A simulator or physical system may require low-level controllers. The requirement is attribution, boundedness, and falsification of any stronger capability claim.

## 1. Research pressure

The external literature does not dictate one Noema action space. It does show that the action interface materially changes what must be learned.

Relevant pressure includes:

- developmental and neurorobotics work treating sensitivity to **sensorimotor contingencies**—relations between action and sensory consequence—as a major substrate for body knowledge, generalization, goal-directedness, and later skill acquisition;
- developmental robotics work in which perceptual structure and object-relevant regularities can be acquired from predictive action-effect relations rather than supplied semantic object/action labels;
- affordance-learning work in which functional categories and action possibilities are learned from action-effect relations;
- continuous-action affordance learning showing that useful manipulation structure can be acquired without a manually supplied library of exploratory motor primitives;
- robotics evidence that action-space choice substantially changes sample complexity, emerging behavior, and transfer;
- hierarchical-RL work showing that predefined options, macro-actions, task decomposition, and action primitives can speed learning precisely because they inject useful temporal/action structure;
- agency research showing that efference/action-related signals contribute evidence for self-causation, but agency remains an inference integrating predicted and actual effects rather than an infallible semantic flag.

Representative sources used as design pressure:

- Jacquey et al., *Sensorimotor Contingencies as a Key Drive of Development: From Babies to Robots* (Frontiers in Neurorobotics, 2019), DOI `10.3389/fnbot.2019.00098`.
- Laflaquière et al., *Grounding Perception: A Developmental Approach to Sensorimotor Contingencies* (IROS / arXiv), arXiv `1810.01870`.
- Högman, Björkman & Kragic, *Interactive object classification using sensorimotor contingencies* (IROS, 2013), DOI `10.1109/IROS.2013.6696752`.
- Wang, Hindriks & Babuška, *Active Affordance Learning in Continuous State and Action Spaces* (Humanoids, 2014).
- Aljalbout et al., *On the Role of the Action Space in Robot Manipulation Learning and Sim-to-Real Transfer* (IEEE RA-L, 2024), DOI `10.1109/LRA.2024.3398428`.
- Synofzik et al., *Misattributions of agency in schizophrenia are based on imprecise predictions about the sensory consequences of one's actions* (Brain, 2010), DOI `10.1093/BRAIN/AWP291`.
- Synofzik, Vosgerau & Voss, *The experience of agency: an interplay between prediction and postdiction* (Frontiers in Psychology, 2013), DOI `10.3389/FPSYG.2013.00127`.

These findings constrain information attribution. They do not require Noema to copy human motor anatomy, a Bayesian comparator, or any particular affordance representation.

## 2. Five actuation planes

Formal experiments and F0 should distinguish five planes.

### A0 — evaluator action/effect truth

Evaluator-side facts may include:

- requested learner command;
- exact simulator/physics control applied;
- target object/entity if the evaluator uses one internally;
- true actuator transform;
- true causal contribution to later effects;
- collision/contact truth;
- hidden action feasibility;
- hidden safety intervention;
- exact success/failure state;
- true tool/object identity;
- world-state transition caused jointly by multiple actors.

A0 is for world execution, scoring, and audit. It is not automatically learner-visible evidence.

### A1 — actuator/transducer implementation

The actuator layer may perform engineering transformations such as:

- scaling and clipping;
- force/velocity/position control;
- inverse kinematics;
- low-level servo loops;
- interpolation;
- command buffering;
- collision limits;
- rate limits;
- dead zones;
- saturation;
- actuator latency;
- motor mixing;
- safety stops;
- macro-action expansion, if deliberately used.

Every A1 transformation is supplied capability and belongs in the evaluator-side actuator manifest.

### A2 — learner-issued command and learner-visible efference

The first-core cognitive action remains conceptually:

```text
CognitiveAction {
  actuator_port_id
  command_payload
}
```

`actuator_port_id` is opaque supplied actuator topology. `command_payload` is the bounded low-level command accepted by that port.

If an efference trace is available, it may expose that **this command was issued** and the command payload that was issued. It does not say:

- the command succeeded;
- an effect was self-caused;
- which later observation is the consequence;
- what object was acted upon;
- whether the action was appropriate;
- whether the environment obeyed;
- whether another agent contributed.

### A3 — learned sensorimotor contingency / affordance inference

Noema may learn revisable relations such as:

- this command tends to change this sensory stream;
- this action has different effects in different contexts;
- a visible structure supports some outcomes but not others;
- a tool changes reachable effects;
- a command is unreliable under load;
- a delayed consequence is probably related to an earlier issued action;
- two different motor patterns are functionally equivalent;
- some apparently self-caused effects were actually external or joint.

These are learned predictive/control relations, not A2 metadata.

### A4 — learned semantic actions, skills, and agency

Later concepts may include:

- `push`;
- `grasp`;
- `point`;
- `walk there`;
- `use this as a tool`;
- `I caused that`;
- `we caused that together`;
- `this action is one way to open it`;
- named reusable skills.

A4 should arise from reusable learned structure and communication, unless a later experiment deliberately supplies semantic action primitives and narrows its claims.

## 3. Primitive action does not mean "raw torque or nothing"

The anti-subsidy rule should not become performative purity.

A physical or simulated embodiment may be unstable, inefficient, or impossible to use through literal raw motor torques. It is legitimate to expose a lower-dimensional control interface such as:

- bounded joint velocity;
- bounded body-relative velocity;
- bounded actuator position increment;
- normalized scalar intervention intensity;
- a simple continuous steering/thrust channel.

But the control layer must be described honestly.

For example, a body-relative velocity controller supplies stabilization and coordinate transformation. Noema may still learn the action-effect contingencies of that controller. It may not be credited with learning stabilization or inverse dynamics that the controller already solved.

The preferred principle is:

> **Use the weakest action interface that is stable and experimentally useful; attribute every controller-side capability; test stronger action-space conveniences as subsidies rather than pretending they are neutral.**

## 4. Forbidden default semantic action subsidies

The first developmental core should not, by default, receive APIs such as:

- `pick_up(object_id)`;
- `move_to(global_xyz)`;
- `look_at(entity_id)`;
- `ask(person_id, question)`;
- `use_tool(tool_id, target_id)`;
- `intervene_on(variable_name)`;
- `repair(machine_id)`;
- `execute_skill(skill_name)` where the skill was evaluator-authored;
- `wait_until(event_id)`;
- `open(container_id)`.

These interfaces can be useful engineering comparators. But they encode one or more of object identity, affordance, semantics, reference resolution, action decomposition, trajectory generation, or skill structure.

If used, the supplied capability must be explicit and the corresponding learned-capability claim must be narrowed.

## 5. Action availability masks are not neutral

A common RL convenience is to expose only actions that are currently valid.

That can quietly solve affordance learning.

A learner-visible mask such as:

```text
can_grasp = true
can_open = false
can_push = true
```

is semantic action-state knowledge unless it is a direct physical property of the actuator interface.

The default rule is:

- fixed actuator bounds and direct hardware safety limits may be supplied when declared;
- evaluator-derived feasibility, reachability, object compatibility, task legality, or success likelihood remains withheld;
- failed, ineffective, blocked, saturated, and context-inappropriate commands should be possible when physically meaningful;
- Noema learns which actions tend to work from consequence.

## 6. Action completion and temporal segmentation

A macro-action completion flag can provide a hidden event boundary.

The learner should not automatically receive evaluator fields such as:

- `action_complete=true`;
- `grasp_finished`;
- `subgoal_reached`;
- `navigation_done`;
- `skill_failed`;
- `intervention_applied`.

If the actuator exposes direct operational state—motor stopped, limit reached, contact sensor changed, command queue empty—that may be learner-visible as ordinary declared sensory/proprioceptive evidence.

Whether that state means a semantic action has completed remains learned unless deliberately supplied.

For temporally extended learned skills, initiation and termination should eventually be properties of Noema's own learned control policy, not evaluator annotations that are then credited as temporal abstraction.

## 7. Efference is evidence of issuance, not success or authorship

Candidate A already permits an efference-like trace. This contract narrows it.

A minimal efference trace may say, in effect:

> actuator route R received command payload C from the learner at learner-visible time T.

It must not say:

> result Y was caused by me.

The environment should support hostile cases including:

- command failure;
- partial/attenuated realization;
- delayed consequence;
- external cancellation;
- external duplication of the same effect;
- another agent producing an indistinguishable effect;
- joint causation;
- tool-mediated effects;
- changed actuator calibration;
- actuator damage or drift.

This preserves agency/source attribution as a fallible learned inference.

## 8. Tool use and embodiment extension

A tool can extend what the action interface can accomplish without changing the learner's actuator topology.

The evaluator must not silently update the learner with fields such as:

- `new_reach_radius`;
- `tool_equipped=true`;
- `tool_affords_cutting`;
- `controlled_proxy_id`;
- `body_extension=true`.

Noema may instead observe ordinary changes in action-effect contingencies and body-relative sensory evidence.

This aligns the spatial-interface contract: peripersonal/action space can be revised from consequence rather than fixed by evaluator geometry.

## 9. Action-space comparators

No single action granularity should be treated as architecture proof.

Where feasible, validation should compare at least two interfaces that preserve broad world capability but differ in supplied structure, for example:

- low-level continuous actuator commands;
- controller-assisted body-relative commands;
- a deliberately convenience-rich semantic/macro-action comparator.

If a richer action space learns much faster, that is useful evidence about the value of the supplied controller/action prior. It is not evidence that the learner independently discovered the structure encoded by the richer action API.

This parallels the synchronized-vector subsidy baseline on the sensory side.

## 10. Experiment A mapping

Experiment A does not require a robotic body.

Its action interface can remain deliberately tiny:

```text
CognitiveAction {
  actuator_port_id = opaque intervention route
  command_payload = bounded numeric command
}
```

The world/transducer may interpret that command as an attempted clamp or perturbation internally, but the cognitive boundary does not expose:

- `intervention=true`;
- target causal graph node name;
- edge deletion;
- success/failure bit;
- realized post-intervention distribution;
- evaluator chain/fork label.

Later ordinary observations reveal what happened.

Failed, attenuated, delayed, or noisy realization should remain possible so command issuance is not equivalent to world obedience.

## 11. F0/F1 actuator manifest

The first implementation specification should define an evaluator-side actuator manifest for every cognitive action port.

At minimum:

```text
ActuatorPortManifest {
  schema_version
  actuator_port_key
  evaluator_semantic_description
  learner_visible_port_id
  command_payload_encoding
  command_bounds
  transformation_chain
  control_law_or_controller
  buffering_and_latency
  saturation_and_rate_limits
  safety_interventions
  externally_supplied_targeting_or_registration
  learner_visible_efference
  learner_visible_operational_feedback
  withheld_fields
  known_failure_modes
  claim_restrictions
}
```

The semantic description, hidden target mapping, hidden safety state, exact control transform, and success truth remain evaluator-side unless explicitly projected as ordinary learner evidence.

## 12. Hostile falsification sequence

### AAS-0 — action-field audit

Enumerate every learner-issued action field, actuator-side transformation, and learner-visible feedback channel.

Kill condition: evaluator semantic target, affordance, success, causal, or subgoal information crosses undeclared.

### AAS-1 — semantic action-name rejection

Replace human-readable action names with opaque port/payload encoding while preserving capability.

Pass expectation: competence does not depend on names such as `push`, `grasp`, `intervene`, or `look` unless language grounding of those names is itself the experiment.

### AAS-2 — target-ID leakage test

Mutate evaluator object/agent/variable IDs while preserving physical/transducer evidence and command mapping.

Pass: cognitive action bytes and learner-visible feedback are unchanged.

### AAS-3 — action-space granularity comparator

Compare a low-subsidy continuous/control interface with a richer macro/object-centric interface.

Any gain from the richer interface is attributed to supplied action structure.

### AAS-4 — controller-remapping test

Change a reversible actuator mapping or calibration while preserving broad capability.

Pass requires recalibration or calibrated uncertainty rather than permanent assumption that one command has one immutable effect.

### AAS-5 — failed/attenuated action test

Some issued commands fail, saturate, or only partly realize.

Kill condition: learner treats issuance as guaranteed success.

### AAS-6 — duplicate/exogenous consequence trap

Produce an effect normally associated with Noema's action without Noema issuing that action, or have another agent produce the same effect.

Pass requires authorship/source inference to remain evidence-sensitive.

### AAS-7 — joint-causation test

Require learner and external agent/environment contribution for an effect.

Pass requires avoiding forced binary `self` versus `external` attribution when evidence supports shared influence.

### AAS-8 — action-availability-mask test

Remove any convenience feasibility mask and allow ineffective/context-invalid actions where physically meaningful.

Kill condition: claimed affordance competence collapses because evaluator legality/feasibility was doing the work.

### AAS-9 — macro-boundary withdrawal

Where a comparator exposes macro-action initiation/completion, withdraw or alter those boundaries while retaining low-level capability.

This tests whether temporal skill structure was learned or supplied.

### AAS-10 — tool/proxy extension

Alter action consequences through a tool, changed embodiment, or controlled proxy without adding semantic body/tool flags.

Pass requires learned contingency revision from ordinary evidence.

### AAS-11 — hidden-controller subsidy

Ablate or weaken inverse-kinematics, stabilization, collision-avoidance, or trajectory-planning help where safe/feasible.

Any performance difference is credited to the controller, not Noema.

### AAS-12 — efference/consequence separation

Verify learner-visible efference contains issued command information only and no realized outcome, success, evaluator causal parent, or future consequence handle.

### AAS-13 — replay fidelity

Replay must preserve learner-issued command sequence, learner-visible efference, actuator-visible timing, and subsequent learner-visible observations. Evaluator target/success/causal metadata is not required to reconstruct cognitive input after the learner-visible streams have been recorded.

## 13. Claim ceiling

Passing this contract supports narrow claims such as:

> The learner acquired action-conditioned predictive/control relations under the declared actuator topology and controller without identified evaluator target, affordance, success, or causal-label leakage.

or later:

> The learned sensorimotor policy remained adaptive under specified actuator remappings, failures, tool-mediated effects, and action-space transformations.

It does not by itself establish:

- human-like motor control;
- human-like agency;
- learned semantic action concepts;
- learned affordances in an unrestricted sense;
- learned skill hierarchy;
- learned body ownership;
- causal understanding;
- that raw torques are epistemically superior to controller-assisted action spaces.

## 14. Architecture implication

No new cognitive module is warranted by this pass.

The architecture-level consequence is a stronger actuator boundary:

> **Noema may be born with bounded actuator topology and engineering control transforms, but the meaning, efficacy, affordance, causal reach, skill structure, and authorship of those actions remain revisable learned relations unless explicitly supplied and claim-limiting.**

Together with the merged sensory/event contracts, this closes the basic developmental loop more symmetrically:

`declared sensory transducer -> cognitive evidence -> learned prediction/control -> declared actuator transducer -> ordinary world consequence -> new cognitive evidence`

The evaluator may know exactly what command meant, what target it affected, and whether it succeeded. Noema receives only the action/efference evidence and later consequences deliberately exposed across the learner boundary.
