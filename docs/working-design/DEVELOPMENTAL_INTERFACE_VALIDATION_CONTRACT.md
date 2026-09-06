# Noema developmental interface validation contract

Status: **BRAINSTORMING / PROVISIONAL INTERFACE EVIDENCE CONTRACT / NOT IMPLEMENTED**

Date: 2026-09-06

## Purpose

The interface research pass established that the Noema Console is not merely a usability layer. It is part of the developmental environment and therefore part of the evidence chain for any later claim about grounding, communication, social learning, source attribution, or teacher independence.

This contract turns that conclusion into explicit validation requirements.

It does not choose a UI framework, transducer implementation, speech recognizer, renderer, or cognitive substrate. It constrains what an interface implementation may supply, what must remain learnable, and what evidence is required before interface-mediated capability claims can be trusted.

## Core rule

> **Every convenience offered to Patrick must be classified by what information it adds to Noema's experience.**

A convenience may be operationally acceptable while still being a developmental subsidy. The subsidy must be declared rather than silently credited to Noema.

## 1. Boundary classes

The practical interface has four operator-facing surfaces while preserving the existing learner-visible event distinctions.

### A. Shared world / perceptual surface

Learner-visible world state, ordinary sensory consequences, visible gestures, pointing cues, action results, and declared transducer outputs.

It may expose modality and timing required for perception.

It must not expose hidden simulator identity, class, causal role, evaluator answer, or semantic role.

### B. Learned communication / social-action surface

Patrick and Noema may both initiate ordinary signals/actions.

Typed symbols, acoustic input, gesture, gaze/pointing, demonstrations, corrections, requests, repairs, and later learned expressive acts may enter here.

No semantic meaning, trusted-speaker role, correction flag, command label, or truth status is supplied by the surface itself.

### C. Operator diagnostics

Direct instrumentation, deterministic derived diagnostics, and explicitly separate interpretive glosses.

These remain outside Noema's evidence stream by default.

### D. Experiment controls

Pause, reset, checkpoint, recording, scenario selection, diagnostic visibility, replay, and evaluator-only intervention controls.

These remain outside Noema unless an intended consequence is routed back through A or B as an ordinary observable event.

## 2. Transducer attribution ledger

Every communication or sensory route used in development or evaluation must declare at least:

- physical/original source;
- transformation chain;
- learner-visible payload;
- timing information supplied;
- segmentation/framing supplied;
- identity/source metadata supplied;
- semantic structure supplied;
- information deliberately withheld;
- whether the route is credited to Noema or to an external transducer.

Examples:

### Typed text — framed message mode

Possible supplied structure:

- character/byte identity;
- message start/end boundary;
- source-channel identity;
- send-event timing.

Not automatically learned by Noema:

- word meaning;
- sentence meaning;
- speaker identity as a person;
- pragmatic force;
- truth/reliability;
- reference.

Important caveat: a message-level submit boundary is itself segmentation. It may be an acceptable interface prior, but it must be listed as supplied structure rather than treated as discovered conversational segmentation.

### Typed text — keystroke stream mode

Possible supplied structure:

- individual symbols/bytes;
- inter-key timing;
- edit/backspace events if exposed;
- channel provenance.

This supplies less utterance framing but creates a different motor/UI artifact. Neither mode is intrinsically "purer"; each declares what it supplies.

### Push-to-talk voice

Push-to-talk supplies an externally imposed speech interval boundary even if raw waveform is preserved.

That boundary must not later be counted as learned utterance segmentation.

### External ASR

External transcription may supply:

- speech segmentation;
- lexical hypotheses;
- normalized spelling/punctuation;
- sometimes speaker diarization or confidence.

Only fields deliberately passed across the learner boundary become Noema evidence. The rest remain operator/transducer state.

Success through ASR is evidence of learning from a text-like transducer, not evidence that Noema learned speech perception.

### UI pointing

A pointer/click may generate an observable ray, cursor, gesture, gaze-like cue, or world event.

The hidden clicked object ID must remain withheld.

`joint_attention=true` is not a valid learner-visible substitute for those cues.

## 3. Temporal fidelity contract

Temporal contingency is part of the developmental signal, not just logging metadata.

Formal learner-visible events should therefore preserve, where meaningful:

- one monotonic learner-visible clock;
- event onset;
- event duration;
- delivery latency;
- transducer latency;
- dropped/unavailable event state;
- delayed/reordered state;
- action issuance time separate from sensed outcome time.

Replay used as evidence must preserve the learner-visible temporal relationships within a preregistered tolerance.

A UI, network layer, ASR buffer, renderer, or log replayer that silently smooths timing can change the developmental problem.

## 4. Mixed initiative without privileged query semantics

Noema should eventually be able to influence its own teaching interaction.

A valid mixed-initiative path permits Noema to emit ordinary learned behavior that Patrick may interpret as:

- request for repetition;
- request for contrast;
- request for demonstration;
- request for clarification;
- attention redirection;
- uncertainty disclosure;
- proposal of an experiment or test.

The learner need not receive or emit a privileged semantic opcode such as `ASK_CLARIFICATION`.

Operator diagnostics may classify a behavior after the fact, but the credited communicative act must originate from Noema's learned output/action policy.

Querying must have opportunity cost or resource cost so constant interrogation cannot replace world learning.

