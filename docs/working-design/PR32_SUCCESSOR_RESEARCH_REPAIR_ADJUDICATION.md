# PR #32 Successor Research Repair Adjudication

Classification: **IP_CONFIDENTIAL**

Status: **EXACT-HEAD RESEARCH ADJUDICATION / PASS FOR RESEARCH-CONTRACT HANDOFF / IMPLEMENTATION GATE REMAINS CLOSED / NOT BT2 R1 REMEDIATION**

Adjudication date: 2026-09-13

Reviewed repository: `thebrazenbeard/noema`

Reviewed base: `main@890efdca01cf496ce1b8686d86f8442a149a9d34`

Reviewed PR: `#32 — Research scope continuity and structural-value falsification`

Reviewed exact head: `8238d38fe752dcef38a85207d42d1dbfd9e5eb6c`

Verdict: **PASS / RESEARCH CONTRACT READY FOR HANDOFF TO A SEPARATELY AUTHORIZED IMPLEMENTATION-SOURCE LANE**

This PASS means only that the successor research contracts are internally coherent enough to define the evidence, fairness, preregistration, and comparator obligations for a future implementation subject. It does not authorize implementation, training, experiment execution, paid/hosted compute, merge, deployment, publication, provider/credential/ruleset changes, repository-visibility changes, or protected-system connection.

No real implementation subject exists in this research lane. Therefore no experiment manifest has or can honestly receive `PASS_FROZEN_VALID` yet.

## 1. Parent hostile-review disposition

The earlier exact-head review of `e282369e13f9ea801a2964665dc4062cd38b8ea9` returned **FAIL / REPAIR REQUIRED** and recorded H1-H11 in `PR32_SUCCESSOR_RESEARCH_HOSTILE_REVIEW.md`.

This adjudication rechecks those defects against the repaired exact head rather than carrying the old FAIL forward by assumption.

## 2. H1 — SVF-0 claim/comparator contradiction

**RESOLVED.**

`EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V2.json` introduces claim `P` for the Gate-1 persistent-online/replay baseline.

V2 requires SVF-0 to contain C1 and C2, constrains its primary claim to `P`, requires no world intervention, and sets C2-vs-C4 external comparison to false.

The V2 validator independently rechecks those stage semantics.

## 3. H2 — externally scheduled intervention could act as evaluator oracle

**RESOLVED.**

SVF-1 V2 requires an immutable intervention schedule artifact plus commitment and requires the schedule not to adapt to:

- hidden family identity;
- candidate predictions;
- scored outcomes;
- evaluator diagnostics.

The V2 validator resolves the schedule artifact/commitment and checks that externally scheduled intervention is non-oracular.

## 4. H3 — C2/C4 base-substrate fairness not closed

**RESOLVED.**

V2 requires base-substrate identity for C1/C2/C4 candidates. The V2 validator requires matched C2/C4 base substrate and non-structural base configuration for a narrow structural-marginal claim.

A stronger C4 backbone becomes a different architecture condition rather than structural evidence.

## 5. H4 — ablation/variant provenance not representable

**RESOLVED.**

V2 adds `variant_of_candidate_id` and `variant_dimension`.

For learned-scope claim `G`, the V2 validator requires learned-scope and simple-audition C4 conditions to share candidate machinery, base substrate, information, opportunity, replay, and scoring conditions, differing only in the preregistered scope-policy dimension.

## 6. H5 — transfer claim T lacked explicit lineage/state carryover contract

**RESOLVED.**

V2 adds `lineage_transfer_contract`. Validator V2 binds claim `T` to:

- explicit cross-world transfer use;
- immutable transfer-policy artifact;
- matched continuation/reset opportunity;
- state-scope manifest;
- no-meta-learning ablation;
- evaluator lineage IDs remaining outside learner evidence;
- operation verification under the canonical lineage/state-transfer contract.

Reset/carryover laundering is explicitly invalid.

## 7. H6 — replay/resource condition identifiers not reconciled

**RESOLVED.**

V2 gives top-level information, opportunity, resource, replay, and scope-policy identities. The validator requires candidate condition IDs to resolve to the frozen top-level conditions and requires fixed-condition C2/C4 equality except for the explicitly isolated experimental factor.

## 8. H7 — fictional restart persistence semantics

**RESOLVED.**

V2 restart fields are conditional rather than always true.

If checkpointing is false, restart equivalence must be false. If restart equivalence is claimed, required causal state must be persisted and independently checked.

The V2 resource addendum further closes the first-core resource seam: primary fixed-envelope SVF-0/SVF-1 trajectories under V2 require `checkpointing_used=false` because V2 does not yet carry a separate numeric checkpoint-resource envelope.

## 9. H8 — commitments lacked retrievable immutable preimages

**RESOLVED.**

V2 binds immutable artifacts for parameter-distribution and seed commitments and an immutable intervention schedule artifact for SVF-1.

The validator resolves and hashes those preimages. Unavailable authoritative preimages are `BLOCKED_UNAVAILABLE_EVIDENCE`, never inferred from prose.

## 10. H9 — metric/comparator references weakly typed

**RESOLVED AT VALIDATOR LAYER.**

V2 metrics use `comparator_candidate_id`. The validator requires candidate and metric IDs unique by key and every comparator reference to resolve to a frozen candidate/variant with a claim-compatible role.

JSON Schema alone does not provide referential integrity; the validator contract correctly owns that obligation.

