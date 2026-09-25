# Noema Implementation Decision Record V1

Classification: **IP_CONFIDENTIAL**

Status: **I0 IMPLEMENTATION CHOICE / I1 DETERMINISTIC VERIFICATION ONLY / NOT E0 / NOT P0**

Research parent: `be8eeb9a5f71e992180f3b3272ca5a0b80d8fc33`.

## Runtime

The first implementation-source lane uses CPython 3.13.5. Third-party dependencies are limited to `jsonschema==4.26.0` at runtime and `pytest==9.0.2` for deterministic source verification. No numerical/ML framework, pretrained component, embedding service, hosted inference service, or network runtime is part of the source subject.

This is an implementation choice, not research evidence and not a claim that Noema's mature architecture is Python-based.

## Serialization and hashing

Canonical JSON for content-addressed implementation artifacts is UTF-8 JSON with sorted keys, compact separators `(',', ':')`, no NaN/Infinity values, and SHA-256 for declared content digests.

## State discipline

Learner state is represented with immutable source values and pure transition functions. Evaluator-only provenance is represented by different source types and must not enter learner-visible event objects through free-form metadata bags.

## Verification boundary

I1 permits deterministic schema, serialization, hashing, invariant, pure-function, hostile unit, and property-style checks. This lane does not run developmental curricula, persist learned trajectory state, estimate empirical performance, execute SVF-0/SVF-1, train a model, or use hosted/paid compute.

## Resource discipline

Resource accounting must expose durable state, replay, structural candidate state, scope/audition work, comparator shadow work, and missing measurements. Unmeasured consumption is never treated as zero.

## Dependency policy

Dependencies are pinned exactly for this first source subject. Any dependency or runtime change creates a new implementation-source subject and requires fresh exact-head review.
