# Gateway: requirements contract

This directory describes what the entry point must do, without prescribing a product (ADR 0002). Any candidate (open-source proxy, cloud service, commercial product) is assessed against these requirements.

| Requirement | Description |
|---|---|
| G1 Mandatory entry point | Every model call goes through the gateway. Direct access is blocked at network level (`infra/`). |
| G2 Authentication | Every caller (user, application, agent) is authenticated. No shared key. |
| G3 Policy decision | The gateway queries the policy engine (`policies/`) before every routing decision and every tool call, and denies by default. |
| G4 Filtering | Input and output: personal data, injection attempts, prohibited content. |
| G5 Limits | Quotas, rate limits and token budgets per identity and per system. |
| G6 Logging | Request, policy decision, model, tool, identity, timestamp; immutable storage; sensitive data masked. |
| G7 Telemetry | OpenTelemetry export. |
| G8 Availability | A defined failure mode (safe refusal) and a continuity plan. |
| G9 Portability | Exportable, versioned configuration; no policy coded inside the product. |
