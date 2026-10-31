> **License:** Source-visible, not open source. Original material is proprietary. Commercial use, redistribution, hosted-service use, and commercial derivative products require written permission. See [LICENSE](LICENSE) and [COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md). Separately identified third-party components retain their own licenses.

# Noema

**A research toolkit for building and testing predictive learning components against explicit evidence and resource limits.**

Noema explores whether a persistent system can discover useful predictive structure about its environment before language or an existing AI model becomes its organizing core. It provides Python source, deterministic fixtures, measurement contracts, and qualification artifacts for that investigation. It is not a pretrained model, general-purpose agent, hosted inference service, or production learning runtime.

The current implementation is deliberately bounded. Its reusable parts let researchers represent observations and predictions, commit predictions before outcomes are revealed, compare candidate update/replay strategies, account for resources, and validate precisely scoped research manifests. A passing deterministic test does **not** establish learned reasoning, generalization, autonomy, or successful real-world behavior.

## What is available

| Module | Public source contract | Boundary |
| --- | --- | --- |
| `noema.provenance` | `ArtifactRef`, `ArtifactRecord`, `DictArtifactResolver`, canonical JSON and digest helpers | An artifact reference pins a repository, exact 40-character commit, relative path, and optional blob/SHA-256 digest. The dictionary resolver checks supplied bytes; it does not fetch or authenticate GitHub. |
| `noema.boundary` | `LearnerEvent`, `InterventionPacket`, `Prediction`, `PredictionTicket`, `ScopeTicket`, `commit_prediction`, `commit_scope`, `EvaluatorRecord` | Prediction commitments are deterministic; evaluator-only truth and scores are separate from learner events. |
| `noema.candidates` | Candidate state, prediction, update, reset-reference, and bounded replay primitives | Experimental building blocks, not a trained or deployed model. |
| `noema.accounting` | Resource measurements, ledgers, fixed-envelope checks | Tracks measured or explicitly unmeasured costs; a budget check is not evidence of generalization. |
| `noema.svf0`, `noema.svf0_runner`, `noema.svf0_statistics`, `noema.svf0_experiment`, `noema.svf0_evaluator` | Deterministic SVF-0 change-point fixtures, candidate-step records, statistics, and evaluation tooling | Synthetic research environment and source-level qualification, not an authorized empirical E0 run. |
| `noema.validator` | Structured manifest validation | Validation checks declared contracts; it cannot grant experimental, deployment, or effect authority. |

Imports use these module paths directly; `noema.__init__` does not provide a consolidated top-level API. Existing designs and qualification artifacts remain under `docs/`, `implementation/`, and `governance/`.

## Quickstart: deterministic source checks

Requirements from [`pyproject.toml`](pyproject.toml): **CPython 3.13** (`>=3.13,<3.14`), `jsonschema==4.26.0`, and optional test dependency `pytest==9.0.2`. Use an isolated environment. Run the dependency-free source-safety check before installing dependencies.

On Linux or macOS, from a checkout:

```sh
python3.13 scripts/check_editor_source_safety.py --root .
python3.13 -m venv .venv
.venv/bin/python -m pip install -e ".[test]"
.venv/bin/python -m pytest -q
```

On Windows PowerShell:

```powershell
py -3.13 scripts/check_editor_source_safety.py --root .
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[test]"
.\.venv\Scripts\python.exe -m pytest -q
```

The source-safety check looks for editor-startup execution configuration and disguised executable font assets. A pass applies to the checked source tree; it is **not** a security attestation for a workstation or installed environment.

### Minimal Python API example

With the package installed, this example creates a deterministic prediction commitment. It **does not train anything**:

```python
from noema.boundary import LearnerEvent, Prediction, commit_prediction

event = LearnerEvent(step=0, channels=(0.25, -0.5), intervention=None)
prediction = Prediction(mean=(0.0, 0.0), variance=(1.0, 1.0))
ticket = commit_prediction("baseline", event.step, prediction)

assert ticket.step == event.step
assert len(ticket.commitment) == 64  # SHA-256 hex commitment
print(ticket.commitment)
```

