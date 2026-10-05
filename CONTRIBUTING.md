# Contributing

French version: `CONTRIBUTING_FR.md`.

## Before you start

This is a reference implementation maintained by one owner. Contributions are welcome and reviewed at the owner's discretion, with no commitment on response time. Open an issue before starting anything larger than a fix, so the direction can be agreed first. Many documents are still drafts (see the Status section of `README.md`). By taking part you agree to follow the Code of Conduct (`CODE_OF_CONDUCT.md`). Report security issues privately, as described in `SECURITY.md`, never in a public issue.

## What is welcome

- Corrections of errors or unclear passages in documents, in either language.
- Reports of differences in meaning between an English document and its French twin.
- Additional tests, especially negative tests, and new synthetic evaluation cases.
- Improvements to policies and to the registry validator, with tests.
- Vendor-neutral integrations, discussed first through an ADR.

## What is not accepted

- Real data of any kind: client data, personal data, credentials, corpus excerpts.
- Third-party text copied in (standards, regulations, vendor documentation). Cite and link instead.
- Legal citations that do not point to the official text.
- Any change that sets a model, tool or system to `approved`: that status is the owner's decision.
- Product-specific configuration in `policies/` or in the registry schemas (ADR 0002).
- Machine-generated content that the contributor has not reviewed and cannot stand behind.

## Licence and sign-off

Contributions are licensed under the project's licences: Apache-2.0 for code and CC BY 4.0 for documents and data (see `LICENSING.md`).

Every commit must carry a sign-off line, `Signed-off-by: Your Name <you@example.com>`, whose email matches the commit author. `git commit -s` adds it. The sign-off certifies the Developer Certificate of Origin 1.1 (https://developercertificate.org/). The certification is personal: never sign off on someone else's behalf. CI checks the sign-off on pull requests; commits authored by the owner are exempt (`.github/dco-exempt.txt`).

## Languages

Every document exists in English (`name.md`) and in French (`name_FR.md`) with the same structure, and `make validate` enforces it. If you write in one language, provide the other, or say in the pull request that you could not and why. Registry entries need `name_en` and `name_fr`; evaluation cases need both languages. Keep to the register rules: no em dash, British spelling in English, and the French rules in `CLAUDE.md`.

## Workflow

1. Fork the repository and create a branch per topic from `main`.
2. Prefix commit messages with `policy:`, `registry:`, `docs:`, `tools:`, `infra:` or `eval:`, and sign them off.
3. For any change to behaviour or content, update `CHANGELOG.md`, `CHANGELOG_FR.md` and `VERSION` (semantic versioning).
4. Run `make setup`, then `make check`. It must pass before you open the pull request.
5. Open a pull request to `main`: say what changes, why, and what you did not verify. CI must be green.

## Quality checks

Every policy rule has a positive and a negative Rego test, and every validation rule has a negative test. Tools and tests make no network access. Dependencies are pinned in `requirements.txt`. Every `.py` and `.rego` file carries the SPDX header. Data is synthetic.

## Decisions and review

The owner reviews every pull request and may decline it. Significant decisions need an ADR (`docs/adr/template.md`). A contribution gives no commit access and no right over the repository.
