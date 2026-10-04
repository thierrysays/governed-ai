# Infrastructure

Infrastructure as code, à écrire une fois le cloud cible choisi (ADR 0002). Exigence structurante : isolation réseau empêchant tout appel direct aux modèles, de sorte que le gateway soit le seul chemin (exigence G1). Aucun secret, état Terraform ou clé dans le dépôt (`.gitignore`).
