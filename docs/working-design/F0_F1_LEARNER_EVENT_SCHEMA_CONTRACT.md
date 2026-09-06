# Noema F0/F1 learner-event schema contract

Status: **BRAINSTORMING / REVISED CONCRETE FIRST-CORE INTERFACE SYNTHESIS / NOT IMPLEMENTED**

Date: 2026-09-06

Revised after: `F0_EVENT_SCHEMA_HOSTILE_ATTACK.md`

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

The earlier contracts define what Noema must not be given accidentally. This document binds those constraints into one concrete F0/F1 information surface.

The hostile self-attack exposed an important refinement: a clean event field list is not enough. Information can leak through parser metadata, preprocessing, encoder routing, random-number coupling, queue order, host timing, backpressure, diagnostics, or shared runtime objects.

The authoritative rule is therefore:

> **Noema's learner boundary is the complete set of variables that can causally influence cognitive state or action, not merely the fields we intended to serialize.**

F0 must audit the whole evaluator-to-cognition path. F1 must consume that audited path directly rather than training through a richer convenience representation.

## 1. Boundary layers

The first core distinguishes six layers.

### A. Evaluator event record — evaluator only

The evaluator may retain exact truth required for generation, scoring, lineage, and audit.

Illustrative fields include:

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

None of these fields becomes cognitive evidence merely because the evaluator knows or logs it.

### B. Evaluator-side transducer/actuator manifests

Every sensor, communication route, efference route, and actuator has an evaluator-side manifest documenting the supplied transformation.

```text
TransducerPortManifest {
  manifest_version
  port_key
  evaluator_semantic_description
  physical_or_virtual_source
  transformation_chain
  payload_encoding
  payload_shape_or_bounds
  sampling_or_emission_policy
  preprocessing_parameter_origin
  buffering_or_windowing_policy
  learner_visible_time_basis
  externally_supplied_auxiliary_fields
  withheld_fields
  encoder_family_and_provenance
  known_failure_modes
  claim_restrictions
}
```

```text
ActuatorManifest {
  manifest_version
  actuator_key
  evaluator_semantic_description
  command_encoding
  command_bounds
  addressing_structure
  clipping_or_saturation
  latency_policy
  failure_or_attenuation_policy
  physical_world_mapping
  claim_restrictions
}
```

Semantic descriptions, evaluator identities, and hidden truth remain evaluator-side.

### C. Runtime port manifest — supplied machine topology, not cognitive evidence

The runtime needs enough information to parse and route each port.

```text
RuntimePortManifest {
  transport_schema_version
  port_id
  payload_kind
  payload_shape
  numeric_or_byte_domain
}
```

This is supplied architecture. It is used to construct/route low-level encoders but is **not automatically concatenated into cognitive input**.

Rules:

- `port_id` is opaque route topology, not semantic modality/person/agent/source identity;
- payload kind/shape/domain are supplied inductive structure and must be counted as such;
- no human-readable semantic port names such as `vision`, `Patrick`, `teacher`, `memory`, `self_action`, or `correction` enter cognition;
- modality-specific or pretrained encoders are allowed only with explicit provenance and claim restriction.

### D. Runtime transport envelope — parser-visible

The first-core wire/runtime envelope is:

```text
RuntimeEnvelope {
  transport_schema_version
  port_id
  payload
  dt_bin
}
```

`transport_schema_version` exists only so runtime machinery can decode the record. It terminates at the parser/router and is **not a cognitive feature**.

### E. Cognitive event — actual learner evidence

After parsing/routing, the cognitive learner receives only:

```text
CognitiveEvent {
  port_id
  payload_or_declared_encoded_payload
  dt_bin
}
```

If an encoder transforms the raw payload before cognition, that encoder is part of supplied transducer/architectural machinery and its provenance is recorded in F0.

### F. Cognitive action — learner output before actuator realization

The learner emits:

```text
CognitiveAction {
  actuator_port_id
  command_payload
}
```

The runtime may wrap/version this for transport, but transport metadata is not a cognitive action feature.

Command issuance does not imply successful realization.

## 2. `port_id`: topology without semantic source truth

`port_id` is a small opaque route identifier.

It may support:

- routing to compatible low-level encoders;
- learning route-specific statistical regularities;
- learning changing reliability of a route;
- learning cross-route relationships.

It does not by itself mean:

- `vision`;
- `Patrick`;
- `self-generated`;
- `memory`;
- `simulation`;
- `correction`;
- `trusted`;
- `same source as another route`.

The older Candidate A wording that listed semantic source classes such as `external observation`, `communication`, `retrieved memory`, and `internal simulation` is therefore tightened: evaluator/source taxonomy is not automatically learner-visible source knowledge.

Port-label permutation tests are restricted to machine-compatible routes unless the experiment deliberately tests encoder transfer. Encoder differences themselves remain declared supplied priors.

## 3. Payload rule

`payload_or_declared_encoded_payload` is the output of a declared low-level transducer/encoder path.

Permitted examples depend on the experiment:

- continuous scalar/vector measurements;
- image-like numeric arrays;
- low-level acoustic windows;
- typed bytes/symbols;
- proprioceptive measurements;
- low-level efference copies of issued commands.

The cognitive payload must not silently include:

- stable evaluator object/agent IDs;
- hidden world coordinates not explicitly supplied by the sensor;
- semantic body/self masks;
- `correct`, `wrong`, `trusted`, `goal`, `intent`, `cause`, `command`;
- common-source/common-event IDs;
- action-cause links;
- hidden regime IDs;
- evaluator model-adequacy labels;
- true simulator noise parameters;
- evaluator truth/confidence values.

Richer transducers are legitimate comparators only when their additional supplied structure is declared and capability claims narrow accordingly.

## 4. `dt_bin`: first-core chronoception

F0/F1 needs temporal order plus coarse duration without exposing one perfect global clock.

The default is:

> `dt_bin = quantized elapsed T2 learner-visible experimental time since the prior cognitive event`

Crucially, **T2 time is not host wall-clock delivery latency**.

For the initial simulated F1/F2 worlds:

- host scheduling, CPU/GPU latency, garbage collection, diagnostic rendering, and queue wait remain evaluator/transducer instrumentation;
- T2 advances according to the preregistered world/learner timing policy;
- the resulting elapsed interval is quantized before cognitive input.

The cognitive event contains:

- no UTC/wall time;
- no absolute simulator tick;
- no run age;
- no numeric event index;
- no curriculum/intervention counter;
- no hidden-boundary reset marker.

`dt_bin` does not assert that events on different ports are physically simultaneous or causally related.

The exact bin edges remain an implementation parameter to preregister. Order-only and richer-time comparators remain valid ablations.

### Scope limitation: silence

A time value delivered only with events does not provide autonomous cognitive updates during indefinite silence.

That is acceptable for first-core F1/F2 only if their declared emission schedule supplies events often enough for the tested capability.

Do not silently fix the problem with semantic `NO_EVENT` messages. A later capability requiring cognition through silence must separately specify endogenous chronoceptive/cognitive-time dynamics; any periodic pulse/tick is itself supplied temporal structure.

## 5. No generic availability or confidence field by default

The default cognitive event has no generic:

- `confidence`;
- `variance`;
- `quality`;
- `valid`;
- `reliability`;
- simulator noise parameter.

First-core default:

- a produced sample arrives as an event;
- missingness is represented by absence/timing unless a particular sensor needs declared operational status;
- clipping/saturation should be reflected by the declared payload encoding where feasible;
- any explicit operational health/status field is a supplied auxiliary signal documented in the manifest;
- external confidence/reliability estimates are withheld unless they are the explicit comparator.

This keeps uncertainty estimation inside Noema rather than in the simulator API.

## 6. Packetization does not define meaningful events

One `RuntimeEnvelope` is one transducer emission, not one evaluator-defined world event.

No cognitive field carries:

- `same_event_id`;
- synchronized-frame semantic ID;
- cross-modal correspondence ID;
- episode ID;
- common-source group.

Transducer frame/window boundaries are supplied segmentation and are documented in the manifest.

Formal tests must allow:

- meaningful processes spanning multiple emissions;
- multiple unrelated changes within one sensor window;
- asynchronous sampling across ports;
- related signals arriving across packet boundaries.

## 7. Spatial information remains transducer-specific

The generic event boundary adds no:

- global XYZ;
- stable object location;
- body mask;
- target identity;
- reachability flag;
- exact cross-modal registration.

Any port supplying spatial structure declares its reference frame, calibration, distortion, range/depth/bearing information, and external registration in the transducer manifest.

The cognitive learner receives only the declared sensor/transducer result, not S0 evaluator geometry.

