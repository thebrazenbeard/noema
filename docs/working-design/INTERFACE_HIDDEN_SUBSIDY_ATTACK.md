# Noema interface hidden-subsidy attack

Status: **HOSTILE DESIGN REVIEW / PROVISIONAL / NOT IMPLEMENTED**

Date: 2026-09-06

## Purpose

Attack the developmental interface contract from the opposite direction:

> Even if no explicit semantic label crosses the learner boundary, what low-level conveniences could still solve part of the developmental problem for Noema?

The goal is not to eliminate every prior. That would make interaction impractical and may be impossible. The goal is to make each prior visible enough that later capability claims cannot accidentally credit Noema for structure supplied by the interface.

## Attack 1 — stable channel address can become a hidden speaker identity token

The current event contract permits a source-channel address such as `human_input_channel_1` while requiring person identity to remain learned.

That is only safe if the distinction is taken seriously.

If Patrick is always the sole producer of one stable channel, then the channel address is an almost perfect proxy for Patrick identity. Noema need not infer cross-modal person continuity to know that all events on that channel belong together.

### Required accounting

Classify stable channel identity as a **source-segmentation prior**.

Tests that claim learned speaker/person identity should later break this shortcut by varying devices/channels, sharing a channel across agents, or exposing the same agent through multiple channels.

A stable channel may remain operationally useful; it just cannot count as evidence that Noema discovered person identity.

## Attack 2 — modality labels can become semantic roles by convention

An event field such as `modality=text` is low-level provenance, but repeated developmental use can make it a near-perfect cue for social versus world input.

If all human teaching arrives through one labeled modality and all non-agent events through another, Noema receives a strong partition between "communication" and "world" before learning either concept.

### Required accounting

Treat modality labels as supplied sensor partitioning.

Later tests of learned communication/agent distinction should include ambiguous or overlapping routes where possible: gesture as world-visible motion, audio containing both speech and non-speech, or multiple agents/world sources sharing a modality.

## Attack 3 — message submission is an utterance-boundary oracle

Framed typed text commonly arrives only after Patrick presses Send.

Even without words or semantics, that provides a clean segmentation unit. The learner can treat each submitted frame as a candidate conversational act.

### Required accounting

Framed text is acceptable, but the supplied message boundary belongs in the transducer ledger.

Claims about learned utterance segmentation require a less pre-segmented route or a direct ablation showing competence does not depend on the framing oracle.

## Attack 4 — push-to-talk is also segmentation

A push-to-talk button creates a start/end interval around speech.

Raw waveform inside that interval is not the same developmental problem as continuous ambient sound.

### Required accounting

Treat push-to-talk intervals as supplied speech-event framing. Do not count their boundaries as learned speech segmentation.

## Attack 5 — UI pointing can still over-constrain reference without object IDs

Replacing hidden object IDs with an observable cursor/ray avoids the worst leak, but a perfectly precise ray terminating exactly on the evaluator target can still collapse reference ambiguity far more than natural pointing would.

### Required accounting

Pointing affordances should have declared geometry, precision, visibility, latency, and noise characteristics.

Grounded-reference tests should include imprecise, conflicting, occluded, or misleading attention cues so the learner cannot reduce reference to deterministic ray-object intersection.

## Attack 6 — a world viewport can privilege the operator's ontology

If Patrick interacts with simulator objects through drag handles, bounding boxes, selectable outlines, or named UI widgets, those controls may not be delivered directly to Noema, yet they can make Patrick's teaching unnaturally precise and ontology-aligned.

That can indirectly shape the learner's curriculum.

### Required accounting

Operator-side affordances that expose evaluator object segmentation should be recorded in the operator-exposure log when they can change teaching behavior.

Formal grounding evaluation should include interaction where the teacher cannot rely on evaluator-perfect object selection.

## Attack 7 — diagnostic visibility can make Patrick an external inference module

Even when diagnostic text never feeds back directly, Patrick can read the exact challenger, uncertainty, or failure mode and then construct the perfect next example.

The effective cognitive system during development becomes `Noema + diagnostic interpreter + Patrick`.

That may be useful engineering, but it is not evidence of independent Noema capability.

### Required accounting

Retain full diagnostics in development mode, but separate claims from conditions with blinded/delayed diagnostics and held-out teachers.

Measure Patrick's behavior as part of the experimental system whenever diagnostics are visible.

## Attack 8 — operator controls may be indirectly learner-visible through time

The contract says pause/checkpoint/reset controls are outside Noema by default.

But if Noema has chronoception or persistent internal clocks, pausing the host process and resuming later can create a detectable discontinuity even if no `pause` event is delivered.

Similarly, loading a checkpoint may rewind learner state while world time advances, or rewind world state while an internal clock does not.

### Required accounting

