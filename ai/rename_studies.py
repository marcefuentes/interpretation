#!/usr/bin/env python3
"""Apply study renames from naming.csv across results, figures, cesga, graph, interpretation."""

from __future__ import annotations

import re
from pathlib import Path

HOME = Path.home()
RESULTS = HOME / "results"
FIGURES = HOME / "figures"
CESGA = Path("/home/marcelino/code/cesga/python")
GRAPH = Path("/home/marcelino/code/graph")
INTERP = Path("/home/marcelino/code/interpretation")

# Unambiguous renames (longest first). Excludes bare "diagonal" and "mutualism".
UNAMBIGUOUS: list[tuple[str, str]] = [
    ("mutualism_infocost_1run", "asymmetric_cost0_cost1_1run"),
    ("mutualism_infocost", "asymmetric_cost0_cost1"),
    ("mutualism_cost_1run", "asymmetric_c1_cost_1run"),
    ("mutualism_cost", "asymmetric_c1_cost"),
    ("mutualism_1run", "asymmetric_c0_c1_1run"),
    ("diagonal_infocost_1run", "symmetric_cost_1run"),
    ("diagonal_infocost", "symmetric_cost"),
    ("symmetric_cost_1run", "symmetric_c_cost_1run"),
    ("symmetric_cost", "symmetric_c_cost"),
    ("diagonal_1run", "symmetric_c_1run"),
]

STUDY_RENAMES: list[tuple[str, str]] = [
    ("diagonal", "symmetric_c"),
    ("mutualism", "asymmetric_c0_c1"),
]

COLLIDING = {
    "symmetric_cost": "symmetric_c_cost",
    "symmetric_cost_1run": "symmetric_c_cost_1run",
    "diagonal_infocost": "symmetric_cost",
    "diagonal_infocost_1run": "symmetric_cost_1run",
}

TEMP_PREFIX = "__renaming__"

TEXT_EXTENSIONS = {
    ".py",
    ".md",
    ".toml",
    ".yaml",
    ".yml",
    ".json",
    ".txt",
    ".csv",
    ".ini",
    ".cfg",
    ".sh",
}

# Regex patterns for bare study names (avoid off-diagonal, DIAGONAL_*, etc.).
STUDY_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"graphgen\.studies\.(?P<old>diagonal|mutualism)\b"), r"graphgen.studies.\g<new>"),
    (re.compile(r"studies\.(?P<old>diagonal|mutualism)\b"), r"studies.\g<new>"),
    (re.compile(r"studies/(?P<old>diagonal|mutualism)\b"), r"studies/\g<new>"),
    (re.compile(r'load_study\("(diagonal|mutualism)"\)'), r'load_study("\2")'),  # fixed below
    (re.compile(r'study="(diagonal|mutualism)"'), r'study="\2"'),
    (re.compile(r"name=\"(diagonal|mutualism)\""), r'name="\2"'),
    (re.compile(r"results_name=\"(diagonal|mutualism)\""), r'results_name="\2"'),
    (re.compile(r"results_folder\"\] = \"(diagonal|mutualism)\""), r'results_folder"] = "\2"'),
    (re.compile(r"results_folder = \"(diagonal|mutualism)\""), r'results_folder = "\2"'),
    (re.compile(r'build_trps_config\("(diagonal|mutualism)"\)'), r'build_trps_config("\2")'),
    (re.compile(r"~/results/(diagonal|mutualism)\b"), r"~/results/\2"),
    (re.compile(r"~/figures/(diagonal|mutualism)\b"), r"~/figures/\2"),
    (re.compile(r"\|\s`(diagonal|mutualism)`\s*\|"), r"| `\2` |"),
    (re.compile(r"\[(diagonal|mutualism)\.md\]"), r"[\2.md]"),
    (re.compile(r"\*\*(diagonal|mutualism)\*\*"), r"**\2**"),
    (re.compile(r"`(diagonal|mutualism)`"), r"`\2`"),
    (re.compile(r"the (diagonal|mutualism) study"), r"the \2 study"),
    (re.compile(r"(diagonal|mutualism) pop_"), r"\2 pop_"),
    (re.compile(r"(diagonal|mutualism) gs="), r"\2 gs="),
    (re.compile(r"from (diagonal|mutualism) import"), r"from \2 import"),
    (re.compile(r"import (diagonal|mutualism)\b"), r"import \2"),
    (re.compile(r"/results/(diagonal|mutualism)/"), r"/results/\2/"),
    (re.compile(r"assert config\.name == \"(diagonal|mutualism)\""), r'assert config.name == "\2"'),
    (re.compile(r"assert \(config\.results_name or config\.name\) == \"(diagonal|mutualism)\""),
     r'assert (config.results_name or config.name) == "\2"'),
    (re.compile(r'"(diagonal|mutualism)"(?=\s*,|\s*\)|\s*$|\s*\|)'), r'"\2"'),
]

NAME_MAP = dict(STUDY_RENAMES)


def _subst_study(match: re.Match[str]) -> str:
    text = match.group(0)
    for old, new in STUDY_RENAMES:
        text = text.replace(old, new)
    return text


def apply_study_patterns(text: str) -> str:
    for pattern, _ in STUDY_PATTERNS:
        text = pattern.sub(_subst_study, text)
    return text


