# Politique IA (brouillon à valider par le COMEX ou le CODIR)

Statut : brouillon. Aucune clause n'est en vigueur avant approbation par l'organe de direction compétent.

## 1. Objet et périmètre
Cette politique encadre la conception, l'acquisition, le déploiement et l'exploitation des systèmes d'IA, y compris les agents et les outils qu'ils appellent. Elle s'applique à tout usage passant par la plateforme, et la plateforme est le seul chemin autorisé (voir `gateway/README.md`).

## 2. Principes
1. **Registre d'abord** : un modèle, un outil ou un système non inscrit au registre (`registry/`) n'est pas autorisé.
2. **Classification avant usage** : tout système reçoit une classe de risque (`unacceptable`, `high`, `limited`, `minimal`) justifiée dans `system-register.md`. Un système `unacceptable` n'est jamais approuvé.
3. **Responsabilité nominative** : chaque système a un responsable désigné (champ `accountable`). Pas d'approbation sans responsable.
4. **Supervision humaine** : obligatoire pour les systèmes à risque élevé et pour toute action irréversible d'un agent.
5. **Données** : un modèle ne reçoit que les classes de données pour lesquelles il est habilité (`allowed_data_classes`).
6. **Évaluation continue** : aucun modèle ni prompt n'entre en production sans évaluation versionnée (`evals/`). Les seuils sont fixés par l'évaluation de risque de chaque cas d'usage.
7. **Traçabilité** : toute requête et toute décision de politique sont journalisées (`observability/`).
8. **Retrait** : tout système a une condition de suspension et un plan de retrait.

## 3. Gestion des exceptions
Une exception est écrite, datée, bornée dans le temps et approuvée par le responsable du risque. Elle est inscrite au registre, jamais accordée oralement.

## 4. Revue
Revue au moins annuelle par le CODIR et après tout incident significatif. Les décisions structurantes passent par un ADR.
