# Registre des systèmes : méthode

La source de vérité machine est `registry/systems.yaml`. Ce document porte la justification humaine de chaque classification.

## Fiche par système (à copier)

| Champ | Contenu |
|---|---|
| Identifiant | Identique à `registry/systems.yaml` |
| Finalité | Décision ou tâche soutenue, utilisateurs concernés |
| Classe de risque | `unacceptable`, `high`, `limited` ou `minimal`, avec la justification et la référence au texte applicable (citation exacte à prendre dans le texte officiel) |
| Données traitées | Classes de données, présence de données personnelles, base légale |
| Modèles et outils | Références au registre |
| Supervision humaine | Modalité et point de contrôle |
| Responsable | Personne nommée |
| Évaluation | Référence au jeu d'évaluation et aux critères d'arrêt |
| Conditions de suspension | Déclencheurs et procédure |

## Systèmes enregistrés

| Identifiant | Statut | Classe | Fiche |
|---|---|---|---|
| `internal-assistant` | candidate | limited | `use-cases/internal-assistant.md`, ADR 0003 |

L'entrée `example-internal-assistant` du registre est synthétique.
