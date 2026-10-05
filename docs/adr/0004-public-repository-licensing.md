# 0004. Licensing of the public repository

- Status: accepted
- Date: 2026-10-05
- Deciders: Thierry Sayegh-Sauvage

## Context

The repository is public, although it was first created and documented as private. It contains code (policies, validator, tests), governance drafts, a registry schema and synthetic data. Without a licence, copyright remains with the owner and nobody may reuse the content beyond what the hosting platform's terms of service allow (viewing and forking). On 2026-10-05 the owner decided to keep the repository public and to open it under licences.

This ADR is not legal advice; the wording should be confirmed with a legal adviser (`docs/open-questions.md`, item 7).

## Decision

- Code is licensed under Apache License 2.0 (`LICENSE`). It covers `policies/`, `tools/`, `tests/`, `Makefile`, `.github/` and `requirements.txt`. Every `.py` and `.rego` file carries an SPDX header, checked by `make validate`.
- Documents and data are licensed under Creative Commons Attribution 4.0 International (`LICENSE-docs.txt`). They cover everything else, including `docs/`, the READMEs, the registry and the evaluation data.
- Names and marks (Glossolalie Advisory, ECM™, PLCF™, VEGA™, TDG™, CORE™, LEGATE™) are not licensed.
- A plain `NOTICE` carries the Apache attribution notice; `LICENSING.md` explains the scope in both languages.
- Drafts stay marked as drafts (README Status section): a licence does not make them reviewed.

## Consequences

Easier: reuse and external credibility; the code license matches the OPA ecosystem and includes a patent grant. Harder: the choice cannot be withdrawn for versions already published; the governance documents can be republished by anyone with attribution, so the owner's advantage lies in execution rather than in the text; documents that are still drafts, with unverified legal citations, are now reusable. Contributions need a policy (none yet).

## Alternatives considered

- All rights reserved: protects the content; no reuse and no external credibility. Kept only as the interim position until this decision.
- MIT for code: shorter, but without a patent grant.
- AGPL-3.0 for code: keeps derivative work open; deters the large organisations the project addresses.
- CC BY-NC for documents: the notion of non-commercial use is unclear and discourages reuse without protecting the owner reliably.
- Make the repository private again: rejected by the owner on 2026-10-05.
