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
