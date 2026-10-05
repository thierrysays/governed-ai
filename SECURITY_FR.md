# Politique de sécurité

English version: `SECURITY.md`.

## Versions prises en charge

Seule la branche `main` actuelle est prise en charge. Les corrections sont faites sur `main` ; les versions plus anciennes ne sont pas corrigées.

## Ce qu'il faut signaler

Ce dépôt contient des politiques, un validateur de registre et des documents, et n'exécute aucun service. Un problème de sécurité ici relève de l'un des cas suivants :

- Une faille de politique : une requête que `policies/routing.rego` ou `policies/actions.rego` autorise alors que le registre exige un refus, ou un contournement de l'approbation humaine requise pour les actions irréversibles.
- Une faille du validateur : un fichier de registre ou d'évaluation invalide qui passe `make validate`.
- Une faiblesse du workflow de CI (`.github/workflows/`), par exemple un traitement non sûr des données d'une demande de fusion.
- Un secret, un identifiant d'accès ou une donnée personnelle versé dans le dépôt ou son historique.

Sont hors périmètre : les avis sur le contenu des documents de gouvernance (ouvrez un ticket ordinaire), les vulnérabilités d'outils tiers tels qu'OPA ou GitHub Actions (signalez-les à leurs éditeurs) et les entrées d'exemple synthétiques de `registry/`.

## Comment signaler

N'ouvrez pas de ticket public. Utilisez le signalement privé de vulnérabilités de GitHub : ouvrez l'onglet Security du dépôt et choisissez « Report a vulnerability », ou rendez-vous sur https://github.com/thierrysays/governed-ai/security/advisories/new. Seul le propriétaire voit le signalement. Si vous ne pouvez pas utiliser GitHub, envoyez-le plutôt à conduct@glossolalie.pro. Écrivez en français ou en anglais et indiquez le fichier ou la règle concernés, les étapes de reproduction (une entrée qui échoue est idéale) et l'impact que vous voyez.

## À quoi vous attendre

Le propriétaire lit chaque signalement, l'évalue et, s'il est confirmé, le corrige sur `main` et vous cite si vous le souhaitez. Il s'agit d'un projet tenu par une seule personne : aucun délai de réponse n'est fixé, aucune prime n'est versée et aucun niveau de service n'est garanti. Laissez au propriétaire un délai raisonnable pour corriger avant toute divulgation publique.

## Bonne foi

Une recherche limitée à la lecture de ce dépôt public et à l'exécution de son code sur votre propre machine est bienvenue. N'effectuez aucun test sur des systèmes dont vous n'êtes pas propriétaire. Cette politique n'accorde aucune immunité juridique.
