# 0004. Licence du dépôt public

- Statut : proposé
- Date : 2026-10-05
- Décideurs : Thierry Sayegh-Sauvage

## Contexte

Le dépôt est public, alors qu'il avait d'abord été créé et documenté comme privé. Il contient du code (politiques, validateur, tests), des brouillons de gouvernance, un schéma de registre et des données synthétiques. Aucun fichier de licence n'existe. Sans licence, le droit d'auteur reste au propriétaire et personne ne peut réutiliser le contenu au-delà de ce que les conditions d'utilisation de la plateforme permettent (consultation et duplication). Le 2026-10-05, le propriétaire a décidé de garder le dépôt public. Il n'a pas encore décidé d'ouvrir ou non le contenu, ni sous quelle licence.

Cet ADR consigne des options. Il ne constitue pas un avis juridique ; le choix et sa rédaction doivent être confirmés avec un conseil juridique avant l'ajout d'un fichier de licence.

## Décision

Position provisoire, jusqu'à la décision du propriétaire : conserver le contenu sous « tous droits réservés », l'indiquer dans `NOTICE_FR.md`, n'accorder aucune licence et signaler chaque brouillon comme tel (section Statut du README). Cette décision n'ajoute aucune licence open source.

## Conséquences

Les visiteurs peuvent lire le travail mais ne peuvent pas légalement le réutiliser, ce qui protège la propriété intellectuelle du propriétaire et évite de s'engager trop tôt sur une licence. Le coût est une réutilisation réduite et l'absence de voie de contribution externe. Les brouillons restent visibles : leur statut doit rester explicite.

## Alternatives examinées

- Licence permissive pour le code (par exemple Apache-2.0, qui inclut une concession de brevets, ou MIT) et licence d'attribution pour les documents (par exemple CC BY 4.0) : maximise la réutilisation et la visibilité ; irréversible pour les versions déjà publiées ; les documents de gouvernance deviennent réutilisables par tous, concurrents compris.
- Licence à copyleft pour le code (par exemple AGPL-3.0) : maintient ouvertes les œuvres dérivées ; dissuade certains adoptants en entreprise.
- Repasser le dépôt en privé : supprime l'exposition des brouillons ; perd la visibilité et la relecture externe. Écartée par le propriétaire le 2026-10-05.
