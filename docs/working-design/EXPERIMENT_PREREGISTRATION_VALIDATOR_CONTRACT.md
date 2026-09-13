# Experiment Preregistration Validator Contract

Classification: **IP_CONFIDENTIAL**

Status: **SUCCESSOR WORKING DESIGN / VALIDATION CONTRACT ONLY / NOT IMPLEMENTED / NOT EXECUTION AUTHORITY / NOT BT2 R1 REMEDIATION**

Date: 2026-09-13

Schema under validation:
- `EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V1.json`

Companion design:
- `MINIMAL_STRUCTURAL_VALUE_FALSIFICATION_FAMILY.md`
- `C0_C4_FAIR_COMPARISON_AND_CLAIM_BOUNDARY_MATRIX.md`
- `EXPERIMENT_SCOPE_SUPPORT_AND_AUDITION_LEDGER.md`
- `PREQUENTIAL_SCOPE_APPLICABILITY_CONTRACT.md`
- `REPRESENTATION_DRIFT_SCOPE_CONTINUITY_CONTRACT.md`

## 1. Purpose

The JSON Schema can enforce shape, many constants, required candidate roles, numeric bounds, and effect-boundary declarations. It cannot by itself establish several cross-record and repository-currentness facts that determine whether a future preregistered experiment is actually the frozen subject it claims to be.

This contract defines the validator responsibilities that must exist before a manifest can be treated as **FROZEN_VALID**.

No validator implementation is authorized here.

## 2. Validation result classes

A future validator returns exactly one top-level result:

- `PASS_FROZEN_VALID`
- `FAIL_SCHEMA`
- `FAIL_CROSS_FIELD_INVARIANT`
- `FAIL_SOURCE_BINDING`
- `FAIL_INFORMATION_BOUNDARY`
- `FAIL_RESOURCE_ACCOUNTING`
- `FAIL_SUPPORT_AUDITION_CONTRACT`
- `FAIL_FREEZE_INTEGRITY`
- `BLOCKED_UNAVAILABLE_EVIDENCE`

`BLOCKED_UNAVAILABLE_EVIDENCE` is not PASS and must not be coerced to FAIL unless the unavailable evidence is itself prohibited by the experiment contract.

## 3. Validation layers

Validation is ordered. A later layer cannot rescue an earlier failure.

### V0 — syntactic/schema validation

Validate the manifest against `EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V1.json` using JSON Schema Draft 2020-12 semantics.

Failure returns `FAIL_SCHEMA`.

### V1 — candidate-key uniqueness and role integrity

Standard `uniqueItems` compares whole objects and therefore does not guarantee unique `candidate_id` values.

The validator must verify:

- each `candidate_id` is unique;
- exactly one implementation subject is bound by the manifest;
- every developmental candidate role uses `developmental_evidence_eligible=true`;
- `REFERENCE`, `ORACLE_DIAGNOSTIC`, and `CHEAT_DIAGNOSTIC` are always ineligible for developmental evidence;
- no candidate changes role by aliasing the same source under multiple IDs without explicit ablation provenance;
- C2 and C4 in SVF-1 are independently identifiable in the evidence ledger.

Violation returns `FAIL_CROSS_FIELD_INVARIANT`.

## 4. Source binding

### V2 — exact immutable subject binding

For every candidate and artifact reference, verify against GitHub or another declared immutable source route:

- repository identity;
- exact commit exists;
- exact path exists at that commit;
- declared Git blob matches when supplied;
- declared SHA-256 matches when supplied;
- candidate `source_commit` is compatible with every source artifact bound to that candidate;
- top-level `implementation_subject_commit` is the exact implementation subject intended for execution.

A branch name is not sufficient source identity.

If any mismatch is observed, return `FAIL_SOURCE_BINDING`.

If an authoritative immutable source cannot be checked, return `BLOCKED_UNAVAILABLE_EVIDENCE` rather than guessing.

### V2.1 — exact-head currentness before execution

