# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Thierry Sayegh-Sauvage
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

import check_dco as d  # noqa: E402


def commit(email="a@example.org", message="docs: x\n\nSigned-off-by: A <a@example.org>\n"):
    return {"sha": "0123456789abcdef", "author_email": email, "message": message}


def test_signed_commit_passes():
    assert d.check_commits([commit()], set()) == []


def test_missing_signoff_rejected():
    errors = d.check_commits([commit(message="docs: x\n")], set())
    assert any("missing" in e for e in errors)


def test_signoff_with_other_email_rejected():
    errors = d.check_commits([commit(message="docs: x\n\nSigned-off-by: B <b@example.org>\n")], set())
    assert any("does not match" in e for e in errors)


def test_malformed_signoff_rejected():
    for bad in ("Signed-off-by: A\n", "Signed-off-by: <a@example.org>\n", "signed off: A <a@example.org>\n"):
        assert d.check_commits([commit(message="docs: x\n\n" + bad)], set())


def test_email_comparison_ignores_case():
    c = commit(email="A@Example.org", message="docs: x\n\nSigned-off-by: A <a@example.org>\n")
    assert d.check_commits([c], set()) == []


def test_exempt_author_passes_without_signoff():
    assert d.check_commits([commit(message="docs: x\n")], {"a@example.org"}) == []


def test_every_commit_is_checked():
    errors = d.check_commits([commit(), commit(message="docs: y\n")], set())
    assert len(errors) == 1


def test_exempt_list_loaded_and_comments_ignored(tmp_path):
    (tmp_path / ".github").mkdir()
    (tmp_path / ".github" / "dco-exempt.txt").write_text("# owner\nOwner@Example.org\n\n")
    assert d.load_exempt(tmp_path) == {"owner@example.org"}
    assert d.load_exempt(tmp_path / "missing") == set()
