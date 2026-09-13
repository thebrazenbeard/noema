# Experiment Preregistration Validator Contract V2

Classification: **IP_CONFIDENTIAL**

Status: **SUCCESSOR WORKING DESIGN / V2 VALIDATION CONTRACT / NOT IMPLEMENTED / NOT EXECUTION AUTHORITY / NOT BT2 R1 REMEDIATION**

Date: 2026-09-13

Validates:
- `EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V2.json`

Normative companion addenda:
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_SOURCE_BINDING_ADDENDUM.md`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_RESOURCE_ADDENDUM.md`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_DECIDABILITY_ADDENDUM.md`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_COMPARATOR_MATRIX_ADDENDUM.md`

Supersedes for future preregistration use:
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_CONTRACT.md`

Historical V1 artifacts remain provenance. They are not rewritten or deleted.

## 1. Purpose

Schema V2 repairs the internal contradictions found by the exact-head hostile review of PR #32 at `e282369e13f9ea801a2964665dc4062cd38b8ea9`. JSON Schema still cannot prove repository identity, keyed uniqueness, cross-candidate equality, commitment preimages, causal ordering, transfer fairness, or authority separation at runtime.

This contract defines those validator obligations.

A validator PASS is evidence-governance status only. It never authorizes execution.

## 2. Result classes

A V2 validator returns exactly one top-level result:

- `PASS_FROZEN_VALID`
- `FAIL_SCHEMA`
- `FAIL_STAGE_SEMANTICS`
- `FAIL_CROSS_FIELD_INVARIANT`
- `FAIL_SOURCE_BINDING`
- `FAIL_INFORMATION_BOUNDARY`
- `FAIL_WORLD_SCHEDULE_INTEGRITY`
- `FAIL_COMPARATOR_FAIRNESS`
- `FAIL_RESOURCE_ACCOUNTING`
- `FAIL_SUPPORT_AUDITION_CONTRACT`
- `FAIL_LINEAGE_TRANSFER_CONTRACT`
- `FAIL_SCORING_CONTRACT`
- `FAIL_RESTART_INTEGRITY`
- `FAIL_FREEZE_INTEGRITY`
- `BLOCKED_UNAVAILABLE_EVIDENCE`

`BLOCKED_UNAVAILABLE_EVIDENCE` is never coerced to PASS.

## 3. Ordered validation

Validation is monotonic: later checks cannot rescue an earlier failure.

### V0 — JSON Schema V2

Validate with JSON Schema Draft 2020-12 against the exact immutable V2 schema artifact.

Failure: `FAIL_SCHEMA`.

### V1 — stage semantics

For `SVF-0` verify:

- C1 and C2 are present;
- primary claims are exactly `P`;
- C2-vs-C4 external comparison is false;
- intervention mode is `NONE`;
- no intervention schedule artifact/commitment is claimed;
- learned scope is not a primary claim and no simple-audition rival is required merely to pass Gate 1.

For `SVF-1` verify:

- C2 and C4 are present;
- primary claims are drawn only from `S/T/L/G`;
- C2-vs-C4 external comparison is required;
- intervention mode is `EXTERNALLY_SCHEDULED`;
- observational equivalence verification is present;
- the schedule artifact/commitment is present;
- all four schedule-adaptation flags are false.

Failure: `FAIL_STAGE_SEMANTICS`.

## 4. Exact source binding

### V2 — implementation subject

Verify:

- `subject.repository` exists and is the intended private Noema source;
- `implementation_subject_commit` exists and is immutable;
- every developmental candidate `source_commit` resolves under that frozen implementation subject or an explicitly frozen derivation relation;
- every source artifact path exists at its declared commit;
- declared Git blobs and SHA-256 digests match when present;
- diagnostic/reference sources that are outside the implementation subject are explicitly ineligible for developmental evidence.

A mutable branch name never substitutes for an implementation commit.

Mismatch: `FAIL_SOURCE_BINDING`.

Unavailable authoritative bytes: `BLOCKED_UNAVAILABLE_EVIDENCE`.

## 5. Key and reference closure

### V3 — keyed uniqueness

Require uniqueness by key for:

- `candidate_id`;
- `metric_id`.

Whole-object `uniqueItems` is insufficient.

### V3.1 — candidate reference closure

Every:

- `variant_of_candidate_id` when non-null;
- `comparator_candidate_id`;

must resolve to a candidate in the frozen manifest.

A candidate may not be its own variant parent.

### V3.2 — scope-policy closure

Every candidate `scope_policy_id` must appear in `audition_scope_contract.scope_policy_ids`.

Violation: `FAIL_CROSS_FIELD_INVARIANT`.

## 6. Information boundary

### V4 — field-set disjointness

The learner-visible and evaluator-only field-name sets must be disjoint.

### V4.1 — immutable schema closure

Resolve both schema artifacts and verify all possible transport fields are accounted for. Reject permissive metadata bags, undeclared extension fields, or wrappers able to smuggle evaluator state into the learner path.

### V4.2 — forbidden ingress

No learner path may contain semantic applicability labels, hidden family/world identity, evaluator score, future-derived target, or exact intervention-success truth unless a new experiment subject explicitly makes such information learner-visible and lowers the claim ceiling.

Failure: `FAIL_INFORMATION_BOUNDARY`.

## 7. World and schedule integrity

### V5 — commitment preimages

Resolve and hash the immutable preimages for:

- parameter distribution;
- seed manifest;
- intervention schedule when used.

Each digest must match its declared commitment.

A bare hash whose authoritative preimage cannot be retrieved is `BLOCKED_UNAVAILABLE_EVIDENCE`, not evidence of reproducibility.

### V5.1 — externally scheduled means non-oracular

For SVF-1 verify from the schedule artifact/policy that schedule generation cannot adapt to:

- hidden family identity;
- candidate predictions;
- scored outcomes;
- evaluator diagnostics.

The schedule must be fixed before the outcomes it can influence are visible.

If adaptation is scientifically desired later, it creates a different experiment subject.

Failure: `FAIL_WORLD_SCHEDULE_INTEGRITY`.

### V5.2 — negative-control rule

Verify the negative-control generator is immutable and `negative_control_acceptance_rule` was frozen before result visibility.

The rule must distinguish acceptable bounded overhead from false structural advantage/destructive search.

## 8. C2/C4 comparator fairness

### V6 — base-substrate equality

For equal-condition SVF-1 structural claims, C2 and the primary C4 must bind the same `base_substrate_id` and validator-resolved non-structural base configuration.

A stronger C4 backbone creates a different architecture condition and cannot establish structural marginal value.

### V6.1 — condition-ID equality

For fixed-condition primary C2/C4 comparisons require equality of:

- candidate `information_condition_id` with the top-level information condition;
- candidate `opportunity_condition_id` with the top-level opportunity condition;
- candidate `resource_condition_id` with the top-level resource condition;
- candidate `replay_policy_id` with the top-level replay policy.

Any intentionally changed condition must be named as the experimental factor and the claim narrowed accordingly.

### V6.2 — equal learner-visible stream

Using the experiment ledger, prove matched C2/C4 opportunities received equal learner-visible event bindings, including externally scheduled intervention packets.

Additional C4 shadow computation is not an additional world-outcome opportunity and must be separately charged.

### V6.3 — replay isolation

Verify matched buffer capacity, sampling policy, update budget, learner-side target contents, priority provenance, and replay compute where the structural comparison claims replay matching.

Candidate audition may not mutate shared base/replay policy state before marginal scoring.

Failure: `FAIL_COMPARATOR_FAIRNESS`.

## 9. Candidate variant identity and claim G

### V7 — variant provenance

For any candidate with `variant_of_candidate_id`, verify the parent exists and the declared `variant_dimension` accurately describes the source/config delta.

### V7.1 — learned scope versus simple audition

For primary claim `G`, require two C4 conditions whose:

- source implementation;
- base substrate;
- structural candidate machinery;
- learner-visible information;
- opportunity stream;
- replay condition;
- scoring contract;

are identical except for the preregistered `SCOPE_POLICY` dimension.

The simple-audition rival must have nonzero preregistered audition probability and complete ledger support.

If this identity cannot be established, claim `G` is unavailable even when structural claim `S` survives.

Failure: `FAIL_SUPPORT_AUDITION_CONTRACT`.

## 10. Scope/support integrity

### V8 — pre-outcome ticket ordering

Every scored scope decision must bind a ticket committed before its outcome.

### V8.1 — real propensity provenance

For stochastic selection/audition, the recorded probability must come from the actual policy state that made the decision before outcome visibility. Post-hoc reconstruction is not sufficient.

### V8.2 — support before confidence

`ZERO_OR_UNKNOWN_SUPPORT` can never satisfy a strong empirical scope claim. IPS, doubly robust estimation, learned reward models, or another estimator cannot manufacture support.

### V8.3 — representation-version continuity

Each support interval is representation-versioned. A material representation change requires an explicit invariant/transport/relearning/compatibility-bridge disposition before confidence crosses the boundary.

Failure: `FAIL_SUPPORT_AUDITION_CONTRACT`.

## 11. Transfer and lineage integrity

### V9 — claim T requires an explicit transfer subject

If `T` is primary, require:

- `cross_world_transfer_used=true`;
- non-null immutable `policy_artifact`;
- `no_meta_learning_ablation=true`;
- a state-scope manifest for each carried/reset condition;
- matched C2/C4 continuation/reset opportunity except for the structural state dimension explicitly under test;
- evaluator lineage IDs kept out of learner-visible state.

### V9.1 — no reset/carryover laundering

Do not compare a C4 that carries meta/structural state into a remapped world with a C2 that was reset and label the difference structural transfer unless that reset/carryover difference is the preregistered experimental factor.

### V9.2 — operation verification

Checkpoint/restore/continuation claims must be backed by the lineage/state-transfer provenance required by `EXPERIMENT_LINEAGE_AND_STATE_TRANSFER_CONTRACT.md`.

Failure: `FAIL_LINEAGE_TRANSFER_CONTRACT`.

## 12. Resource accounting

### V10 — all consumed resources measured

Verify measurement routes and ledger charges for every consumed resource relevant to the claim, including:

- learner update/query compute;
- replay compute/storage;
- structural proposal/search;
- structural memory;
- scope/gate inference;
- shadow audition;
- C4 base-shadow diagnostic computation;
- probation/consolidation state;
- checkpoint/restart cost when used.

Unmeasured is not zero.

### V10.1 — fixed envelope

Any result called `FIXED_TOTAL_ENVELOPE` must remain within the frozen envelope on every declared resource axis. Over-budget runs may remain exploratory but cannot satisfy the fixed-envelope primary claim.

Failure: `FAIL_RESOURCE_ACCOUNTING`.

## 13. Scoring closure

### V11 — claim/metric closure

Require:

- unique metric IDs;
- every metric claim appears in `primary_claims` when that metric is primary;
- every comparator candidate resolves;
- comparator role is meaningful for the claim;
- SVF-0 `P` metrics compare the declared persistent/replay baseline conditions rather than silently importing a structural claim;
- SVF-1 structural claims use the frozen C2/C4/variant conditions as preregistered.

### V11.1 — transfer and gate conditional controls

If `T` is primary, no-meta-learning ablation and V9 must pass.

If `G` is primary, uniform/simple audition rival and V7/V8 must pass.

### V11.2 — missingness integrity

Never collapse success, failure, `NOT_AUDITED`, `COUNTERFACTUAL_UNOBSERVED`, unresolved, or invalidated opportunities.

### V11.3 — post-result changes

Changing metrics, aggregation, thresholds, support requirements, confidence method, stopping rule, negative-control rule, or kill criteria creates a new subject. Old results may be reanalyzed only as explicitly exploratory analyses.

Failure: `FAIL_SCORING_CONTRACT`.

## 14. Restart integrity

### V12 — conditional restart claim

If `checkpointing_used=false`, `restart_equivalence_claimed` must be false.

If `restart_equivalence_claimed=true`, verify causally complete persistence of outstanding tickets, unresolved outcomes, learner/assignment RNG state, audit-policy state, support intervals, representation boundaries, and stopping-rule state, plus the implementation-specific learner/replay/candidate state required by the comparator interface.

If checkpointing occurs without a restart-equivalence claim, classify resumed evidence according to what state was actually restored; do not upgrade it to trajectory equivalence.

Failure: `FAIL_RESTART_INTEGRITY`.

## 15. Freeze integrity

### V13 — freeze precedes result visibility

The manifest and its commitment artifacts must be frozen before scored outcomes become visible to any actor authorized to mutate the subject.

### V13.1 — receipt

The later immutable freeze receipt must bind at least:

- repository;
- manifest path;
- manifest commit;
- manifest Git blob;
- implementation subject commit;
- schema version;
- logical experiment ID;
- freeze timestamp.

### V13.2 — mutation creates a new subject

Any change after freeze to source, information boundary, world/randomization/schedule, lineage/transfer policy, resources, support/audition policy, scoring, controls, stopping rule, or acceptance criteria creates a new subject.

Failure: `FAIL_FREEZE_INTEGRITY`.

## 16. Authority separation

`PASS_FROZEN_VALID` authorizes nothing by itself.

A future runner must require a separate exact execution-authority receipt naming the frozen subject before any model training or experiment execution.

The validator must not perform training, execution, paid compute, merge, deployment, publication, provider/credential/ruleset changes, repository-visibility changes, or protected-system connection as a side effect of validation.

## 17. Fixture discipline

The V1 contract's request for `minimal valid` SVF fixtures is superseded.

Before a real implementation subject exists, lawful research fixtures are limited to:

- **shape exemplars** explicitly labeled `NON_EXECUTABLE / CANNOT_PASS_FROZEN_VALID` because they use no real implementation subject; and
- **intentionally invalid hostile fixtures** designed to trigger specific validator failures.

Do not fabricate a real-looking implementation commit or source binding merely to make a fixture pass.

After a real implementation subject exists under separate implementation authority, an exact frozen manifest may be created and independently validated.

## 18. Minimum hostile validator suite

A future validator must reject or block at least:

1. SVF-0 using claim `S` instead of `P`;
2. SVF-0 demanding a nonexistent C4 comparison;
3. SVF-1 null/mutable intervention schedule;
4. schedule policy conditioned on hidden family or scored outcomes;
5. missing commitment preimage;
6. C4 stronger base substrate than C2 under an equal-base claim;
7. mismatched information/opportunity/resource/replay condition IDs;
8. duplicate candidate or metric IDs;
9. unresolved comparator candidate;
10. learned-scope rival not variant-linked to the same C4 machinery;
11. replay enrichment with evaluator labels;
12. uncharged base-shadow/scope/audition compute;
13. scope ticket emitted post-outcome;
14. propensity reconstructed after policy update;
15. strong scope claim under zero support;
16. old support crossing representation drift without disposition;
17. claim T with C4 carryover but C2 reset;
18. negative controls with no frozen null/acceptance rule;
19. restart-equivalence claim with incomplete causal state;
20. changed stopping/acceptance rule after freeze;
21. a structurally valid manifest with no real immutable implementation subject;
22. a `PASS_FROZEN_VALID` manifest presented without separate execution authority.

For test 22 the validator result may remain PASS while the runner must still block execution.

## 19. Exact next frontier

After schema V2 and this validator contract are committed, run a new exact-head hostile review against the repaired PR #32 research chain.

If that review finds no remaining research-blocking contradiction, the next frontier is no longer another conceptual research artifact. It becomes a separately authorized implementation-source lane for the smallest C1/C2 recurrent probabilistic substrate and C4 structural candidate realization plus hostile unit tests.

This contract does not authorize that transition.