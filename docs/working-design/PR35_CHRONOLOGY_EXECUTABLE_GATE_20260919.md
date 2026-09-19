# PR35 Chronology Executable Gate — 2026-09-19

Classification: **IP_CONFIDENTIAL**

Status: **SOURCE IMPLEMENTATION / FAIL-CLOSED CHRONOLOGY SUBGATE / PROSPECTIVE PASS STILL BLOCKED WITHOUT SEMANTIC ABSENCE VERIFIER**

Exact base: `748b569faec484968857901bde8fa5bed2711b9d`.

This implementation closes the "written contract only" gap for the preregistration chronology surface without pretending that a shape-valid receipt can prove historical absence.

## Implemented source

- `tools/noema_prereg_chronology_validator.py`
- `tests/test_prereg_chronology_validator.py`
- CI integration in `.github/workflows/research-contract-integrity.yml`

The validator mechanically enforces:

- exact active freeze-schema identity and fail-closed claim ceiling;
- exact receipt top-level shape and provenance-only status;
- canonical repository binding;
- immutable manifest commit/path/blob/SHA-256 readback;
- exact logical experiment and manifest bindings on every chronology evidence subject;
- typed Git versus external-readback evidence subjects;
- canonical Git remote binding, including tokenized GitHub Actions clone URLs;
- exact Git commit/path/blob/SHA-256 verification for Git evidence;
- coverage cutoffs reaching through the freeze frontier;
- observation timestamps not predating their claimed coverage;
- complete visibility inventory and COMPLETE per-surface status;
- unique surface IDs and evidence subject IDs;
- no scored outcome visibility for a prospective claim;
- execution NOT_STARTED for a prospective claim;
- separate execution authority and post-freeze-new-subject rules.

External readback evidence is intentionally not accepted merely because its JSON shape is valid. Without a separately reviewed provider resolver, it returns `BLOCKED_UNAVAILABLE_EVIDENCE`.

Likewise, immutable Git identity/digest/coverage alone does not prove that the underlying evidence represents the complete authoritative result/execution universe and contains no qualifying event through the freeze. Until a separately reviewed semantic absence verifier exists, an otherwise shape-valid `PROSPECTIVE_CONFIRMED` receipt returns `BLOCKED_UNAVAILABLE_EVIDENCE`, never `PASS_FROZEN_VALID`.

That ceiling is intentional.

## Hostile executable suite

The source suite covers:

1. shape-valid self-asserted prospective receipt cannot PASS;
2. malformed/replaced governance schema;
3. stale manifest binding;
4. partial inventory;
5. evidence coverage ending before freeze;
6. scored outcome visibility under a prospective claim;
7. execution already started under a prospective claim;
8. external-readback shape without provider resolution;
9. duplicate chronology evidence identities;
10. tokenized GitHub Actions remote normalization.

Fresh local result before publication: **10/10 PASS**, py_compile PASS, diff-check PASS.

## Remaining gate

This source does not yet implement the independently authoritative semantic resolver needed to establish:

- that the frozen inventory names the complete authoritative result/execution visibility universe;
- that each resolved surface is immutable/append-only enough for historical absence claims;
- that no qualifying scored result or execution event exists at or before the freeze frontier.

Therefore no current receipt can acquire empirical `PROSPECTIVE_CONFIRMED` weight from self-asserted evidence alone.

A future resolver implementation must be separately reviewed and exact-subject-bound. It must not be injectable by the experiment/execution lane and must preserve the evidence-only authority ceiling.

## Non-effects

This work does not authorize or perform:

- implementation-source promotion;
- experiment execution;
- training or learning;
- E0/P0 action;
- merge;
- deployment;
- publication;
- provider/credential mutation;
- repository visibility change;
- spend;
- protected-system connection.
