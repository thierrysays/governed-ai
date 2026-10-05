# Journal des modifications

English version: `CHANGELOG.md`.

## 0.6.3

- `SECURITY.md` et `SECURITY_FR.md` : le signalement privé de vulnérabilités de GitHub, désormais activé sur le dépôt, devient le canal principal (avec le lien du formulaire) ; le courriel reste la solution de repli. Question ouverte 8 mise à jour.

## 0.6.2

- CI : `open-policy-agent/setup-opa` est remplacé par un téléchargement figé du binaire OPA 1.4.2 avec vérification SHA-256 (la somme de contrôle correspond à celle publiée avec la version). Cela supprime le dernier avertissement de dépréciation Node.js 20 et la dépendance à une action tierce. Pour changer de version d'OPA, il faut désormais mettre à jour ensemble `OPA_VERSION` et `OPA_SHA256`.

## 0.6.1

- CI : `actions/checkout` de v4 à v5 et `actions/setup-python` de v5 à v6, pour quitter l'environnement Node.js 20 déprécié. `open-policy-agent/setup-opa` reste en v2.

## 0.6.0

- Santé de la communauté : `CODE_OF_CONDUCT.md` et `CODE_OF_CONDUCT_FR.md` (Contributor Covenant 2.1, textes officiels anglais et français, contact renseigné) et `SECURITY.md` et `SECURITY_FR.md` (périmètre, signalement privé, attentes) ; liés depuis `CONTRIBUTING` et la paire de README ; `LICENSING` mentionne l'adaptation.

## 0.5.0

- Processus de contribution : `CONTRIBUTING.md` et `CONTRIBUTING_FR.md` (périmètre, licence, signature DCO, langues, marche à suivre, relecture), un modèle bilingue de demande de fusion et un contrôle en CI de la ligne `Signed-off-by` sur les demandes de fusion (`tools/check_dco.py`, propriétaire dispensé via `.github/dco-exempt.txt`). Les modèles de `.github/` sont dispensés du contrôle de parité des documents.

## 0.4.0

- Licence décidée (ADR 0004, accepté) : Apache-2.0 pour le code (`LICENSE`, en-têtes SPDX sur chaque fichier `.py` et `.rego`), CC BY 4.0 pour les documents et les données (`LICENSE-docs.txt`), marques non concédées. Ajout d'un `NOTICE` simple ; `NOTICE_FR.md` est remplacé par `LICENSING_FR.md`. `make validate` contrôle les fichiers de licence et les en-têtes SPDX.

## 0.3.2

- Le dépôt est public : suppression des mentions « privé », `NOTICE_FR.md` indique désormais « tous droits réservés, aucune licence accordée », le README gagne une section Statut (les brouillons ne sont ni une politique approuvée, ni un avis juridique, ni une attestation de conformité) et l'ADR 0004 (proposé) consigne les options de licence.

## 0.3.1

- Comparaison de structure entre les versions anglaise et française de chaque document : mêmes niveaux de titres, mêmes formes de tableaux (lignes et colonnes), même nombre de blocs de code. Un écart fait échouer `make validate`.

## 0.3.0

- Dépôt bilingue : chaque document existe en anglais (`nom.md`) et en français (`nom_FR.md`) ; les entrées du registre portent `name_en` et `name_fr` ; les cas d'évaluation portent les deux langues. `make validate` contrôle la parité des documents et les champs bilingues.

## 0.2.0

- Premier cas d'usage : assistant interne (risque limité), fiche du cas d'usage et ADR 0003 (proposé).
- Les systèmes portent désormais `allowed_data_classes` ; la politique de routage vérifie ensemble le système, le modèle et la classe de données (plafond du système et habilitation du modèle). Un système approuvé doit avoir un modèle.
- Cas d'évaluation synthétiques pour l'assistant interne, avec validation structurelle.

## 0.1.0

- Squelette initial : documents de gouvernance (brouillons), ADR, modèle de menaces, schéma et validateur du registre, politiques de routage et d'action avec tests, CI.
