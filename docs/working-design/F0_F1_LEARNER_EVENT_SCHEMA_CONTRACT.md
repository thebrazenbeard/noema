# Noema F0/F1 learner-event schema contract

Status: **BRAINSTORMING / CONCRETE FIRST-CORE INTERFACE SYNTHESIS / NOT IMPLEMENTED**

Date: 2026-09-06

Related:
- `INTERACTION_EVENT_CONTRACT.md`
- `DEVELOPMENTAL_INTERFACE_VALIDATION_CONTRACT.md`
- `ORIGIN_EVIDENCE_AND_PROVENANCE_CONTRACT.md`
- `TIMEBASE_AND_CHRONOCEPTION_CONTRACT.md`
- `SENSORY_PACKETIZATION_AND_CHANNEL_IDENTITY_CONTRACT.md`
- `SENSORY_RELIABILITY_METADATA_ADDENDUM.md`
- Draft PR #28 `SPATIAL_INTERFACE_AND_REFERENCE_FRAME_CONTRACT.md`
- `NOEMA_ARCHITECTURE_CANDIDATE_A.md`

## Purpose

The earlier contracts define what Noema must **not** be given accidentally. This document turns those constraints into one concrete F0/F1 data boundary.

It is intentionally narrower than a full runtime implementation specification. It binds the shape of the first learner-visible event interface closely enough that F0 can audit it and F1 can consume the same boundary without a convenience-only training representation.

The main synthesis is:

> **Evaluator truth, transducer description, learner-visible topology, learner-visible events, and learner actions are separate artifacts. Only the latter three cross the learner/runtime boundary, and only to the degree explicitly declared below.**

This document also tightens one older Candidate A phrase: the learner-visible event envelope should **not** contain semantic source classes such as `external observation`, `communication`, `retrieved memory`, or `simulation` merely because the evaluator can classify them that way. Low-level routing/efference cues may exist; higher source meaning remains learned unless explicitly supplied and claim-limiting.

## 1. Boundary artifacts

F0/F1 should distinguish four concrete artifacts.

### A. Evaluator event record — never direct learner input

The evaluator may record exact ground truth needed for reproducibility, scoring, lineage, and leakage audit.

Illustrative evaluator-only record:

```text
EvaluatorEventRecord {
  evaluator_event_id
  run_id
  evaluator_sequence
  evaluator_time
  world_time
  physical_or_simulator_origin
  transducer_chain
  source_entity_id
  object_or_process_id
  causal_parent_ids
  intervention_id
  common_event_group_id
  world_geometry
  true_noise_parameters
  transducer_confidence
  hidden_regime_or_scenario_state
  learner_delivery_record
}
```

The exact evaluator schema may evolve. None of these fields is learner-visible merely because it is logged.

### B. Transducer/port manifest — evaluator description of supplied structure

For every learner-visible port, F0 records what the transducer does before delivery.

Required evaluator-side fields include:

```text
TransducerPortManifest {
  schema_version
  port_key
  evaluator_semantic_description
  physical_or_virtual_source
  transformation_chain
  payload_encoding
  payload_shape_or_bounds
  sampling_or_emission_policy
  buffering_or_windowing_policy
  learner_visible_time_basis
  externally_supplied_auxiliary_fields
  withheld_fields
  known_failure_modes
  claim_restrictions
}
```

The semantic description and withheld-field list remain evaluator-side.

### C. Learner port manifest — supplied low-level topology

The learner/runtime needs enough information to accept and encode the stream. The first-core default therefore permits a deliberately small supplied port manifest:

```text
LearnerPortManifest {
  schema_version
  port_id
  payload_kind
  payload_shape
  numeric_or_byte_domain
}
```

Rules:

- `port_id` is an opaque route identifier, not a semantic modality, person, agent, object, or source label.
- `payload_kind`, shape, and domain are supplied transducer/topology structure and must be counted as such.
- the learner-visible manifest contains no human-readable semantic port name such as `vision`, `Patrick`, `self_action`, `memory`, or `teacher_correction`;
- if different encoder families are used for different payload kinds, that is also supplied inductive structure and belongs in the capability ledger.

A later implementation may test weaker or richer port manifests as ablations. The first core should not pretend that payload shape/type was learned if the runtime requires it from birth.

