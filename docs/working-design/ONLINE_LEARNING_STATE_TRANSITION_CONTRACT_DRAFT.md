# Online Learning State-Transition Contract — Research Draft

Status: **WORKING DESIGN / RESEARCH SYNTHESIS / NOT APPROVED IMPLEMENTATION**  
Branch subject: PR #31 successor research lane  
Base architecture: `main@20f7f699ea15b2300c4aa796b286bdab658f52a3`  
Purpose: turn the vague phrase “Noema learns continuously from experience” into a falsifiable causal contract without prematurely choosing a specific optimizer, neural architecture, replay implementation, or slow-structure mechanism.

## 1. Why this contract is needed

BT2 qualification findings exposed a real ambiguity: a mutable online learner can produce materially different evidence depending on when prediction, scoring, base updates, replay, candidate updates, routing changes, and checkpointing occur. “Use the same experience” is not enough if the compared learners have already diverged internally.

Streaming-learning research strongly favors **prequential / interleaved test-then-train** evaluation for adaptive systems: each incoming outcome is evaluated against a prediction made before that outcome is used for learning. This prevents the learner from receiving credit for information it had already consumed. Continual-learning research also shows that replay can materially reduce catastrophic forgetting, but replay policy, optimizer state, and update ordering become part of the learner’s causal history and therefore cannot be treated as neutral plumbing.

This document proposes the narrow architecture-level responsibility. It does **not** freeze a realization.

## 2. Architecture-level invariant

For every learner-visible transition used as evidence of predictive learning:

> **prediction is committed before the scored outcome becomes available; scoring occurs before any outcome-dependent learner mutation; all compared candidates are scored from explicitly declared pre-outcome state; every subsequent mutation is causally ordered, resource-accounted, and checkpointable according to its claimed persistence scope.**

This is stronger than “online learning” and weaker than choosing SGD, Adam, RTRL, replay type, PSR, latent SSM, adapter architecture, or another concrete mechanism.

## 3. Minimal state classes

The runtime must be able to distinguish these state classes even if a concrete realization stores them jointly:

### A. Predictive/behavioral learner state

State that can affect the next learner prediction or action, including recurrent/working state and learned parameters.

### B. Plasticity state

State that affects how future learning updates occur, including optimizer moments, eligibility-like traces, adaptive learning-rate state, local plasticity statistics, or equivalent hidden update state.

### C. Replay/history state

The bounded learner-accessible replay store or compressed-history mechanism, plus its sampling/index/cursor state where those can affect future updates.

### D. Probationary/slow candidate state

Any optional shadow candidate, gate, adapter, structural fragment, recruitment counter, evidence ledger, dormancy/reactivation state, or slow consolidation state.

### E. Learner-visible interface calibration state

Low-level port-map version, declared temporal calibration, transducer calibration learned or supplied to the learner, and any other interface state that can change interpretation of learner-visible evidence.

### F. Stochastic execution state

RNG/sampler state or equivalent stochastic frontier when reproducible continuation is claimed.

Evaluator-only truth remains outside these learner state classes.

## 4. One causal learning cycle

The following sequence is the proposed architecture-level causal order. Implementations may pipeline work internally only if they are observationally equivalent to this order.

### Phase 0 — boundary closure

All learner-affecting mutations from the previous cycle are complete or have a declared serialized frontier. The learner is at state `L_t`.

No future/outcome information from cycle `t+1` may already be present in `L_t`.

### Phase 1 — pre-outcome snapshot / causal frontier

Declare the exact learner state from which scored predictions will be made:

`F_t = snapshot_or_equivalent(L_t)`

This need not imply an expensive physical copy. It requires an equivalent causal read frontier.

For probationary comparisons, the base and all compared shadow candidates must identify the state they read at this frontier.

### Phase 2 — prediction and optional action commitment

Using only evidence available at `F_t`, commit:

- prediction(s) over reachable learner-visible future evidence;
- uncertainty/calibration outputs required by the experiment;
- action-conditioned predictions where actions are under consideration;
- the selected action, when this cycle contains an intervention.

Committed predictions become immutable evaluator records for this cycle.

No outcome-dependent learner update is allowed yet.

### Phase 3 — world/transducer progression

The selected learner action, if any, is sent through the declared actuator boundary. The environment evolves. Learner-visible evidence returns through the declared sensory/communication boundary.

Evaluator truth may be recorded separately but must not enter the learner except through deliberately exposed evidence.

### Phase 4 — score before train

The evaluator scores the committed prediction(s) against the newly available learner-visible outcome.

This is prequential: the outcome is evidence **for evaluation before it is evidence for learning**.

Base and probationary candidate scores for a comparison window must be computed from predictions committed before either learner consumed the outcome.

### Phase 5 — current-experience fast update

Only after Phase 4 may the learner update from the current experience.

The realization must define which state this mutates:

