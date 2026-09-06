# Noema timebase and chronoception contract

Status: **BRAINSTORMING / PROVISIONAL DEVELOPMENTAL-EVIDENCE CONTRACT / NOT IMPLEMENTED**

Date: 2026-09-06

## Purpose

Noema's existing design treats chronoception as an innate-access signal family and the developmental interface contract currently allows a monotonic learner-visible clock or equivalent timing representation.

This document tightens that boundary.

The central correction is:

> **Innate access to temporal structure does not imply access to an exact global wall clock.**

A perfectly precise absolute timestamp can silently solve parts of event ordering, action-outcome matching, regime detection, cross-modal binding, recurrence estimation, curriculum-phase identification, and delayed-credit assignment. If those capabilities are later credited to Noema, the timebase has become a developmental subsidy.

The goal is not to deprive Noema of time. The goal is to distinguish:

- evaluator-exact experiment time;
- transducer delivery time;
- learner-visible temporal cues;
- Noema's learned estimates of duration/order/synchrony;
- semantic temporal concepts learned later.

## 1. Why this matters

Time enters nearly every Noema subsystem:

- predictive state;
- action/efference and sensed consequences;
- event segmentation;
- episodic memory;
- temporal abstraction and skill learning;
- delayed credit;
- communication turn structure;
- active inquiry;
- temporary cognitive-mode decay;
- checkpoint/restore;
- source and agency attribution;
- regime-change detection.

A single exact global timestamp can become an unintended common answer key across all of them.

Example failure:

1. the evaluator changes the environment every exactly 10,000 ticks;
2. Noema receives an exact monotonically increasing tick counter;
3. Noema learns `tick mod 10000` as a regime predictor;
4. evaluation credits it with detecting contextual change from experience.

The behavior may be adaptive while the developmental claim is false or overstated.

## 2. Research pressure

The external evidence does not establish one correct artificial timing mechanism. It does establish that biological timing is not well-described as universal access to one perfect absolute timestamp.

Relevant findings include:

- humans and other animals estimate intervals without external clocks, but estimates are variable and uncertainty-bearing;
- multiple timing processes or context-dependent temporal representations can coexist;
- perceived duration varies with modality, temporal context, attention, and stimulus properties;
- audiovisual and sensorimotor temporal judgments recalibrate after repeated asynchrony;
- perceived action-feedback synchrony and agency can shift after delay adaptation;
- event boundaries can emerge from prediction error, prediction uncertainty, learned temporal structure, contextual stability, and working-memory dynamics rather than one universal explicit boundary signal.

Representative sources:

- Allman, Teki, Griffiths & Meck, *Properties of the Internal Clock: First- and Second-Order Principles of Subjective Time* (Annual Review of Psychology, 2014), DOI `10.1146/annurev-psych-010213-115117`.
- Buhusi & Meck, *Relativity Theory and Time Perception: Single or Multiple Clocks?* (PLOS ONE, 2009), DOI `10.1371/journal.pone.0006268`.
- Hanson, Heron & Whitaker, *Recalibration of perceived time across sensory modalities* (Experimental Brain Research, 2008), DOI `10.1007/s00221-008-1282-3`.
- Heron, Hanson & Whitaker, *Effect before cause: supramodal recalibration of sensorimotor timing* (PLOS ONE, 2009), DOI `10.1371/journal.pone.0007681`.
- Arikan, Yarrow & Fiehler, *Recalibration of perceived agency transfers across modalities* (Royal Society Open Science, 2025), DOI `10.1098/rsos.231962`.
- Nolden et al., *Prediction error and event segmentation in episodic memory* (Neuroscience & Biobehavioral Reviews, 2024), DOI `10.1016/j.neubiorev.2024.105533`.
- Güler, Serin & Günseli, *Prediction error is out of context: The dominance of contextual stability in structuring episodic memories* (Psychonomic Bulletin & Review, 2025), DOI `10.3758/s13423-025-02723-4`.
- Ezzyat & Clements, *Neural activity differentiates novel and learned event boundaries* (Journal of Neuroscience, 2024), DOI `10.1523/jneurosci.2246-23.2024`.

These sources are used as pressure on the design, not as a blueprint for copying human timing anatomy.

## 3. Five temporal planes

Formal experiments should distinguish five temporal planes.

### Plane T0 — evaluator time

Exact experiment-side ground truth:

- host monotonic time;
- simulator time;
- event-generation time;
- operation start/end;
- checkpoint time;
- true intervention schedule;
- true communication/transducer latency.

T0 exists for audit and scoring.

It is not automatically learner-visible.

### Plane T1 — transducer/interface timing

What the external pipeline does before a learner-visible event exists:

- sensor sampling frequency;
- buffering;
- batching;
- ASR endpointing;
- renderer frame rate;
- input-device polling;
- network delay;
- jitter correction;
- timestamp quantization;
- synchronization policy.

T1 may alter the temporal problem even when event content is unchanged.

### Plane T2 — learner-visible temporal cues

The temporal information Noema actually receives.

Possible examples:

- event order;
- local elapsed-time signal;
- an endogenous monotonic accumulator;
- interval since an issued action;
- periodic oscillatory/time-basis signals;
- event onset/duration estimates from a declared transducer;
- queue arrival order;
- coarse timestamp bins.

T2 must be explicitly declared.

### Plane T3 — learned temporal inference

Noema's fallible learned beliefs about:

- simultaneity;
- duration;
- sequence;
- recurrence;
- action-feedback delay;
- event boundaries;
- temporal context;
- process persistence;
- likely future timing.

T3 may be wrong and recalibrated.

### Plane T4 — learned temporal concepts

Later semantic/abstract concepts such as:

- `before` / `after`;
- `soon`;
- `yesterday`;
- `same time`;
- `episode`;
- `deadline`;
- `for a long time`;
- `this keeps happening every morning`.

T4 must not be confused with the lower-level temporal signals that made those concepts learnable.

## 4. Chronoception as an innate capability

Noema may retain the design decision that chronoception is available from birth.

But the architectural commitment should be weak:

> Noema receives enough endogenous temporal structure to learn order, duration, contingency, persistence, and recurrence from experience.

This does **not** require:

- UTC or wall-clock time;
- exact simulator tick number;
- perfect duration measurement;
- globally synchronized modality timestamps;
- semantic `before/after` labels;
- evaluator-defined event boundaries;
- exact age/developmental-phase counters;
- a single universal clock representation.

A precise clock may still be used in some engineering experiments. If used, it is a supplied capability and the capability claim must narrow accordingly.

## 5. Exact time can be a developmental subsidy

An exact common timebase can simplify several learning problems.

### Cross-modal binding subsidy

If visual and auditory streams carry perfectly synchronized global timestamps, Noema can bind events by timestamp equality rather than learning latency distributions and temporal contingency.

### Agency subsidy

If action issuance and consequences share exact timestamps and low deterministic latency, action-feedback matching becomes easier than in a world with variable delay.

### Event segmentation subsidy

If message, scene, task, or scenario boundaries reset a clock or align with special tick values, segmentation can be inferred from infrastructure regularity.

### Regime-detection subsidy

If curriculum phases or environment switches occur on a fixed schedule visible through time, Noema can predict hidden regime from age/tick rather than evidence.

### Delayed-credit subsidy

Exact timestamps make temporal proximity trivial to recover and can encourage chronology-as-credit if the benchmark is not designed carefully.

### Memory-index subsidy

Perfect absolute timestamps can become globally unique episode identifiers, making retrieval and continuity easier than the architecture is supposed to learn.

These subsidies are not automatically forbidden. They must be declared and ablated when corresponding capabilities are claimed.

## 6. No single privileged simultaneity bit

The interface should not provide `simultaneous=true` merely because evaluator timestamps fall within a designer threshold.

Noema may receive the underlying cues necessary to learn synchrony:

- local timing signals;
- action issuance trace;
- sensor arrival timing;
- modality-specific onset cues;
- repeated contingency.

The learner's synchrony estimate should remain revisable when modality/transducer delays change.

## 7. Cross-modal latency model

Every formal multimodal run should declare at least:

- sampling rate per modality;
- nominal latency;
- latency variance/jitter;
- buffering window;
- batching/frame interval;
- clock domain used by the transducer;
- timestamp resolution exposed to Noema, if any;
- whether timestamps are generated at physical event time, transducer sampling time, processing completion, or learner delivery time;
- synchronization/reconciliation logic.

If the pipeline retroactively corrects timestamps to evaluator ground truth, that correction is a supplied temporal prior.

## 8. Action-time and consequence-time separation

Candidate A correctly distinguishes action issuance from later sensed action consequence.

The time contract strengthens this:

- Noema may receive an efference/action-origin signal at issuance;
- consequences arrive through ordinary sensing later;
- delay may be noisy, modality-dependent, or context-dependent;
- the learner may estimate the action-consequence delay incorrectly;
- repeated delay adaptation may change its predictions;
- a later sensory event is not semantically marked `caused_by_action` merely because the evaluator knows the causal relation.

This links the timebase contract to the origin-evidence/provenance correction.

## 9. Curriculum and developmental age

Developmental phase is evaluator knowledge unless deliberately exposed.

Dangerous examples:

- `age=stage_4`;
- a reset clock at curriculum transitions;
- exact fixed-length phases visible to the learner;
- every new capability test beginning at tick zero;
- environment difficulty increasing on a perfectly periodic schedule.

Formal claims should include at least one condition where the timing of regime/curriculum changes is irregular or decoupled from a learner-visible absolute age signal.

## 10. Replay and checkpoint consequences

Replay fidelity requires more than preserving evaluator timestamps.

A replay should specify:

- whether T2 learner-visible timing is reproduced exactly;
- whether host wall-clock delays matter to cognition;
- whether background consolidation continues during pause;
- whether internal temporal state is checkpointed;
- whether a restore resumes local elapsed-time state or creates a detectable discontinuity;
- whether world time and learner time both rewind, both advance, or diverge.

