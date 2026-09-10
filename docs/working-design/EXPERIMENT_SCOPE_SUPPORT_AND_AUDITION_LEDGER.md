# Experiment Scope Support and Audition Ledger

Classification: **IP_CONFIDENTIAL**

Status: **SUCCESSOR WORKING DESIGN / RESEARCH ONLY / NOT IMPLEMENTATION APPROVAL / NOT BT2 R1 REMEDIATION**

Date: 2026-09-10

Companion contracts:
- `ONLINE_LEARNING_STATE_TRANSITION_CONTRACT.md`
- `REPRESENTATION_DRIFT_SCOPE_CONTINUITY_CONTRACT.md`
- `PREQUENTIAL_SCOPE_APPLICABILITY_CONTRACT.md`

## 1. Purpose

The earlier contracts establish causal update order, lawful scope continuity under representation drift, and prequential applicability scoring. They still require one experiment-level accounting object that can answer a simpler question:

> **Did a more complex learner actually earn its claimed advantage from evidence and resources that a simpler rival could not equally use, or did the evaluation quietly change support, opportunity, bookkeeping, or oracle access?**

This document defines the weakest credible ledger for answering that question without choosing a final optimizer, neural architecture, gate implementation, replay algorithm, or evaluator ontology.

The ledger is evaluator-side provenance. It must not become a learner-visible semantic label channel.

## 2. Scope

The ledger is intended to compare, at minimum:

- **C0** — simple incremental predictive/system-identification baseline;
- **C1** — recurrent probabilistic predictor without replay;
- **C2** — recurrent probabilistic predictor with bounded replay;
- **C3a** — PSR-like/predictive-state realization under the same causal contract;
- **C3b** — stochastic latent/recurrent world-model realization under the same causal contract;
- **C4** — scoped structural/candidate extension only after simpler rivals are measured.

The ledger does not assert that any candidate is sufficient, desirable, or implementation-ready.

## 3. Core invariant

Every comparative claim must be reconstructible from four separable accounts:

1. **what the learner could observe**;
2. **what opportunities it received**;
3. **what resources it consumed**;
4. **what evidence the evaluator used to score it**.

If two candidates differ on more than the declared experimental factor, the difference must be recorded rather than silently attributed to architecture.

No evaluator-only field may cross into learner-visible evidence merely because the ledger stores it.

## 4. Run identity

Each experimental run receives an evaluator-side immutable `run_id` and a frozen run manifest.

The manifest binds:

- source subject / design version under evaluation;
- candidate family and candidate version;
- comparator family and comparator version;
- environment/world generator version;
- transducer/interface version;
- action-interface version if applicable;
- learner-visible channel schema version;
- timebase policy;
- learner RNG policy and declared seeds where reproducibility requires them;
- evaluator RNG policy and seeds where they affect assignment/audition;
- resource envelope;
- replay policy if present;
- scope/audition policy if present;
- checkpoint/restart policy;
- scoring protocol and frozen aggregation rule;
- preregistered stopping rule.

`run_id` is evaluator provenance and must not become a learner-visible task or regime identifier.

## 5. Opportunity identity without semantic leakage

The evaluator may need to determine that several candidates were exposed to the same experimental opportunity. It may therefore maintain an evaluator-side `opportunity_id`.

The `opportunity_id` may bind:

- environment causal state snapshot/reference;
- learner-visible input payload actually delivered;
- action opportunity available at that point;
- target horizon(s);
- assignment/audition decision;
- outcome resolution record.

The learner does not receive `opportunity_id` unless an implementation independently exposes an ordinary transport identity whose semantics are justified at the learner boundary.

Equal opportunity means equality of the declared learner-visible and action opportunity, not equality of evaluator semantic labels.

## 6. Four-plane ledger

For each scored opportunity, the evaluator records four logically separate planes.

### Plane A — learner-visible evidence

Record exactly what entered the cognitive boundary:

- channel/port identity in the allowed learner-visible namespace;
- payload bytes or a cryptographic binding to them;
- learner-visible timing information;
- learner-visible reliability/provenance cues explicitly authorized by the interface contract;
- efference/action feedback legitimately returned to the learner.

Do not include hidden world state, semantic task labels, regime IDs, true causal graph IDs, exact intervention-success truth, or evaluator scoring labels.

