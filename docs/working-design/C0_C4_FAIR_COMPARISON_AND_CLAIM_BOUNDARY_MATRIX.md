# C0–C4 Fair Comparison and Claim-Boundary Matrix

Classification: **IP_CONFIDENTIAL**

Status: **SUCCESSOR WORKING DESIGN / RECONCILED WITH PR #32 V2 PREREGISTRATION / NO IMPLEMENTATION OR EXECUTION AUTHORITY / NOT BT2 R1 REMEDIATION**

Date: 2026-09-13

Reconciliation provenance:
- canonical successor line: PR #32
- independently proposed stacked repair: PR #33 at `d73db33295810623de93e2fe24eead32f26738dc`
- this artifact imports the useful whole-ladder fairness/claim-boundary constraints from that repair while preserving the canonical minimality rule that C0 is a diagnostic persistence floor rather than a mandatory member of every SVF-0 manifest.

Companion contracts:
- `MINIMAL_STRUCTURAL_VALUE_FALSIFICATION_FAMILY.md`
- `C2_C4_COMPARATOR_INTERFACE_CONTRACT.md`
- `EXPERIMENT_SCOPE_SUPPORT_AND_AUDITION_LEDGER.md`
- `EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V2.json`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_CONTRACT_V2.md`

## 1. Purpose

The minimal structural-value family names C0, C1, C2, C3, and C4, while the decisive falsifier concentrates on C2 versus C4. This matrix prevents a future result from silently changing comparison class or claim ceiling between the persistence floor, replay comparison, non-scoped structural diagnostic, and scoped-structure claim.

It is evaluator-side specification and audit material only.

## 2. Global comparison invariants

A primary comparison is admissible only when information, opportunity, causal frontier, and resources are accounted separately.

### 2.1 Equal learner-visible information

Matched developmental candidates receive the same ordered learner-visible event envelope under the frozen information condition.

Evaluator-only family identity, orientation, task/regime identity, applicability labels, scores, split membership, and exact intervention-success truth remain outside learner evidence unless a different subject explicitly admits them and lowers the claim ceiling.

Candidate-derived internal features are architectural computation, not an extra external channel; their state and compute are charged.

### 2.2 Equal external opportunity

Matched candidates receive independent replicas of the same evaluator-constructed world/seed stream and, in SVF-1, the same frozen externally scheduled intervention sequence.

Candidate predictions, scope decisions, audit outcomes, or resource use may not alter that primary externally scheduled stream. Any such coupling creates a different behavior-affecting subject.

### 2.3 Equal causal frontier

Every scored prediction, action, or scope decision is committed before its scored outcome becomes visible.

Hypothetical-intervention forecasts during passive ambiguity remain evaluator-side counterfactual scoring records. They are not converted into observed learner evidence.

### 2.4 Equal declared resources

Every causally material consumed resource must have a measurement route and ledger charge for a fixed-envelope claim.

Structural state, candidate snapshots, anchors, traces, transport maps, scope inference, audition, proposal search, replay, durable-state growth, and diagnostic base-shadow computation are not free sidecars.

Consumed-but-unmeasured resources invalidate fixed-envelope primary claims.

## 3. Candidate ladder and claim ceilings

### C0 — persistence floor

C0 is the deliberately weak incremental persistence/system-identification floor.

It may be included to establish that a world and scoring setup are nontrivial and to separate trivial learning from recurrent persistence. It is **not required in every SVF-0 manifest** and is never the primary structural-value rival.

A C4 win over C0 establishes no structural necessity.

### C1 — recurrent predictor without replay

C1 is the recurrent probabilistic online predictor without replay.

Where C0 is present, C0-versus-C1 can support only a narrow persistence/recurrent-state claim under matched stream and resource accounting.

### C2 — recurrent predictor with bounded replay

C2 is C1's declared base substrate plus the preregistered replay capability for the C1-versus-C2 comparison.

C2 is the minimum serious simpler rival for C4.

### C3 — optional non-scoped structural diagnostic

C3 is an optional continuous soft-structure, predictive-state, or other non-scoped structural realization.

C3 is not required for the smallest negative C2-versus-C4 falsifier. However, omission of C3 limits any positive C4 result:

> A C4-over-C2 result is evidence only against the tested recurrent+replay rival. It is not evidence that scoped/explicit structure beats the strongest non-scoped structural alternative.

A broader scoped-value claim requires a preregistered C3 or equivalent comparison.

### C4 — scoped structural candidate

C4 uses the declared C2 base substrate class plus bounded structural candidate machinery and, where separately tested, learned scope/routing.

C4 may not receive a richer base, extra learner-visible evidence, hidden replay privilege, extra world opportunities, or uncharged retained state while the comparison is described as architecture-only or equal-resource.

## 4. Fair comparison matrix

| Comparison | Question | Intended factor | Minimum admissibility | Claim ceiling |
| --- | --- | --- | --- | --- |
| C0 vs C1 | Does recurrent state add persistent online value over the floor? | recurrent state/update mechanism | same stream and declared resource/accounting condition | persistence evidence only |
| C1 vs C2 | Does bounded replay add value beyond recurrence? | replay storage/selection/update/compute | same C1 base; replay difference frozen and charged | replay-adjusted persistence/retention |
| C2 vs C3 | Does non-scoped structural/predictive-state machinery add value beyond recurrence + replay? | declared C3 structural realization | same learner-visible stream and matched declared comparison conditions | narrow non-scoped structural claim |
| C2 vs C4 | Does C4 as a whole add value over the primary simpler rival? | bounded C4 structure/scope machinery | same external stream, base substrate, causal frontier, replay condition, and declared resource view | C4-over-C2 whole-system claim only |
| C3 vs C4 | Does scoped/candidate machinery add value beyond a stronger non-scoped structural rival? | scope/candidate/routing machinery | matched comparison substrate/resource view plus support/audition controls | scoped-value claim under the tested family |
| C4 learned-scope vs C4 bounded-audition | Does learned scope earn itself? | scope/audition policy only | variant-linked same candidate/base/information/opportunity/replay/scoring conditions | claim G only |

A comparison row may be omitted only before outcomes and only with the corresponding claim ceiling preserved.

## 5. Replay and retained-state fairness

Replay and structural memory are distinct resource classes but both retain evidence/state.

For comparisons that claim replay or architecture fairness:

- replay contains only information lawful at original encoding;
- evaluator annotations and future-derived labels cannot enrich replay;
- structural traces, anchors, candidate snapshots, support maps, compatibility bridges, and transport state count as learner state when they influence future computation or preserve evidence;
- replay priorities must be learner-derived or explicitly declared as a changed information condition;
- equal raw replay-buffer size does not make unequal total retained state free.

## 6. Diagnostic isolation

Reference, oracle, and semantic-cheat diagnostics are evaluator diagnostics only.

They may not share mutable learner weights, replay, RNG state, optimizer state, structural state, outputs used for updates, or other causal side effects with a developmental candidate.

Shared immutable world/seed schedules are permitted where intended. Shared learner state is not.

If a diagnostic influences a developmental candidate, that creates a different information/architecture subject.

## 7. C3 omission rule

C3 is deliberately optional because the minimal family is meant to falsify C4 cheaply.

This creates an asymmetric interpretation:

- if C2 matches or beats C4, the scoped structural claim can be rejected for the tested family without C3;
- if C4 beats C2 and the project wants only the narrow whole-system C4-over-C2 claim, C3 can remain omitted;
- if the project wants to claim the advantage is specifically due to scoped/explicit structure beyond strong non-scoped structural alternatives, C3 or a predeclared equivalent becomes mandatory.

This preserves minimal falsifiability without inflating a positive result's claim ceiling.

## 8. Scope/support claim admissibility

Non-audition is not evidence of success or failure.

Strong positive learned-scope evidence requires the frozen support rule. Weak, unknown, not-audited, counterfactual, unresolved, and invalidated states remain distinct and cannot be silently pooled into strong support.

Off-policy support is not direct support and must preserve its overlap/uncertainty burden.

Claim G additionally requires the variant-linked learned-scope versus bounded-audition comparison defined above.

## 9. Passive ambiguity and held-out intervention separation

All developmental candidates receive the same passive stream and same frozen query/intervention schedule within a matched subject.

Held-out intervention evaluation must be separated by the frozen world/parameter/intervention allocation rule strongly enough that a candidate cannot win merely by memorizing one world parameterization or interpolation surface.

A win confined to the first analytic chain/fork family remains a claim about that family, not universal structure learning.

## 10. Representation drift and restart

Support is representation-versioned. Material representation change closes the old support interval unless the declared continuity route lawfully preserves or transports it.

If restart loses state required by a claimed trajectory equivalence, that equivalence is forfeited. The run cannot be restored to primary status by reviewer assertion that missing state was probably irrelevant.

For V2 first-core primary fixed-envelope subjects, the separate resource addendum currently requires no checkpointing during the scored primary trajectory.

## 11. Falsification interpretation

- C2 >= C4 under the primary matched condition: scoped structural machinery has not earned itself for the family.
- C4 wins only under extra declared resources: resource-frontier evidence, not an equal-resource win.
- C4 > C2 but C3 >= C4: only the narrow C2-relative whole-system claim survives; scoped-value interpretation fails.
- C4 > C2 while learned scope fails against bounded audition: retain/defer structural candidate machinery but reject learned gating claim G.
- Any result dependent on semantic labels, hidden replay subsidy, unmatched base substrate, unmeasured resources, unsupported scope, or evaluator diagnostic leakage is invalid rather than positive evidence.

## 12. V2 validator obligations added by this matrix

For future V2 validation, require:

- diagnostic isolation as defined in section 6;
- C0, when present, is treated as a floor and not as the serious C4 rival;
- C1/C2 base parity for replay claims;
- C2/C4 base-substrate parity for structural marginal claims;
- C3 presence/absence controls the claim ceiling exactly as section 7 states;
- claim G variant identity is exact except for the scope/audition policy;
- total retained state is resource-accounted rather than equating replay-buffer size with total memory fairness.

These are validator/cross-field obligations; they need not all be expressible in JSON Schema.

## 13. Effect boundary

This matrix does not authorize implementation, training, experiment execution, hosted/paid compute, merge, deployment, publication, provider/credential/ruleset mutation, repository-visibility change, or another protected effect.