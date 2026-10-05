# Contribuer

English version: `CONTRIBUTING.md`.

## Avant de commencer

Ce dépôt est une mise en œuvre de référence entretenue par un seul propriétaire. Les contributions sont bienvenues et examinées à la discrétion du propriétaire, sans engagement de délai de réponse. Ouvrez un ticket avant de commencer tout ce qui dépasse une correction, afin de convenir d'abord de la direction. Beaucoup de documents sont encore des brouillons (voir la section Statut de `README_FR.md`). En participant, vous vous engagez à respecter le code de conduite (`CODE_OF_CONDUCT_FR.md`). Signalez les problèmes de sécurité en privé, comme décrit dans `SECURITY_FR.md`, jamais dans un ticket public.

## Ce qui est bienvenu

- Corrections d'erreurs ou de passages peu clairs dans les documents, dans l'une ou l'autre langue.
- Signalement d'écarts de sens entre un document anglais et sa version française.
- Tests supplémentaires, en particulier des tests négatifs, et nouveaux cas d'évaluation synthétiques.
- Améliorations des politiques et du validateur de registre, avec des tests.
- Intégrations sans dépendance à un fournisseur, discutées d'abord dans un ADR.

## Ce qui n'est pas accepté

- Toute donnée réelle : données clients, données personnelles, identifiants d'accès, extraits de corpus.
- Tout texte de tiers recopié (normes, règlements, documentation d'éditeurs). Citez et mettez un lien à la place.
- Toute citation juridique qui ne renvoie pas au texte officiel.
- Tout changement qui fait passer un modèle, un outil ou un système au statut `approved` : ce statut relève du propriétaire.
- Toute configuration propre à un produit dans `policies/` ou dans les schémas du registre (ADR 0002).
- Tout contenu généré par machine que le contributeur n'a pas relu et dont il ne peut pas répondre.

## Licence et signature

Les contributions sont placées sous les licences du projet : Apache-2.0 pour le code et CC BY 4.0 pour les documents et les données (voir `LICENSING_FR.md`).

Chaque commit doit porter une ligne de signature, `Signed-off-by: Votre Nom <vous@exemple.fr>`, dont l'adresse correspond à celle de l'auteur du commit. `git commit -s` l'ajoute. La signature atteste le Developer Certificate of Origin 1.1 (https://developercertificate.org/). Cette attestation est personnelle : ne signez jamais au nom de quelqu'un d'autre. La CI contrôle la signature sur les demandes de fusion ; les commits dont le propriétaire est l'auteur en sont dispensés (`.github/dco-exempt.txt`).

## Langues

Chaque document existe en anglais (`nom.md`) et en français (`nom_FR.md`), avec la même structure, et `make validate` le contrôle. Si vous écrivez dans une seule langue, fournissez l'autre, ou indiquez dans la demande de fusion que vous ne l'avez pas pu et pourquoi. Les entrées du registre exigent `name_en` et `name_fr` ; les cas d'évaluation exigent les deux langues. Respectez les règles de registre : aucun tiret cadratin, orthographe britannique en anglais, et les règles françaises de `CLAUDE.md`.

## Marche à suivre

1. Dupliquez le dépôt (fork) et créez une branche par sujet à partir de `main`.
2. Préfixez les messages de commit par `policy:`, `registry:`, `docs:`, `tools:`, `infra:` ou `eval:`, et signez-les.
3. Pour tout changement de comportement ou de contenu, mettez à jour `CHANGELOG.md`, `CHANGELOG_FR.md` et `VERSION` (versionnage sémantique).
4. Lancez `make setup`, puis `make check`. Il doit passer avant d'ouvrir la demande de fusion.
5. Ouvrez une demande de fusion vers `main` : indiquez ce qui change, pourquoi, et ce que vous n'avez pas vérifié. La CI doit être verte.

## Contrôles de qualité

Chaque règle de politique a un test Rego positif et un test négatif, et chaque règle de validation a un test négatif. Les outils et les tests n'accèdent pas au réseau. Les dépendances sont figées dans `requirements.txt`. Chaque fichier `.py` et `.rego` porte l'en-tête SPDX. Les données sont synthétiques.

## Décisions et relecture

Le propriétaire relit chaque demande de fusion et peut la refuser. Les décisions significatives exigent un ADR (`docs/adr/template.md`). Une contribution ne donne ni droit d'écriture ni droit sur le dépôt.
