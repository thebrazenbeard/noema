import copy
import hashlib
import json
import subprocess
import unittest
from pathlib import Path

from tools import noema_prereg_chronology_validator as v


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "governance" / "EXPERIMENT_PREREGISTRATION_FREEZE_RECEIPT_SCHEMA_V1.json"
MANIFEST_PATH = "docs/working-design/EXPERIMENT_PREREGISTRATION_MANIFEST_SCHEMA_V2.json"
EVIDENCE_PATH = "governance/RESEARCH_CURRENTNESS.json"
FREEZE = "2026-09-19T18:00:00-04:00"
OBSERVED = "2026-09-19T18:05:00-04:00"
COVERAGE = "2026-09-19T18:01:00-04:00"
EXPERIMENT_ID = "NOEMA_HOSTILE_CHRONOLOGY_FIXTURE_NON_EXECUTABLE"


def git(*args: str, binary: bool = False):
    out = subprocess.check_output(["git", "-C", str(ROOT), *args])
    return out if binary else out.decode("utf-8").strip()


def git_subject(subject_id: str, *, path: str = EVIDENCE_PATH) -> dict:
    head = git("rev-parse", "HEAD")
    blob = git("rev-parse", f"{head}:{path}")
    raw = git("show", f"{head}:{path}", binary=True)
    return {
        "source_kind": "GIT_IMMUTABLE",
        "subject_id": subject_id,
        "repository": "thebrazenbeard/noema",
        "commit": head,
        "path": path,
        "git_blob": blob,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bound_manifest_commit": head,
        "logical_experiment_id": EXPERIMENT_ID,
        "observed_at": OBSERVED,
        "coverage_cutoff": COVERAGE,
    }


def external_subject(subject_id: str) -> dict:
    head = git("rev-parse", "HEAD")
    return {
        "source_kind": "EXTERNAL_READBACK",
        "subject_id": subject_id,
        "provider": "hostile-fixture-provider",
        "surface_id": "fixture-surface",
        "observation_id": "fixture-observation",
        "result_digest": "7" * 64,
        "bound_manifest_commit": head,
        "logical_experiment_id": EXPERIMENT_ID,
        "observed_at": OBSERVED,
        "coverage_cutoff": COVERAGE,
    }


def receipt() -> dict:
    head = git("rev-parse", "HEAD")
    manifest_blob = git("rev-parse", f"{head}:{MANIFEST_PATH}")
    manifest_raw = git("show", f"{head}:{MANIFEST_PATH}", binary=True)
    return {
        "schema_version": "NOEMA_EXPERIMENT_PREREGISTRATION_FREEZE_RECEIPT_V1",
        "classification": "IP_CONFIDENTIAL",
        "status": "FROZEN_PROVENANCE_ONLY_NOT_EXECUTION_AUTHORITY",
        "repository": "thebrazenbeard/noema",
        "manifest_subject": {
            "path": MANIFEST_PATH,
            "commit": head,
            "git_blob": manifest_blob,
            "sha256": hashlib.sha256(manifest_raw).hexdigest(),
            "schema_version": "NOEMA_EXPERIMENT_PREREGISTRATION_MANIFEST_V2",
        },
        "implementation_subject_commit": head,
        "logical_experiment_id": EXPERIMENT_ID,
        "freeze_observed_at": FREEZE,
        "outcome_visibility_frontier": {
            "status": "NO_SCORED_OUTCOME_VISIBLE",
            "observed_at": OBSERVED,
            "evidence_refs": [git_subject("outcome-frontier")],
        },
        "execution_frontier": {
            "status": "NOT_STARTED",
            "observed_at": OBSERVED,
            "evidence_refs": [git_subject("execution-frontier")],
        },
        "visibility_inventory": {
            "inventory_owner_subject": git_subject("inventory-owner"),
            "required_surface_inventory_digest": "1" * 64,
            "surface_receipts": [
                {
                    "surface_id": "surface-a",
                    "status": "COMPLETE",
                    "observed_at": OBSERVED,
                    "result_digest": "2" * 64,
                    "evidence_subject": git_subject("surface-a-evidence"),
                }
            ],
            "overall_completeness": "COMPLETE",
        },
        "chronology_status": "PROSPECTIVE_CONFIRMED",
        "post_freeze_change_creates_new_subject": True,
        "separate_execution_authority_required": True,
        "claim_ceiling": "PREREGISTRATION_CHRONOLOGY_ONLY_NOT_EXECUTION_NOT_TRAINING_NOT_RESULT_VALIDITY",
    }