### D. Learner event stream — actual evidence presented to F1

The default F0/F1 learner-visible event is:

```text
LearnerEvent {
  schema_version
  port_id
  payload
  dt_bin
}
```

Each field is constrained below.

## 2. `schema_version`

`schema_version` identifies only the machine-level event encoding contract.

It must not correlate with:

- experiment answer;
- scenario class;
- hidden regime;
- intervention status;
- teacher identity;
- developmental phase.

Changing a transducer implementation without changing the learner-visible schema does not require a new learner-visible version value. Evaluator manifests can version their internal description independently.

Formal evaluation should keep `schema_version` constant across conditions whose semantic difference the learner is expected to discover.

## 3. `port_id`

`port_id` is a small opaque identifier for the delivery route.

It supplies **stable low-level topology**, not semantic source truth.

Allowed use:

- route payloads to compatible low-level encoders;
- learn route-specific statistical regularities;
- learn that one route is more or less reliable in a context;
- learn relationships among routes from experience.

Not supplied by `port_id`:

- `this is vision`;
- `this came from Patrick`;
- `this is self-generated`;
- `this is memory rather than perception`;
- `this is a correction`;
- `this is trustworthy`;
- `this is the same source as another port`.

If a claimed capability could be solved by a permanent route-name shortcut, the evaluator should include port permutation/rerouting controls.

## 4. `payload`

`payload` is the raw or declared minimally transformed output of the port transducer.

Permitted examples depend on the experiment:

- continuous scalar/vector measurements;
- image-like numeric arrays;
- raw or low-level acoustic windows;
- bytes/symbols from typed communication;
- proprioceptive actuator/body-state measurements;
- an efference copy of an issued command encoded at the action interface's low level.

The payload must not silently include evaluator semantic fields such as:

- stable object or agent IDs;
- hidden world coordinates not physically/transducer supplied;
- semantic body/self masks;
- `correct`, `wrong`, `trusted`, `command`, `goal`, `intent`, `cause`;
- common-source/common-event IDs;
- action-cause links;
- hidden regime IDs;
- evaluator model-adequacy labels;
- exact simulator noise parameters;
- evaluator truth confidence.

A richer transducer may deliberately emit additional information, but then the transducer manifest and capability claim must say exactly what it supplied.

## 5. `dt_bin`: the first-core chronoception choice

F0/F1 needs temporal order and enough duration information for streaming prediction without exposing absolute age or one perfect world clock.

The first-core default is therefore **relative, quantized learner-delivery time**:

`dt_bin = quantized elapsed learner-visible time since the previous delivered LearnerEvent`

Properties:

- no wall-clock/UTC time;
- no absolute simulator tick;
- no run age;
- no event UUID encoded in time;
- no reset value tied to hidden scenario boundaries;
- no guarantee of exact physical simultaneity across ports;
- quantization policy fixed by the declared T2 timebase for a preregistered run family;
- the evaluator retains exact T0/T1 timing separately.

Why use `dt_bin` at all:

- pure event order would make duration unavailable;
- exact timestamps would create a stronger temporal subsidy;
- relative quantized duration supplies a weak chronoceptive basis while preserving a real learning problem around recurrence, cross-modal latency, action-feedback delay, and event segmentation.

The exact bin edges are an implementation parameter to preregister before F1. They must be chosen from engineering/experimental needs, not tuned against hidden test answers.

A no-explicit-time/order-only comparator and a richer timestamp comparator remain valid ablations.

## 6. No learner-visible numeric event index

The learner receives events sequentially, so event order already exists causally in the runtime.

The first-core event does **not** add:

- global sequence number;
- episode step index;
- message number;
- intervention counter;
- developmental age counter.

Those values remain evaluator-side.

This avoids turning a convenient identifier into a regime, curriculum, or memory-index shortcut.

If the learner later develops an internal count/age estimate, that is learned state derived from its experience and supplied temporal basis.

## 7. Availability and quality metadata: omitted by default

The default `LearnerEvent` has no generic `confidence`, `variance`, `quality`, `valid`, or `reliability` field.

For first-core F0/F1:

