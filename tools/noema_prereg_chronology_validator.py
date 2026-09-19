from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

PASS = "PASS_FROZEN_VALID"
FAIL_SCHEMA = "FAIL_SCHEMA"
FAIL_FREEZE = "FAIL_FREEZE_INTEGRITY"
BLOCKED = "BLOCKED_UNAVAILABLE_EVIDENCE"

_SCHEMA_ID = "urn:noema:experiment-preregistration-freeze-receipt:v1"
_SCHEMA_VERSION = "NOEMA_EXPERIMENT_PREREGISTRATION_FREEZE_RECEIPT_V1"
_CLAIM_CEILING = (
    "PREREGISTRATION_CHRONOLOGY_ONLY_NOT_EXECUTION_NOT_TRAINING_NOT_RESULT_VALIDITY"
)
_CANONICAL_REPOSITORY = "thebrazenbeard/noema"
_CANONICAL_REMOTE = "https://github.com/thebrazenbeard/noema"
_SHA40 = re.compile(r"^[0-9a-f]{40}$")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")

_TOP_KEYS = {
    "schema_version", "classification", "status", "repository",
    "manifest_subject", "implementation_subject_commit", "logical_experiment_id",
    "freeze_observed_at", "outcome_visibility_frontier", "execution_frontier",
    "visibility_inventory", "chronology_status", "post_freeze_change_creates_new_subject",
    "separate_execution_authority_required", "claim_ceiling",
}


@dataclass(frozen=True)
class Validation:
    result: str
    reasons: tuple[str, ...]


def _fail(result: str, *reasons: str) -> Validation:
    return Validation(result=result, reasons=tuple(reasons))


def _parse_time(value: Any) -> datetime:
    if not isinstance(value, str) or not value:
        raise ValueError("timestamp must be a non-empty string")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timestamp must be timezone-aware")
    return parsed


def _normalize_remote(value: str) -> str:
    remote = value.strip()
    if remote.startswith("git@github.com:"):
        remote = "https://github.com/" + remote[len("git@github.com:"):]
    if remote.startswith("https://") or remote.startswith("http://"):
        parts = urlsplit(remote)
        host = parts.hostname or ""
        remote = f"https://{host}{parts.path}"
    if remote.endswith(".git"):
        remote = remote[:-4]
    return remote.rstrip("/").lower()


