# Dossier d'instruction : assistant interne

Statut : brouillon de travail préparé pour le propriétaire. Il ne décide rien : il ordonne ce qui manque avant que `internal-assistant` puisse être approuvé, et il n'invente ni personne, ni modèle, ni seuil, ni citation juridique. Fiche du cas d'usage : `internal-assistant_FR.md`. Classification : ADR 0003.

## 1. Statut des conditions d'approbation

Les six conditions viennent de la fiche du cas d'usage. Aucune n'est entièrement remplie aujourd'hui ; la condition 4 a un projet.

| Condition | Statut | Preuve dans le dépôt | Reste à faire |
|---|---|---|---|
| 1. Responsable et propriétaire du système nommés | Non remplie | `registry/systems.yaml` : `accountable` et `owner` valent `to-be-assigned` | Le propriétaire désigne les deux |
| 2. Modèle approuvé avec évaluation de référence, habilité pour `internal` | Non remplie | Le système ne liste aucun modèle ; le registre ne contient que des exemples synthétiques | Choisir un modèle (section 5), exécuter l'évaluation (section 6), consigner la référence |
| 3. Exécution documentée des cas d'évaluation, avec seuils | Non remplie | Neuf cas synthétiques dans `evals/internal-assistant/cases.yaml` ; aucune exécution, aucun seuil | Le responsable du risque IA fixe les seuils ; les cas sont exécutés (section 6) |
| 4. Utilisateurs informés qu'ils interagissent avec un système d'IA | Projet rédigé | Projet de notice en section 7.1 | Vérifier la formulation dans le texte officiel ; l'afficher dans l'interface |
| 5. Gateway en place, accès direct aux modèles bloqué | Non remplie | Contrat d'exigences seulement (`gateway/README_FR.md`) ; aucun produit choisi | Choisir et déployer le gateway (l'ADR 0002 reste ouvert) |
| 6. Analyse de protection des données avec le DPO | Non commencée | Questions de cadrage en section 3 | Y répondre avec le DPO, qui décide de la suite |

## 2. Décisions attendues du propriétaire

| Décision | Pourquoi elle compte | Contrainte ou options |
|---|---|---|
| Responsable | Pas d'approbation sans personne nommée | Une personne nommée, pas une fonction |
| Propriétaire du système | Exploite le système au quotidien (première ligne de maîtrise) | Une personne nommée ou un responsable d'équipe |
| Fréquence de supervision et taille de l'échantillon | Définit la supervision humaine | À fixer par le propriétaire ; aucune valeur n'est proposée ici |
| Durée de conservation des journaux | Détermine l'impact sur la vie privée de la revue par échantillonnage | À fixer avec le DPO ; plus court est plus sûr |
| Seuils d'évaluation et critères d'arrêt | Sans eux, l'évaluation ne peut ni réussir ni échouer | À fixer par le responsable du risque IA à partir du registre des risques (section 4) |
| Cloud cible et produit de gateway | Bloque les conditions 2 et 5 | L'ADR 0002 est ouvert ; les exigences sont dans `gateway/README_FR.md` |
| Périmètre de la base documentaire | C'est le véritable périmètre de données | Quelles collections l'assistant peut lire, chacune avec une classe de données |

## 3. Pré-analyse de protection des données

Ce sont des questions de cadrage, pas des conclusions juridiques. Le DPO y répond et décide de la suite, y compris de la nécessité d'une analyse d'impact relative à la protection des données.

| Question | Pourquoi elle est posée | Réponse |
|---|---|---|
| Les utilisateurs peuvent-ils coller dans les prompts des données personnelles de tiers ? | Ces données sont hors périmètre de ce système | À compléter avec le DPO |
| Les journaux contiennent-ils des données personnelles de collaborateurs (identité, contenu des prompts) ? | La journalisation est exigée (G6) et la revue par échantillonnage les lit | À compléter avec le DPO |
| Qui peut lire les journaux, et pendant combien de temps ? | L'accès et la conservation déterminent l'impact sur la vie privée | À compléter avec le DPO |
| Quelle base légale couvre la revue par échantillonnage des conversations ? | La revue traite des données de collaborateurs ; le DPO établit la base, elle n'est pas présumée ici | À compléter avec le DPO |
| Comment les collaborateurs sont-ils informés de la journalisation et de la revue ? | L'information préalable est une condition d'approbation (condition 4) | À compléter avec le DPO |
| Les documents que l'assistant peut lire contiennent-ils des données personnelles ? | La recherche peut les faire remonter, même depuis un document `internal` | À compléter avec le DPO |
| Une analyse d'impact relative à la protection des données est-elle nécessaire ? | Seul le DPO peut la qualifier ; les réponses ci-dessus alimentent cette décision | À compléter avec le DPO |
| Quels sous-traitants traitent les prompts et les journaux, et où ? | La région d'hébergement du modèle et des journaux compte (section 5) | À compléter avec le DPO |

## 4. Registre des risques du cas d'usage

Le registre est qualitatif : aucun score de probabilité ou d'impact n'est fixé ici. Le responsable du risque IA évalue chaque risque et en déduit les seuils de la section 6.

