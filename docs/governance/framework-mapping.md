# Mapping to reference frameworks

Status: working mapping. Clause and article numbers must be verified by the author against the official texts before any external use. No legal citation is reproduced here.

| Platform capability | ISO/IEC 42001 (AI management system) | NIST AI RMF 1.0 | EU AI Act (Regulation 2024/1689) | Control in this repository |
|---|---|---|---|---|
| Policy, roles, risk appetite | Leadership, policy, roles | GOVERN | Obligations of providers and deployers | `docs/governance/ai-policy.md`, `raci.md` |
| Inventory and classification of systems | Planning, risk assessment | MAP | Classification by risk level | `registry/systems.yaml`, `system-register.md` |
| Admission of models and tools | Controls on resources and third parties | MAP, MANAGE | Obligations for general-purpose models, value chain | `registry/models.yaml`, `registry/tools.yaml`, `policies/routing.rego` |
| Human oversight, irreversible actions | Operational controls | MANAGE | Human oversight of high-risk systems | `policies/actions.rego` |
| Evaluation and testing | Performance evaluation | MEASURE | Accuracy, robustness, cybersecurity | `evals/` |
| Logging and traceability | Documented information, monitoring | MEASURE, MANAGE | Record keeping | `observability/` |
| Incidents and continual improvement | Improvement | MANAGE | Post-market monitoring, reporting | `docs/governance/ai-policy.md` §4 |

References: ISO/IEC 42001:2023; NIST, Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1, 2023; Regulation (EU) 2024/1689; COBIT 2019.
