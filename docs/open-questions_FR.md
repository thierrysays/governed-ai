# Questions ouvertes

Points à trancher par le propriétaire. Aucun n'est résolu dans le code. English version: `open-questions.md`.

1. Cloud cible et fournisseur d'identité (l'ADR 0002 reste proposé tant que la question est ouverte).
2. Produit de gateway, ou construction sur un proxy open source (ADR 0002).
3. Premier cas d'usage retenu : assistant interne, risque limité (`docs/governance/use-cases/internal-assistant_FR.md`). Restent ouverts : le responsable et le propriétaire, le modèle, la fréquence de supervision et l'analyse de protection des données avec le DPO.
4. Citations juridiques exactes pour l'EU AI Act, le RGPD et les règles sectorielles applicables au premier cas d'usage : à prendre dans les textes officiels, pas dans ce dépôt.
5. Seuils d'évaluation et critères d'arrêt : aucune valeur chiffrée n'est fixée ici ; elle doit venir de l'évaluation de risque du premier cas d'usage.
6. Relecture des textes français et anglais par l'auteur : les deux versions sont rédigées en parallèle et doivent être relues en paire avant tout usage externe.
7. Licence du dépôt public : décidée le 2026-10-05, Apache-2.0 pour le code et CC BY 4.0 pour les documents et les données (ADR 0004). Reste ouverte : la confirmation de la rédaction par un conseil juridique. Le processus de contribution est défini dans `CONTRIBUTING_FR.md` (version 0.5.0).

8. Canal de signalement des failles de sécurité et code de conduite : décidés le 2026-10-05, `SECURITY_FR.md` et `CODE_OF_CONDUCT_FR.md` (Contributor Covenant 2.1). Le signalement privé de vulnérabilités de GitHub est activé (confirmé par le propriétaire) ; une adresse dédiée remplace l'adresse personnelle : conduct@glossolalie.pro, utilisée à la fois pour le code de conduite et pour la politique de sécurité (security@glossolalie.pro n'est pas en service). Restent ouverts : une adresse de sécurité distincte, la confirmation que la boîte est relevée, et le renouvellement automatique du domaine glossolalie.pro.