| Risque | Description | Contrôles dans le dépôt | Point ouvert |
|---|---|---|---|
| Dérive de finalité | L'assistant devient un outil de décision sur des personnes | Déclencheurs de reclassification (ADR 0003) ; cas `ia-scope-001` et `ia-scope-002` | La détection repose sur la revue par échantillonnage |
| Documents mal étiquetés | Des documents au-dessus du plafond deviennent lisibles par l'assistant | Plafonds de classes de données dans `policies/routing.rego` | La qualité des étiquettes des documents n'est pas mesurée |
| Injection de prompt par les documents | Des instructions intégrées sont traitées comme des ordres | Cas `ia-inj-001` et `ia-inj-002` ; filtrage du gateway (G4) | Le gateway n'est pas déployé |
| Fuite de données personnelles | Des données de tiers ou de collaborateurs sont exposées | Cas `ia-leak-001` et `ia-leak-002` ; classes de données | Le filtrage dépend du gateway |
| Réponses inventées | Une règle ou un chiffre est inventé en l'absence de source | Cas `ia-ground-001` et `ia-ground-002` | Les seuils ne sont pas fixés |
| IA fantôme | Les équipes contournent la plateforme | Exigence G1 et isolation réseau (`infra/`) | Non mis en œuvre |
| Exposition des journaux | Les journaux révèlent le contenu des conversations des collaborateurs | Journalisation immuable (G6) | Les règles de conservation et d'accès ne sont pas décidées |
| Juridiction du modèle | Les prompts sont traités hors de la juridiction prévue | Région et habilitation par classe dans `registry/models.yaml` | Aucun modèle n'est choisi |

## 5. Critères d'admission d'un modèle

Les critères ne dépendent d'aucun fournisseur. Aucun fournisseur n'est nommé et aucune affirmation sur un fournisseur n'est faite ici : chaque critère exige une preuve fournie par le fournisseur.

| Critère | Preuve exigée | Condition de réussite |
|---|---|---|
| Région d'hébergement | La documentation du fournisseur sur le lieu de traitement des prompts | La région correspond à la politique fixée par le propriétaire et le DPO |
| Habilitation par classe de données | La décision du propriétaire consignée dans `allowed_data_classes` | L'habilitation couvre `internal` seulement si le DPO est d'accord |
| Usage des entrées pour l'entraînement | Une déclaration contractuelle écrite du fournisseur | Les entrées ne servent pas à entraîner les modèles du fournisseur, confirmé par écrit |
| Conservation chez le fournisseur | Une déclaration contractuelle écrite | La conservation est compatible avec la décision du DPO |
| Évaluation | Une exécution des neuf cas dans les deux langues (section 6) | Les seuils fixés par le responsable du risque IA sont atteints |
| Compatibilité avec la journalisation | Un test à travers le gateway | Les requêtes et les décisions sont journalisées (G6), données sensibles masquées |
| Plan de sortie | Un chemin de remplacement documenté | Un autre modèle ou fournisseur approuvé peut prendre le relais sans modifier les politiques |

## 6. Protocole d'évaluation

1. Préalables : le gateway est en place et le modèle est un candidat du registre.
2. Exécuter chacun des neuf cas de `evals/internal-assistant/cases.yaml` en anglais et en français, à travers le gateway.
3. Consigner, pour chaque cas : le modèle, la date, la langue, la sortie, le verdict (conforme, non conforme, à examiner) et le nom du relecteur.
4. Un cas est réussi seulement si le comportement attendu est obtenu dans les deux langues.
5. Le nombre de répétitions et les seuils de réussite sont fixés par le responsable du risque IA ; aucune valeur n'est proposée ici.
6. Ranger les résultats sous `evals/internal-assistant/` et les référencer dans `evaluation_ref` (`make validate` vérifie que le fichier référencé existe).
7. Tout changement de modèle, de prompt ou de politique exige une nouvelle exécution.

## 7. Supervision et information des utilisateurs

### 7.1 Projet de notice aux utilisateurs

> Vous interagissez avec un assistant d'IA. Il peut se tromper : vérifiez les réponses importantes auprès de leur source. Vos conversations sont journalisées, et un échantillon peut être relu pour contrôler la qualité et la conformité de l'assistant. Ne saisissez pas de données personnelles sur d'autres personnes, ni de documents classés au-dessus de « interne ». L'assistant ne prend ni ne recommande aucune décision concernant des personnes.

Cette formulation est une proposition. Elle doit être vérifiée dans le texte officiel de l'obligation de transparence et validée par le DPO avant d'être affichée.

### 7.2 Supervision par échantillonnage

Principes proposés, à confirmer par le propriétaire et le DPO : les relecteurs sont nommés ; le contenu relu se limite à ce que la revue exige ; l'échantillon ne vise pas des personnes en particulier ; les constats servent à améliorer le système, pas à évaluer les collaborateurs. La fréquence et la taille de l'échantillon relèvent du propriétaire (section 2).

## 8. Prochaines étapes

1. Le propriétaire désigne le responsable et le propriétaire du système.
2. Le propriétaire et le DPO répondent aux questions de cadrage (section 3).
3. Le propriétaire choisit le cloud cible et le produit de gateway, ce qui clôt l'ADR 0002.
4. Le responsable du risque IA évalue les risques (section 4) et fixe les seuils.
5. Un modèle est sélectionné selon les critères d'admission (section 5) et l'évaluation est exécutée (section 6).
6. Quand les six conditions sont remplies, le propriétaire peut demander que `internal-assistant` passe à `approved`. Cette décision lui revient seul.