### Plane B — opportunity / assignment / support

Record:

- which candidate/comparator was eligible to observe or act;
- whether evaluation was paired, shadow, replayed, or behaviorally live;
- audition/logging policy version;
- assignment probability or deterministic assignment rule;
- scope ticket reference where applicable;
- support class at decision time;
- whether a candidate was excluded from an opportunity and why.

This plane is required to distinguish lack of evidence from evidence of lack.

### Plane C — resource consumption

Record causally relevant resources under the frozen accounting policy, including as applicable:

- learner update compute;
- predictive-query compute;
- replay retrieval/update compute;
- replay memory/storage;
- candidate/gate compute;
- candidate probation memory;
- internal simulation/thinking budget;
- checkpoint persistence overhead;
- durable-state growth;
- action/intervention opportunities consumed;
- wall-clock latency where the experiment claims operational feasibility.

A resource not measured directly must be declared unmeasured rather than treated as zero.

### Plane D — evaluator scoring

Record evaluator-only quantities needed for adjudication:

- immutable prediction/action ticket references;
- outcome resolution;
- frozen metric contributions;
- hidden ground truth used only to score;
- exclusion reason under preregistered rules;
- aggregation-window membership;
- confidence/uncertainty computation inputs;
- audit flags.

Plane D must be noninterfering with learner computation unless a field is separately and explicitly admitted into Plane A.

## 7. Paired comparison frontier

Where causally possible, comparisons should use a common pre-outcome frontier.

For an opportunity at state `C_(t-1)`, the evaluator should be able to identify:

- the base prediction/action proposal before outcome evidence;
- the candidate prediction/action proposal before outcome evidence;
- the scope/gate decision before outcome evidence;
- whether either proposal influenced the world;
- the common learner-visible evidence frontier from which each proposal was generated.

Shadow comparison is preferred where the candidate can be evaluated without changing the world.

If both proposals cannot coexist causally because action changes the world, the ledger must mark the comparison as **counterfactual-unobserved** rather than fabricating a paired outcome.

## 8. Shadow, live, and counterfactual status

Each candidate opportunity has exactly one status:

- `SHADOW_OBSERVED` — candidate generated a prediction/evaluation but did not alter world behavior;
- `LIVE_OBSERVED` — candidate influenced behavior and the resulting outcome was observed;
- `BASE_LIVE_CANDIDATE_SHADOW` — paired base-live/candidate-shadow comparison;
- `CANDIDATE_LIVE_BASE_SHADOW` — paired candidate-live/base-shadow comparison where meaningful;
- `COUNTERFACTUAL_UNOBSERVED` — no valid outcome exists for the unrealized action/path;
- `NOT_AUDITED` — no candidate evidence was collected;
- `INVALIDATED` — opportunity excluded by a preregistered causal/integrity rule.

An evaluator model may estimate a counterfactual for analysis, but the estimate must remain distinguishable from an observed outcome.

## 9. Support classes

At scope decision time, support is recorded as one of:

- `DIRECT_STRONG` — adequate direct audition under materially comparable collection policy;
- `DIRECT_WEAK` — some direct audition, insufficient for strong confidence;
- `OFF_POLICY_SUPPORTED` — reused evidence with declared nontrivial overlap;
- `OFF_POLICY_WEAK` — overlap exists but is poor enough to materially widen uncertainty;
- `TRANSPORTED_SUPPORT` — support lawfully transported across representation versions under the representation-drift contract;
- `ZERO_OR_UNKNOWN_SUPPORT` — no defensible empirical support basis;
- `RELEARNING` — prior support invalidated or insufficient after drift; fresh evidence is being collected.

Thresholds for these classes must be frozen per experiment before outcomes are used to tune them.

The labels themselves are evaluator diagnostics unless a learner-side uncertainty mechanism independently represents analogous information from ordinary evidence.

## 10. Equal-information rule

For any claim that candidate `X` beats rival `Y`, the ledger must make visible whether `X` received any additional information channel or derived target unavailable to `Y`.

Differences include:

- semantic annotations;
- hidden state labels;
- privileged correspondence keys;
- future-derived training targets;
- richer replay records;
- evaluator-selected hard cases;
- exact intervention success;
- oracle calibration/noise parameters;
- task/regime IDs;
- retrospective scope labels.

