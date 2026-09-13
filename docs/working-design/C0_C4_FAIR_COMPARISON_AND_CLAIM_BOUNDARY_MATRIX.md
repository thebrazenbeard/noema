# C0–C4 Fair Comparison and Claim-Boundary Matrix

Classification: **IP_CONFIDENTIAL**

Status: **SUCCESSOR WORKING DESIGN / INERT FALSIFICATION CONTRACT / NO IMPLEMENTATION OR EXECUTION AUTHORITY / NOT BT2 R1 REMEDIATION**

Date: 2026-09-13

Companion contracts:

- `MINIMAL_STRUCTURAL_VALUE_FALSIFICATION_FAMILY.md`
- `C2_C4_COMPARATOR_INTERFACE_CONTRACT.md`
- `EXPERIMENT_SCOPE_SUPPORT_AND_AUDITION_LEDGER.md`
- `EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V1.json`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_CONTRACT.md`

## 1. Purpose

The minimal structural-value family names C0, C1, C2, C3, and C4, while the comparator interface necessarily concentrates on the decisive C2-versus-C4 seam.

This matrix binds the whole ladder. It prevents a future result from silently changing the comparison class between the sanity gate, replay comparison, continuous-structure diagnostic, and scoped-structure claim.

It is specification and audit material only. It does not select an optimizer, implement a learner, authorize training, or authorize experiment execution.

## 2. Comparison invariants

A primary comparison is admissible only when these four conditions are separately demonstrated.

### 2.1 Equal learner-visible information

Matched candidates receive the same ordered learner-visible event envelope, including the same externally scheduled intervention packets in SVF-1.

The envelope may contain ordinary data, timing, reliability/provenance cues, and issued action/efference packets admitted by the frozen interface. It may not contain hidden family identity, causal orientation, task/regime identity, applicability labels, evaluator scores, future split membership, or exact intervention-success truth that is not ordinarily observable.

Candidate-derived internal features are an architectural difference, not an extra external information channel. They must be produced from the same lawful input frontier and charged as computation/state.

### 2.2 Equal external opportunity

Each matched candidate sees an independent replica of the same evaluator-constructed world/seed stream and externally scheduled intervention sequence. Common-random-number pairing is permitted; sharing learner state is not.

Candidate predictions, scope decisions, audit outcomes, or resource use may not alter the SVF-0/SVF-1 world generator, intervention schedule, test allocation, or learner-visible stream. If a realization can alter those quantities, it is a behavior-affecting condition and cannot be part of the primary externally scheduled SVF comparison without a separately declared causal design.

### 2.3 Equal causal frontier

Every scored prediction, action, or scope decision is emitted from a committed pre-outcome state and receives an immutable ticket before the corresponding outcome is visible.

A hypothetical intervention forecast produced during passive ambiguity is evaluator-scored counterfactual evidence. Its status remains `COUNTERFACTUAL_UNOBSERVED`; it is not converted into an observed outcome and is not fed back as learner evidence.

### 2.4 Equal declared resources

A fixed-total-envelope claim is admissible only when every causally material consumed resource has a measurement route and a ledger charge.

C4 structural state, candidate snapshots, anchors, traces, transport maps, gate inference, audition, proposal search, replay, checkpointing, and durable-state growth are not free sidecars. Any such state or compute that can affect the learner or reconstruct retained evidence is charged to the declared envelope.

If a material resource is unmeasured, the result may remain exploratory but cannot support a fixed-total-envelope primary claim. If C4 receives extra resources without displacing base/replay resources inside the envelope, the result belongs only to the resource-performance frontier.

## 3. Candidate ladder

### C0 — persistence floor

C0 is the deliberately simple incremental predictor/system-identification floor.

C0 answers whether the stream, scoring, and basic persistence setup are nontrivial. It is not a structural-value rival and cannot be used to make C4 look valuable by comparison with a deliberately weak system.

### C1 — recurrent predictor without replay

C1 is the recurrent probabilistic online predictor with no replay.

C1 must use the same declared base substrate family, learner-visible schema, event order, initialization policy, and non-replay update budget used by the corresponding C2 comparison. The C1-to-C2 contrast isolates bounded replay, subject to the declared replay-memory and replay-compute difference.

### C2 — recurrent predictor with bounded replay

C2 is the primary simpler rival.

C2 must be C1's declared base substrate with only the preregistered replay capability added for the C1-to-C2 comparison. Replay capacity, selection policy, update limit, insertion order, priority provenance, and compute/storage charges are frozen before outcomes.

C2 is the minimum serious rival for any C4 claim.

### C3 — continuous or predictive-state structural diagnostic

C3 is the strongest non-scoped structural/soft-structure diagnostic admitted by the manifest. It may be a continuous soft-structure, predictive-state, or other non-scoped realization, but the realization must be fixed before outcomes and must not receive semantic task labels.

C3 uses the same learner-visible event envelope and the same declared base/resource conditions as the comparison it enters. A C3 result is not silently treated as either C2 or C4.

A minimal negative C2-versus-C4 falsifier may omit C3. If C4 wins and the project wants to claim that scoped/explicit structure adds value beyond the strongest non-scoped structural alternative, C3 (or a predeclared equivalent) becomes mandatory evidence. Omitting C3 limits the claim to the tested C2-versus-C4 whole-system comparison.

### C4 — scoped structural candidate

C4 uses the declared C2 base substrate plus bounded structural candidate machinery and, when under test, learned scope/routing.

C4 may trade base, replay, and structural resources within the fixed envelope only when the trade is declared. It may not receive a larger hidden base, richer replay, extra learner-visible evidence, or uncharged candidate/audition state.

C4's candidate handles, scope tickets, support intervals, representation versions, promotion records, and resource meters follow the C2/C4 comparator interface.

## 4. Fair comparison matrix

| Comparison | Question | Only intended factor | Minimum admissibility | Claim ceiling |
| --- | --- | --- | --- | --- |
| C0 vs C1 | Does recurrent state add persistent online value over the floor? | Recurrent state/update mechanism | Same stream, seed policy, outcome order, and declared envelope; C0 remains a floor | Persistence evidence only |
| C1 vs C2 | Does bounded replay add value beyond recurrence? | Replay storage, selection, update, and compute | Same C1 base and update contract; replay differences fully charged | Replay-adjusted persistence/retention claim |
| C2 vs C3 | Does non-scoped structural/predictive-state machinery add value beyond recurrence + replay? | Declared C3 structural realization | Same learner-visible stream, base conditions, matched resource view, and no semantic labels | Narrow non-scoped structural diagnostic claim |
| C2 vs C4 | Does scoped structural machinery add value over the primary simpler rival? | Bounded C4 structure/scope machinery | Same external stream, base conditions, pre-outcome tickets, support/audition accounting, and fixed or frontier resource view | Whole-system C4-over-C2 claim only |
| C3 vs C4 | Does scope/candidate machinery add value beyond the strongest non-scoped diagnostic? | Scope/candidate/routing machinery | C3 and C4 share the declared comparison substrate and resource view; C4 passes support and simpler-audition controls | Scoped-value claim under the tested family |
| C4-learned vs C4-bounded | Does learned scope earn itself over simpler audition? | Learned scope versus frozen bounded audition policy | Same candidate implementation, base state, learner-visible stream, candidate budget, meter, scoring, and audit quota; only the scope/audition policy differs | Claim G only |

A row may be omitted only when the manifest records the omission and applies the corresponding claim ceiling. No row may be selectively omitted after outcomes are visible.

## 5. Replay and durable-state fairness

For C1/C2 and C2/C4 comparisons:

- replay records contain only information available at original encoding;
- evaluator annotations, hidden labels, future split membership, and post-hoc scope judgments cannot enrich replay;
- structural traces, anchors, candidate snapshots, scope maps, and compatibility bridges count as learner state when they affect future computation or retain evidence;
- replay priorities must be learner-derived or explicitly declared as a different information/resource condition;
- C4 cannot receive both a larger replay privilege and an uncharged structural memory privilege while the result is described as an equal-resource architecture comparison.

The ledger must distinguish raw replay capacity from derived structural memory. Equal raw buffer size does not make unequal total retained evidence free.

## 6. Scope and support claim admissibility

A C4 gate may not turn non-audition into success or failure.

For a supported positive scope claim:

- `DIRECT_STRONG` requires the frozen direct-audition threshold;
- `TRANSPORTED_SUPPORT` requires a valid representation-continuity disposition and its uncertainty charge;
- `DIRECT_WEAK`, `OFF_POLICY_WEAK`, `ZERO_OR_UNKNOWN_SUPPORT`, `NOT_AUDITED`, `COUNTERFACTUAL_UNOBSERVED`, unresolved, and invalidated opportunities cannot supply strong positive support;
- `OFF_POLICY_SUPPORTED` requires a preregistered nonzero-overlap condition and widened uncertainty; it is not equivalent to direct support;
- missingness remains a separate aggregation state.

Claim G requires the C4-learned-versus-C4-bounded comparison in the matrix. The learned gate cannot lower its own audit quota, suppress its own falsifying opportunities, or use evaluator support labels as learner targets.

## 7. Passive ambiguity and intervention holdouts

The passive chain/fork world is a useful first falsifier, not a universal structural proof.

Before outcomes are observed, all developmental candidates receive the same passive stream and the same query schedule. Evaluator-generated hypothetical-intervention forecasts remain counterfactual and non-learning.

Decisive and held-out intervention evaluation must be separated by more than an unseen numeric value. The manifest must freeze independent world/episode or parameter draws and intervention-value allocation so a candidate cannot win by memorizing a shared world parameterization or interpolation surface.

A result that wins only on the first analytic chain/fork family is limited to that family. Broader structural claims require a predeclared successor family with hidden mediators, higher-order dependencies, or another non-isomorphic generator pressure.

## 8. Representation drift and restart boundary

Every scope/support record is representation-versioned.

A material internal representation change closes the old support interval. Reuse requires exactly one declared continuity route: invariant scope, lawful transport, fresh relearning, or bounded compatibility bridge. Transported support remains distinct from fresh support; old and new intervals are not pooled to manufacture strong coverage.

If a checkpoint or restart loses any state required by the frozen restart contract, restart equivalence is forfeited for the affected run. The run is quarantined from primary trajectory claims; continuing it requires a new run identity or a separately predeclared recovery protocol. A reviewer may not restore equivalence by assertion that the missing state was probably irrelevant.

## 9. Falsification interpretation

The family is successful when it can produce a defensible negative result.

- If C2 matches or beats C4 under the declared primary condition, scoped structure has not earned itself for this family.
- If C4 wins only on the resource frontier, the result is not an equal-resource win.
- If C4 wins against C2 but not C3, the result supports only a C2-relative whole-system claim.
- If C4 wins but learned scope does not beat bounded audition, defer learned scope and retain the simpler policy.
- If a result depends on semantic labels, stable channel identity, hidden replay subsidy, unmeasured resources, unsupported scope regions, or restart ambiguity, the relevant claim is invalid rather than positive evidence.

## 10. Effect boundary

This matrix does not authorize implementation, training, model execution, hosted or paid compute, merge, deployment, publication, provider/credential/ruleset mutation, repository-visibility change, or any other protected effect.
