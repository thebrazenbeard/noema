# Online Learning State Transition Contract

Status: **SUCCESSOR WORKING DESIGN / NOT IMPLEMENTATION APPROVAL / NOT R1 REMEDIATION**

Date: 2026-09-06

Source cut at drafting: `main@20f7f699ea15b2300c4aa796b286bdab658f52a3`

Companion research: `LEARNING_AND_TRAINING_RESEARCH_SYNTHESIS.md`

Independent convergent draft retained for provenance: `ONLINE_LEARNING_STATE_TRANSITION_CONTRACT_DRAFT.md`

Reconciliation: `PR31_ONLINE_LEARNING_CONTRACT_RECONCILIATION.md`

Hostile test companion: `ONLINE_UPDATE_ORDER_HOSTILE_ATTACK.md`

## 1. Purpose

Noema cannot claim online learning merely because several components are allowed to update continuously. A persistent learner needs a causal contract for **which state is read, which prediction is scored, which evidence is available to which update, when replay is sampled, when candidate structure can learn, when any change becomes behaviorally live, and what must survive restart**.

This contract makes that order explicit without selecting a final neural architecture, optimizer, slow-memory anatomy, or structural-growth mechanism.

The core rule is:

> **A learning result must be attributable to a declared causal state transition rather than to incidental scheduler order, hidden shared mutation, retrospective rescoring, or evaluator bookkeeping.**

This is successor design. It does not alter the frozen Noema BT2 R1 subject and must not be cited as evidence that R1 passed.

## 2. Architecture level versus realization level

This document constrains any serious first-core realization at the architecture-contract level. It does **not** require:

- a particular recurrent cell;
- a PSR implementation;
- a latent state-space model;
- backpropagation;
- Adam/AdamW;
- an explicit hypothesis population;
- adapters or experts;
- a two-module fast/slow anatomy;
- a specific replay algorithm;
- a particular programming language or concurrency model.

A realization may be synchronous, asynchronous, parallel, event-driven, differentiable, or partly non-differentiable. But if execution order can change the committed learner state, that order is part of the learner's effective algorithm and must be declared, persisted where necessary, and charged in evaluation.

The default evidence discipline is **prequential/test-then-train**: a prediction must be fixed before the scored outcome is used for learner mutation.

## 3. State classes

The evaluator must maintain a state manifest that classifies every causally relevant variable into one of four planes.

### L0 — learner-committed state

State that can affect future Noema prediction, action, learning, retrieval, evidence interpretation, or internal allocation. Examples may include:

- recurrent predictive state;
- learned parameters;
- optimizer/plasticity state;
- replay contents;
- replay sampling/policy/cursor/priority state;
- uncertainty/calibration state;
- candidate structural state;
- routing/gating state;
- consolidation/probation state;
- learned skills or temporal abstractions if present;
- meta-control state;
- learner-visible interface namespace/calibration state when it changes interpretation of evidence;
- learner RNG state when stochasticity is part of the algorithm;
- learner scheduler/internal-work state when ordering is intentionally algorithmically causal;
- pending internal work whose completion may later alter committed state.

The exact decomposition is realization-specific. The obligation is causal completeness, not semantic modularity. A concrete system may store several of these together or use no named module corresponding to them.

### L1 — learner-visible evidence

Only the declared cognitive boundary may enter here, including legitimate learner-visible sensory, communication, temporal, and efference evidence. Evaluator truth, semantic labels, hidden target identity, true noise parameters, causal graph identity, exact success bits, and similar oracle information do not enter unless deliberately supplied and claim-limiting.

### E0 — evaluator/world causal state

Hidden state that legitimately affects world dynamics or transducer behavior. Changes here may later alter learner-visible evidence through declared causal paths.

### E1 — evaluator bookkeeping and diagnostics

Run IDs, scoring labels, ground-truth causal graph names, test split labels, semantic object identities, exact lineage records, debug annotations, logging order, UI diagnostics, and other bookkeeping that must not directly influence learner computation unless explicitly put into the developmental environment.

A critical distinction follows:

> **E1 mutations should be noninterfering with Noema; E0 mutations may legitimately change Noema's evidence, but only through declared world/transducer paths.**

## 4. Committed-state boundary

At any learner event boundary, there is one logically authoritative committed learner state, written `C_t`.

`C_t` is not required to be one physical blob. It is the causally complete set of L0 state whose values are authoritative before the next learner-visible event is consumed.

A realization may compute speculative/shadow work concurrently, but speculative work is not part of `C_t` until an explicit commit rule admits it.

