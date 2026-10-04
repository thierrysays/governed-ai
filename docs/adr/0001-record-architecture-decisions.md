# 0001. Record architecture decisions

- Status: accepted
- Date: 2026-10-04
- Deciders: Thierry Sayegh-Sauvage

## Context

The platform combines normative, architectural and vendor choices that will be questioned by auditors and successors. Decisions must stay traceable.

## Decision

Every significant decision is recorded as an ADR in `docs/adr/` using `template.md`, numbered sequentially, never rewritten: a change of mind creates a new ADR that supersedes the old one.

## Consequences

Slight overhead per decision; durable audit trail, aligned with ISO/IEC 42001 documented information requirements.

## Alternatives considered

Decisions in tickets or chat: not durable, not versioned with the code.
