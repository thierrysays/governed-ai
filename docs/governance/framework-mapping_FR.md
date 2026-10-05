# Correspondance avec les référentiels

Statut : cartographie de travail. Les numéros de clauses et d'articles doivent être vérifiés par l'auteur dans les textes officiels avant tout usage externe. Aucune citation juridique n'est reproduite ici.

| Capacité de la plateforme | ISO/IEC 42001 (système de management de l'IA) | NIST AI RMF 1.0 | EU AI Act (Règlement 2024/1689) | Contrôle dans ce dépôt |
|---|---|---|---|---|
| Politique, rôles, appétence au risque | Leadership, politique, rôles | GOVERN | Obligations des fournisseurs et déployeurs | `docs/governance/ai-policy_FR.md`, `raci_FR.md` |
| Inventaire et classification des systèmes | Planification, évaluation des risques | MAP | Classification par niveau de risque | `registry/systems.yaml`, `system-register_FR.md` |
| Admission des modèles et outils | Contrôles sur les ressources et les tiers | MAP, MANAGE | Obligations liées aux modèles à usage général, chaîne de valeur | `registry/models.yaml`, `registry/tools.yaml`, `policies/routing.rego` |
| Supervision humaine, actions irréversibles | Contrôles opérationnels | MANAGE | Supervision humaine des systèmes à risque élevé | `policies/actions.rego` |
| Évaluation et tests | Évaluation des performances | MEASURE | Exactitude, robustesse, cybersécurité | `evals/` |
| Journalisation et traçabilité | Informations documentées, surveillance | MEASURE, MANAGE | Tenue de journaux | `observability/` |
| Incidents et amélioration continue | Amélioration | MANAGE | Surveillance après commercialisation, signalement | `docs/governance/ai-policy_FR.md` §4 |

Références : ISO/IEC 42001:2023 ; NIST, Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1, 2023 ; Règlement (UE) 2024/1689 ; COBIT 2019.
