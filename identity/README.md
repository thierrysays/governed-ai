# Identité

Principes (à implémenter selon le fournisseur d'identité retenu, voir `docs/open-questions.md`) :

- Identités de charge de travail pour les agents et applications, pas de secret statique partagé.
- Délégation au nom de l'utilisateur (OAuth 2.x, on-behalf-of) avec le périmètre minimal.
- Jetons de courte durée, rotation et révocation testées.
- Chaque agent a un propriétaire nommé, présent dans `registry/systems.yaml`.