If such a difference is deliberate, the result is a different information condition and cannot be attributed solely to architecture.

## 11. Equal-opportunity rule

Candidates may differ in internal computation, but experimental opportunity must be accounted separately.

The ledger records differences in:

- number of learner-visible events;
- action opportunities;
- audition opportunities;
- shadow-evaluation opportunities;
- replay exposures;
- internal update steps;
- reset/restart frequency;
- developmental curriculum order.

A candidate that receives more opportunities may still be useful, but the advantage is not an equal-opportunity architecture comparison unless adjusted by a preregistered design.

## 12. Equal-resource rule

The first comparison report should include both:

- **fixed-envelope performance** — what each candidate achieves under the same declared resource ceiling where practical;
- **resource-performance frontier** — how performance changes as declared resources vary.

This prevents two opposite errors:

- rejecting a useful mechanism merely because it consumes more resources while delivering substantially more value;
- granting architecture status to a mechanism that wins only because it silently consumes more memory/compute/audition.

No single scalar resource conversion is mandatory. If CPU, memory, latency, storage, and action opportunity cannot be credibly collapsed into one value, preserve them as separate axes.

## 13. Replay accounting

For replay candidates, each replay event binds:

- source experience reference;
- learner-visible evidence available when originally encoded;
- replay selection policy/version;
- selection probability if stochastic;
- replay count for that experience;
- compute charged;
- whether priorities were updated;
- whether replay occurred before or after current-event insertion under the frozen contract.

Replay records may not become semantically richer because evaluator annotations were added after the original experience.

C1 versus C2 must therefore make explicit whether C2's gain is attributable to replay memory/compute rather than to an accidental target-information subsidy.

## 14. Structural candidate accounting

For C4 or another scoped structural mechanism, the ledger additionally binds:

- candidate birth/proposal boundary;
- parent/base state version;
- probation start/end boundaries;
- audition policy version;
- scope ticket references;
- candidate-local resource consumption;
- any base resources shared with the candidate;
- promotion/retirement decision evidence window;
- support state across the claimed applicability region;
- representation version(s) under which scope evidence was gathered;
- continuity/relearning disposition after material representation drift.

Candidate creation itself does not establish a new semantic regime.

## 15. Missingness is first-class

The evaluator must never collapse these into one category:

- candidate was evaluated and failed;
- candidate was not evaluated;
- candidate could not be evaluated causally;
- candidate was excluded by policy;
- outcome has not resolved yet;
- outcome was invalidated by integrity failure.

These states must remain distinguishable through aggregation.

A gate that reduces the number of observed negative examples by refusing audition must not receive credit as though those missing outcomes were successes.

## 16. Aggregation contract

Before a comparison begins, freeze:

- primary metric(s);
- secondary diagnostics;
- aggregation horizon;
- weighting rule;
- handling of unresolved outcomes;
- handling of invalidated opportunities;
- minimum support needed for regional claims;
- uncertainty method;
- multiple-comparison correction if many scope regions/candidates are probed;
- stopping rule;
- promotion threshold if promotion is in scope.

Post-result metric substitution creates a new exploratory analysis, not the preregistered result.

## 17. Claim classes

Reports should separate at least four claim classes:

### Global predictive claim

Candidate improves declared predictive metrics across the preregistered evaluation distribution.

### Scoped predictive claim

Candidate improves metrics only within a scope region whose support is independently adequate.

### Control / intervention claim

Candidate improves behavior under live intervention, with induced-distribution effects explicitly accounted.

### Resource-efficiency claim

Candidate reaches comparable quality with lower declared resources or provides enough quality gain to justify additional resource cost.

Evidence for one claim class does not automatically establish another.

## 18. Cross-representation evidence

When learner representation changes during an experiment:

- close the old representation-version support interval;
- retain old tickets as historical evidence;
- open a new interval for the new representation;
- record the continuity route used by each dependent gate/scope;
- downgrade support where continuity is not established;
- distinguish transported support from fresh direct support;
- require fresh audition before restoring strong confidence where needed.

This preserves representation plasticity without pretending that old latent regions retain semantic identity by fiat.

## 19. Restart and crash integrity