This is the same public interface exercised in [`tests/test_boundary.py`](tests/test_boundary.py). `commit_prediction` binds candidate, step, mean, and variance in canonical JSON before an evaluator observes outcomes; it does not score the prediction or update weights. For deeper deterministic scenarios, begin with the tests for `candidates`, `svf0`, and `svf0_runner`.

## Data and evidence contract

- **Observations versus evaluation:** `LearnerEvent` carries a step, finite channels, and an optional intervention. `EvaluatorRecord` separately carries hidden-family and realized-score fields. Do not copy evaluator-only information into the learner's inputs.
- **Pre-outcome commitments:** `Prediction` requires finite mean/variance vectors with strictly positive variance. `commit_prediction` emits a reproducible digest-bound ticket; it is a testable commitment, not a quality score.
- **Source identity:** `ArtifactRef` identifies `owner/repo@<exact-commit>:<relative-path>`; optional digest checks fail on mismatch. Resolve and verify exact bytes independently before treating a source as retrieved evidence.
- **Resource claims:** Measured costs and explicitly unmeasured cost classes remain distinct. A deterministic simulator or synthetic measurement is not a physical host probe.
- **Qualification:** Preserve exact source, configuration, runtime, test method, and evidence class for each result. Source presence, deterministic verification, experimental execution, empirical effectiveness, and deployment are separate gates.

## Qualification status and non-claims

The frozen implementation subject currently recorded in [`implementation/NOEMA_MINIMAL_SUBJECT_V1.json`](implementation/NOEMA_MINIMAL_SUBJECT_V1.json) covers **I0 source** and **I1 deterministic non-learning verification**. Its [I1 receipt](implementation/NOEMA_MINIMAL_SOURCE_I1_VERIFICATION_RECEIPT.md) records **103/103 tests passing** on Windows with CPython 3.13.5, `jsonschema` 4.26.0, and `pytest` 9.0.2 at the specified frozen source commit. That is a historical, exact-subject verification record—not a fresh test result for every later Git head.

The current [implementation currentness record](governance/IMPLEMENTATION_CURRENTNESS.json) does **not** establish or authorize:

- E0 training, learner experimentation, or an empirical Gate-1 result;
- a model-weight update, learned reasoning, or generalization;
- paid/hosted compute, provider activation, or production deployment;
- publication of confidential research material or protected-system effects.

There is no default language model, tokenizer, model-provider identity, consent authority, or tool-execution permission in this reusable core. Those belong to separately selected and qualified host integrations, if they are ever introduced.

## Project map

- [`docs/working-design/`](docs/working-design/) — research architecture and hypothesis contracts.
- [`docs/implementation/IMPLEMENTATION_DECISION_RECORD_V1.md`](docs/implementation/IMPLEMENTATION_DECISION_RECORD_V1.md) — first implementation decision boundary.
- [`implementation/NOEMA_MINIMAL_SUBJECT_V1.json`](implementation/NOEMA_MINIMAL_SUBJECT_V1.json) — frozen implementation subject and source/test paths.
- [`implementation/NOEMA_MINIMAL_SOURCE_I1_VERIFICATION_RECEIPT.md`](implementation/NOEMA_MINIMAL_SOURCE_I1_VERIFICATION_RECEIPT.md) — exact historical I1 verification.
- [`governance/IMPLEMENTATION_CURRENTNESS.json`](governance/IMPLEMENTATION_CURRENTNESS.json) — authority ceiling and staleness rule.
- [`tests/`](tests/) — deterministic and hostile contract checks.

Noema intentionally keeps research proposals, implementation source, verification receipts, and real-system claims separate. A stronger claim requires a newly authorized, independently checkable experiment—not just more prose or another green unit test.
