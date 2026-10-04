import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

import validate_registry as v  # noqa: E402

OK_MODEL = {"id": "m", "status": "candidate", "owner": "o", "hosting_region": "eu",
            "allowed_data_classes": ["public"]}
OK_TOOL = {"id": "t", "status": "candidate", "owner": "o", "irreversible": False}
OK_SYSTEM = {"id": "s", "status": "candidate", "owner": "o", "risk_class": "limited",
             "human_oversight": "required", "models": ["m"], "tools": ["t"]}


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
