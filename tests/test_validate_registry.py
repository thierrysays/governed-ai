# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Thierry Sayegh-Sauvage
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

import validate_registry as v  # noqa: E402

OK_MODEL = {"id": "m", "name_en": "M", "name_fr": "M", "status": "candidate", "owner": "o", "hosting_region": "eu",
            "allowed_data_classes": ["public"]}
OK_TOOL = {"id": "t", "name_en": "T", "name_fr": "T", "status": "candidate", "owner": "o", "irreversible": False}
OK_SYSTEM = {"id": "s", "name_en": "S", "name_fr": "S", "status": "candidate", "owner": "o", "risk_class": "limited",
             "human_oversight": "required", "allowed_data_classes": ["public"],
             "models": ["m"], "tools": ["t"]}


def test_repository_registry_is_valid():
    assert v.validate(Path(__file__).resolve().parent.parent) == []


def test_valid_entries_pass():
    assert v.check_models([OK_MODEL]) == []
    assert v.check_tools([OK_TOOL]) == []
    assert v.check_systems([OK_SYSTEM], [OK_MODEL], [OK_TOOL]) == []


def test_duplicate_id_rejected():
    assert any("duplicate" in e for e in v.check_models([OK_MODEL, OK_MODEL]))


def test_invalid_status_rejected():
    assert any("invalid status" in e for e in v.check_models([{**OK_MODEL, "status": "live"}]))


def test_missing_owner_rejected():
    assert any("missing owner" in e for e in v.check_models([{**OK_MODEL, "owner": ""}]))


def test_unknown_data_class_rejected():
    bad = {**OK_MODEL, "allowed_data_classes": ["secret"]}
    assert any("unknown data class" in e for e in v.check_models([bad]))


def test_approved_model_requires_evaluation():
    bad = {**OK_MODEL, "status": "approved"}
    assert any("evaluation_ref" in e for e in v.check_models([bad]))


def test_tool_irreversible_must_be_boolean():
    bad = {**OK_TOOL, "irreversible": "no"}
    assert any("irreversible" in e for e in v.check_tools([bad]))


def test_unacceptable_risk_cannot_be_approved():
    bad = {**OK_SYSTEM, "risk_class": "unacceptable", "status": "approved", "accountable": "x"}
    assert any("unacceptable" in e for e in v.check_systems([bad], [OK_MODEL], [OK_TOOL]))


def test_high_risk_requires_human_oversight():
    bad = {**OK_SYSTEM, "risk_class": "high", "human_oversight": "sampling"}
    assert any("high risk" in e for e in v.check_systems([bad], [OK_MODEL], [OK_TOOL]))


def test_approved_system_requires_accountable():
    bad = {**OK_SYSTEM, "status": "approved", "accountable": "to-be-assigned"}
    assert any("accountable" in e for e in v.check_systems([bad], [OK_MODEL], [OK_TOOL]))


def test_unknown_references_rejected():
    bad = {**OK_SYSTEM, "models": ["ghost"], "tools": ["ghost"]}
    errors = v.check_systems([bad], [OK_MODEL], [OK_TOOL])
    assert any("unknown model" in e for e in errors)
    assert any("unknown tool" in e for e in errors)


def test_system_data_classes_required_and_known():
    assert any("allowed_data_classes" in e for e in v.check_systems(
        [{**OK_SYSTEM, "allowed_data_classes": []}], [OK_MODEL], [OK_TOOL]))
    assert any("unknown data class" in e for e in v.check_systems(
        [{**OK_SYSTEM, "allowed_data_classes": ["secret"]}], [OK_MODEL], [OK_TOOL]))


def test_approved_system_requires_a_model():
    bad = {**OK_SYSTEM, "status": "approved", "accountable": "x", "models": []}
    assert any("without any model" in e for e in v.check_systems([bad], [OK_MODEL], [OK_TOOL]))


OK_CASE = {"id": "c", "category": "data_leakage", "system": "s", "synthetic": True,
           "prompt": "p", "prompt_fr": "p", "expected_behaviour": "refuse",
           "expected_behaviour_fr": "refuser"}


def test_valid_eval_case_passes():
    assert v.check_evals([OK_CASE], [OK_SYSTEM]) == []


def test_eval_case_invalid_category_rejected():
    assert any("invalid category" in e for e in v.check_evals([{**OK_CASE, "category": "x"}], [OK_SYSTEM]))


def test_eval_case_unknown_system_rejected():
    assert any("unknown system" in e for e in v.check_evals([{**OK_CASE, "system": "ghost"}], [OK_SYSTEM]))


def test_eval_case_must_be_synthetic():
    assert any("synthetic" in e for e in v.check_evals([{**OK_CASE, "synthetic": False}], [OK_SYSTEM]))


def test_eval_case_missing_fields_and_duplicates_rejected():
    errors = v.check_evals([{**OK_CASE, "prompt": ""}, OK_CASE, OK_CASE], [OK_SYSTEM])
    assert any("missing prompt" in e for e in errors)
    assert any("duplicate" in e for e in errors)


