# 0004. Licensing of the public repository

- Status: proposed
- Date: 2026-10-05
- Deciders: Thierry Sayegh-Sauvage

## Context

The repository is public, although it was first created and documented as private. It contains code (policies, validator, tests), governance drafts, a registry schema and synthetic data. No licence file exists. Without a licence, copyright remains with the owner and nobody may reuse the content beyond what the hosting platform's terms of service allow (viewing and forking). On 2026-10-05 the owner decided to keep the repository public. The owner has not yet decided whether, or under which licence, to open the content.

This ADR records options. It is not legal advice; the choice and its wording should be confirmed with a legal adviser before any licence file is added.

## Decision

Interim position, until the owner decides: keep the content under "all rights reserved", state it in `NOTICE.md`, grant no licence, and mark every draft as such (README Status section). No open-source licence is added by this decision.

## Consequences

Visitors can read the work but cannot lawfully reuse it, which protects the owner's intellectual property and avoids committing to a licence prematurely. The cost is lower reuse and no external contribution path. Drafts remain visible: their status must stay explicit.

## Alternatives considered

- Permissive licence for code (for example Apache-2.0, which includes a patent grant or MIT) and an attribution licence for documents (for example CC BY 4.0): maximises reuse and visibility; irreversible for versions already published; governance documents become reusable by anyone, including competitors.
- Copyleft licence for code (for example AGPL-3.0): keeps derivative work open; deters some corporate adopters.
- Make the repository private again: removes the exposure of drafts; loses visibility and external review. Rejected by the owner on 2026-10-05.
