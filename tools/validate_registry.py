# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Thierry Sayegh-Sauvage
"""Validate registry/*.yaml. Exit 1 on any error. No network access."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

STATUS = {"candidate", "approved", "suspended", "retired"}
DATA_CLASSES = {"public", "internal", "confidential", "restricted"}
RISK_CLASSES = {"unacceptable", "high", "limited", "minimal"}
OVERSIGHT = {"required", "sampling", "none"}


def load(path: Path, key: str) -> list[dict]:
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    items = doc.get(key)
    if not isinstance(items, list):
        raise ValueError(f"{path}: top-level key '{key}' must be a list")
    return items


def check_ids(kind: str, items: list[dict]) -> list[str]:
    errors, seen = [], set()
    for item in items:
        ident = item.get("id")
        if not ident:
            errors.append(f"{kind}: entry without id")
            continue
        if ident in seen:
            errors.append(f"{kind}: duplicate id {ident}")
        seen.add(ident)
    return errors


def check_common(kind: str, items: list[dict]) -> list[str]:
    errors = check_ids(kind, items)
    for item in items:
        ident = item.get("id", "?")
        for field in ("name_en", "name_fr"):
            if not item.get(field):
                errors.append(f"{kind} {ident}: missing {field}")
        if item.get("status") not in STATUS:
            errors.append(f"{kind} {ident}: invalid status {item.get('status')!r}")
        if not item.get("owner"):
            errors.append(f"{kind} {ident}: missing owner")
    return errors


def check_models(models: list[dict]) -> list[str]:
    errors = check_common("model", models)
    for m in models:
        ident = m.get("id", "?")
        if not m.get("hosting_region"):
            errors.append(f"model {ident}: missing hosting_region")
        classes = m.get("allowed_data_classes")
        if not isinstance(classes, list) or not classes:
            errors.append(f"model {ident}: allowed_data_classes must be a non-empty list")
        elif not set(classes) <= DATA_CLASSES:
            errors.append(f"model {ident}: unknown data class in {classes}")
        if m.get("status") == "approved" and not m.get("evaluation_ref"):
            errors.append(f"model {ident}: approved without evaluation_ref")
    return errors


def check_tools(tools: list[dict]) -> list[str]:
    errors = check_common("tool", tools)
    for t in tools:
        if not isinstance(t.get("irreversible"), bool):
            errors.append(f"tool {t.get('id', '?')}: irreversible must be true or false")
    return errors


def check_systems(systems: list[dict], models: list[dict], tools: list[dict]) -> list[str]:
    errors = check_common("system", systems)
    model_ids = {m.get("id") for m in models}
    tool_ids = {t.get("id") for t in tools}
    for s in systems:
        ident = s.get("id", "?")
        if s.get("risk_class") not in RISK_CLASSES:
            errors.append(f"system {ident}: invalid risk_class {s.get('risk_class')!r}")
        if s.get("human_oversight") not in OVERSIGHT:
            errors.append(f"system {ident}: invalid human_oversight {s.get('human_oversight')!r}")
        classes = s.get("allowed_data_classes")
        if not isinstance(classes, list) or not classes:
            errors.append(f"system {ident}: allowed_data_classes must be a non-empty list")
        elif not set(classes) <= DATA_CLASSES:
            errors.append(f"system {ident}: unknown data class in {classes}")
        if s.get("risk_class") == "unacceptable" and s.get("status") == "approved":
            errors.append(f"system {ident}: unacceptable risk cannot be approved")
        if s.get("risk_class") == "high" and s.get("human_oversight") != "required":
            errors.append(f"system {ident}: high risk requires human_oversight 'required'")
        if s.get("status") == "approved" and s.get("accountable") in (None, "", "to-be-assigned"):
            errors.append(f"system {ident}: approved without an accountable person")
        if s.get("status") == "approved" and not s.get("models"):
            errors.append(f"system {ident}: approved without any model")
        for ref in s.get("models", []):
            if ref not in model_ids:
                errors.append(f"system {ident}: unknown model {ref}")
        for ref in s.get("tools", []):
            if ref not in tool_ids:
                errors.append(f"system {ident}: unknown tool {ref}")
    return errors


EVAL_CATEGORIES = {"prompt_injection", "data_leakage", "out_of_scope", "grounding", "oversight"}


def check_evals(cases: list[dict], systems: list[dict]) -> list[str]:
    errors = check_ids("eval case", cases)
    system_ids = {s.get("id") for s in systems}
    for c in cases:
        ident = c.get("id", "?")
        if c.get("category") not in EVAL_CATEGORIES:
            errors.append(f"eval case {ident}: invalid category {c.get('category')!r}")
        if c.get("system") not in system_ids:
            errors.append(f"eval case {ident}: unknown system {c.get('system')!r}")
        if c.get("synthetic") is not True:
            errors.append(f"eval case {ident}: must be marked synthetic: true")
        for field in ("prompt", "prompt_fr", "expected_behaviour", "expected_behaviour_fr"):
            if not c.get(field):
                errors.append(f"eval case {ident}: missing {field}")
    return errors


EXEMPT_DOCS = {"CLAUDE.md"}
SKIP_DIRS = {".git", ".github", ".venv", ".pytest_cache", "__pycache__"}  # .github: single-file templates read by GitHub


def structure(text: str) -> dict:
    """Skeleton of a Markdown document: heading levels, table shapes, fenced blocks."""
    headings, tables, fences = [], [], 0
    in_fence, rows = False, []

    def close_table():
        if rows:
            tables.append((len(rows), len(rows[0].strip().strip("|").split("|"))))
            rows.clear()

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            close_table()
            in_fence = not in_fence
            fences += 0 if in_fence else 1
            continue
        if in_fence:
            continue
        if stripped.startswith("|"):
            rows.append(stripped)
            continue
        close_table()
        if line.startswith("#"):
            headings.append(len(line) - len(line.lstrip("#")))
    close_table()
    return {"heading levels": headings, "tables (rows, columns)": tables, "code blocks": fences}


def check_structure_pair(rel: str, english: str, french: str) -> list[str]:
    en, fr = structure(english), structure(french)
    return [
        f"document {rel}: {kind} differ between EN {en[kind]} and FR {fr[kind]}"
        for kind in en
        if en[kind] != fr[kind]
    ]


def check_bilingual_docs(root: Path) -> list[str]:
    """Every English `name.md` needs a French `name_FR.md`, and the reverse."""
    errors = []
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if SKIP_DIRS & set(rel.parts) or rel.name in EXEMPT_DOCS:
            continue
        if path.stem.endswith("_FR"):
            twin = path.with_name(path.stem[: -len("_FR")] + ".md")
            if not twin.exists():
                errors.append(f"document {rel}: missing English counterpart {twin.name}")
        else:
            twin = path.with_name(path.stem + "_FR.md")
            if not twin.exists():
                errors.append(f"document {rel}: missing French counterpart {twin.name}")
            else:
                errors += check_structure_pair(
                    str(rel), path.read_text(encoding="utf-8"), twin.read_text(encoding="utf-8")
                )
    return errors


LICENSE_FILES = ("LICENSE", "LICENSE-docs.txt", "NOTICE")
SPDX = "SPDX-License-Identifier: Apache-2.0"
CODE_GLOBS = ("tools/*.py", "tests/*.py", "policies/*.rego")


def check_licensing(root: Path) -> list[str]:
    """Licence files must exist and every code file must carry the SPDX header."""
    errors = [f"licensing: missing {name}" for name in LICENSE_FILES if not (root / name).is_file()]
    for pattern in CODE_GLOBS:
        for path in sorted(root.glob(pattern)):
            head = "\n".join(path.read_text(encoding="utf-8").splitlines()[:3])
            if SPDX not in head:
                errors.append(f"licensing: {path.relative_to(root)} lacks the header '{SPDX}'")
    return errors


def validate(root: Path) -> list[str]:
    models = load(root / "registry/models.yaml", "models")
    tools = load(root / "registry/tools.yaml", "tools")
    systems = load(root / "registry/systems.yaml", "systems")
    errors = check_models(models) + check_tools(tools) + check_systems(systems, models, tools)
    for path in sorted((root / "evals").glob("*/cases.yaml")):
        errors += check_evals(load(path, "cases"), systems)
    return errors + check_bilingual_docs(root) + check_licensing(root)


def main() -> int:
    errors = validate(Path(__file__).resolve().parent.parent)
    for e in errors:
        print(f"ERROR {e}")
    print(f"registry: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