The evaluator must be able to answer for every scored prediction or action:

1. which committed state authorized it;
2. which learner-visible evidence had been consumed by that state;
3. which parameter/optimizer/replay/candidate versions it depended on;
4. whether any speculative state was behaviorally live;
5. which commit made later changes authoritative.

This record is evaluator-side provenance; it need not be exposed semantically to Noema.

## 5. Prediction tickets

Predictions must be scored against the state that actually issued them.

A **prediction ticket** is evaluator-side accounting that binds:

- the learner-visible target/query class being predicted;
- the action/intervention conditioning legitimately available at issue time;
- the committed learner state version that issued the prediction;
- issue time in the declared experimental time basis;
- the horizon/expiry rule;
- the eventual score if/when corresponding learner-visible evidence arrives.

The ticket itself is not a learner-visible semantic object unless a realization independently requires an internal analogue.

The evaluator may know exact correspondence needed to score a ticket. That correspondence must not become a hidden learner-side event ID or causal label merely because evaluation needs it.

## 6. Canonical event transition

For an incoming learner-visible event `e_t`, the logical transition from `C_(t-1)` to `C_t` is:

### Phase A — freeze causal entry state

Capture the authoritative pre-event committed state `C_(t-1)` and the exact learner-visible event bytes/cues delivered as `e_t`.

No learner mutation caused by `e_t` is authoritative yet. No future/outcome information that was unavailable before the event may already be present in the causal state used to score the prediction.

### Phase B — score already-issued predictions before learning from `e_t`

Resolve and score every eligible prediction ticket that `e_t` can evaluate using the prediction as it existed when issued.

Scoring must not silently rerun the predictor after `e_t` has been consumed or after parameters have changed.

The immutable score/evidence record becomes available to later learning logic according to the declared learner-side feedback path. Evaluator-only metrics remain E1.

### Phase C — assimilate the learner-visible event into working predictive state

The realization may update its recurrent/working state from `e_t` so it can represent the newly observed situation.

This assimilation is distinct from learning long-lived parameters. A realization may combine them physically, but evaluation must still preserve the causal distinction: prediction quality for `e_t` came from the pre-event state, not from a state that had already ingested `e_t`.

### Phase D — form the current learning proposal

Using only information legitimately available after Phases A-C, compute the fast-learning proposal for long-lived learner state.

The proposal must name its causal inputs at the evaluator level: current event, pre-event prediction residuals/calibration evidence, relevant internal state, and any allowed replay sample.

### Phase E — sample replay from a declared replay snapshot

If replay is used, its sampling point must be explicit.

Default first-core rule:

> **Sample replay from the pre-insertion replay store for the current event.**

This prevents the just-arrived event from receiving accidental duplicate weight merely because insertion happened before sampling. A realization may intentionally choose another policy, but then that policy is part of the algorithm and must be compared under equal accounting.

The replay sample order, identities, and stochastic state must be reproducible or explicitly treated as learner stochasticity.

Replay may contain learner-side evidence/state needed to reconstruct legitimate training signals. It must not contain evaluator semantic truth unavailable when the experience originally occurred.

### Phase F — evaluate shadow/candidate repairs without contaminating the comparator

Any probationary adapter, expert, structural hypothesis, consolidation candidate, or other slow repair being compared against a base predictor must be evaluated from a declared causal snapshot.

A candidate must not improve the baseline it is being compared against through shared mutable state before its marginal value is scored.

Permitted patterns include:

- immutable/copy-on-write base snapshots;
- functionally isolated parameter/state copies;
- schedule-invariant update algebra with proof/tests that worker order cannot alter the comparator;
- another mechanism that provides equivalent causal separation.

The contract does not require physical copying if the implementation can establish equivalent isolation.

### Phase G — commit fast learner mutation

Apply the accepted fast-learning update to a new committed learner state candidate.

The commit must include every causally coupled state change required by the update, such as optimizer moments, calibration accumulators, replay-policy counters, or recurrent state persistence when those variables affect future computation.

Partial visibility of a multi-part update is not allowed to create an accidental algorithm.

### Phase H — insert/update replay state

Commit the current experience to replay according to the declared policy after the sampling point unless the chosen algorithm explicitly specifies another order.

Eviction, reservoir counters, priority statistics, and related policy state are learner state if they affect future samples.

### Phase I — consider slow consolidation/promotion at an explicit boundary

Slow consolidation or structural promotion may become behaviorally live only at a declared promotion boundary.

Promotion must use an immutable evidence window or equivalently snapshot-bound evidence. It may not retroactively change the scores that justified promotion.

