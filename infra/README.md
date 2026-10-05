# Infrastructure

Infrastructure as code, to be written once the target cloud is chosen (ADR 0002). Structuring requirement: network isolation preventing any direct call to the models, so that the gateway is the only path (requirement G1). No secret, Terraform state or key in the repository (`.gitignore`).