A checkpoint operation is not invisible merely because no explicit `checkpoint` event is delivered.

## 11. Resource allocation and subjective time

Finite-resource cognition introduces another possible confound.

If internal deliberation consumes wall-clock/world time, Noema can learn opportunity cost through ordinary consequences.

If the simulator freezes while Noema thinks, then cognition may be effectively free in world-time terms unless another resource cost exists.

Both are legitimate experimental regimes, but they test different systems.

The experiment ledger must declare whether:

- world time advances during internal cognition;
- sensory input accumulates while cognition is busy;
- action deadlines can be missed;
- memory/consolidation runs asynchronously;
- meta-cognitive operations have learner-visible duration/cost.

## 12. Timebase falsification sequence

### TB0 — clock leakage audit

Inspect every learner-visible field and interface operation for exact evaluator time, hidden phase counters, scenario-reset ticks, or semantic temporal labels.

Kill condition: a supposedly learned temporal capability is directly answered by an undeclared time field.

### TB1 — timestamp resolution ablation

Train/evaluate equivalent learners with:

1. exact/high-resolution timestamps;
2. coarse/quantized timing;
3. order plus local elapsed-time cues but no global timestamp.

Measure which claimed capabilities depend on precision.

### TB2 — clock-origin perturbation

Change timestamp offset, scale, and origin while preserving physical temporal relations.

Pass requires competence to survive transformations that should be semantically irrelevant.

Fail if absolute tick identity itself becomes ontology.

### TB3 — cross-modal latency reversal

Train one modality pair with a stable latency ordering, then reverse or alter the delays.

Pass requires recalibration from evidence rather than permanent timestamp/channel preference.

### TB4 — exact-synchrony removal

Introduce jitter and asynchronous sampling while preserving useful causal/contingent relationships.

Pass requires degraded but recoverable binding proportional to evidence quality rather than collapse or a hidden synchrony oracle.

### TB5 — irregular regime schedule

Break any fixed relation between learner-visible age/time and environment regime.

Pass requires regime detection from actual predictive evidence.

This directly complements the adequacy-without-oracle attack.

### TB6 — temporal-proximity trap

Create delayed outcomes where the nearest prior action is not the influential action and a more distant action is.

Pass requires credit beyond simple timestamp proximity.

### TB7 — replay temporal fidelity

Replay the same learner-visible content under controlled changes to timing and verify whether behavior changes only where the changed temporal evidence warrants it.

Fail if evaluator believes the run is "the same" while learner-visible timing has materially changed without attribution.

### TB8 — multi-timescale interruption

Create concurrent short, medium, and long temporal dependencies. Interrupt one timescale without changing the others.

Pass requires behavior compatible with multiple temporal contexts or an equally capable alternative representation rather than one brittle global countdown assumption.

### TB9 — cognitive-time opportunity cost

Compare environments where thinking consumes world time versus where it does not.

Pass requires meta-control to adapt to the actual cost regime rather than rely on an unchanging hidden assumption that cognition is free or expensive.

## 13. Claim ceiling

Passing this contract supports claims such as:

> Noema learns useful temporal contingencies and duration/order structure under the tested learner-visible timing regime without relying on identified hidden evaluator clocks or fixed schedule shortcuts.

It does not establish:

- human-like subjective time;
- one correct neural timing mechanism;
- phenomenological experience of time;
- learned temporal abstraction in general;
- correct causal attribution merely from temporal competence;
- that exact timestamps are forbidden in every future interface.

## 14. Effect on Candidate A

Classification: **L2 developmental-subsidy strengthening + first-core F0/F1 evaluation refinement, not a Candidate A break.**

Candidate A's broad requirement for temporal structure survives.

However, wording that implies one exact monotonic learner-visible clock should remain optional rather than architectural. The stronger architecture requirement is:

> The learner receives a declared temporal signal basis sufficient for online temporal learning, while evaluator-exact timing and transducer timing remain separately auditable and are not silently promoted into learner semantics.

This keeps chronoception innate without pretending that a perfect clock is neutral.

## 15. Cross-lane implications

### Origin evidence / provenance

Temporal provenance should obey the same evaluator-versus-learner separation as source provenance.

### Adequacy without oracle

A visible exact developmental schedule can become a regime oracle. Adequacy/regime tests should randomize or withhold schedule information when regime discovery is being claimed.

### Continuity / state transfer

Evaluator exact lineage time may be recorded, but copied/restored learners need not receive semantic age or branch-time labels unless explicitly supplied.

### Interface

The Console may display exact wall-clock and experiment time to Patrick while Noema receives a different declared temporal basis.

### Delayed credit

Time can support credit assignment but cannot substitute for influence evidence.

## Verdict

Noema should have temporal access from birth, but **time itself must obey the same anti-oracle discipline as source, adequacy, identity, and event structure**.

The evaluator may know exact time. The transducer may use exact time internally. Noema should receive only the temporal structure deliberately chosen as part of its developmental contract, and later claims must be bounded by what that temporal structure already solved.