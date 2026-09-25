# Experiment Preregistration Validator V2 — Resource Addendum

Classification: **IP_CONFIDENTIAL**

Status: **NORMATIVE V2 VALIDATOR ADDENDUM / RESEARCH ONLY / NOT IMPLEMENTED / NOT EXECUTION AUTHORITY / NOT BT2 R1 REMEDIATION**

Date: 2026-09-13

Applies to:
- `EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V2.json`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_CONTRACT_V2.md`
- `EXPERIMENT_RESOURCE_FRONTIER_SERIES_CONTRACT.md`

## 1. Purpose

Schema V2 deliberately models one fixed resource envelope per manifest. It also carries causal restart fields, but it does not yet encode a separate numeric checkpoint-cost envelope.

Without an explicit rule, a checkpointed C2/C4 run could claim equal fixed resources while persistence work remained outside the frozen budget.

This addendum closes that seam for first-core SVF-0/SVF-1 evidence.

## 2. One manifest is one frontier point

`PASS_FROZEN_VALID` applies to one fixed-envelope experiment subject.

A resource-performance frontier is adjudicated only from a preregistered series of such subjects under `EXPERIMENT_RESOURCE_FRONTIER_SERIES_CONTRACT.md`.

The validator must not infer a frontier from post-hoc runs at convenient budgets.

## 3. V2 primary-run checkpoint rule

For schema V2, a run intended to support a **primary fixed-envelope SVF-0 or SVF-1 claim** must have:

`restart_contract.checkpointing_used = false`

through the scored primary trajectory.

Reason: V2 has no independent numeric checkpoint-cost ceiling, so it cannot prove fixed-envelope equivalence when checkpoint work is consumed.

A schema-valid manifest with `checkpointing_used=true` may still describe:

- a diagnostic restart experiment;
- a future extension subject;
- non-primary evidence.

But under V2 it cannot qualify a primary fixed-envelope structural/replay result.

If such a manifest is presented for a primary fixed-envelope claim, return:

`FAIL_RESOURCE_ACCOUNTING`

rather than treating checkpoint cost as zero.

## 4. Future checkpoint extension

A later schema revision may admit checkpointed primary trajectories by freezing explicit checkpoint resource axes, including at minimum:

- serialized bytes;
- checkpoint compute/time;
- restart-to-ready compute/time;
- material storage/write amplification;
- candidate-specific versus shared checkpoint cost;
- learner-visible opportunity/time cost when applicable.

That later revision creates a new experiment subject. Do not retroactively extend V2.

## 5. Resource-frontier validation

For any reported C2/C4 resource-performance frontier, require a frozen frontier-series receipt created before constituent scored outcomes are available for series redesign.

Verify:

- every point references an independently frozen manifest;
- all points share the declared non-resource conditions;
- the ordered resource grid was frozen;
- omitted, invalid, over-budget, or unexecuted points remain visible;
- no point is silently moved to a larger envelope after overrun;
- any axis changed besides resource budget is separately declared and prevents a one-dimensional frontier claim.

Failure of these conditions invalidates the frontier claim without retroactively invalidating otherwise valid individual fixed-envelope runs.

## 6. Authority boundary

Neither this addendum nor a resource/frontier validation PASS authorizes experiment execution, training, paid compute, merge, deployment, publication, provider/credential/ruleset mutation, repository-visibility change, or connection to protected systems.