def test_missing_bilingual_names_rejected():
    errors = v.check_models([{**OK_MODEL, "name_fr": ""}])
    assert any("missing name_fr" in e for e in errors)
    errors = v.check_tools([{**OK_TOOL, "name_en": None}])
    assert any("missing name_en" in e for e in errors)
    errors = v.check_systems([{**OK_SYSTEM, "name_fr": ""}], [OK_MODEL], [OK_TOOL])
    assert any("missing name_fr" in e for e in errors)


def test_eval_case_requires_french_fields():
    errors = v.check_evals([{**OK_CASE, "prompt_fr": "", "expected_behaviour_fr": ""}], [OK_SYSTEM])
    assert any("missing prompt_fr" in e for e in errors)
    assert any("missing expected_behaviour_fr" in e for e in errors)


def test_bilingual_docs_pass_when_paired(tmp_path):
    (tmp_path / "a.md").write_text("en")
    (tmp_path / "a_FR.md").write_text("fr")
    (tmp_path / "CLAUDE.md").write_text("exempt")
    assert v.check_bilingual_docs(tmp_path) == []


def test_missing_french_document_rejected(tmp_path):
    (tmp_path / "a.md").write_text("en")
    assert any("missing French counterpart" in e for e in v.check_bilingual_docs(tmp_path))


def test_missing_english_document_rejected(tmp_path):
    (tmp_path / "a_FR.md").write_text("fr")
    assert any("missing English counterpart" in e for e in v.check_bilingual_docs(tmp_path))


DOC_EN = "# Title\n\n## Part\n\n| a | b |\n|---|---|\n| 1 | 2 |\n\n```\ncode\n```\n"
DOC_FR = "# Titre\n\n## Partie\n\n| a | b |\n|---|---|\n| 1 | 2 |\n\n```\ncode\n```\n"


def test_structure_ignores_text_and_code_content():
    assert v.check_structure_pair("a.md", DOC_EN, DOC_FR) == []
    assert v.structure("```\n# not a heading\n| x |\n```\n")["heading levels"] == []


def test_structure_detects_missing_heading():
    errors = v.check_structure_pair("a.md", DOC_EN, DOC_FR.replace("## Partie\n\n", ""))
    assert any("heading levels" in e for e in errors)


def test_structure_detects_heading_level_change():
    errors = v.check_structure_pair("a.md", DOC_EN, DOC_FR.replace("## Partie", "### Partie"))
    assert any("heading levels" in e for e in errors)


def test_structure_detects_missing_table():
    no_table = DOC_FR.replace("| a | b |\n|---|---|\n| 1 | 2 |\n\n", "")
    assert any("tables" in e for e in v.check_structure_pair("a.md", DOC_EN, no_table))


def test_structure_detects_table_row_or_column_difference():
    extra_row = DOC_FR.replace("| 1 | 2 |\n", "| 1 | 2 |\n| 3 | 4 |\n")
    extra_col = DOC_FR.replace("| a | b |\n|---|---|\n| 1 | 2 |", "| a | b | c |\n|---|---|---|\n| 1 | 2 | 3 |")
    assert any("tables" in e for e in v.check_structure_pair("a.md", DOC_EN, extra_row))
    assert any("tables" in e for e in v.check_structure_pair("a.md", DOC_EN, extra_col))


def test_structure_detects_missing_code_block():
    no_code = DOC_FR.replace("```\ncode\n```\n", "")
    assert any("code blocks" in e for e in v.check_structure_pair("a.md", DOC_EN, no_code))


def test_structure_mismatch_reported_by_directory_check(tmp_path):
    (tmp_path / "a.md").write_text(DOC_EN)
    (tmp_path / "a_FR.md").write_text(DOC_FR.replace("## Partie\n\n", ""))
    assert any("heading levels" in e for e in v.check_bilingual_docs(tmp_path))


def _licensed_tree(tmp_path):
    for name in v.LICENSE_FILES:
        (tmp_path / name).write_text("text")
    (tmp_path / "tools").mkdir()
    (tmp_path / "tools" / "a.py").write_text("# SPDX-License-Identifier: Apache-2.0\nprint(1)\n")
    (tmp_path / "policies").mkdir()
    (tmp_path / "policies" / "a.rego").write_text("# SPDX-License-Identifier: Apache-2.0\npackage a\n")


def test_licensed_tree_passes(tmp_path):
    _licensed_tree(tmp_path)
    assert v.check_licensing(tmp_path) == []


def test_missing_licence_file_rejected(tmp_path):
    _licensed_tree(tmp_path)
    (tmp_path / "LICENSE-docs.txt").unlink()
    assert any("missing LICENSE-docs.txt" in e for e in v.check_licensing(tmp_path))


def test_code_file_without_spdx_header_rejected(tmp_path):
    _licensed_tree(tmp_path)
    (tmp_path / "tools" / "b.py").write_text("print(2)\n")
    (tmp_path / "policies" / "b.rego").write_text("package b\n")
    errors = v.check_licensing(tmp_path)
    assert any("tools/b.py" in e for e in errors)
    assert any("policies/b.rego" in e for e in errors)


def test_github_templates_are_exempt_from_parity(tmp_path):
    (tmp_path / ".github").mkdir()
    (tmp_path / ".github" / "pull_request_template.md").write_text("one file")
    assert v.check_bilingual_docs(tmp_path) == []