def _git(repo_root: Path, *args: str, binary: bool = False):
    completed = subprocess.run(
        ["git", "-C", str(repo_root), *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout if binary else completed.stdout.decode("utf-8").strip()


def _canonical_repo_is_bound(repo_root: Path) -> bool:
    try:
        origin = _git(repo_root, "remote", "get-url", "origin")
    except (OSError, subprocess.CalledProcessError):
        return False
    return _normalize_remote(origin) == _normalize_remote(_CANONICAL_REMOTE)


def _schema_surface_valid(schema: Any) -> bool:
    if not isinstance(schema, dict):
        return False
    props = schema.get("properties")
    return (
        schema.get("$id") == _SCHEMA_ID
        and isinstance(props, dict)
        and props.get("schema_version", {}).get("const") == _SCHEMA_VERSION
        and props.get("claim_ceiling", {}).get("const") == _CLAIM_CEILING
        and schema.get("additionalProperties") is False
        and set(schema.get("required", ())) == _TOP_KEYS
    )


def _shape_manifest(subject: Any) -> bool:
    if not isinstance(subject, dict):
        return False
    if set(subject) != {"path", "commit", "git_blob", "sha256", "schema_version"}:
        return False
    return (
        isinstance(subject["path"], str) and bool(subject["path"])
        and bool(_SHA40.fullmatch(subject["commit"]))
        and bool(_SHA40.fullmatch(subject["git_blob"]))
        and bool(_SHA256.fullmatch(subject["sha256"]))
        and subject["schema_version"] == "NOEMA_EXPERIMENT_PREREGISTRATION_MANIFEST_V2"
    )


def _verify_git_subject(
    subject: dict[str, Any],
    *,
    repo_root: Path,
    manifest_commit: str,
    experiment_id: str,
    freeze_at: datetime,
) -> str | None:
    exact = {
        "source_kind", "subject_id", "repository", "commit", "path", "git_blob",
        "sha256", "bound_manifest_commit", "logical_experiment_id", "observed_at",
        "coverage_cutoff",
    }
    if set(subject) != exact or subject.get("source_kind") != "GIT_IMMUTABLE":
        return "git evidence subject shape mismatch"
    if subject.get("repository") != _CANONICAL_REPOSITORY:
        return "git evidence repository is not canonical"
    if subject.get("bound_manifest_commit") != manifest_commit:
        return "evidence manifest binding mismatch"
    if subject.get("logical_experiment_id") != experiment_id:
        return "evidence experiment binding mismatch"
    if not isinstance(subject.get("subject_id"), str) or not subject["subject_id"]:
        return "evidence subject_id is missing"
    if not _SHA40.fullmatch(str(subject.get("commit", ""))):
        return "evidence commit shape mismatch"
    if not _SHA40.fullmatch(str(subject.get("git_blob", ""))):
        return "evidence blob shape mismatch"
    if not _SHA256.fullmatch(str(subject.get("sha256", ""))):
        return "evidence sha256 shape mismatch"
    try:
        observed_at = _parse_time(subject.get("observed_at"))
        coverage = _parse_time(subject.get("coverage_cutoff"))
    except ValueError as exc:
        return str(exc)
    if observed_at < coverage:
        return "evidence observation predates its claimed coverage cutoff"
    if coverage < freeze_at:
        return "evidence coverage does not reach freeze_observed_at"
    try:
        observed_blob = _git(repo_root, "rev-parse", f"{subject['commit']}:{subject['path']}")
        raw = _git(repo_root, "show", f"{subject['commit']}:{subject['path']}", binary=True)
    except (OSError, subprocess.CalledProcessError):
        return "immutable Git evidence is unavailable"
    if observed_blob != subject["git_blob"]:
        return "immutable Git evidence blob mismatch"
    if hashlib.sha256(raw).hexdigest() != subject["sha256"]:
        return "immutable Git evidence sha256 mismatch"
    return None


def _verify_external_subject_shape(
    subject: dict[str, Any],
    *,
    manifest_commit: str,
    experiment_id: str,
    freeze_at: datetime,
) -> str | None:
    exact = {
        "source_kind", "subject_id", "provider", "surface_id", "observation_id",
        "result_digest", "bound_manifest_commit", "logical_experiment_id",
        "observed_at", "coverage_cutoff",
    }
    if set(subject) != exact or subject.get("source_kind") != "EXTERNAL_READBACK":
        return "external evidence subject shape mismatch"
    for name in ("subject_id", "provider", "surface_id", "observation_id"):
        if not isinstance(subject.get(name), str) or not subject[name]:
            return f"external evidence {name} is missing"
    if not _SHA256.fullmatch(str(subject.get("result_digest", ""))):
        return "external evidence result digest shape mismatch"
    if subject.get("bound_manifest_commit") != manifest_commit:
        return "evidence manifest binding mismatch"
    if subject.get("logical_experiment_id") != experiment_id:
        return "evidence experiment binding mismatch"
    try:
        observed_at = _parse_time(subject.get("observed_at"))
        coverage = _parse_time(subject.get("coverage_cutoff"))
    except ValueError as exc:
        return str(exc)
    if observed_at < coverage:
        return "external evidence observation predates its claimed coverage cutoff"
    if coverage < freeze_at:
        return "evidence coverage does not reach freeze_observed_at"
    return None


def _verify_external_subject_shape(
    subject: dict[str, Any],
    *,
    manifest_commit: str,
    experiment_id: str,
    freeze_at: datetime,
) -> str | None:
    exact = {"source_kind", "subject_id", "provider", "surface_id", "observation_id", "result_digest", "bound_manifest_commit", "logical_experiment_id", "observed_at", "coverage_cutoff"}
    if set(subject) != exact or subject.get("source_kind") != "EXTERNAL_READBACK":
        return "external evidence subject shape mismatch"
    for name in ("subject_id", "provider", "surface_id", "observation_id"):
        if not isinstance(subject.get(name), str) or not subject[name]:
            return f"external evidence {name} is missing"
    if not _SHA256.fullmatch(str(subject.get("result_digest", ""))):
        return "external evidence result digest shape mismatch"
    if subject.get("bound_manifest_commit") != manifest_commit:
        return "evidence manifest binding mismatch"
    if subject.get("logical_experiment_id") != experiment_id:
        return "evidence experiment binding mismatch"
    try:
        observed_at = _parse_time(subject.get("observed_at"))
        coverage = _parse_time(subject.get("coverage_cutoff"))
    except ValueError as exc:
        return str(exc)
    if observed_at < coverage:
        return "external evidence observation predates its claimed coverage cutoff"
    if coverage < freeze_at:
        return "evidence coverage does not reach freeze_observed_at"
    return None


def _verify_evidence_subject(
    subject: Any,
    *,
    repo_root: Path,
    manifest_commit: str,
    experiment_id: str,
    freeze_at: datetime,
) -> tuple[str | None, bool]:
    if not isinstance(subject, dict):
        return "chronology evidence subject must be an object", False
    kind = subject.get("source_kind")
    if kind == "GIT_IMMUTABLE":
        return (
            _verify_git_subject(
                subject,
                repo_root=repo_root,
                manifest_commit=manifest_commit,
                experiment_id=experiment_id,
                freeze_at=freeze_at,
            ),
            True,
        )
    if kind == "EXTERNAL_READBACK":
        reason = _verify_external_subject_shape(
            subject,
            manifest_commit=manifest_commit,
            experiment_id=experiment_id,
            freeze_at=freeze_at,
        )
        # External provider readback must be independently resolved by a separately
        # reviewed provider adapter. Shape-valid evidence therefore remains blocked.
        return reason, False
    return "unknown chronology evidence subject type", False


def validate_freeze_receipt(
    receipt: Any,
    *,
    schema: Any,
    repo_root: str | Path,
) -> Validation:
    repo_root = Path(repo_root)
    if not _schema_surface_valid(schema):
        return _fail(FAIL_SCHEMA, "freeze receipt governance schema malformed or replaced")
    if not isinstance(receipt, dict) or set(receipt) != _TOP_KEYS:
        return _fail(FAIL_SCHEMA, "freeze receipt top-level shape mismatch")
    if receipt.get("schema_version") != _SCHEMA_VERSION:
        return _fail(FAIL_SCHEMA, "freeze receipt schema_version mismatch")
    if receipt.get("classification") not in {"IP_CONFIDENTIAL", "IP_REVIEW_REQUIRED"}:
        return _fail(FAIL_SCHEMA, "freeze receipt classification mismatch")
    if receipt.get("status") != "FROZEN_PROVENANCE_ONLY_NOT_EXECUTION_AUTHORITY":
        return _fail(FAIL_FREEZE, "freeze receipt status exceeds provenance-only ceiling")
    if receipt.get("repository") != _CANONICAL_REPOSITORY:
        return _fail(FAIL_FREEZE, "freeze receipt repository mismatch")
    if receipt.get("claim_ceiling") != _CLAIM_CEILING:
        return _fail(FAIL_FREEZE, "freeze receipt claim ceiling mismatch")
    if receipt.get("post_freeze_change_creates_new_subject") is not True:
        return _fail(FAIL_FREEZE, "post-freeze mutation rule is not fail-closed")
    if receipt.get("separate_execution_authority_required") is not True:
        return _fail(FAIL_FREEZE, "separate execution authority is not required")
    if not _canonical_repo_is_bound(repo_root):
        return _fail(BLOCKED, "local repository origin is not the canonical Noema repository")

    manifest = receipt.get("manifest_subject")
    if not _shape_manifest(manifest):
        return _fail(FAIL_SCHEMA, "manifest subject shape mismatch")
    experiment_id = receipt.get("logical_experiment_id")
    if not isinstance(experiment_id, str) or not experiment_id:
        return _fail(FAIL_SCHEMA, "logical experiment id is missing")
    if not _SHA40.fullmatch(str(receipt.get("implementation_subject_commit", ""))):
        return _fail(FAIL_SCHEMA, "implementation subject commit shape mismatch")
    try:
        freeze_at = _parse_time(receipt.get("freeze_observed_at"))
    except ValueError as exc:
        return _fail(FAIL_SCHEMA, str(exc))

    try:
        manifest_blob = _git(repo_root, "rev-parse", f"{manifest['commit']}:{manifest['path']}")
        manifest_bytes = _git(repo_root, "show", f"{manifest['commit']}:{manifest['path']}", binary=True)
    except (OSError, subprocess.CalledProcessError):
        return _fail(BLOCKED, "frozen manifest subject is unavailable")
    if manifest_blob != manifest["git_blob"] or hashlib.sha256(manifest_bytes).hexdigest() != manifest["sha256"]:
        return _fail(FAIL_FREEZE, "frozen manifest immutable binding mismatch")

    chronology = receipt.get("chronology_status")
    outcome = receipt.get("outcome_visibility_frontier")
    execution = receipt.get("execution_frontier")
    inventory = receipt.get("visibility_inventory")
    if not all(isinstance(x, dict) for x in (outcome, execution, inventory)):
        return _fail(FAIL_SCHEMA, "chronology frontier/inventory shape mismatch")
    if set(outcome) != {"status", "observed_at", "evidence_refs"}:
        return _fail(FAIL_SCHEMA, "outcome visibility frontier shape mismatch")
    if set(execution) != {"status", "observed_at", "evidence_refs"}:
        return _fail(FAIL_SCHEMA, "execution frontier shape mismatch")
    if set(inventory) != {"inventory_owner_subject", "required_surface_inventory_digest", "surface_receipts", "overall_completeness"}:
        return _fail(FAIL_SCHEMA, "visibility inventory shape mismatch")
    if not _SHA256.fullmatch(str(inventory.get("required_surface_inventory_digest", ""))):
        return _fail(FAIL_SCHEMA, "visibility inventory digest shape mismatch")

    if chronology == "CONTRADICTED":
        return _fail(FAIL_FREEZE, "chronology receipt explicitly contradicted")
    if chronology != "PROSPECTIVE_CONFIRMED":
        return _fail(BLOCKED, "chronology is not prospectively confirmed")

    if outcome.get("status") != "NO_SCORED_OUTCOME_VISIBLE":
        return _fail(FAIL_FREEZE, "scored outcome visibility contradicts prospective freeze")
    if execution.get("status") != "NOT_STARTED":
        return _fail(FAIL_FREEZE, "execution visibility contradicts prospective freeze")
    if inventory.get("overall_completeness") != "COMPLETE":
        return _fail(FAIL_FREEZE, "visibility inventory is not complete")

    try:
        if _parse_time(outcome.get("observed_at")) < freeze_at:
            return _fail(FAIL_FREEZE, "outcome frontier observation does not reach freeze")
        if _parse_time(execution.get("observed_at")) < freeze_at:
            return _fail(FAIL_FREEZE, "execution frontier observation does not reach freeze")
    except ValueError as exc:
        return _fail(FAIL_SCHEMA, str(exc))

    surfaces = inventory.get("surface_receipts")
    if not isinstance(surfaces, list) or not surfaces:
        return _fail(FAIL_SCHEMA, "visibility surface inventory is empty")
    surface_ids: list[str] = []
    for surface in surfaces:
        if not isinstance(surface, dict):
            return _fail(FAIL_SCHEMA, "visibility surface receipt must be an object")
        if set(surface) != {"surface_id", "status", "observed_at", "result_digest", "evidence_subject"}:
            return _fail(FAIL_SCHEMA, "visibility surface receipt shape mismatch")
        if not _SHA256.fullmatch(str(surface.get("result_digest", ""))):
            return _fail(FAIL_SCHEMA, "visibility surface result digest shape mismatch")
        if surface.get("status") != "COMPLETE":
            return _fail(FAIL_FREEZE, "visibility surface is partial/unavailable/unauthorized")
        sid = surface.get("surface_id")
        if not isinstance(sid, str) or not sid:
            return _fail(FAIL_SCHEMA, "visibility surface_id is missing")
        surface_ids.append(sid)
        try:
            if _parse_time(surface.get("observed_at")) < freeze_at:
                return _fail(FAIL_FREEZE, "visibility surface observation does not reach freeze")
        except ValueError as exc:
            return _fail(FAIL_SCHEMA, str(exc))
    if len(surface_ids) != len(set(surface_ids)):
        return _fail(FAIL_FREEZE, "visibility surface inventory contains duplicate surface ids")

    evidence_subjects: list[Any] = []
    for frontier in (outcome, execution):
        refs = frontier.get("evidence_refs")
        if not isinstance(refs, list) or not refs:
            return _fail(FAIL_SCHEMA, "chronology frontier evidence refs are absent")
        evidence_subjects.extend(refs)
    evidence_subjects.append(inventory.get("inventory_owner_subject"))
    evidence_subjects.extend(surface.get("evidence_subject") for surface in surfaces)

    has_unresolved_external = False
    subject_ids: list[str] = []
    for subject in evidence_subjects:
        reason, independently_resolved = _verify_evidence_subject(
            subject,
            repo_root=repo_root,
            manifest_commit=manifest["commit"],
            experiment_id=experiment_id,
            freeze_at=freeze_at,
        )
        if reason:
            return _fail(FAIL_FREEZE, reason)
        if isinstance(subject, dict):
            sid = subject.get("subject_id")
            if isinstance(sid, str):
                subject_ids.append(sid)
        if not independently_resolved:
            has_unresolved_external = True
    if len(subject_ids) != len(set(subject_ids)):
        return _fail(FAIL_FREEZE, "chronology evidence subject ids are not unique")

    if has_unresolved_external:
        return _fail(BLOCKED, "external chronology evidence requires independently reviewed provider resolution")

    # Immutable Git identity/digest/coverage can be verified here, but the current
    # governance schema does not define a machine-readable semantic proof that a
    # resolved artifact contains the complete authoritative result/execution
    # history and no qualifying event through the freeze. Do not silently infer it.
    return _fail(
        BLOCKED,
        "authoritative result/execution absence semantics are not yet machine-verifiable",
    )


def load_and_validate(receipt_path: str | Path, *, repo_root: str | Path) -> Validation:
    root = Path(repo_root)
    schema = json.loads(
        (root / "governance" / "EXPERIMENT_PREREGISTRATION_FREEZE_RECEIPT_SCHEMA_V1.json")
        .read_text(encoding="utf-8")
    )
    receipt = json.loads(Path(receipt_path).read_text(encoding="utf-8"))
    return validate_freeze_receipt(receipt, schema=schema, repo_root=root)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Noema preregistration chronology receipt")
    parser.add_argument("receipt", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    result = load_and_validate(args.receipt, repo_root=args.repo_root)
    print(json.dumps({"result": result.result, "reasons": list(result.reasons)}, sort_keys=True))
    return 0 if result.result == PASS else 2


if __name__ == "__main__":
    raise SystemExit(main())
