from __future__ import annotations

import datetime as dt
import hashlib
import json
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

SCHEMA_ID = "urn:noema:experiment-preregistration-freeze-receipt:v1"
SCHEMA_VERSION = "NOEMA_EXPERIMENT_PREREGISTRATION_FREEZE_RECEIPT_V1"
CLAIM_CEILING = "PREREGISTRATION_CHRONOLOGY_ONLY_NOT_EXECUTION_NOT_TRAINING_NOT_RESULT_VALIDITY"


@dataclass(frozen=True)
class EvidenceResolution:
    available: bool
    authoritative: bool
    subject_exact: bool
    coverage_cutoff: dt.datetime | None
    qualifying_result_visible_at_or_before_freeze: bool | None
    qualifying_execution_visible_at_or_before_freeze: bool | None


class EvidenceResolver(Protocol):
    def resolve(self, subject: dict[str, Any], *, freeze_observed_at: dt.datetime) -> EvidenceResolution:
        ...


def _time(value: Any) -> dt.datetime:
    if not isinstance(value, str) or not value:
        raise ValueError("timestamp must be non-empty string")
    parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timestamp must include timezone")
    return parsed.astimezone(dt.timezone.utc)


def _subjects(receipt: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for key in ("outcome_visibility_frontier", "execution_frontier"):
        value = receipt.get(key)
        if not isinstance(value, dict):
            raise ValueError(f"{key} must be object")
        refs = value.get("evidence_refs")
        if not isinstance(refs, list) or not refs:
            raise ValueError(f"{key}.evidence_refs must be non-empty")
        out.extend(refs)
    inventory = receipt.get("visibility_inventory")
    if not isinstance(inventory, dict):
        raise ValueError("visibility_inventory must be object")
    owner = inventory.get("inventory_owner_subject")
    if not isinstance(owner, dict):
        raise ValueError("inventory_owner_subject must be object")
    out.append(owner)
    surfaces = inventory.get("surface_receipts")
    if not isinstance(surfaces, list) or not surfaces:
        raise ValueError("surface_receipts must be non-empty")
    for item in surfaces:
        if not isinstance(item, dict) or not isinstance(item.get("evidence_subject"), dict):
            raise ValueError("surface receipt evidence_subject must be object")
        out.append(item["evidence_subject"])
    return out


def validate_freeze_receipt(
    receipt: dict[str, Any],
    *,
    schema: dict[str, Any],
    resolver: EvidenceResolver,
) -> dict[str, Any]:
    if schema.get("$id") != SCHEMA_ID:
        return {"status": "FAIL_FREEZE_INTEGRITY", "reason": "freeze schema identity mismatch"}
    if schema.get("properties", {}).get("schema_version", {}).get("const") != SCHEMA_VERSION:
        return {"status": "FAIL_FREEZE_INTEGRITY", "reason": "freeze schema version mismatch"}
    if receipt.get("schema_version") != SCHEMA_VERSION:
        return {"status": "FAIL_FREEZE_INTEGRITY", "reason": "receipt schema version mismatch"}
    if receipt.get("claim_ceiling") != CLAIM_CEILING:
        return {"status": "FAIL_FREEZE_INTEGRITY", "reason": "claim ceiling mismatch"}

    manifest = receipt.get("manifest_subject")
    if not isinstance(manifest, dict):
        return {"status": "FAIL_FREEZE_INTEGRITY", "reason": "manifest subject missing"}
    manifest_commit = manifest.get("commit")
    experiment_id = receipt.get("logical_experiment_id")
    if not isinstance(manifest_commit, str) or len(manifest_commit) != 40:
        return {"status": "FAIL_FREEZE_INTEGRITY", "reason": "manifest commit invalid"}
    if not isinstance(experiment_id, str) or not experiment_id:
        return {"status": "FAIL_FREEZE_INTEGRITY", "reason": "logical experiment id invalid"}

    try:
        freeze = _time(receipt.get("freeze_observed_at"))
        subjects = _subjects(receipt)
    except Exception as exc:
        return {"status": "FAIL_FREEZE_INTEGRITY", "reason": str(exc)}

    chronology = receipt.get("chronology_status")
    if chronology == "CONTRADICTED":
        return {"status": "FAIL_FREEZE_INTEGRITY", "reason": "receipt chronology contradicted"}
    if chronology != "PROSPECTIVE_CONFIRMED":
        return {"status": "UNPROVEN", "reason": "prospective chronology not confirmed"}

    outcome = receipt.get("outcome_visibility_frontier", {})
    execution = receipt.get("execution_frontier", {})
    if outcome.get("status") != "NO_SCORED_OUTCOME_VISIBLE":
        return {"status": "FAIL_FREEZE_INTEGRITY", "reason": "scored outcome visible or unknown"}
    if execution.get("status") != "NOT_STARTED":
        return {"status": "FAIL_FREEZE_INTEGRITY", "reason": "execution started or unknown"}

    inventory = receipt["visibility_inventory"]
    if inventory.get("overall_completeness") != "COMPLETE":
        return {"status": "BLOCKED_UNAVAILABLE_EVIDENCE", "reason": "inventory is not complete"}
    for surface in inventory["surface_receipts"]:
        if surface.get("status") != "COMPLETE":
            return {"status": "BLOCKED_UNAVAILABLE_EVIDENCE", "reason": "authoritative surface is not complete"}

    for subject in subjects:
        if subject.get("bound_manifest_commit") != manifest_commit:
            return {"status": "FAIL_FREEZE_INTEGRITY", "reason": "stale/mismatched manifest binding"}
        if subject.get("logical_experiment_id") != experiment_id:
            return {"status": "FAIL_FREEZE_INTEGRITY", "reason": "stale/mismatched experiment binding"}
        try:
            resolution = resolver.resolve(subject, freeze_observed_at=freeze)
        except Exception as exc:
            return {"status": "BLOCKED_UNAVAILABLE_EVIDENCE", "reason": f"resolver unavailable: {exc}"}
        if not resolution.available or not resolution.authoritative:
            return {"status": "BLOCKED_UNAVAILABLE_EVIDENCE", "reason": "evidence unavailable or non-authoritative"}
        if not resolution.subject_exact:
            return {"status": "FAIL_FREEZE_INTEGRITY", "reason": "evidence subject digest/binding mismatch"}
        if resolution.coverage_cutoff is None or resolution.coverage_cutoff < freeze:
            return {"status": "FAIL_FREEZE_INTEGRITY", "reason": "evidence coverage does not reach freeze"}
        if resolution.qualifying_result_visible_at_or_before_freeze is None:
            return {"status": "BLOCKED_UNAVAILABLE_EVIDENCE", "reason": "result visibility is unresolved"}
        if resolution.qualifying_execution_visible_at_or_before_freeze is None:
            return {"status": "BLOCKED_UNAVAILABLE_EVIDENCE", "reason": "execution visibility is unresolved"}
        if resolution.qualifying_result_visible_at_or_before_freeze:
            return {"status": "FAIL_FREEZE_INTEGRITY", "reason": "pre-freeze scored result visible"}
        if resolution.qualifying_execution_visible_at_or_before_freeze:
            return {"status": "FAIL_FREEZE_INTEGRITY", "reason": "pre-freeze execution visible"}

    return {"status": "PASS_PROSPECTIVE_CONFIRMED", "reason": "all authoritative chronology evidence passed"}


class GitIdentityResolver:
    """Verify Git evidence identity only.

    This resolver intentionally cannot interpret arbitrary evidence bytes as proving
    absence of scored outcomes/execution. Those semantic visibility fields remain
    unresolved, so a PROSPECTIVE_CONFIRMED receipt stays BLOCKED until a separately
    qualified evidence-specific resolver is supplied.
    """

    def __init__(self, repository_root: str | Path) -> None:
        self.root = Path(repository_root)

    def resolve(self, subject: dict[str, Any], *, freeze_observed_at: dt.datetime) -> EvidenceResolution:
        if subject.get("source_kind") != "GIT_IMMUTABLE":
            return EvidenceResolution(False, False, False, None, None, None)
        commit = str(subject.get("commit", ""))
        path = str(subject.get("path", ""))
        expected_blob = str(subject.get("git_blob", ""))
        expected_sha = str(subject.get("sha256", ""))
        observed_blob = subprocess.check_output(
            ["git", "rev-parse", f"{commit}:{path}"], cwd=self.root, text=True
        ).strip()
        data = subprocess.check_output(["git", "cat-file", "blob", observed_blob], cwd=self.root)
        exact = observed_blob == expected_blob and hashlib.sha256(data).hexdigest() == expected_sha
        try:
            cutoff = _time(subject.get("coverage_cutoff"))
        except Exception:
            cutoff = None
        return EvidenceResolution(True, True, exact, cutoff, None, None)


def load_json(path: str | Path) -> dict[str, Any]:
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("JSON root must be object")
    return value