Immediately before any separately authorized run, re-check that the executable artifacts still resolve to the frozen implementation subject.

If a PR/branch head moved after manifest freeze, the frozen commit may still be executed only if the authority receipt explicitly names that frozen commit. The moved mutable head does not silently redefine the subject.

## 5. Information-boundary validation

### V3 — learner/evaluator field disjointness

Compute the intersection of:

- `learner_visible_field_names`
- `evaluator_only_field_names`

The intersection must be empty.

If nonempty, return `FAIL_INFORMATION_BOUNDARY`.

This check is necessary even if both schema references are individually valid.

### V3.1 — schema closure

Resolve both immutable schema artifacts and verify that the declared field-name lists account for all fields that can cross their respective boundaries.

A hidden extension field, permissive `additionalProperties`, dynamic metadata bag, or transport wrapper that can carry evaluator-only information into the learner path invalidates closure unless explicitly governed.

### V3.2 — forbidden learner ingress

Verify that no learner-visible path contains:

- semantic applicability labels;
- hidden family/world identity;
- evaluator ground truth;
- evaluator score;
- future-derived training targets;
- exact physical intervention-success truth when only issued command/efference is supposed to be visible;
- stable task/regime IDs not justified as ordinary sensory/transport identity;
- post-hoc labels derived from final evaluation partitions.

Violation returns `FAIL_INFORMATION_BOUNDARY`.

### V3.3 — diagnostic isolation

A reference, oracle, or semantic-cheat diagnostic may be run only as an evaluator diagnostic. It must not share learner weights, learner state, replay, RNG state, outputs, or mutable side effects with a developmental candidate. Any shared path must be declared as a different subject, and diagnostic outputs must not enter developmental updates.

Violation returns `FAIL_INFORMATION_BOUNDARY`.

## 6. Comparator fairness

### V4 — information-condition equivalence

For the primary SVF-1 C2-versus-C4 comparison, verify that both candidates bind the same declared learner-visible information condition.

If candidate source requires preprocessing that changes learner-visible information, that change must produce a distinct information condition and the result cannot be labeled an equal-information architecture comparison.

### V4.1 — opportunity-condition equivalence

For the primary SVF-1 C2-versus-C4 comparison, verify that both candidates bind the same external world stream construction and externally scheduled intervention policy.

C4 may receive additional **audition computation** only when that opportunity is separately recorded and charged. It may not receive additional hidden world outcomes.

### V4.2 — replay-condition reconciliation

Verify that replay privilege is explicit:

- raw buffer capacity;
- replay sampling policy;
- replay update budget;
- replay target contents;
- priority provenance;
- replay compute charge.

If C4 receives richer or more frequent replay than C2, the comparison must be labeled as a different opportunity/resource condition unless a matched condition exists.

### V4.3 — C0–C4 ladder and claim boundary

Resolve the immutable `comparator_fairness_contract` artifact and apply its matrix.

For SVF-0, require independently identifiable C0, C1, and C2 entries. C0 is a persistence floor; C1/C2 must share the declared base substrate and differ only by the preregistered replay condition for the replay comparison.

For SVF-1, require C2 and C4. C2 and C4 must resolve to the same declared base-substrate contract, including initialization/state-capacity and logical update-schedule conditions, unless the manifest labels the result as a different comparison condition. A fixed-envelope claim does not waive this requirement.

If C3 is present, verify that it uses the same learner-visible stream and declared base/resource conditions as the comparison row it enters. If C3 is omitted, a future positive C4 result is limited to the explicit C2-versus-C4 whole-system claim; it may not be reported as superiority over the strongest non-scoped structural alternative without a predeclared equivalent C3 comparison.

For claim G, verify the same C4 candidate machinery, base condition, learner-visible stream, resource meter, and declared audit quota in learned-scope and bounded-audition modes; only the scope/audition policy may differ.

Violation returns `FAIL_CROSS_FIELD_INVARIANT` or `FAIL_RESOURCE_ACCOUNTING` as applicable.

