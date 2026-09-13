# PR #32 Post-Adjudication Independent Hostile Review

Classification: **IP_CONFIDENTIAL**

Status: **EXACT-HEAD HOSTILE REVIEW / REPAIR REQUIRED FOR FUTURE MANIFEST BINDING / NOT IMPLEMENTATION AUTHORITY / NOT BT2 R1 REMEDIATION**

Review date: 2026-09-13

Reviewed repository: `thebrazenbeard/noema`

Reviewed base: `main@890efdca01cf496ce1b8686d86f8442a149a9d34`

Reviewed successor subject: `PR #32` research line at exact head `93e846927c3b5dcabb94da0da5b803d0076b4971`

This is an independent recheck after the prior exact-head adjudication at `8238d38fe752dcef38a85207d42d1dbfd9e5eb6c` and the later matrix/addendum commits. It preserves the earlier adjudication as historical provenance; it does not rewrite it.

## 1. Verdict

The research direction and the C0–C4 fairness/claim-boundary principles remain coherent. The machine-bound preregistration layer is **not yet closed for a future exact frozen manifest** because several authoritative artifacts and future source-subject distinctions remain addressable only by prose, a version label, or a boolean.

No implementation, model training, experiment execution, hosted/paid compute, publication, merge, deployment, provider/credential/ruleset mutation, or protected-system connection was performed.

## 2. Blocking findings

### H1 — schema/validator/addendum currentness is not manifest-bound

The V2 manifest carries a schema version and logical ID, while the freeze receipt binds a schema version, but the manifest has no required immutable artifact references for the exact schema, validator, fairness matrix, resource addendum, decidability addendum, comparator-matrix addendum, or comparator interface used for adjudication.

Consequence: a later artifact at the same V2 logical/version label could change the validation subject without changing the manifest's visible schema-version text. Exact-head review and post-freeze repeatability then depend on an implicit tool route.

Required direction: bind named immutable repository/commit/path references for the exact schema and every normative validator/addendum contract used by the subject; validator resolution must reject unavailable or mismatched bytes.

### H2 — an implementation subject is not mechanically distinguished from design-only source

V2 requires an `implementation_subject_commit` and source artifact references, but it does not require a machine-readable implementation-subject manifest that enumerates actual source entrypoints, comparator instrumentation, and hostile-test artifacts. A design-only commit could therefore be presented as the implementation subject if its declared artifacts are only working-design documents.

Consequence: the “no fake implementation fixture” rule is stated, but the future source-binding boundary is not yet mechanically decidable.

Required direction: bind an immutable implementation-subject manifest and require validator evidence that it names real implementation/interface/instrumentation/test artifacts; design-only artifacts cannot satisfy developmental source binding.

### H3 — lineage state-scope manifests are required in prose but not bound in V2

The lineage contract and V2 validator require a state-scope manifest for carried/reset conditions, but `lineage_transfer_contract` currently contains only the boolean `state_scope_manifest_required`; it has no immutable manifest locator list.

Consequence: claim T can carry/reset state under an unlocatable scope description, reopening transfer/reset ambiguity and making the claim impossible to reproduce exactly.

Required direction: bind one or more immutable state-scope manifest artifact references and validate coverage of every declared carried/reset condition.

### H4 — resource measurement remains a free-form route

V2 has a free-form `measurement_method` string and a decidability addendum, but no immutable measurement-contract/instrumentation artifact that enumerates the resource classes, shared-overhead allocation, and missing-measurement behavior.

Consequence: a future fixed-envelope subject can state that measurement is decidable while leaving the actual meter and allocation procedure outside the frozen source binding; replay, scope, base-shadow, checkpoint, or durable-state work could still be subsidized.

Required direction: bind an immutable measurement artifact and require it to cover every resource class relevant to the claim; consumed-but-unmeasured remains ineligible for fixed-envelope PASS.

### H5 — two SVF-1 stage requirements remain schema-fail-open

The V2 stage prose requires observational-equivalence verification and a usable simple-audition condition, but the schema's general definitions permit `observational_equivalence_verification: null` and `simple_audition_probability: null` while the stage condition only forces `intervention_mode` and `simple_audition_rival_required`.

Consequence: shape validation can admit a stage shape that is later rejected only if every validator implementation interprets “present” strictly. The machine contract should fail closed at the schema boundary as well.

Required direction: constrain SVF-1 verification to the non-null object form and require a strictly positive audition probability whenever the stage requires the simple rival.

## 3. Surviving controls

The following remain materially sound and should be preserved:

- pre-outcome prediction/scope tickets;
- separated learner-visible and evaluator-only planes;
- missingness and counterfactual status;
- zero-support prohibition;
- representation-versioned support;
- replay enrichment prohibition;
- C2/C4 base and condition fairness rules;
- C0 floor and C3 claim ceilings from the matrix/addendum;
- learned-scope versus bounded-audition claim G;
- resource-frontier separation;
- restart quarantine and V2 no-checkpoint primary rule;
- explicit authority separation and frozen BT2 R1 boundary.

## 4. Repair boundary

The repair should remain research-only and private:

- add exact artifact bindings to the V2 manifest shape;
- add state-scope and resource-measurement bindings;
- tighten SVF-1 schema conditions;
- extend the V2 validator contract with corresponding checks;
- preserve all historical V1/V2 reviews and prior adjudications;
- do not fabricate a valid implementation subject or execute a model.

A repaired head still cannot produce `PASS_FROZEN_VALID` until a separately authorized real implementation subject exists.

## 5. Claim ceiling

This review supports only the finding that the research contracts are close but require the bounded closure above. It does not support implementation readiness, training, execution, merge, deployment, publication, or any BT2 R1 conclusion.