## 8. Communication uses ordinary ports

Typed and acoustic communication enters through the same boundary.

A transducer may emit:

- bytes/symbols;
- framed text, with framing credited as supplied segmentation;
- acoustic windows;
- ASR output in an explicit comparator condition.

No generic event field supplies:

- speaker identity;
- teacher status;
- correction intent;
- directive/question type;
- truthfulness;
- reference;
- joint attention.

External ASR lexicalization, endpointing, punctuation, diarization, and confidence remain transducer contributions.

## 9. Efference and action realization

When efference is included as an innate signal family, command issuance generates a low-level learner-visible event on a declared route.

It may represent what Noema attempted to issue.

It must not contain:

- success/failure truth;
- causal attribution to later observation;
- hidden actuator state;
- future consequence;
- evaluator target identity.

Actuator manifests must explicitly document command domain, addressing, clipping, latency, failure/attenuation, and physical mapping.

Experiment A's intervention command is therefore a deliberately supplied actuator capability, while failed/attenuated outcomes keep `command issued` separate from `world obeyed`.

## 10. Preprocessing must be causal or explicitly external

F0 must audit not only payload fields but how payload transformations were fit.

Forbidden without explicit comparator/claim restriction:

- normalization mean/variance computed over the full run;
- min/max using held-out evaluation observations;
- PCA/whitening fitted on future data;
- vocabulary/quantizer built from answer-bearing evaluation data;
- adaptive calibration initialized from the held-out distribution.

Every preprocessing parameter must be classified as:

- fixed a priori from engineering/physical bounds;
- learned causally from past learner-available experience only;
- learned on a separately declared external corpus;
- intentionally non-causal for a comparator condition.

Future/test-dependent preprocessing is F0 leakage even if the resulting payload has no semantic label.

## 11. Randomness isolation

Hidden evaluator metadata must not change learner evidence indirectly by changing random-number consumption.

The harness should use isolated named random streams/seeds for at least:

- world dynamics;
- transducer noise;
- evaluator bookkeeping/labels;
- test perturbations;
- learner initialization/training stochasticity.

With legitimate world/transducer streams fixed, changing withheld evaluator labels must leave cognitive-event bytes unchanged unless the changed fact physically/transducer-causally alters learner evidence.

## 12. Queue, scheduling, and simultaneous-event policy

The event queue itself can leak structure.

The implementation spec must declare:

- queue capacity;
- producer blocking policy;
- overflow/drop policy;
- whether world time advances during learner compute;
- whether learner compute can alter sensor delivery;
- tie policy for multiple emissions at the same T2 time.

First-core default:

> learner compute cost is measured evaluator-side but should not accidentally alter the physical evidence stream through host backpressure.

If simultaneous events must be serialized, tie order must not depend on hidden semantic labels. Where simultaneous-order invariance is claimed, evaluation should permute/randomize legal tie order.

## 13. Diagnostics must not perturb T2 evidence silently

Diagnostics can affect experiments without feeding Noema directly by changing scheduling, memory pressure, or queue latency.

Formal F1/F2 runs should therefore ensure that:

- diagnostic rendering does not define T2 learner time;
- logging is non-blocking or perturbation is measured;
- diagnostic-on/off deterministic runs can be compared for learner-visible stream equality where practical;
- evaluator logging may remain richer than live UI rendering.

Patrick's separate human-teacher observer effect remains governed by the developmental interface contract.

## 14. Whole-path evaluator-to-cognition projection

Conceptually:

```text
Evaluator/world truth
        |
        v
Declared transducer projection + evaluator manifest
        |
        v
RuntimeEnvelope {transport_schema_version, port_id, payload, dt_bin}
        |
      parser/router          transport_schema_version ends here
        |
        v
CognitiveEvent {port_id, payload_or_declared_encoded_payload, dt_bin}
        |
        v
       F1 cognition
        |
        v
CognitiveAction {actuator_port_id, command_payload}
        |
        v
Declared actuator transducer
        |
        v
     world dynamics
```

The parser/runtime manifest is supplied machinery. The cognitive learner should not be handed transport metadata merely because software needs it.

## 15. F0 conformance tests

Before accepting any F1 result, F0 should pass at least these checks.

### LES-0 — cognitive field allowlist

Instrument the actual learner update boundary. Reject undeclared inputs beyond:

- cognitive event fields;
- declared persistent learner state;
- explicitly declared innate signals;
- explicitly allowed internal/resource signals.

### LES-1 — withheld-metadata mutation

Change evaluator-only object/agent/source/regime/intervention/truth annotations while holding legitimate physical/transducer evidence and random streams constant.

Pass: cognitive-event serialization is byte-identical.

### LES-2 — parser metadata termination

Verify transport schema/version, semantic manifest descriptions, evaluator IDs, and hidden source labels do not become model inputs or embeddings.

### LES-3 — time noninterference

Verify T2 `dt_bin` derives from the declared experimental timebase, not host scheduling, diagnostic rendering, or learner compute latency.

### LES-4 — grouping/tie leakage

Verify absence of common-event/episode/correspondence IDs and stress legal tie-order permutations.

### LES-5 — reliability leakage

Verify true noise/error/confidence is absent unless explicitly supplied as a comparator.

### LES-6 — spatial leakage

Verify generic envelopes contain no evaluator geometry and spatial ports emit only declared S2 transducer output.

### LES-7 — action-cause separation

Verify command/efference contains no realized-outcome, success, future-consequence, or evaluator causal link.

### LES-8 — causal preprocessing

Verify normalizers/encoders/quantizers use only declared a-priori, past-causal, or separately sourced statistics. Reject undeclared future/evaluation fitting.

### LES-9 — RNG isolation

With world/transducer RNG fixed, mutate hidden evaluator metadata and verify learner-visible evidence is unchanged.

### LES-10 — queue/backpressure isolation

Verify learner compute and diagnostics do not accidentally change sensor evidence under the first-core timing policy.

### LES-11 — encoder provenance

Inventory per-port encoder family, initialization/pretraining source, weight sharing, and supplied invariances.

### LES-12 — training/evaluation boundary identity

F1 development and held-out evaluation use the same cognitive boundary unless the transformation itself is preregistered.

### LES-13 — input replay fidelity

Recorded cognitive events reproduce identical port IDs, payloads, order, and `dt_bin` on replay.

This is distinct from learner determinism.

### LES-14 — deterministic twin-run noninterference

When learner initialization/RNG/scheduler are fixed, feed identical cognitive events while changing evaluator-only metadata.

Pass: learner state/action trace is identical.

This catches side channels through shared configuration, callbacks, diagnostics, globals, or object references.

## 16. F1 implications

The persistent streaming learner consumes the cognitive-event stream directly.

Do not train through a richer convenience object and strip fields only at evaluation time.

F1 state changes may depend only on:

- prior persistent learner state;
- cognitive events;
- internally generated state allowed by the architecture;
- declared innate signals;
- declared learning/resource mechanics.

Evaluator/world/transducer objects are not reachable from learner code by reference.

This boundary is the comparison seam for:

- simple recurrent probabilistic baselines;
- Candidate A fast predictive realizations;
- later scoped structural mechanisms;
- packetization/time/reliability ablations.

## 17. F2 / Experiment A mapping

Experiment A uses the same boundary.

A minimal mapping can provide:

- continuous observation ports carrying `x`, `y`, `z` values as opaque numeric routes;
- a low-level intervention actuator;
- an efference event describing the issued command;
- later ordinary observations showing actual consequences.

The cognitive learner receives no:

- `intervention=true`;
- graph edge;
- causal parent;
- success bit;
- hidden regime;
- chain/fork label;
- evaluator structure ID.

The evaluator retains those facts for scoring.

Before intervention, calibrated non-commitment is evaluated from predictive behavior. After intervention, revision is evaluated from changed action-conditioned prediction, calibration, transfer, and resource use.

## 18. Open implementation parameters

This contract still does not choose:

- serialized wire format;
- programming language/type system;
- exact `dt_bin` edges;
- queue/runtime implementation;
- per-port normalization values;
- encoder architecture;
- predictive-state realization;
- persistence/checkpoint format;
- F2 world implementation.

Those belong in the next implementation specification.

## 19. Current verdict

The first-core information boundary is now concrete enough for implementation design **after hostile qualification**, without pretending that software transport metadata is cognition.

The key shift from the first draft is:

> **F0 is a whole-path noninterference audit, not merely a schema lint check.**

Everything that can causally influence Noema's cognitive state must either pass through the declared cognitive boundary or be listed as an explicit innate/supplied capability. Everything else is evaluator/transducer infrastructure and must remain causally isolated from cognition.
