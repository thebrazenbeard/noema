# Experiment Preregistration Validator V2 — Decidability Addendum

Classification: **IP_CONFIDENTIAL**

Status: **NORMATIVE V2 VALIDATOR ADDENDUM / RESEARCH ONLY / NOT IMPLEMENTED / NOT EXECUTION AUTHORITY / NOT BT2 R1 REMEDIATION**

Date: 2026-09-13

Applies to:
- `EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V2.json`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_CONTRACT_V2.md`

## 1. Purpose

A rule is not preregistered merely because vague language was frozen before results.

Phrases such as `materially better`, `reasonable`, `substantially intact`, `well calibrated`, `bounded harm`, or `sufficient support` still leave post-result evaluator degrees of freedom unless the experiment subject binds how those phrases become observable decisions.

This addendum requires operational decidability for every rule that can change a primary PASS/FAIL, exclusion, stopping, support, or negative-control judgment.

## 2. Governing rule

For every primary adjudication rule, the validator must be able to answer **before execution**:

> Given a complete valid ledger/result record, can an independent evaluator determine the rule's result without inventing a new threshold, metric, interpretation, or exception?

If no, the subject is not frozen-valid for that claim.

Return:

`FAIL_SCORING_CONTRACT`

or, when the referenced rule artifact cannot be retrieved:

`BLOCKED_UNAVAILABLE_EVIDENCE`.

## 3. Rules requiring decidability

At minimum this applies to:

- every primary metric `aggregation_rule`;
- every primary metric `threshold_rule`;
- every primary metric `support_requirement`;
- `negative_control_acceptance_rule`;
- support-class thresholds;
- uncertainty/confidence method as used for primary adjudication;
- multiple-comparison rule;
- stopping rule;
- kill criteria;
- invalidation/exclusion rules used by aggregation;
- any resource-overrun rule that determines primary eligibility;
- transfer evidence-to-criterion rule for claim `T`;
- learned-scope resource/performance comparison for claim `G`.

## 4. Acceptable forms

A rule may be represented as:

- complete machine-readable expression embedded in the frozen manifest;
- exact immutable artifact reference containing the rule;
- named algorithm plus every consequential parameter/version frozen in an immutable artifact;
- another form that is independently executable or mechanically decidable from frozen evidence.

The representation must make all outcome-sensitive constants discoverable before execution.

## 5. Unacceptable forms

The following fail if left undefined for a primary claim:

- `material improvement`;
- `reasonable compute`;
- `substantially intact`;
- `good calibration`;
- `enough support`;
- `similar performance`;
- `small overhead`;
- `significant damage` when no statistical/operational definition is bound;
- `stop when stable`;
- `exclude pathological runs` without a frozen pathology rule;
- `use appropriate correction`;
- `held-out transfer succeeds` without a criterion.

Natural-language explanation may accompany a rule, but cannot substitute for the adjudication semantics.

## 6. Randomization and schedule rules

`hidden_family_randomization_rule` and any schedule-generation rule must also be operationally closed.

The validator must establish:

- exact random source/seed binding;
- distribution or deterministic rule;
- any stratification/balancing rule;
- whether the rule can observe hidden family, candidate output, or scored outcomes;
- ordering relative to result visibility.

A prose statement that randomization is `balanced` is insufficient unless balance is mechanically defined.

## 7. Resource measurement rule

`measurement_method` must define or resolve the actual accounting procedure strongly enough to decide whether a run exceeded its frozen envelope.

It must not allow the evaluator to choose after results:

- which process/thread costs count;
- whether shadow/base-shadow work counts;
- whether replay/search/gate work counts;
- how shared overhead is allocated;
- whether a missing measurement is treated as zero.

Consumed-but-unmeasured remains invalid.

## 8. Negative-control adjudication

The negative-control rule must predefine both:

- what metric pattern would count as a false structural advantage or destructive structural behavior; and
- what bounded overhead, if any, remains admissible.

A primary structural claim cannot be rescued after results by redefining a negative-control failure as harmless overhead.

## 9. Kill criteria

Kill criteria may be logically composite, but every clause used for a primary design disposition must be operationally grounded.

If a qualitative research judgment remains necessary, label it a secondary human adjudication and do not make the primary statistical/experimental PASS depend on it.

## 10. Fixture test

A future hostile validator suite must include at least one schema-valid manifest whose primary `threshold_rule` is merely `materially better` and one whose negative-control rule is merely `small overhead allowed`.

Both must fail V2 validator adjudication despite passing JSON Schema shape validation.

## 11. Authority boundary

Operationally closed preregistration improves falsifiability. It does not authorize implementation, training, experiment execution, paid compute, merge, deployment, publication, provider/credential/ruleset changes, repository visibility changes, or protected-system connection.