A restart-equivalent experiment must persist enough ledger state to preserve future interpretation, including:

- outstanding prediction/action/scope tickets;
- unresolved outcomes;
- audit-policy state;
- assignment/propensity RNG state where relevant;
- current support intervals;
- representation-version boundaries;
- aggregation-window state;
- preregistered stopping-rule state.

If any of these are lost and future scoring can change, restart equivalence is forfeited and the run must be marked accordingly.

## 20. Minimum hostile tests

### ESL-0 — free oracle column

Inject an evaluator semantic field into a candidate's learner-side record while leaving comparator input unchanged. The ledger must expose the information-condition mismatch.

### ESL-1 — hidden extra audition

Give C4 additional shadow opportunities without recording them. The opportunity totals must fail reconciliation.

### ESL-2 — replay enrichment

Add evaluator labels to old replay records. Replay provenance must reject or flag the enriched records.

### ESL-3 — missing-negative laundering

Route candidate away from likely failures and aggregate only observed candidate opportunities. The report must retain the missing/not-audited mass and block a supported scoped claim.

### ESL-4 — counterfactual fabrication

Score both mutually exclusive live actions as if both outcomes were observed. The ledger must mark one path counterfactual-unobserved.

### ESL-5 — resource shadow subsidy

Perform candidate shadow evaluation without charging its compute. Fixed-envelope accounting must fail.

### ESL-6 — weak-overlap false precision

Reuse off-policy evidence from a barely overlapping logging policy. The support state must remain weak and uncertainty must not collapse spuriously.

### ESL-7 — representation-version laundering

Pool old and new latent-scope evidence as one region after material drift without lawful continuity. Aggregation must reject the pooled strong-support claim.

### ESL-8 — delayed-outcome version confusion

Resolve a delayed outcome after candidate/gate updates. The score must remain bound to the versions recorded on the original ticket.

### ESL-9 — adaptive stopping rescue

Stop the experiment immediately after a favorable fluctuation when the preregistered stopping rule would continue. The result must be classified exploratory/invalid for the frozen primary claim.

### ESL-10 — simpler-rival accounting

Let C4 win raw score while consuming more replay, audition, compute, or action opportunities. The report must expose the resource/opportunity difference rather than calling it an equal-condition architecture win.

## 21. Minimal ledger record

A first implementation specification may encode the ledger differently, but the logical record for each opportunity must be able to reconstruct:

```text
run_id
evaluator_opportunity_id
pre_outcome_committed_state_version
representation_version
candidate_versions
learner_visible_evidence_binding
prediction_action_ticket_refs
scope_ticket_ref | none
audition_policy_version
assignment_rule_or_probability
support_class
shadow_live_counterfactual_status
resource_charges
outcome_resolution_state
metric_contributions
integrity_flags
```

This is a logical schema, not implementation authorization.

## 22. First experimental sequence

The ledger supports a deliberately conservative sequence:

1. establish C0 under fixed information/opportunity/resource accounting;
2. compare C1 against C0;
3. compare C2 against C1 and expose replay-specific cost/value;
4. compare C3a and C3b against the strongest simpler rival under matched causal/evidence rules;
5. only then admit C4 scope/candidate machinery;
6. require C4 to show marginal value after charging gate, audition, probation, representation-continuity, and candidate resource costs;
7. retain a no-scope/simple-audition rival so learned gating can embarrass itself.

Nothing in this sequence authorizes training or compute. It defines what a future authorized experiment would have to record.

## 23. Claim ceiling

Passing the ledger's integrity checks would establish only that a comparison is auditable under its declared experiment contract.

It would not establish:

- consciousness;
- semantic truth of latent variables;
- universal generality;
- optimality;
- safety for deployment;
- implementation readiness of the frozen BT2 R1 subject;
- authority to train, deploy, merge, spend, or connect Noema to protected systems.

## 24. Next frontier

With update order, representation-drift scope continuity, prequential scope applicability, and experiment accounting separated, the next design question becomes narrower:

> **What is the weakest future F0/F1 experiment family that can falsify the claim that scoped structural learning adds value over recurrent prediction + replay under this ledger, while remaining small enough to run only after explicit compute/training authorization?**

That future experiment design must remain inert until separately authorized.
