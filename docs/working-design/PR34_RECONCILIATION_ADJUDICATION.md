# PR #34 Reconciliation Adjudication

Classification: **IP_CONFIDENTIAL**

Status: **EXACT-HEAD CANONICAL RECONCILIATION / PASS FOR RESEARCH-CONTRACT CLOSURE / IMPLEMENTATION AUTHORITY REMAINS CLOSED / NOT BT2 R1 REMEDIATION**

Adjudication date: 2026-09-13

Canonical repository: `thebrazenbeard/noema`

Canonical PR: `#32 — Research scope continuity and structural-value falsification`

Reviewed canonical exact head: `a419bf48721397c593cb04867823048ea01467a3`

Prior canonical handoff-adjudication head: `0cb5cee6e28b9769e1b279447b91ba8cbcf98c9c`

Stacked repair PR: `#34 — Close V2 exact-source and measurement binding gaps`

Stacked repair head: `d367ee701be9f0650797bd586cc24448d39bc55e`

Stacked repair independently reviewed parent: `dcf772514b1ee6056f9b1a9588d068cee789f120`

Verdict: **PASS / PR #34 REPAIRS RECONCILED ONTO CANONICAL PR #32 / RESEARCH-CONTRACT + HANDOFF BOUNDARY CLOSED / NO I0, I1, E0, OR P0 AUTHORITY GRANTED**

## 1. Why reconciliation was required

PR #34 was created as a private stacked research repair while the mutable PR #32 branch was moving. Its recorded base therefore became stale before the repair could be treated as an exact-head canonical review subject.

The correct response is not to carry PR #34's PASS label forward by assumption and not to merge the stacked PR. Its findings and repaired bytes must be checked against the current canonical line, imported deliberately where valid, and then rebound to a new exact canonical head.

## 2. Independent findings disposition

PR #34's independent hostile review identified five bounded defects in the then-current V2 preregistration layer.

### H1 — exact schema/validator/addendum bytes were not manifest-bound

**VALID FINDING / REPAIRED.**

A logical version string is insufficient provenance. The repaired V2 subject now binds immutable references for the exact schema, validator, fairness, resource, decidability, comparator-matrix, and comparator-interface artifacts used to adjudicate the subject.

### H2 — implementation subject could not be mechanically distinguished from design-only source

**VALID FINDING / REPAIRED.**

A future V2 subject now requires an immutable implementation-subject manifest. The source-binding validator addendum requires that manifest to identify real source/interface/instrumentation/hostile-test artifacts and rejects or blocks a documentation-only commit as developmental implementation provenance.

This still does not create an implementation subject on the current research line.

### H3 — lineage state-scope requirement was not locatable

**VALID FINDING / REPAIRED.**

The V2 lineage contract already required state-scope accounting. The repair makes that existing obligation immutable and locatable through `state_scope_manifest_artifacts`; it does not add a new scientific claim.

### H4 — resource measurement route was not immutably bound

**VALID FINDING / REPAIRED.**

A prose measurement method is not enough for an exact fixed-envelope claim. The repaired V2 resource contract binds an immutable measurement artifact, and the source-binding addendum requires the relevant resource classes, allocation behavior, missingness, and invalidation behavior to be independently decidable.

### H5 — two SVF-1 requirements remained schema-fail-open

**VALID FINDING / REPAIRED.**

For SVF-1, the schema now requires the non-null observational-equivalence verification object and a strictly positive simple-audition probability when the simple rival is required.

This is not an evaluator oracle. Experiment A already specifies a first world whose passive chain/fork distributions are analytically identical by construction; the additional numerical verification is evaluator-side generator-integrity evidence. It is not learner-visible semantic information.

## 3. Imported canonical delta

The repaired source-contract bytes from PR #34 were imported onto canonical PR #32 in commit `8856f8b75407f3ad2bde5783df970128664606d2`.

That commit changed exactly five implementation-facing research files:

- `C2_C4_COMPARATOR_INTERFACE_CONTRACT.md`;
- `EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V2.json`;
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_CONTRACT_V2.md`;
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_SOURCE_BINDING_ADDENDUM.md`;
- `MINIMAL_STRUCTURAL_VALUE_FALSIFICATION_FAMILY.md`.