- recurrent/working state;
- fast predictive parameters;
- uncertainty/calibration state;
- plasticity/optimizer state;
- action/efference-conditioned state.

The update rule itself remains L4 unless evidence promotes a narrower requirement.

### Phase 6 — bounded replay / rehearsal

Replay may occur only from evidence that was already learner-available before the current scored outcome, unless the experiment explicitly permits the current experience to enter the replay set after its first fast update.

Default comparison discipline for early Noema experiments:

1. take replay sample from the **pre-current insertion** buffer state;
2. apply the current-experience update;
3. apply a bounded replay budget;
4. insert/refresh the current experience only after its first scored use, according to declared buffer policy.

This prevents one event from receiving hidden multiple-use advantage in the same prediction/score cycle and makes compute accounting simpler.

Replay policy is a candidate mechanism, not architecture canon. A no-replay baseline remains mandatory.

### Phase 7 — slow/probationary learning and consolidation

Optional slower mechanisms may update only after the cycle’s scored evidence exists.

For shadow candidates:

- learning exposure and behavioral influence remain separate;
- the candidate may update on its declared audition evidence;
- its current cycle score cannot be retroactively altered;
- promotion/routing changes take effect only at a later causal frontier;
- candidate-specific compute, memory, replay, shadow forwards, and audit sampling are charged to its resource ledger.

“Cheaper repairs first” cannot be inferred merely from wall-clock ordering. A realization must provide either auditable causal windows or intervention/ablation evidence that identifies which repair path earned a claimed improvement.

### Phase 8 — state commit / next frontier

All learner-affecting updates that are part of this cycle are serialized into `L_(t+1)` or a declared equivalent frontier.

The next scored prediction begins only from this committed frontier.

## 5. Scheduling freedom and equivalence

The contract does not require a single-threaded implementation. It requires **serializable causal semantics**.

A lawful parallel/pipelined implementation must show that changing thread scheduling, kernel scheduling, or benign internal interleaving while preserving the declared causal precedence does not materially change:

- committed predictions;
- score attribution;
- candidate promotion decisions;
- replay membership/sampling semantics;
- checkpoint continuation claims;

outside preregistered numerical/stochastic tolerance.

If scheduling changes those results, scheduling is part of the cognitive/learning mechanism and must be declared rather than hidden as implementation detail.

## 6. Checkpoint and restart contract

A “full learner checkpoint” must contain every state element whose omission can change the claimed continuation trajectory. At minimum the manifest must explicitly decide inclusion/exclusion for:

- predictive model parameters;
- recurrent/working state;
- optimizer/plasticity state;
- uncertainty/calibration state;
- replay buffer or compressed memory state;
- replay sampler/cursor/priorities;
- RNG state where stochastic updates matter;
- slow/probationary candidate parameters;
- gate/routing state;
- probation/promotion/dormancy counters;
- proposal/recruitment controller state;
- provenance statistics used to discount self-selected evidence;
- port-map/interface namespace version;
- learner-visible temporal calibration state.

A partial checkpoint may omit some classes, but then the expected behavioral/learning discontinuity must be declared and tested.

“Same weights” is not enough to claim same continuing learner when omitted optimizer, replay, recurrent, or routing state changes subsequent learning.

## 7. Required hostile tests

### OLT-0 — test-then-train integrity

Replace the scored outcome after prediction commitment but before learner update. The committed prediction must remain unchanged.

### OLT-1 — no-lookahead mutation

Instrument all learner-affecting writes. No write dependent on the scored outcome may occur before the score record is fixed.

### OLT-2 — schedule permutation

Run equivalent cycles under multiple internal legal schedules. Promotion scores and learner outputs must remain within declared tolerance.

### OLT-3 — base/candidate common-frontier test

A probationary candidate and its base comparator must produce their scored predictions from the same declared pre-outcome evidence frontier. If one receives an earlier outcome-dependent update, the comparison is invalid.

### OLT-4 — replay accounting

Charge replay sampling, forward passes, backward/update work, memory, and candidate-only shadow computation. A candidate advantage that disappears after equalized resource accounting does not support architectural promotion.

### OLT-5 — current-sample multiplicity

Verify whether the just-scored event can be used zero, one, or multiple additional times during the cycle. The policy must be explicit and identical across compared candidates unless the difference itself is the treatment.

### OLT-6 — full restart equivalence

Checkpoint at a cycle boundary, resume, and compare the continuation against an uninterrupted run under deterministic mode. Exact equality is preferred where feasible; otherwise preregister bounded stochastic equivalence.

### OLT-7 — partial restart characterization

Intentionally omit optimizer, replay, recurrent, gate, or RNG state one class at a time. Measure the induced divergence. This identifies which state is causally part of claimed persistence.

### OLT-8 — port/remap lifecycle

Remap opaque port tokens across an allowed world/interface reset. Generic learned competence may transfer; hidden semantic meaning tied to globally stable token identity must not.

