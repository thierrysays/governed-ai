# 0001. Consigner les décisions d'architecture

- Statut : accepté
- Date : 2026-10-04
- Décideurs : Thierry Sayegh-Sauvage

## Contexte

La plateforme combine des choix normatifs, d'architecture et de fournisseurs qui seront contestés par des auditeurs et des successeurs. Les décisions doivent rester traçables.

## Décision

Toute décision significative est consignée sous forme d'ADR dans `docs/adr/` à partir de `template.md`, numérotée séquentiellement et jamais réécrite : un changement d'avis crée un nouvel ADR qui remplace l'ancien. Chaque ADR existe en anglais et en français.

## Conséquences

Un léger surcoût par décision ; une piste d'audit durable, alignée sur les exigences d'informations documentées de l'ISO/IEC 42001.

## Alternatives examinées

Décisions dans des tickets ou une messagerie : ni durables ni versionnées avec le code.
