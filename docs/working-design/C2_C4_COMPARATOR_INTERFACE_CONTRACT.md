# C2 / C4 Comparator Interface Contract

Classification: **IP_CONFIDENTIAL**

Status: **SUCCESSOR WORKING DESIGN / IMPLEMENTATION-FACING CONTRACT / NO IMPLEMENTATION AUTHORIZED / NOT BT2 R1 REMEDIATION**

Date: 2026-09-13

Depends on:
- `ONLINE_LEARNING_STATE_TRANSITION_CONTRACT.md`
- `MINIMAL_STRUCTURAL_VALUE_FALSIFICATION_FAMILY.md`
- `EXPERIMENT_SCOPE_SUPPORT_AND_AUDITION_LEDGER.md`
- `EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V2.json`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_CONTRACT_V2.md`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_SOURCE_BINDING_ADDENDUM.md`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_RESOURCE_ADDENDUM.md`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_DECIDABILITY_ADDENDUM.md`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_COMPARATOR_MATRIX_ADDENDUM.md`
- `C0_C4_FAIR_COMPARISON_AND_CLAIM_BOUNDARY_MATRIX.md`

## 1. Purpose

The structural-value falsifier is only meaningful if C2 and C4 can be compared without implementation-specific bookkeeping changing the evidence, opportunity, update order, or resource accounting.

This contract defines the minimum externally observable interface obligations for future C2 and C4 realizations.

It does **not** prescribe:

- programming language;
- neural/recurrent cell type;
- optimizer;
- tensor layout;
- process/thread model;
- storage engine;
- explicit graph structure;
- a particular gate model;
- a particular replay algorithm.

The contract is about causal comparability and auditability.

## 2. Roles

### C2

C2 is the primary simpler rival:

> recurrent probabilistic online predictor + bounded replay.

C2 must be strong enough that C4 cannot win merely by being compared with an intentionally weak baseline.

### C4

C4 contains a comparable declared base substrate plus bounded structural candidate machinery and, where under test, learned scope/routing.

C4's structural layer earns itself only through measured marginal value after its additional costs are charged.

## 3. Shared learner-visible event interface

C2 and C4 must consume the same logical learner-visible event envelope for primary matched comparisons.

The envelope may contain only fields authorized by the frozen learner-visible schema.

At minimum the interface must distinguish, without semantic task labels:

- opaque channel/source address in the authorized learner namespace;
- payload/value data;
- learner-visible timing information;
- learner-visible reliability/provenance cues if admitted by the interface contract;
- ordinary action/efference packets when Experiment A supplies them;
- ordinary realized sensory consequences when they later arrive.

The event interface must not contain evaluator-only:

- hidden family identity;
- causal orientation label;
- task/regime ID;
- expected answer;
- applicability label;
- final score;
- future split membership;
- exact physical intervention-success truth unless that truth is independently learner-observable through the normal boundary.

## 4. Committed-state handle

Every externally scored operation must bind to an immutable logical committed-state handle.

The handle need not expose internal memory. It must identify the causally complete learner state used for the operation.

Required evaluator-visible metadata:

- `candidate_id`;
- committed state version;
- representation version;
- learner-visible event frontier consumed;
- replay-policy version;
- scope-policy version if applicable;
- learner RNG state/version or immutable reference where stochasticity is algorithmically causal.

The handle is evaluator provenance and is not automatically learner-visible.

## 5. Prediction interface

Before the scored outcome is available, C2 and C4 must be able to emit a prediction envelope bound to the current committed state.

The prediction envelope must provide enough machine-readable information to score the frozen proper scoring rule without re-running the predictor after outcome visibility.

Required properties:

- prediction/query class;
- conditioning evidence legitimately available at issue time;
- prediction distribution or sufficient parameters for the frozen scoring rule;
- horizon/expiry;
- committed-state handle;
- issue position in the experiment time basis;
- candidate/base role of the prediction;
- immutable prediction-ticket reference.

Human-readable semantic labels are not required.

## 6. C4 dual prediction requirement

Where the C4 realization can lawfully isolate its base predictor, C4 must expose two pre-outcome predictions from the same committed causal frontier:

1. **combined** — prediction with currently admitted structural influence;
2. **base-shadow** — prediction from the causally isolated base path without the current structural influence being scored.

The base-shadow path must not silently mutate the live base.

This internal marginal diagnostic does not replace independent C2.

If a C4 realization cannot produce a causally isolated base-shadow prediction, it must declare that limitation before results and forfeit the internal marginal-influence claim. It may still participate in the external C2-versus-C4 comparison.

## 7. Snapshot isolation

A structural candidate under audition or probation must not improve or damage the base comparator before marginal evidence is recorded.

Acceptable isolation mechanisms include:

- immutable base snapshot;
- copy-on-write state;
- separate functionally isolated state;
- schedule-invariant algebra with a verification argument;
- another mechanism that proves equivalent causal separation.

Unacceptable pattern:

> candidate updates shared base parameters, then the evaluator compares the candidate against that already-contaminated base and calls the difference marginal value.

That comparison is invalid.

## 8. Event transition interface

For each learner-visible event, the implementation must expose enough phase provenance to reconstruct the state-transition contract.

The implementation may physically fuse phases, but the evaluator must recover the logical order:

1. freeze pre-event committed state;
2. resolve already-issued prediction tickets;
3. assimilate current learner-visible event;
4. form current learning proposal;
5. sample replay from the declared replay snapshot;
6. evaluate shadow/candidate repairs from the declared snapshot;
7. commit fast learner mutation;
8. update replay state under the frozen order;
9. consider structural promotion/retirement at a declared boundary;
10. publish the new committed state;
11. issue future prediction/action tickets.

An implementation whose result changes because hidden scheduler order changes this logical sequence has not satisfied the comparator contract unless scheduler order is explicitly part of learner state and the experiment subject.

## 9. Replay interface

C2 and C4 replay paths must expose equivalent audit fields.

For each replay selection:

- source experience reference;
- original learner-visible evidence binding;
- replay policy/version;
- pre-sampling replay-store version;
- selection probability if stochastic;
- priority source/provenance;
- replay count for the source experience;
- compute charge;
- insertion/eviction state transition.

Replay data must contain only information lawfully available to the learner under the frozen information condition.

Post-hoc evaluator labels cannot be appended to C4 replay while C2 replays only original experience.

## 10. Resource-meter interface

Every C2/C4 implementation subject must expose counters or measurement hooks sufficient to populate the frozen resource ledger.

Required resource classes include:

- resident learner state;
- durable learner state;
- update compute;
- predictive-query compute;
- replay storage;
- replay compute;
- structural candidate state;
- structural proposal/search compute;
- scope/gate inference compute;
- policy-decoupled audition compute;
- probation/consolidation state;
- checkpoint size/time;
- restart-to-ready time.

A realization may report additional resources.

Consumed but unmeasured cost cannot be treated as zero.

## 11. Structural candidate interface

C4 must expose evaluator-side provenance for each provisional candidate without requiring a human semantic label for what the candidate means.

Required fields:

- opaque candidate handle;
- parent/base committed-state version;
- representation version;
- candidate birth boundary;
- proposal mechanism/version;
- candidate-local state/resource charge;
- audition status;
- live-influence status;
- support interval/reference;
- promotion/retirement/dormancy state;
- evidence-window binding for any promotion decision.

The evaluator may attach a separate diagnostic interpretation after the fact, but that interpretation is E1 and cannot become candidate input.

## 12. Scope interface

When learned scope is under test, every C4 influence decision must emit a pre-outcome scope ticket.

Required ticket fields:

- candidate handle/version;
- base state version;
- representation version;
- learner-visible evidence frontier;
- gate/scope policy version;
- applicability score/distribution in the realization's own lawful output space;
- influence decision;
- audition decision;
- selection probability or deterministic selection rule;
- support class;
- resource charge;
- issue time/boundary.

The ticket must exist before the outcome used to judge the decision.

No ticket may contain the evaluator's semantic answer to `was this candidate applicable?` as a learner-side target.

## 13. Simple audition rival interface

The same C4 candidate machinery must support a comparator mode in which learned scope is replaced by the frozen simpler bounded-audition policy.

This mode must not change:

- candidate implementation;
- learner-visible evidence;
- base substrate;
- candidate resource-meter semantics;
- scoring rules.

Only the audition/influence policy may differ as declared.

Without this mode, learned-scope claim `G` is unavailable.

## 14. Representation-version interface

Every committed C4 state that can affect scope must expose a representation-version identifier in evaluator provenance.

When the implementation declares a material representation change, it must also emit one scope-support disposition:

- invariant-by-construction;
- lawful transport;
- relearning;
- bounded compatibility bridge.

Old support cannot silently follow a changed latent coordinate system.

C2 may also version representation/state when necessary for restart and source comparability, but C4 has the additional obligation because learned scope depends on representational continuity.

## 15. Promotion interface

Any structural candidate promotion must bind an immutable evidence window.

The promotion record must identify:

- base version(s);
- candidate version(s);
- scope policy version;
- audition policy version;
- included ticket range;
- excluded ticket range/reasons;
- support diagnostics;
- resource charges;
- frozen promotion rule;
- result: promote / reject / defer / dormant.

Promotion cannot retroactively change the predictions or scores that justified it.

## 16. Checkpoint interface

Checkpoint state must be causally complete for any claimed restart equivalence.

The serialized/checkpoint binding must cover as applicable:

- recurrent/base learner state;
- learned parameters;
- optimizer/plasticity state;
- replay contents and replay policy state;
- learner RNG state;
- candidate structural state;
- scope/gating state;
- support intervals;
- probation/promotion state;
- outstanding prediction tickets;
- outstanding scope tickets;
- unresolved outcomes;
- adaptive audit policy state;
- stopping-rule state;
- representation-version boundaries.

A restart that loses one of these may still be diagnostically useful but cannot silently retain the restart-equivalence claim.

## 17. Evaluator-only scoring interface

The experiment harness may maintain hidden correspondence needed to score predictions and adjudicate the world.

That interface is separate from the candidate process and must include at minimum:

- evaluator opportunity ID;
- hidden world/family state;
- outcome correspondence;
- score contribution;
- invalidation reason;
- aggregation membership;
- run/seed provenance.

No implementation convenience may route these values into C2/C4 learner state unless the frozen information boundary explicitly admits an observable learner-side consequence.

## 18. Equal-stream proof obligation

Before admitting a primary C2-versus-C4 result, the harness must be able to show that the learner-visible stream bindings are equal for the matched comparison opportunities.

Equality is defined over the declared learner-visible representation, not evaluator semantics.

For Experiment A, externally scheduled intervention packets are part of that matched learner-visible stream.

If streams differ, the result must be labeled a different information/opportunity condition rather than an architecture-only comparison.

## 19. Required instrumentation outputs

A future implementation subject must provide enough machine-readable output to reconstruct at least:

```text
candidate_id
committed_state_version
representation_version
learner_visible_frontier_binding
prediction_ticket
prediction_role
replay_snapshot_version
replay_selection_record(s)
structural_candidate_handle(s) | none
scope_ticket(s) | none
resource_meter_delta
promotion_record | none
new_committed_state_version
checkpoint_binding | none
```

The exact serialization format is not fixed here.

## 20. Disallowed comparator shortcuts

The following invalidate the relevant primary claim:

1. C4 sees richer learner-visible evidence than C2 under an equal-information label.
2. C4 receives evaluator applicability labels.
3. C4 replay contains post-hoc semantic enrichment unavailable to C2.
4. Candidate audition mutates the base before marginal scoring.
5. The base-shadow prediction is recomputed after outcome visibility.
6. Structural/gate/audition compute is omitted from accounting.
7. C4 receives more external world/intervention opportunities without that difference being declared.
8. Gate rejection is counted as candidate failure evidence or candidate success evidence rather than `NOT_AUDITED` when no audition occurred.
9. Old scope support follows representation drift without explicit continuity disposition.
10. A restart reconstructs only weights while dropping causally relevant replay/gate/RNG/pending-ticket state and still claims trajectory equivalence.
11. Reference/oracle/semantic-cheat learners are counted as developmental evidence.
12. A branch head rather than an immutable implementation commit defines the executed subject.

## 21. Minimal source-subject consequence

The first implementation PR, if separately authorized, should not be considered experiment-ready merely because C2 and C4 classes/functions exist.

It must bind concrete artifacts implementing these interfaces and expose deterministic evidence that the comparator harness can distinguish:

- learner state from evaluator state;
- pre-outcome prediction from post-outcome update;
- C2 from C4;
- C4 combined from C4 base-shadow where claimed;
- replay from structural audition;
- live influence from shadow audition;
- measured resources from evaluator bookkeeping.

Only then can a real `implementation_subject_commit` populate a preregistration manifest honestly.

## 22. Exact next frontier

The next step now genuinely crosses from research contract into implementation-source design/execution planning.

A future authorized implementation lane would need to choose the smallest concrete C1/C2 recurrent probabilistic substrate and C4 structural-candidate realization that satisfy this interface, then create exact source artifacts and hostile unit tests before any training run.

This document does not authorize that transition.
