# Working agreements for Claude Code in this repository

Governed AI reference platform. Owner: Thierry Sayegh-Sauvage. Public repository: code under Apache-2.0, everything else under CC BY 4.0 (`LICENSING.md`, ADR 0004). Never present drafts as approved policy or legal advice.

## Source of truth
- `registry/*.yaml` and `policies/*.rego`. Governance documents in `docs/governance/` define intent; policies enforce it.
- Nothing is approved outside the registry. An entry's `status` is never changed to `approved` unless the author explicitly asks.

## Commands
- `make setup`, `make validate`, `make test`, `make check`. `make check` must pass before every commit.

## Rules
- Vendor neutral: no product-specific configuration in `policies/` or `registry/` schemas; product choices go through an ADR.
- Every policy rule has a positive and a negative Rego test; every registry validation rule has a negative test.
- Never invent a figure, threshold, legal citation or vendor claim. Unknowns go to `docs/open-questions.md`.
- Bilingual: every Markdown document exists in English (`name.md`) and French (`name_FR.md`), written in parallel, never machine-pasted; registry entries carry `name_en` and `name_fr`; evaluation cases carry both languages. `make validate` enforces parity and identical structure (same heading levels, same table shapes, same code blocks) between the two versions (`CLAUDE.md` is exempt). Follow the French and English register rules (no em dash, British spelling in English).
- Licensing: every `.py` and `.rego` file carries the SPDX header `Apache-2.0` (enforced by `make validate`); everything else is CC BY 4.0. Names and marks are not licensed. Never paste third-party text (standards, regulations, vendor documents) into the repository without checking licence compatibility.
- Synthetic data only. No secrets, keys, client data or personal data in the repository.
- No network access in tools or tests; dependencies pinned in `requirements.txt`.
- French text: no em dashes; keep the word "token"; never "au conseil" for a management body (use COMEX or CODIR).
- Significant decisions get an ADR (`docs/adr/template.md`).

## Git
- Branch per topic; commit prefixes `policy:`, `registry:`, `docs:`, `tools:`, `infra:`, `eval:`.
- Update `CHANGELOG.md` and `VERSION` (semantic versioning).
