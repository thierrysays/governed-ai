# governed-ai

English | [Français](README_FR.md)

Reference implementation of a governed AI platform: a vendor-neutral control plane (identity, gateway, routing, tools, evaluation, audit) driven by policies as code and a versioned registry. Public repository, all rights reserved, synthetic data only (see `NOTICE.md`).

## Status

Work in progress. Documents marked draft or proposed are not approved policy, not legal advice and not an attestation of conformity with ISO/IEC 42001, the NIST AI RMF, the EU AI Act or any other text. Legal citations are deliberately absent until verified against the official texts. No licence is granted (see `NOTICE.md`).

## Principle

Normative governance (policy, risk classification, responsibilities) is defined in `docs/governance/`. It is enforced at runtime by versioned policies (`policies/`, Rego) that rely on a registry (`registry/`, YAML). Nothing is approved outside this registry. The choice of vendors stays open (`docs/adr/0002`).

## Bilingual rule

Every document exists in English (`name.md`) and in French (`name_FR.md`). `make validate` fails when one of the pair is missing, or when the two versions differ in structure (heading levels, table rows and columns, code blocks). Registry entries carry `name_en` and `name_fr`; evaluation cases carry both languages.

| Directory | Role |
|---|---|
| `docs/governance/` | AI policy, system register, RACI, mapping to ISO/IEC 42001, NIST AI RMF, EU AI Act |
| `docs/adr/` | Architecture decisions |
| `docs/threat-model.md` | Threat model (OWASP LLM Top 10) |
| `policies/` | OPA/Rego policies and their tests |
| `registry/` | Approved models, tools and MCP servers, systems (YAML) |
| `gateway/` | Requirements contract for the entry point, product-independent |
| `identity/` | Workload identities and scopes |
| `evals/` | Evaluation sets and stop thresholds |
| `observability/` | Tracing and audit log |
| `infra/` | Infrastructure as code and network isolation |
| `tools/`, `tests/` | Registry validation and tests |

## Commands

`make setup`, `make validate`, `make test`, `make check` (what CI runs). `make test` requires the `opa` binary in the PATH.