The evidence window must make clear which base version and candidate version were compared. If both continue learning during probation, the comparison requires causal windows that prevent `cheaper repairs first` or candidate marginal value from becoming scheduler-dependent.

Promotion can be rejected, deferred, made dormant, or reversed later. None of those outcomes establishes semantic correctness of the candidate.

### Phase J — publish `C_t`

After all state changes admitted by this transition are causally complete, publish the new logically authoritative committed state `C_t`.

Only now may new behavior rely on changes from `e_t` unless the realization explicitly defines a finer-grained learner-visible internal timing model and persists it as part of the algorithm.

### Phase K — issue future predictions/actions

Predictions and action evaluations after the transition are bound to `C_t` (or a later declared internal-cognition commit) and receive evaluator-side provenance tickets.

Actions still cross the separate actuator-transducer contract. An action command does not gain semantic success/authorship merely because it was issued from `C_t`.

Between an issued action/prediction and a later scored event, the world/transducer progression follows the separately declared actuator -> world -> sensory-transducer path. Evaluator truth recorded along that path remains outside learner evidence unless explicitly exposed.

## 7. Internal cognition between external events

Noema may eventually think, retrieve, simulate, compare alternatives, or update internal state between external events.

Such cognition is not exempt from causal accounting. If an internal operation can alter future behavior, its output must either:

- commit through an explicit internal-cognition state transition; or
- remain speculative until a later commit.

Internal computation may consume finite learner resources and learner-visible time/opportunity cost where appropriate. Evaluator bookkeeping time must not become a hidden clock signal.

The first F1 realization may omit rich autonomous internal cognition. This contract leaves the seam explicit so later additions do not create a hidden second update path.

## 8. Concurrency rule

Parallelism is allowed. **Undeclared schedule dependence is not.**

For any two executions with the same learner-visible event/action stream, same declared learner stochastic state, and same causally relevant world/transducer state, changing only:

- worker completion order;
- logging order;
- evaluator thread scheduling;
- diagnostics refresh order;
- noncausal bookkeeping identifiers;

must not change the committed learner trajectory.

If worker completion order is intentionally allowed to affect learning, then it is learner algorithm state rather than infrastructure noise. It must be represented in the experimental contract, persisted for replay/restart claims, and tested as such.

## 9. Replay contract

Replay is not `free memory`. Its budget and contents are part of Noema's learning resources.

Every replay realization must declare:

- capacity/budget;
- insertion policy;
- eviction policy;
- sampling distribution;
- sample count per learner event or per compute unit;
- sample ordering semantics;
- whether priorities change after replay;
- RNG source/state;
- what legitimate learner-side provenance is retained;
- how nonstationarity and stale evidence are handled;
- what survives checkpoint/restart.

A replay record must not become richer than the learner's original experience through evaluator annotation.

Comparator fairness requires charging replay memory, retrieval compute, and extra optimization steps.

## 10. Fast/slow causal ownership

Fast and slow learning may modify overlapping functional behavior, but the ownership of updates must be causally closed.

Minimum requirement:

> **At each promotion/consolidation boundary, the evaluator can identify the exact pre-boundary behaviorally live state, the candidate state being considered, the evidence window used, and the single logical commit that changes which state controls future behavior.**

This directly prevents several failure modes:

- the slow learner silently training the fast baseline it is meant to beat;
- the gate learning from candidate-influenced behavior and then treating that selected evidence as independent support;
- consolidation changing the representation used by a still-running candidate without a declared scope-remapping/relearning process;
- one asynchronous worker winning merely because it commits first;
- promotion metrics being recomputed after promotion using the promoted system.

The deeper representation-drift problem remains a separate architecture frontier: learned scope must either be invariant to behavior-preserving representation change or be relearnable from ordinary evidence without an evaluator correspondence oracle.

## 11. Checkpoint/restart contract

A checkpoint supports **restart-equivalence** only if it captures every L0 variable whose omission could alter the future learner trajectory under the same future evidence.

Depending on realization, this may include:

- predictive recurrent state;
- learned parameters;
- optimizer/plasticity state;
- replay contents and replay-policy/sampler state;
- uncertainty/calibration accumulators;
- probationary candidates and their evidence windows;
- gating/routing state;
- consolidation/promotions pending or committed;
- learner-visible interface namespace/calibration state when it affects evidence interpretation;
- learner RNG state;
- learner scheduler/internal-work state if order is algorithmically causal;
- pending prediction/action accounting needed to preserve learning semantics;
- any causal transducer/actuator state only where checkpoint semantics claim to restore those environment-facing components too.