Every operator control must declare its **temporal consequence**:

- learner clock frozen with no experienced elapsed time;
- learner clock advances and gap is observable;
- world clock freezes/advances separately;
- state is restored/rewound;
- host wall-clock is excluded from cognition.

A control is not truly invisible if its consequences are learner-detectable.

## Attack 9 — replay can accidentally add or remove evidence

A logically identical replay can differ developmentally if it changes timing, buffering, event batching, random seeds, stochastic transducer output, or consolidation scheduling.

### Required accounting

Replay evidence should bind:

- learner-visible event payloads;
- learner-visible timestamps/durations;
- declared stochastic seed/state where deterministic replay is claimed;
- transducer version/configuration;
- whether host wall-clock or background processes are cognitively relevant;
- tolerance for stochastic update divergence.

"Same log" is not enough if the learner experienced a different temporal process.

## Attack 10 — correction interfaces can smuggle reward even without `wrong=true`

Patrick's correction may be ordinary communication, but the UI can still supply extra reinforcement through success animations, sounds, color changes, disabled buttons, score counters, or automatic state transitions.

### Required accounting

All learner-visible consequences of correction/approval need to be in the delivered event stream.

If the UI shows Patrick a private score that changes how he teaches, it belongs in operator exposure even if Noema cannot see it.

## Attack 11 — wrapper-generated Noema behavior can close the teaching loop externally

A UI might automatically convert uncertainty into a puzzled face, spinner, gaze aversion, or "thinking" indicator. Patrick then supplies more information in response.

Noema benefits from communicative behavior it did not learn or choose.

### Required accounting

Any automatic wrapper cue derived from diagnostics must be visually and experimentally classified as operator visualization, not agent behavior.

Formal mixed-initiative/social-learning claims must disable those cues.

## Attack 12 — convenience ASR can import pragmatic structure beyond words

ASR systems may add punctuation, sentence casing, endpointing, diarization, confidence, or normalized disfluency removal.

Even if only the transcript text is passed on, punctuation and endpointing can leak phrase/sentence boundaries and prosodic interpretation.

### Required accounting

The transducer ledger must record normalization and punctuation policy, not merely say "ASR used."

If development uses normalized transcripts, later claims should explicitly exclude the normalized structure from learned speech/prosody competence.

## Attack 13 — persistent UI session state can provide conversational continuity externally

The Console may maintain a transcript, thread ID, message order, speaker-side layout, unread markers, or conversation session boundaries.

If any of these are passed to Noema or influence event framing, they can supply continuity structure the learner would otherwise need to infer.

### Required accounting

Separate operator presentation from learner-visible conversational state.

A transcript visible to Patrick is not automatically learner memory. A stable session/thread identifier delivered to Noema is a supplied continuity prior and must be declared.

## Attack 14 — resource cost can be faked by the interface

Mixed initiative is supposed to make questions cost something. A UI that lets Noema emit unlimited queries while Patrick answers instantly may make active learning unrealistically dominant.

### Required accounting

Question/query cost should come from the same finite-resource and opportunity-cost model as other actions where practical: elapsed world time, action budget, missed alternatives, social response uncertainty, or explicit experimental cost.

Do not use a hidden evaluator penalty that Noema cannot sense while later claiming it learned the cost structure.

## Attack 15 — held-out teacher can still share the same interface dialect

A second human using the same text box, pointing ray, ASR normalization, turn framing, and correction workflow may look like a new teacher while preserving nearly every interface shortcut.

### Required accounting

Held-out-teacher evaluation should distinguish:

- new person, same interface/transducer ecology;
- new person with changed channel/device/framing where feasible;
- changed linguistic/pragmatic habits;
- changed reliability profile.

This makes clear whether transfer is across people, across interface structure, or both.

## Strongest consequence

The interface contract needs a broader notion than "semantic leakage."

The dangerous category is **developmental subsidy**:

> any stable structure supplied by the interface, transducer, evaluator, or operator workflow that reduces the inference/learning problem Noema is later claimed to have solved.

Developmental subsidies are not automatically prohibited. Some are necessary to make a tractable system.

They must be:

1. declared;
2. attributed;
3. ablated or varied when the corresponding capability is being claimed;
4. prevented from silently becoming architecture evidence.

## Candidate A implication

Candidate A's provenanced event boundary remains necessary but is not sufficient if provenance means only `observation`, `communication`, `action`, `memory`, or `simulation`.

For developmental claims, provenance should also be able to point outward to a **transducer/interface descriptor** stating what preprocessing, framing, channel partition, timing, and identity cues were supplied.

That descriptor need not become semantic input to Noema. It can remain experiment-side evidence metadata linked to the learner-visible stream.

This preserves the architecture's minimal learner boundary while making the scientific claim chain auditable.
