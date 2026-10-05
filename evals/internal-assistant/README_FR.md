# Évaluation de l'assistant interne

`cases.yaml` : cas synthétiques par catégorie (injection de prompt, fuite de données, hors périmètre, ancrage dans les sources, supervision). Chaque cas existe en anglais et en français, car l'assistant doit être testé dans les deux langues. Le validateur (`make validate`) contrôle la structure, le rattachement au système, la présence des deux langues et le caractère synthétique.

Ce que ce jeu ne fait pas : il ne fixe aucun seuil de réussite et ne constitue pas une évaluation. Il fixe les scénarios à exécuter. Le moteur d'exécution, les seuils et l'échantillonnage restent à définir (voir `docs/open-questions_FR.md`). Un modèle ne peut être approuvé au registre (`evaluation_ref`) qu'après une exécution documentée de ces cas.
