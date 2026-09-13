# PR #32 Successor Research Hostile Review

Classification: **IP_CONFIDENTIAL**

Status: **EXACT-HEAD HOSTILE REVIEW / REPAIR REQUIRED / NOT IMPLEMENTATION AUTHORITY / NOT BT2 R1 REMEDIATION**

Review date: 2026-09-13

Reviewed repository: `thebrazenbeard/noema`

Reviewed base: `main@890efdca01cf496ce1b8686d86f8442a149a9d34`

Reviewed PR: `#32 — Research scope continuity and structural-value falsification`

Reviewed head: `e282369e13f9ea801a2964665dc4062cd38b8ea9`

Exact-head verdict: **FAIL / REPAIR REQUIRED BEFORE THE PREREGISTRATION LAYER CAN BE TREATED AS INTERNALLY COHERENT**

This verdict is intentionally narrower than a rejection of the successor research direction. The representation-drift, prequential-scope, ledger, falsification-family, and comparator principles are substantially convergent. The failure is in cross-contract closure: the machine preregistration layer still encodes several semantics that contradict the experiment family or leave evaluator-subsidy paths open.

No implementation or experiment execution was performed for this review.

## 1. Review scope

This hostile pass treated the PR as one coupled design rather than reviewing each artifact in isolation.

Primary PR artifacts reviewed:

- `REPRESENTATION_DRIFT_SCOPE_CONTINUITY_CONTRACT.md`
- `PREQUENTIAL_SCOPE_APPLICABILITY_CONTRACT.md`
- `EXPERIMENT_SCOPE_SUPPORT_AND_AUDITION_LEDGER.md`
- `MINIMAL_STRUCTURAL_VALUE_FALSIFICATION_FAMILY.md`
- `EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V1.json`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_CONTRACT.md`
- `C2_C4_COMPARATOR_INTERFACE_CONTRACT.md`

Existing canonical contracts cross-checked include:

- `CAPABILITY_EVIDENCE_ROADMAP.md`
- `EPISTEMIC_FIRST_EXPERIMENT_DECISION.md`
- `EXPERIMENT_A_DESIGN.md`
- `EXPERIMENT_A_ONLINE_PROTOCOL.md`
- `EXPERIMENT_A_CORE_REALIZATION_OPTIONS.md`
- `ONLINE_LEARNING_STATE_TRANSITION_CONTRACT.md`
- `EXPERIMENT_LINEAGE_AND_STATE_TRANSFER_CONTRACT.md`

## 2. Blocking finding H1 — SVF-0 is forced to claim the wrong thing

`MINIMAL_STRUCTURAL_VALUE_FALSIFICATION_FAMILY.md` defines SVF-0 as a Gate-1 persistent-online-learning sanity gate whose serious mandatory comparison is C1 versus C2. C4 is explicitly not entitled to structural credit merely for passing it.

But schema V1 conditionally forces SVF-0 `primary_claims` to contain only `S`, while claim `S` is defined by the falsification family as **structural predictive value** after decisive evidence.

The same schema globally forces `c2_vs_c4_external_comparison_required=true` even though the SVF-0 candidate constraint requires C1 and C2, not C4.

This is not cosmetic. A schema-valid SVF-0 subject can be required to make a structural claim against a candidate it need not contain.

Required repair:

- introduce a distinct Gate-1 claim such as `P` for persistent-online/replay-baseline qualification;
- make SVF-0 require C1+C2 and claim `P`;
- make the C2-vs-C4 external comparison requirement stage-specific to SVF-1, not global.

## 3. Blocking finding H2 — the externally scheduled intervention can still be an evaluator oracle

Experiment A and SVF-1 rely on the intervention being externally scheduled so C2 and C4 can share the same realized world stream without action-policy confounding.

Schema V1 permits `intervention_schedule_commitment` to be null and does not require an immutable schedule-policy artifact or a declaration that schedule generation is independent of hidden family identity and scored outcomes.

That leaves a valid-looking manifest able to choose intervention timing/values adaptively from evaluator-only truth. The learner may never see the hidden label, yet the schedule itself can leak or subsidize the answer through opportunity selection.

Required repair:

- SVF-1 must bind an immutable intervention-schedule artifact/policy and commitment before outcome visibility;
- the schedule policy must declare that hidden family identity, candidate predictions, scored outcomes, and evaluator diagnostics cannot adapt the schedule unless a new experiment subject explicitly studies such adaptation;
- validator source binding must verify the schedule artifact/commitment.

## 4. Blocking finding H3 — C2/C4 base-substrate fairness is asserted but not closed

The falsification family says C4 consists of the same declared base substrate class used by the fair simpler rival plus structural machinery.

Schema V1 provides an optional `base_substrate_id` but does not require it for C2/C4 and cannot establish equality across the candidates. Validator V4 checks information, opportunity, and replay conditions but does not explicitly require matched base-substrate identity/configuration for an architecture-only C2/C4 claim.

Therefore C4 could use a stronger recurrent backbone and attribute the gain to structural machinery.

Required repair:

- C2 and C4 must bind explicit base-substrate identities/artifacts;
- equal-condition primary structural claims require validator proof that the declared base substrate and non-structural learner configuration are matched, except for explicitly isolated structural differences;
- a different base substrate creates a different architecture condition and cannot support the narrow structural-marginal claim.

## 5. Blocking finding H4 — ablation/variant provenance is demanded but not representable

Validator V1 correctly forbids aliasing the same source under multiple candidate IDs without explicit ablation provenance.

But schema V1 has no field that can encode `ablation_of`, `variant_of`, or an equivalent parent candidate relationship.

This matters directly to the learned-scope claim `G`, which requires the **same candidate machinery** under learned scope and a simpler bounded-audition policy.

Required repair:

- add machine-readable candidate-variant provenance;
- validator must verify that the learned-scope and simple-audition variants share the same structural candidate/base implementation and differ only in the preregistered scope/audition dimension for claim `G`.

## 6. Material finding H5 — transfer claim T does not bind cross-world carried state tightly enough

Claim `T` asks whether C4 transfers structural value to surface-remapped worlds with less evidence/cost.

The canonical lineage/state-transfer contract requires evaluator-side provenance for copied/restored/continued state, exact state artifacts where applicable, world-frontier relationships, and what learner-visible consequences accompany state transfer.

Schema V1 has no explicit cross-world lineage/state-transfer contract. A future run could accidentally compare:

- C4 carrying candidate/meta-learning state across worlds;
- C2 reset or carrying a different state scope;

and call the difference structural transfer.

Required repair:

- when `T` is primary, freeze the state-carryover policy and exact state-scope/lineage condition for each candidate;
- C2 and C4 must have matched continuation/reset opportunity except for the structural state dimension explicitly under test;
- evaluator lineage IDs remain E1 and must not leak to the learner.

## 7. Material finding H6 — replay/resource condition identifiers are not reconciled strongly enough

Schema candidates carry `resource_condition_id` and `replay_policy_id`, while the top-level resource contract separately carries resource/replay limits.

Validator V4.2 requires replay reconciliation in prose but does not require exact equality between C2/C4 condition IDs for a fixed-condition structural claim, nor consistency between candidate `replay_policy_id` and the top-level replay policy.

Required repair:

- equal-condition claims require matching information, opportunity, resource, and replay condition IDs;
- those IDs must resolve to the actual frozen contracts used by the run;
- a candidate-specific deviation must produce a different comparison condition rather than being silently accepted.

## 8. Material finding H7 — restart schema semantics overstate persistence when checkpointing is absent

Schema V1 requires all `persist_*` restart fields to be `true` even if `checkpointing_used=false` or `restart_equivalence_claimed=false`.

The validator text is more precise: completeness is required when checkpointing/restart equivalence is actually claimed.

The schema therefore conflates `this run does not checkpoint` with `all checkpoint state is persisted`.

Required repair:

- make restart-state persistence conditional on checkpointing/restart-equivalence claims;
- if no restart-equivalence claim is made, the manifest must say so directly rather than asserting nonexistent persistence;
- if checkpointing is used but restart equivalence is not claimed, preserve enough provenance to classify resumed evidence correctly.

## 9. Material finding H8 — commitment hashes without immutable preimage locators are not fully auditable

Schema V1 binds parameter-distribution and seed commitments as SHA-256 strings but does not require immutable artifact locators for the committed preimages.

A hash is strong only if the validator can later obtain the exact committed bytes/rules that produced it.

Required repair:

- bind parameter-distribution, seed/randomization, and intervention-schedule commitments to immutable artifact references or another explicitly retrievable commitment mechanism;
- validator must classify unavailable authoritative preimages as `BLOCKED_UNAVAILABLE_EVIDENCE`, not infer them from prose.

## 10. Material finding H9 — metric/comparator references remain weakly typed

Schema V1 does not require unique `metric_id` values, and metric `comparator` is an arbitrary nonempty string.

A preregistered metric could therefore reference a nonexistent or ambiguous comparator without failing schema validation.

Required repair:

- validator must require metric IDs unique by key;
- each primary comparator reference must resolve to a frozen candidate/variant or an explicitly allowed diagnostic comparator;
- primary metrics must reference claim-compatible comparator roles.

## 11. Material finding H10 — negative-control existence is frozen, but the null expectation is not

SVF-1 correctly requires negative structural-value worlds. But the schema does not freeze what outcome on those controls would invalidate the structural interpretation.

Without a preregistered negative-control acceptance/null rule, the evaluator can rationalize structural overhead or apparent advantage after seeing results.

Required repair:

- freeze negative-control metrics and the rule distinguishing acceptable bounded overhead from false structural advantage/destructive search;
- post-result reinterpretation is exploratory, not part of the primary structural claim.

## 12. Stale finding H11 — validator next frontier contradicts later provenance discipline

The validator contract says the next research-only gap includes a `minimal valid SVF-0 fixture` and `minimal valid SVF-1 fixture`.

Later PR work correctly recognizes that a truly `PASS_FROZEN_VALID` fixture cannot be fabricated without a real immutable implementation subject.

Required repair:

- replace `valid fixture` language with **schema-shape exemplars explicitly barred from PASS**, or wait until a real implementation subject exists;
- intentionally invalid hostile fixtures remain lawful research artifacts because they do not pretend to bind execution-ready provenance.

## 13. Nonblocking observations

The following parts survived this pass and should be preserved:

- pre-outcome prediction and scope tickets;
- strict separation of learner-visible and evaluator-only planes;
- explicit missingness states;
- zero-support cannot become evidence via an estimator;
- representation-versioned scope support;
- candidate/base snapshot isolation;
- distinction between external C2/C4 comparison and C4 internal base-shadow diagnostics;
- replay enrichment prohibition;
- resource-performance frontier separated from equal-resource claims;
- learned gating required to embarrass itself against simpler bounded audition;
- validation explicitly separated from execution authority;
- immutable commit rather than mutable branch head as execution subject.

## 14. Repair ordering

Repair in this order:

1. supersede schema V1 with a corrected V2 rather than silently pretending the reviewed V1 was always correct;
2. supersede/amend the validator so every new V2 cross-field invariant has an explicit check;
3. bind transfer/lineage policy for claim `T`;
4. run a new exact-head hostile review of the repaired research subject;
5. only after research closure consider requesting separate implementation-source authority.

## 15. Authority / frozen-R1 boundary

This review does not authorize implementation, training, experiment execution, paid/hosted compute, merge, deployment, publication, provider/credential/ruleset changes, repository-visibility changes, or protected-system connection.

It also does not alter the frozen BT2 R1 subject or any R1 verdict.

## 16. Exact-head disposition

`e282369e13f9ea801a2964665dc4062cd38b8ea9` is **not research-closed** for preregistration readiness.

The next available frontier remains research-only: create the corrected V2 schema/validator contract and then re-review that exact successor head.