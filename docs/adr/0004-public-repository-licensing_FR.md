# 0004. Licence du dépôt public

- Statut : accepté
- Date : 2026-10-05
- Décideurs : Thierry Sayegh-Sauvage

## Contexte

Le dépôt est public, alors qu'il avait d'abord été créé et documenté comme privé. Il contient du code (politiques, validateur, tests), des brouillons de gouvernance, un schéma de registre et des données synthétiques. Sans licence, le droit d'auteur reste au propriétaire et personne ne peut réutiliser le contenu au-delà de ce que les conditions d'utilisation de la plateforme permettent (consultation et duplication). Le 2026-10-05, le propriétaire a décidé de garder le dépôt public et de l'ouvrir sous licences.

Cet ADR ne constitue pas un avis juridique ; la rédaction doit être confirmée avec un conseil juridique (`docs/open-questions_FR.md`, point 7).

## Décision

- Le code est placé sous Apache License 2.0 (`LICENSE`). Cela couvre `policies/`, `tools/`, `tests/`, `Makefile`, `.github/` et `requirements.txt`. Chaque fichier `.py` et `.rego` porte un en-tête SPDX, contrôlé par `make validate`.
- Les documents et les données sont placés sous Creative Commons Attribution 4.0 International (`LICENSE-docs.txt`). Cela couvre tout le reste, y compris `docs/`, les README, le registre et les données d'évaluation.
- Les noms et marques (Glossolalie Advisory, ECM™, PLCF™, VEGA™, TDG™, CORE™, LEGATE™) ne sont pas concédés.
- Un `NOTICE` simple porte la mention d'attribution Apache ; `LICENSING_FR.md` explique le périmètre dans les deux langues.
- Les brouillons restent signalés comme tels (section Statut du README) : une licence ne les rend pas relus.

## Conséquences

Plus facile : la réutilisation et la crédibilité externe ; la licence du code correspond à l'écosystème OPA et inclut une concession de brevets. Plus difficile : le choix ne peut plus être retiré pour les versions déjà publiées ; les documents de gouvernance peuvent être republiés par tous avec attribution, donc l'avantage du propriétaire tient à l'exécution plus qu'au texte ; des documents encore à l'état de brouillon, aux citations juridiques non vérifiées, sont désormais réutilisables. Les contributions exigent une politique (aucune pour l'instant).

## Alternatives examinées

- Tous droits réservés : protège le contenu ; aucune réutilisation et aucune crédibilité externe. Conservé seulement comme position provisoire jusqu'à cette décision.
- MIT pour le code : plus court, mais sans concession de brevets.
- AGPL-3.0 pour le code : maintient ouvertes les œuvres dérivées ; dissuade les grandes organisations visées par le projet.
- CC BY-NC pour les documents : la notion d'usage non commercial est floue et décourage la réutilisation sans protéger le propriétaire de façon fiable.
- Repasser le dépôt en privé : écarté par le propriétaire le 2026-10-05.