class ChronologyValidatorHostileTests(unittest.TestCase):
    def setUp(self):
        self.schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    def validate(self, candidate, *, schema=None):
        return v.validate_freeze_receipt(
            candidate,
            schema=self.schema if schema is None else schema,
            repo_root=ROOT,
        )

    def test_shape_valid_self_asserted_prospective_receipt_cannot_pass(self):
        result = self.validate(receipt())
        self.assertEqual(v.BLOCKED, result.result)
        self.assertNotEqual(v.PASS, result.result)
        self.assertIn("not yet machine-verifiable", result.reasons[0])

    def test_malformed_governance_schema_fails_closed(self):
        schema = copy.deepcopy(self.schema)
        schema["$id"] = "urn:hostile:replacement"
        result = self.validate(receipt(), schema=schema)
        self.assertEqual(v.FAIL_SCHEMA, result.result)

    def test_stale_manifest_binding_in_evidence_fails_closed(self):
        candidate = receipt()
        candidate["outcome_visibility_frontier"]["evidence_refs"][0][
            "bound_manifest_commit"
        ] = "0" * 40
        result = self.validate(candidate)
        self.assertEqual(v.FAIL_FREEZE, result.result)
        self.assertIn("manifest binding mismatch", result.reasons[0])

    def test_partial_inventory_surface_fails_closed(self):
        candidate = receipt()
        candidate["visibility_inventory"]["surface_receipts"][0]["status"] = "PARTIAL"
        result = self.validate(candidate)
        self.assertEqual(v.FAIL_FREEZE, result.result)
        self.assertIn("partial", result.reasons[0])

    def test_evidence_cut_before_freeze_fails_closed(self):
        candidate = receipt()
        candidate["execution_frontier"]["evidence_refs"][0][
            "coverage_cutoff"
        ] = "2026-09-19T17:59:59-04:00"
        result = self.validate(candidate)
        self.assertEqual(v.FAIL_FREEZE, result.result)
        self.assertIn("coverage", result.reasons[0])

    def test_visible_scored_outcome_cannot_be_prospective(self):
        candidate = receipt()
        candidate["outcome_visibility_frontier"]["status"] = "VISIBLE"
        result = self.validate(candidate)
        self.assertEqual(v.FAIL_FREEZE, result.result)

    def test_started_execution_cannot_be_prospective(self):
        candidate = receipt()
        candidate["execution_frontier"]["status"] = "STARTED"
        result = self.validate(candidate)
        self.assertEqual(v.FAIL_FREEZE, result.result)

    def test_external_readback_shape_alone_never_establishes_authority(self):
        candidate = receipt()
        candidate["outcome_visibility_frontier"]["evidence_refs"] = [
            external_subject("external-outcome")
        ]
        result = self.validate(candidate)
        self.assertEqual(v.BLOCKED, result.result)
        self.assertIn("provider resolution", result.reasons[0])

    def test_duplicate_evidence_subject_ids_fail_closed(self):
        candidate = receipt()
        candidate["execution_frontier"]["evidence_refs"][0]["subject_id"] = (
            candidate["outcome_visibility_frontier"]["evidence_refs"][0]["subject_id"]
        )
        result = self.validate(candidate)
        self.assertEqual(v.FAIL_FREEZE, result.result)
        self.assertIn("not unique", result.reasons[0])

    def test_tokenized_github_remote_normalizes_to_canonical_repository(self):
        self.assertEqual(
            "https://github.com/thebrazenbeard/noema",
            v._normalize_remote(
                "https://x-access-token:secret-token@github.com/thebrazenbeard/noema.git"
            ),
        )


if __name__ == "__main__":
    unittest.main()
