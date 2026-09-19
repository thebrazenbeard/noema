from __future__ import annotations

import datetime as dt
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("freeze_validator", ROOT / "tools" / "validate_freeze_receipt.py")
validator = importlib.util.module_from_spec(spec)
assert spec and spec.loader
import sys
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


FREEZE = "2026-09-19T12:00:00Z"
COMMIT = "a" * 40
EXPERIMENT = "exp-1"


def subject(subject_id: str = "s1"):
    return {
        "source_kind": "GIT_IMMUTABLE",
        "subject_id": subject_id,
        "repository": "owner/repo",
        "commit": "b" * 40,
        "path": "evidence.json",
        "git_blob": "c" * 40,
        "sha256": "d" * 64,
        "bound_manifest_commit": COMMIT,
        "logical_experiment_id": EXPERIMENT,
        "observed_at": "2026-09-19T12:05:00Z",
        "coverage_cutoff": "2026-09-19T12:00:00Z",
    }


def receipt():
    a, b, c = subject("outcome"), subject("execution"), subject("inventory")
    d = subject("surface")
    return {
        "schema_version": validator.SCHEMA_VERSION,
        "classification": "IP_CONFIDENTIAL",
        "status": "FROZEN_PROVENANCE_ONLY_NOT_EXECUTION_AUTHORITY",
        "repository": "owner/repo",
        "manifest_subject": {
            "path": "manifest.json",
            "commit": COMMIT,
            "git_blob": "e" * 40,
            "sha256": "f" * 64,
            "schema_version": "NOEMA_EXPERIMENT_PREREGISTRATION_MANIFEST_V2",
        },
        "implementation_subject_commit": "1" * 40,
        "logical_experiment_id": EXPERIMENT,
        "freeze_observed_at": FREEZE,
        "outcome_visibility_frontier": {
            "status": "NO_SCORED_OUTCOME_VISIBLE",
            "observed_at": "2026-09-19T12:05:00Z",
            "evidence_refs": [a],
        },
        "execution_frontier": {
            "status": "NOT_STARTED",
            "observed_at": "2026-09-19T12:05:00Z",
            "evidence_refs": [b],
        },
        "visibility_inventory": {
            "inventory_owner_subject": c,
            "required_surface_inventory_digest": "2" * 64,
            "surface_receipts": [{
                "surface_id": "results",
                "status": "COMPLETE",
                "observed_at": "2026-09-19T12:05:00Z",
                "result_digest": "3" * 64,
                "evidence_subject": d,
            }],
            "overall_completeness": "COMPLETE",
        },
        "chronology_status": "PROSPECTIVE_CONFIRMED",
        "post_freeze_change_creates_new_subject": True,
        "separate_execution_authority_required": True,
        "claim_ceiling": validator.CLAIM_CEILING,
    }


def schema():
    return validator.load_json(
        ROOT / "governance" / "EXPERIMENT_PREREGISTRATION_FREEZE_RECEIPT_SCHEMA_V1.json"
    )


class FakeResolver:
    def __init__(self, *, available=True, authoritative=True, exact=True, cutoff=FREEZE, result=False, execution=False):
        self.available = available
        self.authoritative = authoritative
        self.exact = exact
        self.cutoff = cutoff
        self.result = result
        self.execution = execution

    def resolve(self, _subject, *, freeze_observed_at):
        cutoff = validator._time(self.cutoff) if self.cutoff is not None else None
        return validator.EvidenceResolution(
            self.available,
            self.authoritative,
            self.exact,
            cutoff,
            self.result,
            self.execution,
        )


class FreezeChronologyHostileTests(unittest.TestCase):
    def test_23_malformed_schema_fails_closed(self):
        bad = schema()
        bad["$id"] = "wrong"
        result = validator.validate_freeze_receipt(receipt(), schema=bad, resolver=FakeResolver())
        self.assertEqual("FAIL_FREEZE_INTEGRITY", result["status"])

    def test_wrong_receipt_status_fails_exact_schema(self):
        r = receipt()
        r["status"] = "FROZEN"
        result = validator.validate_freeze_receipt(
            r, schema=schema(), resolver=FakeResolver()
        )
        self.assertEqual("FAIL_FREEZE_INTEGRITY", result["status"])

    def test_false_separate_execution_authority_fails_exact_schema(self):
        r = receipt()
        r["separate_execution_authority_required"] = False
        result = validator.validate_freeze_receipt(
            r, schema=schema(), resolver=FakeResolver()
        )
        self.assertEqual("FAIL_FREEZE_INTEGRITY", result["status"])

    def test_malformed_evidence_subject_fails_exact_schema(self):
        r = receipt()
        r["outcome_visibility_frontier"]["evidence_refs"][0]["sha256"] = "not-a-digest"
        result = validator.validate_freeze_receipt(
            r, schema=schema(), resolver=FakeResolver()
        )
        self.assertEqual("FAIL_FREEZE_INTEGRITY", result["status"])

    def test_24_stale_manifest_binding_fails_closed(self):
        r = receipt()
        r["outcome_visibility_frontier"]["evidence_refs"][0]["bound_manifest_commit"] = "9" * 40
        result = validator.validate_freeze_receipt(r, schema=schema(), resolver=FakeResolver())
        self.assertEqual("FAIL_FREEZE_INTEGRITY", result["status"])

    def test_25_partial_inventory_blocks(self):
        r = receipt()
        r["visibility_inventory"]["surface_receipts"][0]["status"] = "PARTIAL"
        result = validator.validate_freeze_receipt(r, schema=schema(), resolver=FakeResolver())
        self.assertEqual("BLOCKED_UNAVAILABLE_EVIDENCE", result["status"])

    def test_26_insufficient_coverage_fails_closed(self):
        result = validator.validate_freeze_receipt(
            receipt(),
            schema=schema(),
            resolver=FakeResolver(cutoff="2026-09-19T11:59:59Z"),
        )
        self.assertEqual("FAIL_FREEZE_INTEGRITY", result["status"])

    def test_27_pre_freeze_result_visibility_fails_closed(self):
        result = validator.validate_freeze_receipt(
            receipt(), schema=schema(), resolver=FakeResolver(result=True)
        )
        self.assertEqual("FAIL_FREEZE_INTEGRITY", result["status"])

    def test_27_pre_freeze_execution_visibility_fails_closed(self):
        result = validator.validate_freeze_receipt(
            receipt(), schema=schema(), resolver=FakeResolver(execution=True)
        )
        self.assertEqual("FAIL_FREEZE_INTEGRITY", result["status"])

    def test_valid_resolved_chronology_passes_at_chronology_scope_only(self):
        result = validator.validate_freeze_receipt(receipt(), schema=schema(), resolver=FakeResolver())
        self.assertEqual("PASS_PROSPECTIVE_CONFIRMED", result["status"])

    def test_unresolved_semantics_blocks_instead_of_self_attesting(self):
        result = validator.validate_freeze_receipt(
            receipt(), schema=schema(), resolver=FakeResolver(result=None, execution=None)
        )
        self.assertEqual("BLOCKED_UNAVAILABLE_EVIDENCE", result["status"])


if __name__ == "__main__":
    unittest.main()