def rename_dir(parent: Path, old: str, new: str) -> None:
    src = parent / old
    dst = parent / new
    if not src.exists():
        return
    if dst.exists():
        raise FileExistsError(f"Cannot rename {src} -> {dst}: destination exists")
    src.rename(dst)
    print(f"  {src} -> {dst}")


def rename_data_dirs(parent: Path) -> None:
    if not parent.is_dir():
        return
    for old, new in COLLIDING.items():
        rename_dir(parent, old, f"{TEMP_PREFIX}{new}")
    for old, new in UNAMBIGUOUS + STUDY_RENAMES:
        if old in COLLIDING:
            continue
        rename_dir(parent, old, new)
    for old, new in COLLIDING.items():
        rename_dir(parent, f"{TEMP_PREFIX}{new}", new)


def rename_study_dirs(parent: Path) -> None:
    studies = parent / "studies" if (parent / "studies").is_dir() else parent
    if not studies.is_dir():
        return
    for old, new in COLLIDING.items():
        rename_dir(studies, old, f"{TEMP_PREFIX}{new}")
    for old, new in UNAMBIGUOUS + STUDY_RENAMES:
        if old in COLLIDING:
            continue
        rename_dir(studies, old, new)
    for old, new in COLLIDING.items():
        rename_dir(studies, f"{TEMP_PREFIX}{new}", new)


def rename_test_files(tests_dir: Path) -> None:
    if not tests_dir.is_dir():
        return
    pairs = [
        ("test_studies_symmetric_cost_1run.py", "test_studies_symmetric_c_cost_1run.py"),
        ("test_studies_symmetric_cost.py", "test_studies_symmetric_c_cost.py"),
        ("test_studies_diagonal_infocost.py", "test_studies_symmetric_cost.py"),
        ("test_studies_diagonal.py", "test_studies_symmetric_c.py"),
        ("test_studies_mutualism_cost_1run.py", "test_studies_asymmetric_c1_cost_1run.py"),
        ("test_studies_mutualism_cost.py", "test_studies_asymmetric_c1_cost.py"),
    ]
    for old, new in pairs:
        rename_dir(tests_dir, old, new)


def rename_journal_files(journal_dir: Path) -> None:
    pairs = [
        ("symmetric_cost.md", "symmetric_c_cost.md"),
        ("mutualism_cost.md", "asymmetric_c1_cost.md"),
        ("mutualism_combined.md", "asymmetric_c0_c1_combined.md"),
        ("mutualism_partner_choice.md", "asymmetric_c0_c1_partner_choice.md"),
        ("mutualism_reciprocity.md", "asymmetric_c0_c1_reciprocity.md"),
        ("mutualism.md", "asymmetric_c0_c1.md"),
        ("diagonal_combined.md", "symmetric_c_combined.md"),
        ("diagonal_partner_choice.md", "symmetric_c_partner_choice.md"),
        ("diagonal_reciprocity.md", "symmetric_c_reciprocity.md"),
        ("diagonal.md", "symmetric_c.md"),
    ]
    for old, new in pairs:
        rename_dir(journal_dir, old, new)


def rename_ai_scripts(ai_dir: Path) -> None:
    pairs = [
        ("analyze_symmetric_cost.py", "analyze_symmetric_c_cost.py"),
        ("analyze_mutualism_cost.py", "analyze_asymmetric_c1_cost.py"),
    ]
    for old, new in pairs:
        rename_dir(ai_dir, old, new)


def iter_text_files(root: Path) -> list[Path]:
    skip_dirs = {".git", ".venv", "__pycache__", ".ruff_cache", ".pytest_cache", "node_modules"}
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in skip_dirs for part in path.parts):
            continue
        if path.suffix in TEXT_EXTENSIONS or path.name in {".gitignore", "AGENTS.md"}:
            files.append(path)
    return files


def transform_text(text: str) -> str:
    for old, new in UNAMBIGUOUS:
        text = text.replace(old, new)
    text = apply_study_patterns(text)
    return text


def apply_text_replacements(root: Path) -> int:
    changed = 0
    for path in iter_text_files(root):
        if path.name == "rename_studies.py":
            continue
        original = path.read_text(encoding="utf-8")
        updated = transform_text(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            print(f"  updated {path}")
    return changed


def main() -> None:
    print("=== Renaming ~/results ===")
    rename_data_dirs(RESULTS)
    print("=== Renaming ~/figures ===")
    rename_data_dirs(FIGURES)

    print("=== Renaming cesga study folders ===")
    rename_study_dirs(CESGA)

    print("=== Renaming graph study folders ===")
    rename_study_dirs(GRAPH / "graphgen")
    rename_test_files(GRAPH / "tests")

    print("=== Renaming interpretation journal + scripts ===")
    rename_journal_files(INTERP / "journal")
    rename_ai_scripts(INTERP / "ai")

    print("=== Text replacements in cesga ===")
    apply_text_replacements(CESGA)

    print("=== Text replacements in graph ===")
    apply_text_replacements(GRAPH)

    print("=== Text replacements in interpretation ===")
    apply_text_replacements(INTERP)

    print("Done.")


if __name__ == "__main__":
    main()
