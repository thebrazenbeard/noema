# Experiment Resource-Frontier Series Contract

Classification: **IP_CONFIDENTIAL**

Status: **SUCCESSOR WORKING DESIGN / EVALUATOR-SIDE SERIES CONTRACT / NOT IMPLEMENTED / NOT EXECUTION AUTHORITY / NOT BT2 R1 REMEDIATION**

Date: 2026-09-13

Companion artifacts:
- `EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V2.json`
- `EXPERIMENT_PREREGISTRATION_VALIDATOR_CONTRACT_V2.md`
- `EXPERIMENT_SCOPE_SUPPORT_AND_AUDITION_LEDGER.md`
- `MINIMAL_STRUCTURAL_VALUE_FALSIFICATION_FAMILY.md`

## 1. Purpose

A resource-performance frontier is not one experiment run operating under two resource envelopes.

It is a preregistered **series of independently frozen fixed-envelope subjects** whose only intended experimental difference is the declared resource point.

This contract preserves that distinction so the project can report both:

- fixed-envelope C2/C4 comparisons; and
- a resource-performance frontier across several fixed envelopes.

## 2. One manifest, one fixed envelope

Each V2 experiment manifest defines one authoritative `resource_condition_id` and one fixed total envelope for its primary run.

A single run must not be post-hoc reinterpreted as belonging to a more generous envelope after it exceeds the one that was frozen.

An over-budget run can remain exploratory evidence but cannot satisfy its original fixed-envelope primary claim.

## 3. Frontier-series receipt

Before any frontier-series scored outcomes are visible to an actor allowed to alter the series, freeze an evaluator-side series receipt binding:

- `series_id`;
- experiment stage (`SVF-0` or `SVF-1`);
- exact implementation subject commit;
- exact ordered list of resource-point IDs;
- the intended fixed envelope at every point;
- the manifest logical ID/path intended for every point;
- common information/opportunity/world/seed/schedule condition identity;
- candidate set/variant identity;
- metrics/aggregation/stopping semantics shared across points;
- allowed difference set, normally only the resource envelope;
- omission/invalidation rule for a failed point;
- frontier aggregation/reporting rule.

The series receipt is evidence provenance, not execution authority.

## 4. No cherry-picked frontier

Do not report only the resource points that make one architecture look favorable.

If a preregistered point fails, exceeds budget, becomes invalid, or is not executed under later authority, preserve that state explicitly in the frontier record.

Missing, invalid, and over-budget points remain distinct.

## 5. Equal-condition requirement across resource points

Unless the series explicitly studies another factor, all frontier points must preserve:

- the same implementation subject;
- same candidate source/configuration except the frozen resource parameter;
- same learner-visible information condition;
- same external opportunity condition;
- same world generator and parameter distribution;
- same seed/randomization commitment family;
- same externally scheduled intervention policy in SVF-1;
- same scoring rules;
- same support/audition semantics;
- same negative-control rules.

Changing another factor creates a multidimensional experiment and cannot be described as a one-dimensional resource frontier.

## 6. C2/C4 resource symmetry

At each fixed-envelope point, C2 and C4 must be evaluated under the same declared total resource ceiling for any claim described as equal-resource.

C4 must charge, when consumed:

- structural state;
- structural proposal/search compute;
- scope inference;
- shadow audition;
- candidate probation/consolidation;
- base-shadow diagnostic computation.

C2 does not receive a compensating artificial handicap merely because C4 has more moving parts.

The point of the frontier is to learn whether extra machinery buys enough value to justify its cost, not to normalize complexity away.

## 7. Replay/resource interaction

A resource point must not silently grant C4 a larger replay budget while describing the difference as structural compute.

Replay capacity, replay updates, replay-selection policy, and replay compute are either:

- held matched at the point; or
- explicitly included in the resource factor being varied.

If replay differs unintentionally, the point is not an architecture-only comparison.

## 8. Checkpoint discipline for first-core primary runs

Schema V2 records restart semantics but does not itself encode a separate numeric checkpoint-cost ceiling.

Therefore, for the first primary fixed-envelope SVF-0/SVF-1 comparisons, the default admissible condition is:

> **`checkpointing_used=false` during the scored primary trajectory.**

This avoids a hidden checkpoint/persistence subsidy while the first resource accounting implementation is still being established.

If future implementation requires checkpointing during a scored primary trajectory, a separately frozen checkpoint-resource extension must bind at minimum:

- maximum serialized bytes;
- maximum checkpoint compute/time;
- maximum restart-to-ready compute/time;
- storage/write amplification accounting where material;
- candidate-specific versus shared checkpoint cost;
- whether checkpoint work consumes learner-visible opportunity/time.

Until such an extension is frozen, a checkpointed run may be diagnostic but cannot claim first-core fixed-envelope equivalence merely because restart state was causally complete.

## 9. Resource measurement is not a semantic channel

CPU counters, memory meters, evaluator timing, checkpoint byte counts, and series IDs are E1 evidence unless a separate experiment explicitly makes some corresponding consequence learner-visible.

Resource accounting must not create a hidden clock, task label, candidate identity cue, or reward signal for the learner.

## 10. Frontier claim ceiling

A frontier can show that one candidate offers a better measured performance/resource tradeoff over the preregistered region.

It does not establish:

- universal efficiency;
- scaling behavior outside the tested range;
- optimality;
- mature Noema architecture status;
- implementation authority;
- training or execution authority.

## 11. First-series recommendation

If execution is later authorized, prefer a small preregistered grid sufficient to reveal whether C4's structural gain survives resource matching rather than a large hyperparameter sweep.

The actual resource points must be chosen only after concrete implementation measurement exists and before final experimental outcomes are visible.

This research artifact intentionally does not invent numerical budgets in the absence of implementation evidence.

## 12. Exact next frontier

With this series contract, the repaired research chain can be hostile-reviewed without pretending a single manifest represents an entire frontier.

If that exact-head review passes, implementation-source design becomes the next gated frontier.