# Gateway : contrat d'exigences

Ce répertoire décrit ce que le point d'entrée doit faire, sans prescrire de produit (ADR 0002). Tout candidat (proxy open source, service de cloud, produit commercial) est évalué contre ces exigences.

| Exigence | Description |
|---|---|
| G1 Point d'entrée obligatoire | Tout appel de modèle passe par le gateway. L'accès direct est bloqué au niveau réseau (`infra/`). |
| G2 Authentification | Chaque appelant (utilisateur, application, agent) est authentifié. Pas de clé partagée. |
| G3 Décision de politique | Le gateway interroge le moteur de politiques (`policies/`) avant chaque routage et chaque appel d'outil, et refuse par défaut. |
| G4 Filtrage | Entrée et sortie : données personnelles, tentatives d'injection, contenus interdits. |
| G5 Limites | Quotas, limites de débit et budgets de tokens par identité et par système. |
| G6 Journalisation | Requête, décision de politique, modèle, outil, identité, horodatage ; stockage immuable ; données sensibles masquées. |
| G7 Télémétrie | Export OpenTelemetry. |
| G8 Disponibilité | Mode de défaillance défini (refus sûr) et plan de continuité. |
| G9 Portabilité | Configuration exportable et versionnée ; aucune politique codée dans le produit. |
