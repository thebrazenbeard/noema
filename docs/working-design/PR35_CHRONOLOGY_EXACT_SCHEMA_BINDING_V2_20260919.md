# PR35 Chronology Exact-Schema Binding V2 — 2026-09-19

Classification: IP_CONFIDENTIAL

Status: SOURCE HARDENING / EMPIRICAL PROSPECTIVE AUTHORITY STILL BLOCKED

Current Radar chronology source already performs Draft 2020-12 schema validation and exact receipt-instance validation with format checking. This successor closes the remaining schema-substitution seam.

The normative freeze schema subject at the reviewed base is:

- path: `governance/EXPERIMENT_PREREGISTRATION_FREEZE_RECEIPT_SCHEMA_V1.json`
- Git blob: `312592b9104ea6e78016cfbcfd80707da80e242b`
- canonical sorted compact JSON SHA-256:
  `b23bf9052b5550b140d8e8ebac31c2608a1639f47d129b3121ee7959eb27c215`

Before the JSON Schema engine is used, the validator now requires the supplied parsed schema to match that exact canonical semantic digest. A weaker schema cannot reuse the same `$id` and schema-version constant and silently redefine receipt validity.

A hostile regression supplies a same-ID/same-version weakened schema and requires `FAIL_SCHEMA`.

This successor also removes the duplicated shadowed `_verify_external_subject_shape()` definition present in the parent source.

All parent fail-closed ceilings remain:
- external/provider evidence remains BLOCKED without separately reviewed provider resolution;
- immutable Git identity/digest/coverage does not establish complete historical absence;
- empirical prospective status remains BLOCKED without a reviewed semantic absence verifier.

No experiment execution, learning/training, I0/I1/E0/P0 action, merge, deployment, publication, provider/credential mutation, visibility change, spend, or protected-system connection is authorized.