## 11. H10 — negative-control world lacked frozen null/acceptance semantics

**RESOLVED.**

V2 adds `negative_control_acceptance_rule`.

The V2 decidability addendum prevents a frozen but vague phrase from masquerading as preregistration: primary threshold, negative-control, stopping, aggregation, support, kill, and resource-overrun rules must be mechanically decidable or resolve to immutable specifications with all consequential constants frozen.

## 12. H11 — fabricated `minimal valid` fixture frontier

**RESOLVED.**

The V2 validator supersedes the V1 fixture frontier. Before a real implementation subject exists, lawful research fixtures are limited to:

- schema-shape exemplars explicitly barred from `PASS_FROZEN_VALID`; and
- intentionally invalid hostile fixtures.

A real PASS subject must bind a real immutable implementation commit. Fake provenance is prohibited.

## 13. Additional resource/frontier closure

The repair pass found and closed a second-order ambiguity that was not part of H1-H11.

`EXPERIMENT_RESOURCE_FRONTIER_SERIES_CONTRACT.md` establishes:

- one V2 manifest = one fixed-envelope subject;
- a resource-performance frontier = a preregistered series of independently frozen fixed-envelope subjects;
- the resource grid and non-resource common conditions are frozen before scored outcomes can be used to redesign the series;
- invalid, omitted, over-budget, and unexecuted points remain visible rather than being cherry-picked away.

`EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_RESOURCE_ADDENDUM.md` makes the first-core no-checkpoint primary rule normative for V2.

## 14. Additional decidability closure

`EXPERIMENT_PREREGISTRATION_VALIDATOR_V2_DECIDABILITY_ADDENDUM.md` closes post-result evaluator discretion that could survive a syntactically frozen manifest.

A rule such as `materially better`, `small overhead`, `well calibrated`, or `stop when stable` is not sufficient for a primary claim unless its operational decision semantics are frozen and independently decidable.

This is necessary because frozen vagueness is still post-result flexibility.

## 15. Schema validation evidence

The exact V2 JSON was checked against JSON Schema Draft 2020-12 metaschema semantics and passed schema validity.

Research-only local shape tests also established that V2:

- accepts a non-executable SVF-0 C1+C2/P shape exemplar;
- accepts a non-executable SVF-1 C2+C4 plus simple-audition-variant shape exemplar;
- rejects SVF-0 structural claim `S` in place of `P`;
- rejects SVF-0 forced C2/C4 comparison;
- rejects SVF-1 null intervention schedule;
- rejects hidden-family-adaptive SVF-1 schedule;
- rejects diagnostic/cheat candidates marked developmental-evidence eligible;
- rejects restart-equivalence claims with checkpointing disabled.

These are schema tests only. The exemplars used SHA-shaped placeholder provenance and are explicitly **not** valid experiment subjects and not executable manifests.

## 16. Comparator/evidence obligations preserved

The repair did not weaken the earlier surviving requirements:

- predictions and scope decisions are committed before scored outcomes;
- learner-visible evidence and evaluator-only bookkeeping remain separate;
- `NOT_AUDITED`, counterfactual, unresolved, invalidated, success, and failure states remain distinct;
- zero support cannot be converted into evidence by an estimator;
- support is representation-versioned;
- candidate audition cannot contaminate the base before marginal scoring;
- independent C2-vs-C4 evidence remains distinct from C4 internal base-shadow diagnostics;
- replay cannot be enriched post hoc with evaluator labels;
- structure/scope/audition/base-shadow resources are charged;
- learned gating must beat a simpler bounded-audition rival before claim `G` is available;
- immutable commits, not branch heads, define implementation subjects;
- validation status remains separate from execution authority.

## 17. Residual nonblocking design dependencies

Research closure does not resolve implementation facts that cannot honestly be chosen without an implementation subject.

Still deferred:

- exact C1/C2 recurrent probabilistic realization;
- exact C4 structural-candidate realization;
- optimizer and concrete software architecture;
- exact numeric resource envelopes;
- exact replay capacities/update counts;
- exact fixed resource-frontier points;
- exact proper scoring-rule implementation parameters where the implementation matters;
- exact world-generator/source artifacts required by a real manifest;
- exact validator software and hostile fixture implementation;
- any training result or empirical performance claim.

These are not defects in the research contract. They are the inputs a separately authorized implementation-source lane would need to create and then freeze.

## 18. Project/qualification separation

PR #32 successor work remains separate from the frozen BT2 R1 qualification subject.

Nothing in this PASS changes any frozen R1 verdict or supplies remediation evidence to that subject.

## 19. Authority ceiling

This PASS is explicitly **RESEARCH-CONTRACT READY**, not implementation approval.

It does not authorize:

- creating the C1/C2/C4 implementation;
- validator implementation;
- model training;
- experiment execution;
- paid/hosted compute;
- merge of PR #32;
- deployment;
- publication;
- provider/credential/ruleset changes;
- repository visibility changes;
- protected-system connection.

## 20. Exact next frontier

The highest-value next frontier is now genuinely outside the current research-only authority:

> **Open a separately authorized implementation-source lane that builds the smallest concrete C1/C2 recurrent probabilistic substrate, C4 structural candidate, comparator instrumentation, and hostile unit tests required by these contracts—without running training until separately authorized.**

Until that authority exists, additional conceptual mechanism documents would mostly add breadth rather than close a known research blocker.