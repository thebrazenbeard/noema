> **License:** Source-visible, not open source. Original material is proprietary. Commercial use, redistribution, hosted-service use, and commercial derivative products require written permission. See [LICENSE](LICENSE) and [COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md). Separately identified third-party components retain their own licenses.

# Noema

A persistent predictive cognitive architecture for learned agency.

Noema is an exploratory research and implementation project asking whether a persistent system can learn predictive structure about a world before language becomes its organizing core.

## Current source status

`main` contains the research architecture plus a bounded **I0/I1 implementation subject**. The implementation is deliberately narrow:

- CPython 3.13 source under `src/noema/`;
- deterministic provenance, boundary, candidate, accounting, comparison, validator, SVF-0 runner/statistics/experiment/evaluator components;
- frozen configuration and qualification artifacts under `implementation/`;
- deterministic tests under `tests/`.

The frozen implementation receipt records **103/103 deterministic tests passing** on Windows / CPython 3.13.5 with jsonschema 4.26.0 and pytest 9.0.2. Repository integration does not promote that receipt into experimental or deployment authority.

## Authority boundary

Current implementation authority is limited to:

- **I0** — implementation source;
- **I1** — deterministic non-learning verification.

This repository state does **not** claim or authorize:

- **E0** learning/training/experiment execution;
- empirical Gate-1 results;
- deployment or provider activation;
- publication of confidential material;
- paid/hosted compute;
- protected-system effects.

Source presence, deterministic verification, experiment execution, empirical evidence, deployment, and runtime effect remain separate states.

## Start here

- `docs/working-design/` — research architecture and contracts;
- `docs/implementation/IMPLEMENTATION_DECISION_RECORD_V1.md` — first implementation decision boundary;
- `implementation/NOEMA_MINIMAL_SUBJECT_V1.json` — frozen implementation subject;
- `implementation/NOEMA_MINIMAL_SOURCE_I1_VERIFICATION_RECEIPT.md` — exact I1 verification evidence;
- `governance/IMPLEMENTATION_CURRENTNESS.json` — implementation currentness and authority ceiling.

The project does **not** assume that an LLM, tokenizer, SPM, or existing AI architecture belongs at the core. Those remain candidate tools only where evidence supports them.
