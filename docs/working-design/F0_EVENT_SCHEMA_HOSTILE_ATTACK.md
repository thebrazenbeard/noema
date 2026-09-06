# F0 learner-event schema hostile attack

Status: **BRAINSTORMING / SELF-RED-TEAM / CORRECTIONS REQUIRED BEFORE IMPLEMENTATION**

Date: 2026-09-06

Target: `F0_F1_LEARNER_EVENT_SCHEMA_CONTRACT.md` in Draft PR #29

## Verdict

The concrete event schema is useful, but the first draft still contains implementation-level ways to smuggle structure or distort experience without adding an obvious semantic field.

The strongest attack is:

> **A schema can be semantically clean and still leak through transport metadata, preprocessing state, random-number coupling, scheduler timing, queue behavior, or encoder routing.**

F0 therefore cannot be only a field allowlist. It must test noninterference of the entire evaluator-to-cognition path.

The current `{schema_version, port_id, payload, dt_bin}` proposal survives only with the corrections below.

## A1 — `schema_version` should be transport-visible, not cognitive evidence

The first synthesis currently places `schema_version` inside `LearnerEvent`.

That is unnecessary for cognition. A parser/runtime may need a version identifier to decode bytes, but the predictive learner does not need to receive that value as a feature.

If schema versions ever correlate with a transducer generation, curriculum phase, experiment family, or deployment epoch, the field becomes a trivial context cue.

Correction:

- keep `schema_version` in the runtime/wire envelope;
- strip it before the cognitive learner update;
- do not embed it into the predictive state unless an experiment explicitly studies learned protocol/version cues.

Thus distinguish:

```text
RuntimeEnvelope {
  schema_version
  port_id
  payload
  dt_bin
}
```

from cognitive evidence:

```text
CognitiveEvent {
  port_id
  payload
  dt_bin
}
```

The transport parser is part of supplied machinery, not Noema's learned cognition.

## A2 — the port manifest is runtime architecture, not a semantic learner feature vector

`payload_kind`, `payload_shape`, and numeric domain may be required to instantiate encoders. They are legitimate supplied inductive structure.

But there is no reason to concatenate a `payload_kind` code or manifest metadata into the learned event representation.

Correction:

- rename the conceptual artifact to `RuntimePortManifest` or otherwise mark it runtime-visible;
- use it to construct/route the low-level encoder;
- count shape/type-specific encoders as supplied architecture;
- expose only the resulting low-level port topology/evidence the learner actually receives.

This also narrows port-permutation tests: arbitrary labels can be permuted only among routes whose machine contracts remain compatible unless the experiment deliberately tests encoder transfer.

## A3 — `dt_bin` must not measure host delivery latency

The first draft defines `dt_bin` as elapsed learner-delivery time. That phrase is dangerous.

If it is measured from wall-clock delivery, then:

- CPU/GPU load;
- garbage collection;
- queue backlog;
- diagnostic rendering;
- learner compute cost;
- host scheduling;

can become sensory evidence.

Worse, Noema's own cognitive workload could change when the next event is delivered, causing a feedback loop where computation changes apparent world time.

Correction:

> `dt_bin` must be derived from the declared learner-visible **T2 experimental timebase**, not host wall-clock delivery latency, unless host latency is intentionally part of the embodiment.

For F1/F2 simulation, exact host timing remains evaluator/transducer instrumentation. The T2 time source should advance according to the preregistered world/learner timing policy and then be quantized for cognitive input.

## A4 — silence exposes an event-driven limitation

If time is conveyed only when the next event arrives, the learner cannot update during a period in which nothing emits.

For the initial F1/F2 signal worlds this may be acceptable because observations can be emitted regularly. It is not a general chronoception solution.

Do not fix this by silently injecting semantic `NO_EVENT` or episode ticks.

Correction:

- explicitly scope the first event schema to F1/F2 environments with a declared emission/scheduling policy sufficient for the test;
- reserve a later design fork for endogenous cognitive-time updates / low-level chronoceptive dynamics when autonomous cognition through silence becomes a tested capability;
- any periodic pulse/tick port introduced later is supplied temporal structure and must be ablated accordingly.

## A5 — simultaneous-event tie order can become a hidden channel

An asynchronous event queue eventually serializes events.

If two ports emit at the same T2 time and the queue always resolves ties by port number, insertion order, object address, or producer registration order, that arbitrary order becomes learnable evidence.

Correction:

- specify the tie policy;
- keep it independent of hidden semantic/evaluator labels;
- test randomized or permuted tie order where simultaneous-order invariance is claimed;
- never use an evaluator common-event ID merely to solve tie handling.

## A6 — preprocessing/normalization can leak future information

A semantically clean payload can still contain test/future knowledge if preprocessing statistics were estimated non-causally.

Examples:

- normalization mean/variance computed over the entire run;
- min/max computed using held-out data;
- PCA/whitening fit on future observations;
- vocabulary/quantizer built from all developmental and evaluation data;
- adaptive calibration initialized from the answer-bearing evaluation distribution.

This is especially dangerous for a persistent online learner because it makes future distribution structure present at birth.

Correction:

Every transducer manifest must state whether preprocessing parameters are:

- fixed a priori from physical/engineering bounds;
- learned causally from past observations only;
- trained on a separately declared external corpus;
- computed non-causally for an explicit comparator.

F0 should reject undeclared future/test-dependent preprocessing.

## A7 — evaluator RNG coupling can leak hidden metadata

Even when hidden fields never enter the payload, they can alter the learner-visible stream if evaluator bookkeeping consumes or seeds the same RNG used for sensor/world noise.

Example:

1. scenario/object ID changes;
2. code consumes a different number of random draws or changes a seed;
3. sensory noise sequence changes;
4. Noema can learn a distributional proxy for the hidden ID.

