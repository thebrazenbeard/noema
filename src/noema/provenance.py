from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import re
from typing import Mapping

_SHA40 = re.compile(r"^[0-9a-f]{40}$")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")


def canonical_json_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_hex(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


@dataclass(frozen=True, slots=True)
class ArtifactRef:
    repository: str
    commit: str
    path: str
    git_blob: str | None = None
    sha256: str | None = None

    def __post_init__(self) -> None:
        if not self.repository or "/" not in self.repository:
            raise ValueError("repository must be owner/name")
        if not _SHA40.fullmatch(self.commit):
            raise ValueError("commit must be an exact 40-character lowercase hex SHA")
        if not self.path or self.path.startswith("/") or ".." in self.path.split("/"):
            raise ValueError("path must be a repository-relative immutable artifact path")
        if self.git_blob is not None and not _SHA40.fullmatch(self.git_blob):
            raise ValueError("git_blob must be 40-character lowercase hex")
        if self.sha256 is not None and not _SHA256.fullmatch(self.sha256):
            raise ValueError("sha256 must be 64-character lowercase hex")


@dataclass(frozen=True, slots=True)
class ArtifactRecord:
    data: bytes


@dataclass(frozen=True, slots=True)
class ImplementationSubjectManifest:
    source_paths: tuple[str, ...]
    test_paths: tuple[str, ...]
    instrumentation_paths: tuple[str, ...]

    def is_implementation_subject(self) -> bool:
        has_source = any(path.startswith("src/") for path in self.source_paths)
        has_tests = any(path.startswith("tests/") for path in self.test_paths)
        has_instrumentation = bool(self.instrumentation_paths)
        return has_source and has_tests and has_instrumentation


class DictArtifactResolver:
    def __init__(
        self,
        records: Mapping[tuple[str, str, str], ArtifactRecord],
    ) -> None:
        self._records = dict(records)

    def resolve(self, ref: ArtifactRef) -> ArtifactRecord:
        key = (ref.repository, ref.commit, ref.path)
        try:
            record = self._records[key]
        except KeyError as exc:
            raise FileNotFoundError(
                f"artifact unavailable: {ref.repository}@{ref.commit}:{ref.path}"
            ) from exc
        if ref.git_blob is not None:
            actual_blob = git_blob_hex(record.data)
            if actual_blob != ref.git_blob:
                raise ValueError(
                    f"git_blob mismatch for {ref.path}: expected {ref.git_blob}, got {actual_blob}"
                )
        if ref.sha256 is not None:
            actual = sha256_hex(record.data)
            if actual != ref.sha256:
                raise ValueError(
                    f"sha256 mismatch for {ref.path}: expected {ref.sha256}, got {actual}"
                )
        return record
