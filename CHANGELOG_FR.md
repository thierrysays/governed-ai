# Journal des modifications

English version: `CHANGELOG.md`.

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
