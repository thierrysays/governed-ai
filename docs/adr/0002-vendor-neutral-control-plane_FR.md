# 0002. Plan de contrôle sans dépendance à un fournisseur

- Statut : proposé
- Date : 2026-10-04
- Décideurs : Thierry Sayegh-Sauvage

## Contexte

Le schéma de référence qui a inspiré ce projet repose sur le gateway et le catalogue d'un seul éditeur. La gouvernance doit survivre au choix d'un fournisseur. Aucun cloud, fournisseur d'identité ni produit de gateway n'a été retenu (`docs/open-questions_FR.md`).

## Décision

Définir la plateforme par des interfaces ouvertes et garder les produits remplaçables :

- Politiques en code dans OPA/Rego, versionnées et testées en CI.
- Registre des modèles, outils et systèmes en YAML dans Git, revu par demande de fusion.
- Télémétrie par OpenTelemetry ; lignage par OpenLineage lorsqu'un catalogue existe.
- Accès aux outils par le Model Context Protocol, derrière le registre.
- Le gateway est spécifié par un contrat d'exigences (`gateway/README_FR.md`), pas par la configuration d'un produit.

Le choix du produit fera l'objet d'un ADR ultérieur, une fois connus le premier cas d'usage et le cloud cible.

## Conséquences

Plus facile : remplacer un gateway, un fournisseur de modèles ou un cloud ; auditer les règles indépendamment du produit. Plus difficile : certaines fonctions natives d'un éditeur (catalogue intégré, lignage) doivent être reproduites par de l'intégration ; le gateway est un point de concentration dont la disponibilité doit être conçue.

## Alternatives examinées

- Pile intégrée d'un seul éditeur : démarrage plus rapide, mais politiques et lignage deviennent non portables.
- Registre dans un outil dédié : meilleur passage à l'échelle, mais la source de vérité quitte Git. À réexaminer si le registre dépasse les capacités du YAML.
