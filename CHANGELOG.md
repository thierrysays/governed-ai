# Changelog

French version: `CHANGELOG_FR.md`.

## 0.3.1

- Structure comparison between the English and French versions of each document: same heading levels, same table shapes (rows and columns), same number of code blocks. Mismatches fail `make validate`.

## 0.3.0

- Bilingual repository: every document exists in English (`name.md`) and French (`name_FR.md`); registry entries carry `name_en` and `name_fr`; evaluation cases carry both languages. `make validate` enforces document parity and the bilingual fields.

## 0.2.0

- First use case: internal assistant (limited risk), use case sheet and ADR 0003 (proposed).
- Systems now carry `allowed_data_classes`; routing policy checks system, model and data class together (system ceiling and model clearance). Approved systems must have a model.
- Synthetic evaluation cases for the internal assistant with structural validation.

## 0.1.0

- Initial skeleton: governance documents (drafts), ADRs, threat model, registry schema and validator, routing and action policies with tests, CI.
