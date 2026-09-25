from noema.provenance import ArtifactRef, ArtifactRecord, DictArtifactResolver, canonical_json_bytes


def test_canonical_json_is_order_independent():
    assert canonical_json_bytes({"b": 2, "a": 1}) == b'{"a":1,"b":2}'


def test_resolver_rejects_digest_mismatch():
    data = b"abc"
    ref = ArtifactRef(repository="thebrazenbeard/noema", commit="a" * 40, path="src/x.py", sha256="0" * 64)
    resolver = DictArtifactResolver({(ref.repository, ref.commit, ref.path): ArtifactRecord(data=data)})
    try:
        resolver.resolve(ref)
    except ValueError as exc:
        assert "sha256" in str(exc)
    else:
        raise AssertionError("digest mismatch accepted")


def test_design_only_subject_is_not_implementation():
    from noema.provenance import ImplementationSubjectManifest
    subject = ImplementationSubjectManifest(
        source_paths=("docs/working-design/x.md",),
        test_paths=("tests/test_x.py",),
        instrumentation_paths=(),
    )
    assert subject.is_implementation_subject() is False


def test_resolver_rejects_git_blob_mismatch():
    from noema.provenance import ArtifactRef, ArtifactRecord, DictArtifactResolver
    ref = ArtifactRef(
        repository="thebrazenbeard/noema",
        commit="a" * 40,
        path="src/x.py",
        git_blob="0" * 40,
    )
    resolver = DictArtifactResolver({(ref.repository, ref.commit, ref.path): ArtifactRecord(data=b"abc")})
    try:
        resolver.resolve(ref)
    except ValueError as exc:
        assert "git_blob" in str(exc)
    else:
        raise AssertionError("git blob mismatch accepted")