The corresponding blob bytes are the repaired PR #34 bytes. PR #34's stale-head hostile-review and recheck records were **not** copied onto the canonical line as if they had reviewed the later PR #32 head.

PR #34 remains open/draft/unmerged historical provenance unless separate authority or its owning lane changes it.

## 4. Independent repair evidence preserved

PR #34's repair recheck reviewed exact repaired parent `dcf772514b1ee6056f9b1a9588d068cee789f120` and recorded PASS for the bounded research repair.

A direct comparison from that reviewed parent to PR #34 head `d367ee701be9f0650797bd586cc24448d39bc55e` shows exactly one added file: the recheck record itself. Therefore the repaired contract bytes imported into canonical PR #32 are the bytes that existed on the independently reviewed repaired parent, not later unreviewed mutations.

That independent evidence is supporting provenance. The current verdict is nevertheless rebound here to canonical exact head `a419bf48721397c593cb04867823048ea01467a3` rather than inherited from the stale stacked PR.

## 5. Canonical handoff dependency refresh

Importing the new source-binding addendum made the previously adjudicated implementation handoff's explicit normative-input list stale by one artifact.

Commit `a419bf48721397c593cb04867823048ea01467a3` corrects that currentness defect by adding exactly `EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_SOURCE_BINDING_ADDENDUM.md` to `IMPLEMENTATION_SOURCE_HANDOFF_NORMATIVE_INPUTS_ADDENDUM.md`.

No authority state changed. The handoff remains inert and the runtime/framework choice remains unresolved.

## 6. Exact canonical delta check

Comparison from prior canonical head `0cb5cee6e28b9769e1b279447b91ba8cbcf98c9c` to reviewed head `a419bf48721397c593cb04867823048ea01467a3` is two commits, zero divergence, and six changed files:

- the five reconciled PR #34 research-contract files above; and
- the one-line normative-input refresh.

There is still no `src/` implementation tree, no `tests/` implementation tree, no approved runtime/framework, no real implementation-subject manifest, and no executable developmental candidate on the canonical research line.

## 7. Scientific and claim-boundary check

**PASS.**

The reconciliation strengthens exact provenance and fail-closed validation without changing the intended scientific falsifier:

- C0 remains an optional persistence floor rather than a mandatory SVF-0 member;
- C1/C2 remain the persistence/replay substrate comparison;
- C2 remains the primary simpler rival for C4;
- C3 remains optional for the smallest negative C2/C4 falsifier but controls stronger positive claim ceilings;
- C4 remains bounded and cannot receive privileged semantic answers;
- learner-visible and evaluator-only information remain separated;
- support, replay, resource, restart, representation-drift, and pre-outcome commitment obligations survive;
- V1 remains historical provenance, not current validation authority.

## 8. Implementation handoff check

**PASS.**

The implementation-source handoff remains coherent after the source-binding repair. In fact, the repaired V2 contract now gives a future source lane a mechanically stronger target for the implementation-subject manifest and resource instrumentation already required by that handoff.

The project still deliberately has not selected a programming language, numerical/ML framework, optimizer, serialization stack, or package topology.

## 9. Frozen BT2 R1 separation

**PASS.**

This reconciliation is successor private research only. It does not alter, remediate, reinterpret, or requalify the frozen BT2 R1 subject or any frozen reviewer verdict.

## 10. Authority ceiling

This PASS establishes only that the current private research contract and the boundary for a future source lane are coherent after PR #34 reconciliation.

It does **not** authorize:

- implementation source creation;
- deterministic source-test execution;
- learner-state updates;
- model training;
- SVF-0/SVF-1 experiment execution;
- hosted or paid compute;
- merge of PR #32, PR #33, or PR #34;
- deployment;
- publication;
- provider/credential/ruleset mutation;
- repository-visibility change;
- protected-system connection.

## 11. Exact conclusion

**PASS / CANONICAL RESEARCH CLOSURE.**

At reviewed exact head `a419bf48721397c593cb04867823048ea01467a3`, the known PR #34 source-binding and measurement gaps are closed on canonical PR #32, and the implementation handoff has been refreshed to include the new normative addendum.

The next material frontier is now genuinely an authority transition: a separately authorized I0 implementation-source lane, optionally accompanied by explicitly authorized I1 deterministic non-learning source verification. E0 learning/experiment execution and P0 protected effects remain separate later gates.
