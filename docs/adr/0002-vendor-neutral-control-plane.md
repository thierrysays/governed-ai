# 0002. Vendor-neutral control plane

- Status: proposed
- Date: 2026-10-04
- Deciders: Thierry Sayegh-Sauvage

## Context

The reference picture that inspired this project is built around a single vendor's gateway and catalog. Governance must outlive a supplier choice. No cloud, identity provider or gateway product has been selected (`docs/open-questions.md`).

## Decision

Define the platform through open interfaces and keep products replaceable:

- Policies as code in OPA/Rego, versioned and tested in CI.
- Registry of models, tools and systems as YAML in Git, reviewed by pull request.
- Telemetry through OpenTelemetry; lineage through OpenLineage where a catalog exists.
- Tool access through the Model Context Protocol, behind the registry.
- The gateway is specified by a requirements contract (`gateway/README.md`), not by a product configuration.

Product selection is a later ADR, taken once the first use case and target cloud are known.

## Consequences

Easier: replacing a gateway, model provider or cloud; auditing the rules independently of the product. Harder: some native vendor features (integrated catalog, lineage) must be matched by integration work; the gateway is a concentration point whose availability must be designed.

## Alternatives considered

- Single-vendor integrated stack: faster to start, but policies and lineage become non-portable.
- Registry in a dedicated tool: scales better, but moves the source of truth out of Git. Revisit if the registry outgrows YAML.
