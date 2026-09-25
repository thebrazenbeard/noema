from importlib.metadata import version


def test_runtime_dependencies_are_exactly_supported():
    assert version("jsonschema") == "4.26.0"
    assert version("pytest") == "9.0.2"


def test_noema_package_imports():
    import noema
    assert noema.__all__ == []
