# 0003. Classify the internal assistant as limited risk, with conditions

- Status: proposed
- Date: 2026-10-04
- Deciders: Thierry Sayegh-Sauvage

## Context

First use case of the platform: an internal assistant for drafting, summarising and searching internal documents. The risk class drives the obligations and controls (`registry/systems.yaml`, `docs/governance/system-register.md`). Classification depends on the real purpose, not on the technology.

## Decision

Classify `internal-assistant` as `limited`, under three verifiable conditions:

1. Bounded purpose: drafting, summarising, document search. No evaluation, selection, scoring, monitoring or decision concerning people (recruitment, career management, performance evaluation, access to benefits).
2. Data capped at `public` and `internal` in the routing policy.
3. No tool with irreversible effects registered for this system.

These conditions are **reclassification triggers**: if any ceases to hold, the system is reclassified (probably `high`) and suspended until reassessed. Cases `ia-scope-001` and `ia-scope-002` test the first condition.

The exact citation of the applicable provisions (high-risk areas, transparency obligation) must be taken from the official text of Regulation (EU) 2024/1689 by the author before approval. It is not reproduced here.

## Consequences

Controls stay proportionate (sampled oversight, no systematic human validation). In return, governance depends on discipline over purpose: usage drift must be watched, which the out-of-scope evaluation cases and sampled review are meant to detect.

## Alternatives considered

- Classify as `high` out of caution: safer legally, but removes the point of a simple first case and imposes disproportionate controls.
- Do not classify before the model is chosen: classification depends on purpose, not on the model; waiting would hide the drift risk.