- a valid emitted sample appears as an event;
- no sample is represented by its absence, which is observable through timing when relevant;
- clipping/saturation should be represented in the declared payload encoding where feasible rather than by an oracle-like semantic warning;
- direct operational status may be added only when a specific transducer requires it, and then it becomes an explicitly supplied auxiliary port/field in the manifest;
- external confidence estimates are not supplied by default.

This prevents simulator noise knobs or decoder confidence from solving uncertainty estimation externally.

## 8. Packetization and grouping

Each `LearnerEvent` is one transducer emission, not a declaration that it corresponds to one meaningful world event.

The learner-visible schema contains no:

- `same_event_id`;
- packet-group semantic ID;
- cross-modal correspondence ID;
- episode ID;
- synchronized-frame ID.

If multiple values are bundled inside one port payload because the transducer physically samples a frame/window, that windowing is listed in the evaluator-side manifest as supplied structure.

The harness must support tests in which meaningful processes span multiple emissions and unrelated processes occur within the same transducer window.

## 9. Spatial information

Spatial encoding is entirely port/transducer specific.

The generic `LearnerEvent` contributes no global coordinates, object position, body mask, target identity, reachability flag, or cross-modal registration.

If a port emits spatial structure, its manifest records:

- coordinate/reference frame;
- calibration;
- distortion/quantization;
- whether depth/range/bearing is supplied;
- any external registration performed.

The learner receives only the declared payload—not the evaluator's S0 geometry.

## 10. Communication

Typed or acoustic communication uses ordinary ports under this same event contract.

Examples:

- a typed-symbol stream can emit one symbol/byte event at a time;
- a framed message transducer can emit a payload/window whose boundary is explicitly credited as supplied segmentation;
- a voice transducer can emit acoustic windows;
- ASR can be used in a comparator, but lexical/endpointing/punctuation/confidence output must be attributed to that transducer.

No generic event field says:

- speaker identity;
- correction;
- directive;
- question;
- truthfulness;
- reference;
- joint attention.

## 11. Learner action interface

F1/F2 also needs an explicit outbound boundary.

Default action request:

```text
LearnerAction {
  schema_version
  actuator_port_id
  command_payload
}
```

Rules:

- `actuator_port_id` is opaque supplied actuator topology;
- `command_payload` is low-level and bounded by the actuator manifest;
- no object/agent target ID is supplied unless that actuator's declared physical interface intrinsically exposes such an address;
- the evaluator records action issuance and world consequences separately;
- command issuance does not imply successful realization.

When an efference trace is part of the innate signal family, the runtime emits a corresponding ordinary learner-visible event on a declared low-level efference port after command issuance. It contains the issued command information needed for prediction but no `success`, `cause`, or future-consequence label.

## 12. Retrieved memory and internal simulation

The older Candidate A event-boundary text listed `retrieved memory` and `internal simulation` as possible source classes. For first-core F0/F1 this should be interpreted more cautiously.

If internal retrieval/simulation later re-enters the predictive substrate through event-like interfaces, the learner may have access to low-level endogenous routing cues sufficient to distinguish streams when the architecture requires it. But those cues must not automatically encode semantic conclusions such as:

- `this is a true memory`;
- `this was personally experienced`;
- `this is imagined`;
- `this branch is counterfactual`;
- `this source is trustworthy`.

F1 does not require mature memory/simulation source attribution. The first schema reserves no privileged semantic source-class field for it.

## 13. Evaluator-to-learner projection function

F0 should treat learner delivery as an explicit projection:

`LearnerEvent = Project(EvaluatorEventRecord, TransducerPortManifest, T2_timebase)`

The projection must be deterministic for deterministic transducers given the same declared transducer state/seed.

Crucially:

> **Changing evaluator-only facts that are supposed to be withheld must not change serialized learner-visible bytes unless those facts legitimately alter the physical/transducer evidence.**

This becomes a direct leakage-test principle.

## 14. F0 conformance tests

Before any F1 learning result is accepted, F0 should run the following schema tests.

### LES-0 — field allowlist

Serialize every learner event and reject any field outside the approved learner schema/declared port payload.

### LES-1 — withheld-metadata mutation

Mutate evaluator-only labels/IDs while holding physical/transducer output constant.

Pass: learner-visible serialization is byte-identical.

Examples of mutated evaluator-only state:

- object ID;
- agent ID;
- source name;
- causal annotation;
- hidden regime name;
- intervention identifier;
- truth label.

### LES-2 — semantic port-name rejection

The learner-visible port manifest must contain opaque IDs and machine payload contracts only.

Fail if human semantic names or evaluator roles cross the boundary.

### LES-3 — time leakage

Verify that absolute evaluator time, simulator step, run age, hidden schedule counters, and scenario resets cannot be recovered directly from event fields beyond what the declared `dt_bin` sequence legitimately reveals.

### LES-4 — grouping leakage

Verify absence of evaluator common-event, episode, object, synchronized-frame, or causal-group identifiers.

### LES-5 — reliability leakage

Verify absence of evaluator noise parameters, expected-error values, correctness probabilities, or external confidence unless the run is an explicitly declared confidence-transducer comparator.

### LES-6 — spatial leakage

Verify generic envelope contains no S0 geometry and each spatial port emits only its declared S2 transducer output.

### LES-7 — action-cause separation

Verify an issued command/efference event contains no realized outcome, success bit, or evaluator causal link to future observation.

### LES-8 — training/evaluation schema identity

F1 training/development and held-out evaluation use the same learner-visible event schema and port-manifest rules unless a transformation is itself the preregistered test.

### LES-9 — replay equivalence

Given recorded learner-visible events, replay reproduces the same serialized event order, payloads, port IDs, and `dt_bin` values. Evaluator metadata is not required to recreate learner input after the learner-visible stream has been captured.

### LES-10 — downstream visibility audit

No model component, structural adapter, gate, retrieval policy, or meta-control path may receive evaluator-only fields through a side channel. The learner-visible event/action boundary is the **maximum information surface** for F1 cognition unless another innate signal is explicitly declared.

## 15. F1 implications

The first persistent streaming learner should consume the `LearnerEvent` stream directly.

Do not train through a richer convenience object and strip fields only at evaluation time.

F1 state updates should be functions of:

- prior persistent learner state;
- current learner-visible event(s);
- internally generated state allowed by Candidate A;
- declared resource/learning mechanics.

They should not depend on evaluator annotations.

The event boundary therefore becomes the clean seam for comparing:

- simple recurrent probabilistic baselines;
- Candidate A's fast predictive realization;
- later scoped structural mechanisms;
- packetization/time/reliability ablations.

## 16. F2 / Experiment A mapping

Experiment A can use the same schema without introducing causal semantics.

A minimal mapping can be:

- one or more observation ports carrying continuous signal values such as `x`, `y`, `z` as opaque numeric channels;
- one actuator/efference route carrying the low-level intervention command;
- later ordinary observation events showing whether the world actually followed the command;
- no `intervention=true`, graph edge, causal-parent, success, regime, or evaluator chain/fork label in the learner event.

The evaluator retains those facts for scoring.

Before intervention, calibrated non-commitment is evaluated from predictions, not from a hidden structure label. After intervention, revision is evaluated from changed action-conditioned prediction and transfer.

## 17. What remains intentionally open

This schema does not yet choose:

- actual serialized wire format;
- programming language/types;
- numeric normalization per port;
- exact `dt_bin` edges;
- event queue implementation;
- async scheduling mechanism;
- encoder architecture;
- persistence file format;
- checkpoint representation;
- F1 predictive-state implementation;
- F2 world implementation.

Those belong in the next implementation specification or concrete experiment harness design.

## 18. Current verdict

The interface/provenance research is now concrete enough to stop adding generic learner-input concepts before implementation design.

For F0/F1, the proposed boundary is:

```text
Evaluator truth/logging
        |
        v
Declared transducer projection + evaluator-side manifest
        |
        +----> learner-visible port manifest
        |
        +----> LearnerEvent {schema_version, port_id, payload, dt_bin}
                        |
                        v
                 F1 learner state
                        |
                        v
LearnerAction {schema_version, actuator_port_id, command_payload}
                        |
                        v
                 world dynamics
```

Everything richer must justify why it crosses that boundary and what capability claim it subsidizes.

This is the first concrete implementation-facing synthesis of the F0/F1 learner information surface. It should now be attacked for insufficiency and hidden subsidy rather than expanded casually.
