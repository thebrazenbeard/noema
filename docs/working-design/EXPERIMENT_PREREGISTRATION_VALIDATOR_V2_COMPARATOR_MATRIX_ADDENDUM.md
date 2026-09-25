# Experiment Preregistration Validator V2 — Comparator Matrix Addendum

Classification: **IP_CONFIDENTIAL**

Status: **NORMATIVE V2 VALIDATOR ADDENDUM / RESEARCH ONLY / NOT IMPLEMENTED / NOT EXECUTION AUTHORITY / NOT BT2 R1 REMEDIATION**

Date: 2026-09-13

Applies to:
- `EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V2.json`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_CONTRACT_V2.md`
- `C0_C4_FAIR_COMPARISON_AND_CLAIM_BOUNDARY_MATRIX.md`

Provenance note:
- the matrix reconciles useful fairness/claim-boundary work independently developed on stacked private PR #33 at `d73db33295810623de93e2fe24eead32f26738dc` into canonical PR #32;
- V1 schema/validator edits from that stacked repair are not normative because V2 supersedes V1 for future preregistration use.

## 1. Purpose

The V2 validator already closes the decisive C2/C4 fairness seam. This addendum binds the whole C0-C4 ladder and its claim ceilings without making optional diagnostic candidates mandatory for the smallest falsifier.

## 2. C0 floor semantics

C0 is optional in an SVF-0 manifest.

If present, verify:

- it is identified as the persistence/system-identification floor rather than the serious structural rival;
- C0-versus-C1 claims are limited to persistence/recurrent-state evidence;
- C4-versus-C0 performance is never used as the primary structural-value comparator;
- C0 does not receive a deliberately disadvantaged information or opportunity condition that is later presented as structural evidence.

Absence of C0 does not invalidate SVF-0 when C1/C2 satisfy the canonical Gate-1 contract.

## 3. C1/C2 replay-isolation rule

For any claim that attributes C2 improvement to replay, verify C1 and C2 share the same frozen non-replay base substrate/configuration.

The intended difference is only the preregistered replay dimension and its charged state/compute.

Differences in base capacity, optimizer family, recurrent state size, learner-visible evidence, external opportunity, or non-replay update schedule create a different comparison condition and cannot support the narrow replay claim.

## 4. C3 claim-ceiling rule

C3 remains optional for the minimal C2-versus-C4 falsifier.

If C3 is absent:

- a negative C2-versus-C4 result remains sufficient to falsify C4 for the tested family;
- a positive C4-versus-C2 result is limited to the whole-system claim that C4 beat the tested recurrent+replay rival;
- no result may be described as showing scoped/explicit structure beats the strongest non-scoped structural alternative.

If C3 is present and a broader scoped-value claim is made, verify:

- C3 source/configuration was frozen before outcomes;
- C3 receives the same learner-visible stream/opportunity condition as its comparison row;
- C3's base/resource condition is matched or the difference is explicitly the experimental factor;
- C3 receives no semantic/oracle labels unavailable to developmental candidates;
- the broader claim uses a preregistered C3-versus-C4 metric/threshold rule.

Violation returns `FAIL_SCORING_CONTRACT` or `FAIL_COMPARATOR_FAIRNESS` as appropriate.

## 5. Diagnostic isolation

Reference, oracle, and semantic-cheat diagnostics may share immutable evaluator-side world/seed/schedule artifacts where pairing is intended.

They may not share mutable developmental learner state, including:

- model weights;
- recurrent/working state;
- optimizer/plasticity state;
- replay state;
- learner RNG state;
- candidate/structural state;
- scope/support state;
- outputs used to update the developmental candidate.

Diagnostic outputs may not become learner evidence or update targets unless a new information condition explicitly admits them and lowers the claim ceiling.

Violation returns `FAIL_INFORMATION_BOUNDARY`.

## 6. Retained-state accounting

For fixed-envelope comparisons, resource validation must account total retained causal state rather than only raw replay capacity.

When consumed, account at minimum:

- raw replay contents;
- replay policy/priority state;
- structural candidate snapshots;
- structural traces/anchors;
- scope/support maps;
- representation-transport/compatibility state;
- probation/consolidation state;
- other durable or resident state able to preserve evidence or alter future computation.

Equal replay-buffer capacity does not establish equal memory/resource conditions when one candidate retains substantial additional structural evidence elsewhere.

Consumed-but-unmeasured retained state returns `FAIL_RESOURCE_ACCOUNTING`.

## 7. Claim G variant identity

For learned-scope claim `G`, recheck that the learned-scope and bounded-audition conditions are variant-linked and identical in:

- candidate implementation;
- base substrate/configuration;
- learner-visible information;
- world/opportunity stream;
- replay condition;
- candidate budget;
- scoring/aggregation rules;
- resource-meter semantics.

Only the frozen scope/audition-policy dimension may differ for the narrow G claim.

## 8. Held-out intervention separation

For SVF-1 held-out intervention claims, verify the frozen world/parameter/intervention allocation rule prevents a purported holdout from being only an unobserved numeric interpolation point within an otherwise reused parameterization when the claim is broader generalization.

The exact required separation is claim-dependent and must be operationally decidable under the V2 decidability addendum.

A result confined to one analytic generator family cannot silently promote itself into a general structural-learning claim.

## 9. Restart quarantine interaction

If a diagnostic or non-primary checkpoint/restart condition loses state required by its claimed restart equivalence, the validator must preserve that loss as an explicit validity state.

The result cannot be upgraded to trajectory-equivalent evidence by qualitative reviewer judgment.

For first-core V2 primary fixed-envelope subjects, the resource addendum already requires no checkpointing during the scored primary trajectory.

## 10. Authority boundary

This addendum changes no effect authority. Validator success does not authorize implementation, training, execution, paid compute, merge, deployment, publication, provider/credential/ruleset changes, repository-visibility change, or protected-system connection.