## 7. Resource accounting validation

### V5 — resource fields must correspond to measurable quantities

The manifest must not use symbolic phrases such as `reasonable`, `bounded`, `small`, or `CPU-feasible` in place of the numeric fields required by the schema.

The future implementation must expose a measurement route for each declared resource axis.

### V5.1 — consumed-but-unmeasured is invalid

If a resource is consumed by the implementation but has no declared measurement/accounting route, return `FAIL_RESOURCE_ACCOUNTING`.

Do not treat unmeasured cost as zero.

This includes:

- replay compute;
- structural proposal compute;
- scope/gate inference;
- policy-decoupled audition;
- candidate probation state;
- checkpoint/restart overhead;
- durable-state growth.

### V5.2 — fixed-envelope reconciliation

For a result described as `FIXED_TOTAL_ENVELOPE`, verify from the ledger that no candidate exceeded the frozen envelope.

A run that exceeded the envelope may remain useful exploratory evidence but cannot satisfy the fixed-envelope primary claim.

### V5.3 — immutable measurement-route closure

The manifest's resource measurement method must resolve to an immutable measurement/interface artifact or an exact implementation-facing contract. Free prose such as "reasonable", "bounded", or "measured locally" is not a measurement route.

Every consumed resource class listed by the comparator contract must map to a counter, deterministic proxy, or declared exclusion. A consumed class with no route invalidates a fixed-envelope claim and returns `FAIL_RESOURCE_ACCOUNTING`.

## 8. Scope/support validation

### V6 — scope-ticket ordering

For every scored C4 scope decision, verify that the corresponding scope ticket was committed before outcome visibility.

Any post-outcome rewrite, replacement, or retroactive score correction invalidates that opportunity for preregistered scope evidence.

Repeated or systematic violations return `FAIL_SUPPORT_AUDITION_CONTRACT`.

### V6.1 — propensity provenance

Where audition/selection is stochastic, verify that the actual selection probability was recorded from the policy state that made the decision, before the outcome.

Post-hoc reconstructed propensity is not sufficient when the policy or hidden mutable state could have changed.

### V6.2 — support before confidence

For any claim of strong scope confidence, verify that the claim's region satisfies the frozen support thresholds.

`ZERO_OR_UNKNOWN_SUPPORT` can never satisfy a strong empirical scope claim.

Importance sampling, doubly robust estimation, or a learned estimator cannot override this rule.

### V6.3 — support-class claim admissibility

For a strong positive scoped claim, verify that each contributing region satisfies the frozen direct or lawful transported support rule. `DIRECT_WEAK`, `OFF_POLICY_WEAK`, `ZERO_OR_UNKNOWN_SUPPORT`, `NOT_AUDITED`, `COUNTERFACTUAL_UNOBSERVED`, unresolved, and invalidated opportunities cannot be silently counted as strong positive support. `OFF_POLICY_SUPPORTED` requires a preregistered nonzero-overlap condition and widened uncertainty; it is not equivalent to direct support.

### V6.4 — simpler audition rival

For primary learned-scope claim `G`, verify that the same candidate machinery was evaluated against the frozen simpler bounded-audition rival.

If no valid simpler-rival comparison exists, `G` is unavailable even if structural claim `S` survives.

## 9. Representation-version validation

### V7 — support intervals are representation-versioned

Verify that every scope/support record is bound to the representation version under which it was collected.

When a material representation change occurs, require one explicit disposition:

- invariant by construction;
- lawfully transported support;
- fresh relearning;
- bounded compatibility bridge.

If confidence crosses a material representation change with no disposition, return `FAIL_SUPPORT_AUDITION_CONTRACT`.

Transported support must remain distinguishable from fresh direct support.

## 10. Scoring and claim integrity

### V8 — metric/claim closure

Every `primary_metrics[*].claim` must appear in `primary_claims`.

If claim `T` is primary, `no_meta_learning_ablation` must be enabled.

