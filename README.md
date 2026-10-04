# governed-ai

Reference implementation of a governed AI platform: a vendor-neutral control plane (identity, gateway, routing, tools, evaluation, audit) driven by policies as code and a versioned registry. Private repository, synthetic data only (see `NOTICE.md`).

Reference implementation of a governed AI platform: vendor-neutral, policies as code, versioned registry, continuous evaluation. Private, synthetic data only.

## Principe

La gouvernance normative (politique, classification des risques, responsabilités) est définie dans `docs/governance/`. Elle est appliquée à l'exécution par des politiques versionnées (`policies/`, Rego) qui s'appuient sur un registre (`registry/`, YAML). Rien n'est approuvé hors de ce registre. Le choix des fournisseurs reste ouvert (`docs/adr/0002`).

| Répertoire | Rôle |
|---|---|
| `docs/governance/` | Politique IA, registre des systèmes, RACI, correspondance ISO/IEC 42001, NIST AI RMF, EU AI Act |
| `docs/adr/` | Décisions d'architecture |
| `docs/threat-model.md` | Modèle de menaces (OWASP LLM Top 10) |
| `policies/` | Politiques OPA/Rego et leurs tests |
| `registry/` | Modèles approuvés, outils et serveurs MCP, systèmes (YAML) |
| `gateway/` | Contrat d'exigences du point d'entrée, indépendant du produit |
| `identity/` | Identités de charge de travail et périmètres |
| `evals/` | Jeux d'évaluation et seuils d'arrêt |
| `observability/` | Traçage et journal d'audit |
| `infra/` | Infrastructure as code et isolation réseau |
| `tools/`, `tests/` | Validation du registre et tests |

## Commandes

`make setup`, `make validate`, `make test`, `make check` (ce que la CI exécute). `make test` exige le binaire `opa` dans le PATH.
