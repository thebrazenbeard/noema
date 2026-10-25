"""Dependency-free guard against editor-startup execution and disguised scripts.

Run immediately after checkout, before installing project dependencies. This
inspects source metadata and font headers without executing any scripts.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re


_AUTORUN = re.compile(r"(?i)[\"']?runOn[\"']?\s*:\s*[\"']?folderOpen\b")
_ALLOW_AUTO = re.compile(
    r"(?i)[\"']?task\.allowAutomaticTasks[\"']?\s*:\s*(?:true\b|[\"'](?:on|allow)[\"'])"
)
_FONT_COMMAND = re.compile(
    r"(?i)\b(?:node|bun|deno|python\d*|bash|sh|powershell|pwsh)\b[^\r\n]{0,256}"
    r"(?:public[/\\]fonts|fonts[/\\])"
)
# JSONC accepts Unicode escapes in property names and values. A textual scan
# cannot safely normalize every JSONC dialect, so reject escaped editor
# configuration instead of allowing run\u004fn/folder\u004fpen to evade checks.
_UNICODE_ESCAPE = re.compile(r"\\u[0-9a-fA-F]{4}")
_FONT_EXTENSIONS = {".eot", ".svg", ".ttf", ".otf", ".woff", ".woff2"}
_FONT_MAGICS = {
    ".woff": (b"wOFF",),
    ".woff2": (b"wOF2",),
    ".ttf": (b"\x00\x01\x00\x00", b"OTTO", b"true", b"typ1"),
    ".otf": (b"OTTO",),
}


def check_source(root: Path) -> tuple[str, ...]:
    """Return bounded path-specific findings without importing dependencies."""
    root = root.resolve()
    violations: list[str] = []
    configs: set[Path] = set()
    for candidate in root.rglob("*"):
        relative = candidate.relative_to(root)
        if ".git" in relative.parts:
            continue
        if candidate.name.casefold().endswith(".code-workspace"):
            configs.add(candidate)
        elif candidate.name.casefold() == ".vscode":
            if candidate.is_symlink():
                violations.append(f"{relative}: symlinked editor config")
            elif candidate.is_dir():
                configs.update(
                    item for item in candidate.rglob("*")
                    if item.name.casefold().endswith(".json")
                )
            else:
                violations.append(f"{relative}: unexpected editor config type")

    for path in sorted(configs):
        relative = path.relative_to(root)
        if path.is_symlink() or not path.is_file():
            violations.append(f"{relative}: unexpected editor config type")
            continue
        with path.open("rb") as source:
            raw = source.read(131073)
        if len(raw) > 131072:
            violations.append(f"{relative}: oversized editor config")
            continue
        content = raw.decode("utf-8", errors="replace")
        if _UNICODE_ESCAPE.search(content):
            violations.append(f"{relative}: escaped editor configuration")
        if _AUTORUN.search(content):
            violations.append(f"{relative}: editor folderOpen task")
        if _ALLOW_AUTO.search(content):
            violations.append(f"{relative}: automatic editor tasks enabled")
        if _FONT_COMMAND.search(content):
            violations.append(f"{relative}: command executes a font-directory file")

    font_root = root / "public" / "fonts"
    if font_root.is_symlink():
        violations.append("public/fonts: symlinked font directory")
    elif font_root.exists() and not font_root.is_dir():
        violations.append("public/fonts: unexpected font directory type")
    elif font_root.is_dir():
        for path in sorted(font_root.rglob("*")):
            if path.is_dir() and not path.is_symlink():
                continue
            relative = path.relative_to(root)
            if path.is_symlink() or not path.is_file():
                violations.append(f"{relative}: unexpected font file type")
                continue
            if path.name == "README.md":
                continue
            extension = path.suffix.casefold()
            if extension not in _FONT_EXTENSIONS:
                violations.append(f"{relative}: non-font file in font directory")
                continue
            with path.open("rb") as source:
                signature = source.read(512)
            if extension in _FONT_MAGICS and not signature.startswith(
                _FONT_MAGICS[extension]
            ):
                violations.append(f"{relative}: invalid font header")
            elif re.search(rb"(?i)\b(?:require|import|process|child_process)\s*\(", signature):
                violations.append(f"{relative}: apparent script in font asset")

    return tuple(violations)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    findings = check_source(args.root)
    for finding in findings:
        print(f"SOURCE-SAFETY BLOCK: {finding}")
    if findings:
        return 1
    print("SOURCE-SAFETY PASS: no editor autorun or disguised font executable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