### OLT-9 — replay/no-replay baseline

A simpler fast recurrent learner with no replay must remain a lawful comparator. Replay is retained only if it earns better retention, transfer, calibration, sample efficiency, or resource-adjusted performance.

### OLT-10 — slow-structure necessity

A fast recurrent + bounded replay learner must remain a lawful architecture. Adapters/fragments/experts are promoted only if they beat this simpler rival on preregistered evidence.

## 8. Research implications for Noema

### Prequential evaluation should become the default evidence discipline

Streaming-learning literature repeatedly uses prequential/interleaved test-then-train evaluation because it preserves the chronological distinction between prediction and learning. This directly matches Noema’s requirement that prediction error be evidence rather than a post-hoc reconstruction.

### Replay is a strong baseline, not architecture truth

Experience replay, compressed replay, and rehearsal repeatedly reduce catastrophic forgetting in continual and online learning. However, replay introduces memory, sampling, compute, provenance, and update-order responsibilities. It therefore belongs as a strong L4 baseline whose cost is fully charged.

### Fast/slow consolidation is plausible but not yet mandatory anatomy

Continual-learning and neuroscience-inspired work supports separating rapid adaptation from slower retention/consolidation, but the evidence does not justify hardcoding a particular dual-network or explicit structural adapter system into Noema’s architecture. The architectural requirement is multi-timescale plasticity with measurable stability/plasticity behavior.

### Optimizer state is part of learning history when it changes future updates

Adaptive optimizers maintain state derived from prior gradients. Research showing that optimizer-state resets can materially change RL performance demonstrates that optimizer state is not neutral when continuation claims depend on it. Full-state persistence must therefore account for it or explicitly disclaim exact continuation.

### Exact online recurrent gradients are a comparator, not an obligation

Real-Time Recurrent Learning offers a mathematically clean per-step recurrent update paradigm but is computationally expensive. It is useful as a conceptual comparator for what “truly online” means, not as a current Noema architectural commitment.

## 9. Candidate comparison frame after this contract

Once the causal cycle is frozen for an experiment, candidate learning substrates can be compared without changing the evidence semantics around them.

Recommended first comparison family:

- **C0:** simple bounded recurrent probabilistic predictor, no replay;
- **C1:** same family with bounded replay;
- **C2:** predictive-state / PSR-like realization with bounded replay;
- **C3:** stochastic recurrent latent state-space realization with bounded replay;
- **C4:** only if earned later, scoped slow structural/adaptive capacity.

All receive the same learner-visible stream, action opportunities, prequential scoring, causal update order, and resource accounting.

This ordering makes it possible for the simplest learner to win.

## 10. What remains unresolved

This contract intentionally does not decide:

- exact state representation;
- optimizer or local learning rule;
- replay buffer representation and sampling policy;
- whether replay uses raw, compressed, or generative experience;
- gradient versus gradient-free updates;
- exact consolidation frequency;
- whether slow structural capacity is needed at all;
- planning algorithm;
- intrinsic-motivation objective.

Those are experiments after the causal evidence boundary is stable.

## 11. Research basis consulted

Representative literature consulted in the research pass includes:

- Vinagre, Jorge & Gama (2015), *Evaluation of recommender systems in streaming environments* — prequential evaluation for streaming adaptive systems.
- Bornschein, Li & Hutter (2022/2023), *Sequential Learning of Neural Networks for Prequential MDL* — sequential prediction, rehearsal/replay streams, calibration.
- Parisi & Lomonaco (2020/2022), *Online Continual Learning on Sequences* — replay, regularization, structural plasticity; replay generally strong in online incremental settings.
- Hayes, Cahill & Kanan (2019), *Memory Efficient Experience Replay for Streaming Learning* — rehearsal and memory-efficient streaming replay.
- Rolnick et al. (2019), *Experience Replay for Continual Learning* — replay as a comparatively simple continual-RL stability mechanism.
- Hayes et al. (2020), *REMIND Your Neural Network to Prevent Catastrophic Forgetting* — compressed latent replay in online learning.
- Lam, Sirignano & Spiliopoulos (2025), *Convergence Analysis of Real-time Recurrent Learning* — per-step recurrent learning with exact forward derivative propagation, at high computational cost.
- Nagarajan, Warnell & Stone (2018), *Deterministic Implementations for Reproducibility in Deep Reinforcement Learning* — training nondeterminism can materially alter results.
- Asadi, Fakoor & Sabach (2023), *Resetting the Optimizer in Deep RL: An Empirical Study* — optimizer internal state can materially affect learning behavior.

These papers provide pressure and comparator evidence; none is treated as proof that Noema should copy a specific architecture.

---

**Working conclusion:** freeze the causal learning cycle before choosing the learning algorithm. A Noema experiment is not interpretable if prediction, scoring, replay, candidate comparison, and persistence can change meaning with implementation scheduling.
