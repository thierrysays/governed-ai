# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Thierry Sayegh-Sauvage
"""Check that commits carry a Signed-off-by line matching the author's email (DCO 1.1).

Usage: check_dco.py <git-range>   e.g. origin/main..HEAD
Merge commits are skipped. Authors listed in .github/dco-exempt.txt are exempt.
No network access.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

SIGNOFF = re.compile(r"^Signed-off-by: .+ <([^<>\s]+@[^<>\s]+)>\s*$", re.MULTILINE)


def check_commits(commits: list[dict], exempt: set[str]) -> list[str]:
    """Each commit is {'sha', 'author_email', 'message'}. Returns error strings."""
    errors = []
    for c in commits:
        email = c["author_email"].strip().lower()
        if email in exempt:
            continue
        signed = {e.lower() for e in SIGNOFF.findall(c["message"])}
        short = c["sha"][:7]
        if not signed:
            errors.append(f"commit {short}: missing 'Signed-off-by: Name <email>' line")
        elif email not in signed:
            errors.append(f"commit {short}: sign-off email does not match author {email}")
    return errors


def load_exempt(root: Path) -> set[str]:
    path = root / ".github" / "dco-exempt.txt"
    if not path.is_file():
        return set()
    return {
        line.strip().lower()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }


def read_commits(git_range: str) -> list[dict]:
    out = subprocess.run(
        ["git", "log", "--no-merges", "--format=%H%x1f%ae%x1f%B%x1e", git_range],
        check=True, capture_output=True, text=True,
    ).stdout
    commits = []
    for record in out.split("\x1e"):
        if record.strip():
            sha, email, message = record.strip("\n").split("\x1f", 2)
            commits.append({"sha": sha, "author_email": email, "message": message})
    return commits


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: check_dco.py <git-range>")
        return 2
    root = Path(__file__).resolve().parent.parent
    errors = check_commits(read_commits(argv[1]), load_exempt(root))
    for e in errors:
        print(f"ERROR {e}")
    print(f"dco: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