Evaluator run IDs and semantic labels are not learner state merely because the evaluator stores them.

Crash consistency matters. A checkpoint must correspond to one valid commit boundary or have a journal/transaction mechanism that lets recovery determine which transition committed. A half-fast/half-slow state is not a legitimate checkpoint unless the algorithm explicitly defines such a state.

## 12. Duplicate, delayed, reordered, and replayed external events

F1 must not assume a perfectly synchronous toy stream if the eventual runtime can receive jittered, duplicated, delayed, or replayed events.

The event boundary must declare how the learner distinguishes or tolerates:

- duplicate transport delivery;
- legitimate repeated sensory values;
- simultaneous or near-simultaneous cross-port observations;
- reordering introduced by transport rather than the world;
- delayed actuator effects;
- externally replayed observation sequences.

Transport-level deduplication may use transport metadata that terminates before cognition, but the learner must not receive a semantic event-identity oracle as a side effect.

The evaluator must distinguish `same cognitive evidence delivered twice by transport error` from `the world produced two similar observations` without leaking that distinction into learner semantics unless deliberately supplied.

## 13. Evaluator scoring versus learner learning

The evaluator may compute richer scores than Noema receives.

For example, the evaluator may know:

- exact structural world class;
- true intervention success;
- exact hidden-state trajectory;
- exact object/source identity;
- exact causal lineage;
- trial split and held-out status.

Those facts may score experiments while remaining E1/E0. They must not enter the learner's update merely because the evaluator uses them to decide whether Noema succeeded.

A learner-side loss must be reconstructible from learner-visible evidence plus declared innate machinery and learner state.

## 14. Equal-information and equal-resource comparison

When comparing realizations, hold constant or explicitly charge:

- learner-visible event stream;
- intervention/action opportunities;
- replay capacity;
- optimization steps;
- internal simulation/thinking budget;
- parameter/state capacity where practical;
- wall-clock/compute budget where relevant;
- evaluator assistance;
- transducer sophistication.

A more complex learner earns architecture status only when it beats a simpler rival under declared accounting.

The first mandatory learning comparators remain:

1. **C0** — simple incremental predictive/system-identification baseline;
2. **C1** — recurrent probabilistic predictor without replay;
3. **C2** — recurrent probabilistic predictor with bounded replay;
4. **C3a** — predictive-state/PSR-like realization under the same causal contract;
5. **C3b** — stochastic latent-state/recurrent world-model realization under the same causal contract;
6. **C4** — only after simpler rivals, scoped structural extension.

## 15. First-core realization default

Absent evidence for a more complex order, the recommended initial F1 realization uses this conservative sequence:

1. score outstanding pre-event predictions;
2. assimilate current event into recurrent working state;
3. sample replay from pre-insertion store;
4. compute one fast-learning proposal from current evidence + bounded replay;
5. atomically commit fast parameters/state/optimizer updates;
6. insert current experience into replay and update replay-policy state;
7. issue future predictions/actions from the new committed state;
8. run any slow candidate in shadow with no live behavioral influence unless and until a separate promotion boundary is earned.

This is a research default, not implementation approval.

## 16. Claim ceilings

Passing this contract can support claims such as:

- online predictive learning followed a declared causal update order;
- replay contribution was resource-accounted;
- candidate marginal value was measured without known shared-mutation contamination;
- checkpoint restored the declared learner state under tested conditions;
- committed state was invariant to tested infrastructure scheduling permutations.

It cannot by itself support:

- general intelligence;
- human-like learning;
- causal understanding;
- selfhood;
- consciousness;
- robust lifelong learning outside tested distributions;
- correctness of any learned latent ontology.

## 17. Open seams

This contract intentionally leaves unresolved:

1. PSR-like versus stochastic latent/recurrent predictive state;
2. exact uncertainty representation;
3. replay policy and capacity;
4. gradient versus non-gradient learning;
5. exact structural-growth mechanism, if any;
6. representation-drift-safe learned scope;
7. long-horizon temporal credit implementation;
8. autonomous internal cognition scheduling;
9. mature consolidation/forgetting policy;
10. motivation/valuation update mechanics.

These should be decided by falsifiable comparison, not by filling architectural boxes.

## 18. Bottom line

Noema's online learning loop should be treated as a sequence of **causally attributable state transitions**, not a bag of asynchronously updating modules.

The operative first-core principle is:

> **Score from the state that made the prediction, learn only from evidence legitimately available afterward, isolate competitors while measuring marginal value, and make every behaviorally live mutation pass through a declared commit boundary.**
