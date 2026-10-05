# Cas d'usage 1 : assistant interne

Statut : instruction en cours. Identifiant registre : `internal-assistant` (statut `candidate`). Décision de classification : ADR 0003.

## Finalité
Assister les collaborateurs dans des tâches de rédaction, de synthèse et de recherche dans la documentation interne. L'assistant ne prend ni ne recommande aucune décision individuelle concernant une personne.

## Fiche

| Champ | Contenu |
|---|---|
| Identifiant | `internal-assistant` |
| Finalité | Rédaction, synthèse, recherche documentaire interne |
| Utilisateurs | Collaborateurs de l'organisation, authentifiés |
| Classe de risque proposée | `limited`, sous les conditions de l'ADR 0003. Citation du texte applicable : à confirmer dans le texte officiel du Règlement (UE) 2024/1689 |
| Données traitées | Plafond proposé : `public` et `internal`. Pas de `confidential` ni `restricted`. Les données personnelles de tiers ne sont pas dans le périmètre |
| Modèles | Aucun choisi (neutralité fournisseur, ADR 0002). Un modèle doit être au registre, approuvé et habilité pour `internal` pour que `policies/routing.rego` laisse passer |
| Outils | Aucun. Lecture de la base documentaire via le gateway uniquement. Aucun outil à effet irréversible |
| Supervision humaine | Par échantillonnage : revue périodique de conversations journalisées, avec information préalable des utilisateurs. Modalités et fréquence à définir |
| Responsable | À désigner (`accountable`). Pas d'approbation sans personne nommée |
| Propriétaire | À désigner |
| Évaluation | `evals/internal-assistant/cases.yaml`, exécution à documenter |
| Suspension | Voir ci-dessous |

## Conditions d'approbation (toutes requises)
1. Un responsable et un propriétaire nommés.
2. Au moins un modèle approuvé au registre, avec évaluation de référence et habilitation pour la classe `internal`.
3. Exécution documentée des cas d'évaluation, avec des seuils fixés par le responsable du risque.
4. Information des utilisateurs qu'ils interagissent avec un système d'IA (obligation de transparence à vérifier dans le texte officiel).
5. Gateway en place et accès direct aux modèles bloqué (exigences G1 à G6).
6. Analyse de protection des données réalisée avec le DPO, notamment sur la journalisation et la revue par échantillonnage.

## Conditions de suspension
Fuite de données hors plafond constatée, contournement du gateway, dérive d'évaluation au-delà des seuils, demande du DPO ou du RSSI, ou changement de finalité non instruit (ADR 0003).

## Risques et points de vigilance
- La dérive de finalité est le risque principal : un assistant interne devient un outil de gestion des personnes sans que personne ne le décide.
- La base documentaire est le vrai périmètre de données : un assistant limité à la classe `internal` peut quand même exposer des documents mal classés. La qualité des étiquettes conditionne la politique.
- L'IA fantôme : tant que l'accès direct n'est pas bloqué, ce système ne gouverne que son propre trafic.
