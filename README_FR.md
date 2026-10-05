# governed-ai

Mise en œuvre de référence d'une plateforme d'IA gouvernée : un plan de contrôle sans dépendance à un fournisseur (identité, gateway, routage, outils, évaluation, audit), piloté par des politiques en code et un registre versionné. Dépôt privé, données synthétiques uniquement (voir `NOTICE_FR.md`). English version: `README.md`.

## Principe

La gouvernance normative (politique, classification des risques, responsabilités) est définie dans `docs/governance/`. Elle est appliquée à l'exécution par des politiques versionnées (`policies/`, Rego) qui s'appuient sur un registre (`registry/`, YAML). Rien n'est approuvé hors de ce registre. Le choix des fournisseurs reste ouvert (`docs/adr/0002`).

## Règle de bilinguisme

Chaque document existe en anglais (`nom.md`) et en français (`nom_FR.md`). `make validate` échoue si l'un des deux manque. Les entrées du registre portent `name_en` et `name_fr` ; les cas d'évaluation portent les deux langues.

| Répertoire | Rôle |
|---|---|
| `docs/governance/` | Politique IA, registre des systèmes, RACI, correspondance ISO/IEC 42001, NIST AI RMF, EU AI Act |
| `docs/adr/` | Décisions d'architecture |
| `docs/threat-model_FR.md` | Modèle de menaces (OWASP LLM Top 10) |
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
