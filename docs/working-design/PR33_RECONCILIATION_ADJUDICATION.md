# PR #33 Fairness-Repair Reconciliation Adjudication

Classification: **IP_CONFIDENTIAL**

Status: **EXACT-HEAD RECONCILIATION / CANONICAL PR #32 RETAINS RESEARCH-CONTRACT PASS / PR #33 NOT MERGED / IMPLEMENTATION GATE CLOSED / NOT BT2 R1 REMEDIATION**

Date: 2026-09-13

Canonical repository: `thebrazenbeard/noema`

Canonical successor PR: #32

Canonical head reviewed for this reconciliation: `93e846927c3b5dcabb94da0da5b803d0076b4971`

Stacked repair reviewed: PR #33 head `d73db33295810623de93e2fe24eead32f26738dc`

PR #33 historical base: PR #32 at `e282369e13f9ea801a2964665dc4062cd38b8ea9`

Verdict: **RECONCILED / USEFUL CONSTRAINTS ADOPTED ON CANONICAL PR #32 / ONE PROPOSED RULE REJECTED AS OVER-CONSTRAINT / PR #33 DOES NOT NEED MERGE FOR RESEARCH CLOSURE**

## 1. Why reconciliation was required

PR #33 was created concurrently from an older PR #32 head while the canonical line was undergoing a separate hostile review and V2 preregistration repair.

Blindly merging #33 would have reintroduced edits to V1 schema/validator artifacts that are now superseded for future preregistration use by V2. Blindly ignoring #33 would have discarded useful whole-ladder fairness constraints.

This adjudication therefore compares the stacked repair semantically rather than treating branch ancestry as authority.

## 2. Adopted from PR #33

The following ideas were materially useful and are now represented on canonical PR #32 through `C0_C4_FAIR_COMPARISON_AND_CLAIM_BOUNDARY_MATRIX.md` plus `EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_COMPARATOR_MATRIX_ADDENDUM.md`:

- explicit C0-C4 comparison/claim ceilings;
- C0 treated as a weak persistence floor, not a serious structural rival;
- C1/C2 base parity for replay claims;
- C2/C4 base-substrate parity for structural marginal claims;
- C3 omission limiting the interpretation of a positive C4-over-C2 result;
- a stronger C3-versus-C4 comparison required before claiming superiority over non-scoped structural alternatives;
- learned-scope versus bounded-audition variant identity for claim G;
- total retained-state accounting rather than raw replay-buffer accounting alone;
- strong isolation of oracle/reference/semantic-cheat diagnostics from developmental state;
- support-class claim discipline;
- restart evidence cannot be rescued by qualitative assertion after required state is lost;
- held-out intervention claims must respect the claim's actual generalization level.

These constraints were adapted to the V2 preregistration/validator line rather than applying PR #33's patches to superseded V1.

## 3. Rejected proposed rule — mandatory C0 in every SVF-0 manifest

PR #33 proposed making C0, C1, and C2 all mandatory in SVF-0.

That rule is **rejected as an unnecessary strengthening of the canonical minimal falsifier**.

`MINIMAL_STRUCTURAL_VALUE_FALSIFICATION_FAMILY.md` defines C0 as a deliberately weak floor and defines SVF-0's required observations around C1 persistence and C2 replay value. Its kill condition is whether C1/C2 satisfy Gate-1 persistence.

Therefore the reconciled rule is:

- C0 is useful and may be included to establish a persistence/system-identification floor;
- when present, its claim ceiling is narrow;
- absence of C0 does not invalidate an otherwise valid SVF-0 C1/C2 subject.

This preserves the project's stated preference for the weakest experiment that can falsify the architecture claim.

## 4. V1 edits from PR #33 are not normative

PR #33 modifies:

- `EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V1.json`;
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_CONTRACT.md`.

Those artifacts are historical provenance after the canonical V2 repair.

Future preregistration use is governed by:

- `EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V2.json`;
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_CONTRACT_V2.md`;
- V2 resource, decidability, and comparator-matrix addenda.

Therefore applying #33's V1 mutations to the canonical line would create two competing normative preregistration tracks and is rejected.

## 5. C3 claim ceiling after reconciliation

C3 remains optional for the smallest negative C2-versus-C4 falsifier.

Interpretation is now explicit:

- C2 >= C4 can falsify C4 for the tested family without C3;
- C4 > C2 without C3 supports only the narrow whole-system result against the tested recurrent+replay rival;
- a claim that scoped/explicit structure beats stronger non-scoped structural alternatives requires a preregistered C3 or equivalent comparison.

This prevents a cheap falsifier from becoming an overbroad positive claim.

## 6. Diagnostic isolation after reconciliation

Reference/oracle/semantic-cheat diagnostics may share immutable evaluator-side world schedules but may not share mutable learner weights, recurrent state, replay, RNG, optimizer, candidate state, scope/support state, or update-producing outputs with developmental candidates.

This rule is now explicitly part of V2 validation through the comparator-matrix addendum.

## 7. Resource interpretation after reconciliation

The canonical line now treats all evidence-retaining causal state as resource-relevant when consumed.

Equal raw replay capacity does not establish equal memory conditions when a candidate additionally retains structural snapshots, anchors, traces, support maps, transport state, or other persistent evidence elsewhere.

This is compatible with the existing one-manifest/one-fixed-envelope resource contract and preregistered resource-frontier series.

## 8. PR #33 disposition

PR #33 remains private, draft, open, and unmerged as provenance at the time of this adjudication.

No merge is required to preserve its useful findings because those findings have been reconciled onto the canonical PR #32 line in V2-native form.

This adjudication does not close or delete #33 because another project worker created that bounded lane and it may be useful as historical review provenance.

## 9. Effect and authority boundary

The reconciliation changes no effect authority.

It does not authorize implementation, validator code, training, experiment execution, paid/hosted compute, merge of PR #32 or #33, deployment, publication, provider/credential/ruleset mutation, repository-visibility change, or protected-system connection.

Frozen BT2 R1 remains separate and unchanged.

## 10. Research-contract status

No new research-blocking contradiction was introduced by the PR #33 reconciliation.

Canonical PR #32 remains **RESEARCH-CONTRACT READY FOR HANDOFF TO A SEPARATELY AUTHORIZED IMPLEMENTATION-SOURCE LANE**, subject to exact-head review semantics.

The only changes above the prior research PASS are the reconciled matrix, its V2 validator addendum, and this adjudication record; they strengthen claim ceilings and fairness constraints without relaxing the prior evidence burden.

## 11. Next frontier

The next frontier remains implementation-source work, not another conceptual mechanism layer:

> Build the smallest concrete C1/C2 recurrent probabilistic substrate and C4 candidate implementation, comparator instrumentation, V2 validator tooling, and hostile unit tests under separate implementation authority; keep training/execution separately gated.
