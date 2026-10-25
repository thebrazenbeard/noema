"""Regression tests for the dependency-free editor startup source guard."""

from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from scripts.check_editor_source_safety import check_source


ROOT = Path(__file__).resolve().parents[1]


def test_actual_checkout_has_no_editor_autorun_or_nonfont_script():
    assert check_source(ROOT) == ()


def test_jsonc_editor_task_and_automatic_settings_are_rejected():
    with TemporaryDirectory() as directory:
        root = Path(directory)
        editor = root / ".vscode"
        editor.mkdir()
        (editor / "tasks.json").write_text(
            '{"tasks":[{"runOn":"folderOpen", "command":"node public/fonts/payload.woff2",},]}',
            encoding="utf-8",
        )
        (editor / "settings.json").write_text(
            '{"task.allowAutomaticTasks":"on"}', encoding="utf-8"
        )
        findings = check_source(root)
        assert any("editor folderOpen task" in item for item in findings)
        assert any("automatic editor tasks enabled" in item for item in findings)
        assert any("command executes a font-directory file" in item for item in findings)


def test_workspace_folderopen_variant_is_rejected_without_tasks_json():
    with TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "project.code-workspace").write_text(
            '{"tasks":{"runOn" : "folderOpen"}}', encoding="utf-8"
        )
        assert any("editor folderOpen task" in item for item in check_source(root))


def test_unicode_escaped_jsonc_keys_cannot_hide_editor_autorun():
    with TemporaryDirectory() as directory:
        root = Path(directory)
        editor = root / ".vscode"
        editor.mkdir()
        (editor / "tasks.json").write_text(
            r'{"tasks":[{"run\u004fn":"folder\u004fpen"}]}',
            encoding="utf-8",
        )
        (editor / "settings.json").write_text(
            r'{"task.allowAutomaticT\u0061sks":"\u006fn"}',
            encoding="utf-8",
        )
        findings = check_source(root)
        assert any("tasks.json: escaped editor configuration" in item for item in findings)
        assert any("settings.json: escaped editor configuration" in item for item in findings)


def test_disguised_script_as_font_is_rejected_but_real_woff2_is_allowed():
    with TemporaryDirectory() as directory:
        root = Path(directory)
        fonts = root / "public" / "fonts"
        fonts.mkdir(parents=True)
        (fonts / "normal.woff2").write_bytes(b"wOF2" + b"\0" * 100)
        assert check_source(root) == ()
        (fonts / "stealth.woff2").write_bytes(b"require('child_process')")
        findings = check_source(root)
        assert any("invalid font header" in item for item in findings)
        (fonts / "stealth.woff2").unlink()
        (fonts / "stealth.lkf").write_bytes(b"require('child_process')")
        findings = check_source(root)
        assert any("non-font file" in item for item in findings)


def test_symlinked_font_directory_is_rejected_without_following_it():
    with TemporaryDirectory() as directory:
        root = Path(directory)
        outside = root / "outside"
        outside.mkdir()
        (root / "public").mkdir()
        try:
            (root / "public" / "fonts").symlink_to(outside, target_is_directory=True)
        except OSError as exc:
            pytest.skip(f"directory symlinks unavailable: {exc}")
        assert any("symlinked font directory" in item for item in check_source(root))


def test_case_variant_editor_folder_is_scanned_for_autorun():
    with TemporaryDirectory() as directory:
        root = Path(directory)
        editor = root / ".VSCode"
        editor.mkdir()
        (editor / "Tasks.JSON").write_text(
            '{"tasks":[{"runOn":"folderOpen"}]}', encoding="utf-8"
        )
        assert any("editor folderOpen task" in item for item in check_source(root))
