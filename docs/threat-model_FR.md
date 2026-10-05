# Modèle de menaces

Méthode : décomposition par couche, menaces nommées d'après l'OWASP Top 10 for LLM Applications (édition 2025). À compléter par MITRE ATLAS pour les techniques adverses. Les niveaux de risque ne sont pas chiffrés ici : ils dépendent du cas d'usage.

| Menace | Couche | Contrôle prévu | Où |
|---|---|---|---|
| LLM01 Injection de prompt | Gateway, agents | Filtrage d'entrée, séparation instructions et données, outils à privilèges minimaux | `gateway/`, `policies/actions.rego` |
| LLM02 Divulgation d'informations sensibles | Gateway, modèles | Routage par classe de données, filtrage de sortie | `policies/routing.rego` |
| LLM03 Chaîne d'approvisionnement | Modèles, outils, MCP | Admission au registre, statut `approved` obligatoire | `registry/` |
| LLM04 Empoisonnement des données et du modèle | Données, évaluation | Provenance des corpus, évaluations de régression | `evals/` |
| LLM05 Traitement inadéquat des sorties | Applications | Validation des sorties avant action | `gateway/` |
| LLM06 Autonomie excessive | Agents | Validation humaine des actions irréversibles, budget d'actions | `policies/actions.rego` |
| LLM07 Fuite du prompt système | Gateway | Aucun secret dans les prompts, revue des prompts | `gateway/` |
| LLM08 Faiblesses des vecteurs et embeddings | Données, RAG | Contrôle d'accès hérité des sources, étiquettes de sensibilité | `registry/`, catalogue |
| LLM09 Désinformation | Évaluation | Jeux d'évaluation, supervision humaine selon la classe de risque | `evals/` |
| LLM10 Consommation non bornée | Gateway, exploitation | Quotas, limites de débit, budgets de tokens | `gateway/` |
| Contournement du gateway | Réseau | Politique réseau interdisant tout accès direct aux modèles | `infra/` |
| Usurpation d'identité d'un agent | Identité | Identités de charge de travail, jetons à portée limitée | `identity/` |

Références : OWASP, Top 10 for LLM Applications 2025 ; MITRE ATLAS ; ISO/IEC 27001:2022.
