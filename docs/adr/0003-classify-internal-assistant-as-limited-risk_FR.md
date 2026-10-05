# 0003. Classer l'assistant interne en risque limité, sous conditions

- Status: proposed
- Date: 2026-10-04
- Deciders: Thierry Sayegh-Sauvage

## Context

Premier cas d'usage de la plateforme : un assistant interne de rédaction, de synthèse et de recherche documentaire. La classe de risque pilote les obligations et les contrôles (`registry/systems.yaml`, `docs/governance/system-register_FR.md`). La classification dépend de la finalité réelle, pas de la technologie.

## Decision

Classer `internal-assistant` en `limited`, sous trois conditions vérifiables :

1. Finalité bornée : rédaction, synthèse, recherche documentaire. Aucune évaluation, sélection, notation, surveillance ou décision concernant des personnes (recrutement, gestion des carrières, évaluation de performance, accès à des prestations).
2. Données plafonnées à `public` et `internal` dans la politique de routage.
3. Aucun outil à effet irréversible enregistré pour ce système.

Ces conditions sont des **déclencheurs de reclassification** : si l'une cesse d'être vraie, le système est reclassé (probablement `high`) et suspendu jusqu'à nouvelle instruction. Les cas `ia-scope-001` et `ia-scope-002` testent la première condition.

La citation exacte des dispositions applicables (domaines à risque élevé, obligation de transparence) doit être prise dans le texte officiel du Règlement (UE) 2024/1689 par l'auteur avant approbation. Elle n'est pas reproduite ici.

## Consequences

Les contrôles restent proportionnés (supervision par échantillonnage, pas de validation humaine systématique). En contrepartie, la gouvernance dépend de la discipline sur la finalité : il faut surveiller la dérive d'usage, ce que les cas d'évaluation hors périmètre et la revue d'échantillons doivent détecter.

## Alternatives considered

- Classer en `high` par prudence : plus sûr juridiquement, mais retire l'intérêt d'un premier cas simple et fait peser des contrôles disproportionnés.
- Ne pas classer avant le choix du modèle : la classification dépend de la finalité et non du modèle ; attendre masquerait le risque de dérive.