## 5. Learner-controlled social legibility

Wrapper-generated expressivity is diagnostic UI, not Noema behavior.

A face, animation, gaze shift, tone, color, confidence bubble, or "thinking" indicator derived directly from internal diagnostics cannot be credited as learned social communication unless Noema itself controls that output through an ordinary actuator/policy.

This yields a strict distinction:

- **operator visualization of state:** permitted diagnostic rendering;
- **Noema communicating state:** must be learner-controlled behavior.

Formal claims about communicative legibility must survive removal of wrapper-generated cues.

## 6. Progressive diagnostics and observer exposure

Development mode may expose rich diagnostics, but diagnostic visibility can change Patrick's teaching policy.

The console should therefore record an operator-exposure stream containing at least:

- which diagnostic panels were visible;
- which drill-downs were opened;
- which interpreter glosses were shown;
- when visibility changed;
- which evaluator-only controls were used.

This stream remains outside Noema unless deliberately reintroduced through ordinary communication.

Formal evaluation should include conditions with reduced, delayed, or absent diagnostics so capability is not inseparable from a bespoke human teacher optimizing against internal state.

## 7. Joint attention claim discipline

The interface may provide cues that make coordinated attention possible.

It must not supply coordinated attention as a semantic fact.

A later evaluator may infer joint attention from observable behavior, or Noema may learn a concept functionally equivalent to coordinated attention. Neither justifies claiming that joint attention was an innate interface primitive.

Communication competence should also be tested when one familiar cue is replaced, removed, delayed, or contradicted.

## 8. Human fallibility and source independence

Patrick remains ordinary fallible evidence.

The interface must not convert:

- confidence inferred by an external classifier;
- "correct/incorrect" evaluator state;
- teacher role;
- user identity;
- correction intent;

into privileged learner-visible fields unless the experiment explicitly studies that supplied transducer and excludes the supplied information from developmental claims.

Ordinary observable cues such as hesitation, explicit uncertainty statements, response time, contradiction, correction history, or changed behavior may remain available because they are part of the interaction itself.

Formal evaluation should include a held-out or minimally co-adapted teacher condition once grounded social learning is mature enough to test it.

## 9. Interface falsification sequence

The interface should earn trust through a staged sequence rather than one polished demo.

### I0 — event-boundary audit

For every operator action, verify exactly what Noema receives and what is withheld.

Kill condition: hidden semantic or evaluator state crosses the boundary without being declared.

### I1 — replay fidelity

Record and replay learner-visible events.

Pass only if ordering/timing/payload equivalence stays within declared tolerance and learner updates are equivalent within expected deterministic/stochastic variation.

### I2 — segmentation subsidy audit

Compare at least two framing regimes where practical, such as framed text versus finer-grained symbol stream or push-to-talk versus continuous acoustic windows.

Goal: identify which communication competence depends on supplied segmentation.

### I3 — cue substitution

Train with one family of shared-attention cues and evaluate with changed but informative cues.

Kill condition: apparent grounding is only a hard dependence on one interface affordance.

### I4 — cue conflict

Create disagreement among communication, gaze/pointing, and world evidence.

Pass requires source-sensitive uncertainty/revision rather than automatic preference for one privileged channel.

### I5 — teacher fallibility

Introduce bounded teacher error or uncertainty.

Pass requires scoped reliability learning or preserved conflict rather than obedience.

### I6 — mixed-initiative value

Compare information gathering with learner-initiated querying enabled versus suppressed.

Pass only if queries concentrate on consequential reducible uncertainty and improve future competence enough to justify their cost.

### I7 — diagnostic observer effect

Compare full, progressive/demand-driven, and blind/delayed diagnostic conditions.

Measure both Noema outcomes and Patrick teaching behavior.

### I8 — wrapper-expressivity kill

Remove all wrapper-generated social cues while preserving Noema-controlled outputs.

Any claimed Noema social communication must survive.

### I9 — transducer attribution

Compare a richer convenience transducer with a lower-level route where feasible.

Claims must narrow to the capability Noema actually learned rather than the capability the transducer supplied.

### I10 — held-out interaction partner

Evaluate with another human or agent whose history differs from Patrick's.

Pass does not require identical performance, but grounded competence must not collapse merely because the lifelong teacher changed.

## 10. Claim ceiling

Passing this interface contract supports only narrow conclusions such as:

> The tested interface preserves declared information boundaries and permits interaction without identified semantic leakage under the tested conditions.

or, at later stages:

> The tested learner demonstrates grounded, source-sensitive communication that survives specified changes in cues, transducer conditions, diagnostic exposure, and interaction partner.

It does **not** by itself establish:

- general intelligence;
- consciousness;
- human-like language understanding;
- human-like joint attention;
- autonomous social cognition;
- a correct mature cognitive architecture;
- that any specific transducer should become permanent.

## 11. Architecture implication

Candidate A is compatible with this contract if its provenanced event boundary and meta-control are strong enough to represent the differences above without semantic shortcuts.

The strongest new pressure is not a new cognitive module. It is a requirement for **transducer-aware developmental provenance**: Noema's evidence history and the experiment ledger must preserve enough information to distinguish what the learner acquired from what the interface supplied.

If a proposed architecture cannot make that distinction auditable, later claims about grounding and developmental acquisition are not trustworthy even if the behavior looks impressive.