Correction:

Use isolated, named random streams/seeds for at least:

- world dynamics;
- transducer noise;
- evaluator bookkeeping/labels;
- test perturbations;
- learner initialization/training stochasticity.

The LES withheld-metadata mutation test must hold the legitimate world/transducer random streams fixed while hidden metadata changes.

## A8 — queue backpressure can make cognition alter perception accidentally

If sensor producers block on the learner queue, or overflow depends on learner compute speed, harder cognition may cause observations to be dropped or delayed.

That may eventually be an interesting embodied resource coupling, but it is a confound in first-core F1/F2 unless explicitly intended.

Correction:

The harness must declare:

- queue capacity;
- producer blocking policy;
- overflow/drop policy;
- whether world time advances while learner compute runs;
- whether learner compute can alter sensor delivery.

First-core default should isolate learner compute cost from the physical evidence stream while still **accounting** for compute as an evaluator-side resource cost.

A later embodiment can deliberately couple them.

## A9 — low-level encoder routing can be a semantic subsidy

Even an opaque `port_id` becomes strongly semantic if the architecture routes each port through a hand-designed expert that already solves modality-specific invariances.

This is not forbidden, but it is supplied capability.

Correction:

The F0 capability ledger should include, per port:

- encoder family;
- pretrained/fixed/learned status;
- prior data used by the encoder;
- invariances it supplies;
- whether weights are shared across ports;
- whether encoder choice itself identifies modality/source class.

Claims must separate cognition acquired by Noema from perception supplied by the encoder.

## A10 — action ports need the same transducer audit as sensors

`LearnerAction { actuator_port_id, command_payload }` is appropriately low-level, but actuator semantics can still be overpowered.

Potential hidden subsidies:

- exact world-coordinate targeting;
- hidden object addressing;
- guaranteed command realization;
- zero latency;
- evaluator-selected action feasibility;
- semantic high-level actions such as `ask`, `inspect`, `grab object 17`, or `test hypothesis 4`.

Correction:

Create evaluator-side actuator manifests parallel to transducer manifests, including command domain, clipping, delay, failure/attenuation, physical mapping, and any supplied addressing structure.

Experiment A's clamp/intervention command remains a deliberately supplied low-level actuator capability and must include failed/attenuated outcomes.

## A11 — replay equivalence must distinguish input fidelity from learner determinism

Replaying the same learner-visible bytes is an interface property. Requiring identical learner internal updates is stronger and may be false for a stochastic learner unless learner RNG/checkpoint state is also controlled.

Correction:

Define two separate checks:

- **input replay fidelity:** identical learner-visible event sequence/bytes;
- **deterministic run replay:** identical learner state/action trace only when learner initialization, RNG state, scheduler, and deterministic settings are also fixed.

Do not fail the event boundary merely because a deliberately stochastic learner follows a different trajectory under the same input.

## A12 — field-level noninterference is not enough

A component can read evaluator truth through a global config, callback, shared object, debug API, diagnostic state, or closure even if event serialization is clean.

Correction:

F0 should enforce an architectural dependency rule:

> learner components receive only the cognitive event/action interface, declared persistent learner state, declared innate signals, and explicitly allowed resource signals.

Evaluator/world/transducer objects should not be reachable from learner code by reference.

Where practical, F0 should construct a twin-run test:

1. same initial learner state and learner RNG;
2. same learner-visible event stream;
3. evaluator-only metadata changed;
4. learner actions/state trace must remain identical in deterministic mode.

This catches non-serialized side channels.

## A13 — diagnostics can perturb the experiment even when they do not feed Noema

The interface research already recognizes Patrick's diagnostic observer effect. The runtime has a second version: instrumentation can change timing, queue behavior, memory pressure, or scheduler order.

Correction:

For formal F1/F2 runs:

- diagnostic collection should be non-blocking or its perturbation measured;
- operator rendering should not alter T2 learner time;
- diagnostic on/off runs should be compared for learner-visible stream equality where determinism permits;
- exact evaluator logging may be richer than live UI rendering.

## Required revision to the concrete schema

Before implementation, the authoritative first-core picture should become:

```text
Evaluator/world/transducer truth
           |
           v
Runtime projection + manifests
           |
           v
RuntimeEnvelope {schema_version, port_id, payload, dt_bin}
           |
       parser/router                 schema_version ends here
           |
           v
CognitiveEvent {port_id, encoded_payload_or_declared_payload, dt_bin}
           |
           v
      F1 cognition
           |
           v
CognitiveAction {actuator_port_id, command_payload}
           |
           v
Actuator transducer -> world
```

The exact representation of `encoded_payload_or_declared_payload` remains an implementation fork, but its encoder provenance must be in F0.

## Revised F0 kill conditions

Reject the first-core information boundary if any of the following occurs without explicit declaration:

- transport/parser metadata reaches cognitive state as an input feature;
- T2 time depends on host scheduling accidentally;
- hidden metadata changes learner-visible randomness;
- future/evaluation statistics influence preprocessing;
- arbitrary queue tie order encodes target structure;
- learner compute changes sensor evidence through accidental backpressure;
- modality/source semantics are supplied by hand-designed encoders but credited as learned;
- action realization is semantically or causally guaranteed beyond the actuator contract;
- evaluator objects/diagnostics are reachable through side channels;
- replay claims conflate input fidelity with stochastic learner determinism.

## Architecture verdict

No new cognitive module is required.

The attack instead strengthens F0 from a **schema audit** into a **whole-path noninterference audit**.

That is a material improvement: the learner information boundary is not the set of fields we intended to expose. It is the full set of variables that can causally influence Noema's state and actions.