If claim `G` is primary, the simpler audition rival must be enabled and ledger-complete.

### V8.1 — preregistered metric immutability

After freeze, primary scoring rule, aggregation, support threshold, confidence method, stopping rule, and kill criteria cannot change for the same subject.

Any change creates a new subject.

Post-result analyses under altered metrics must be marked exploratory.

### V8.2 — missingness integrity

Verify that these states are not collapsed:

- success;
- failure;
- `NOT_AUDITED`;
- `COUNTERFACTUAL_UNOBSERVED`;
- unresolved outcome;
- invalidated opportunity.

Missing negative evidence cannot be silently counted as success.

## 11. Restart integrity

### V9 — checkpoint completeness

If checkpointing is used and restart equivalence is claimed, verify that persisted state includes:

- outstanding prediction/action/scope tickets;
- unresolved outcomes;
- assignment RNG state;
- adaptive audit-policy state;
- support intervals;
- representation-version boundaries;
- stopping-rule state.

Loss of required state forfeits restart equivalence.

If any required restart state is missing, quarantine the affected run from primary trajectory claims. Continuing after the loss requires a new run identity or a separately predeclared recovery protocol with its own validity conditions; a reviewer may not restore restart equivalence by asserting that the missing state was probably irrelevant.

## 12. Freeze integrity

### V10 — freeze occurs before outcome visibility

The manifest must be frozen before final scored outcomes are visible to the parties allowed to change the experiment subject.

### V10.1 — no self-hash circularity

The manifest need not contain its own final blob/hash.

Instead, use a later immutable freeze receipt at the manifest's declared locator. The receipt must bind at minimum:

- repository;
- manifest path;
- exact manifest commit;
- exact manifest Git blob;
- exact implementation subject commit;
- schema version;
- freeze timestamp;
- experiment logical ID.

The receipt itself is not execution authority.

### V10.2 — mutation after freeze

Any change to the frozen manifest's candidate source, information boundary, world generator, randomization/seed commitment, resources, scoring, support thresholds, controls, stopping rule, or acceptance criteria creates a new subject.

Do not amend the old subject in place and retain its old evidence identity.

## 13. Authority separation

### V11 — validation is not authorization

`PASS_FROZEN_VALID` proves only that the preregistration subject is internally/referentially valid under this contract.

It does not authorize:

- model training;
- experiment execution;
- paid/hosted compute;
- merge;
- deployment;
- publication;
- provider or credential changes;
- repository visibility changes;
- connection to protected systems.

A future runner must require a separate exact execution-authority receipt naming the frozen subject.

## 14. Adversarial validator tests

Before validator implementation is trusted, it should fail fixtures for at least:

- duplicate `candidate_id` with otherwise different objects;
- C4 evaluator-only field smuggled through a permissive metadata bag;
- candidate source commit/path/blob mismatch;
- C2/C4 different learner-visible preprocessing under the same claimed information condition;
- C4 replay buffer enriched with evaluator labels;
- uncharged scope/audition compute;
- scope ticket created after outcome visibility;
- propensity reconstructed after policy update;
- strong scope claim under zero support;
- old support inherited across representation drift with no continuity disposition;
- `NOT_AUDITED` outcomes counted as candidate successes;
- transfer claim without no-meta-learning ablation;
- learned-scope claim without simpler audition rival;
- restart missing unresolved tickets;
- changed stopping rule after freeze;
- freeze receipt bound to the wrong manifest blob;
- exact valid manifest presented with no separate execution authority.

The last fixture must validate the manifest but still block execution.

## 15. Exact next frontier

After this contract, the remaining research-only gap is not another conceptual mechanism. It is a **non-executable example manifest fixture set**:

1. one minimal valid SVF-0 fixture;
2. one minimal valid SVF-1 fixture;
3. a small set of intentionally invalid fixtures corresponding to the highest-risk validator attacks.

Those fixtures can test whether the schema and validator contract are unambiguous without implementing or running Noema.
