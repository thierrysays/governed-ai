# Threat model

Method: decomposition by layer, with threats named after the OWASP Top 10 for LLM Applications (2025 edition). To be completed with MITRE ATLAS for adversarial techniques. Risk levels are not quantified here: they depend on the use case.

| Threat | Layer | Planned control | Where |
|---|---|---|---|
| LLM01 Prompt injection | Gateway, agents | Input filtering, separation of instructions and data, least-privilege tools | `gateway/`, `policies/actions.rego` |
| LLM02 Sensitive information disclosure | Gateway, models | Routing by data class, output filtering | `policies/routing.rego` |
| LLM03 Supply chain | Models, tools, MCP | Registry admission, mandatory `approved` status | `registry/` |
| LLM04 Data and model poisoning | Data, evaluation | Corpus provenance, regression evaluations | `evals/` |
| LLM05 Improper output handling | Applications | Output validation before action | `gateway/` |
| LLM06 Excessive agency | Agents | Human approval of irreversible actions, action budget | `policies/actions.rego` |
| LLM07 System prompt leakage | Gateway | No secret in prompts, prompt review | `gateway/` |
| LLM08 Vector and embedding weaknesses | Data, RAG | Access control inherited from sources, sensitivity labels | `registry/`, catalogue |
| LLM09 Misinformation | Evaluation | Evaluation sets, human oversight according to risk class | `evals/` |
| LLM10 Unbounded consumption | Gateway, operations | Quotas, rate limits, token budgets | `gateway/` |
| Gateway bypass | Network | Network policy forbidding any direct access to models | `infra/` |
| Agent impersonation | Identity | Workload identities, narrowly scoped credentials | `identity/` |

References: OWASP, Top 10 for LLM Applications 2025; MITRE ATLAS; ISO/IEC 27001:2022.
