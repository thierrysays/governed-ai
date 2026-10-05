# Use case 1: internal assistant

Status: under assessment. Registry identifier: `internal-assistant` (status `candidate`). Classification decision: ADR 0003.

## Purpose
Help employees with drafting, summarising and searching internal documentation. The assistant neither takes nor recommends any individual decision about a person.

## Sheet

| Field | Content |
|---|---|
| Identifier | `internal-assistant` |
| Purpose | Drafting, summarising, internal document search |
| Users | Authenticated employees of the organisation |
| Proposed risk class | `limited`, under the conditions of ADR 0003. Citation of the applicable text: to be confirmed in the official text of Regulation (EU) 2024/1689 |
| Data processed | Proposed ceiling: `public` and `internal`. No `confidential` or `restricted`. Personal data of third parties is out of scope |
| Models | None chosen (vendor neutrality, ADR 0002). A model must be in the registry, approved and cleared for `internal` before `policies/routing.rego` lets traffic through |
| Tools | None. Read access to the document base through the gateway only. No tool with irreversible effects |
| Human oversight | By sampling: periodic review of logged conversations, with prior notice to users. Mode and frequency to be defined |
| Accountable person | To be designated (`accountable`). No approval without a named person |
| System owner | To be designated |
| Evaluation | `evals/internal-assistant/cases.yaml`, execution to be documented |
| Suspension | See below |

## Conditions for approval (all required)
1. A named accountable person and system owner.
2. At least one approved model in the registry, with a reference evaluation and clearance for the `internal` class.
3. Documented execution of the evaluation cases, with thresholds set by the AI risk owner.
4. Users informed that they are interacting with an AI system (transparency obligation to be verified in the official text).
5. Gateway in place and direct access to models blocked (requirements G1 to G6).
6. Data protection assessment carried out with the DPO, in particular on logging and sampled review.

## Suspension conditions
A data leak above the ceiling, circumvention of the gateway, evaluation drift beyond the thresholds, a request from the DPO or the CISO, or a change of purpose that has not been assessed (ADR 0003).

## Risks and points of attention
- Purpose drift is the main risk: an internal assistant turns into a people-management tool without anyone deciding it.
- The document base is the real data perimeter: an assistant limited to the `internal` class can still expose badly classified documents. The quality of the labels conditions the policy.
- Shadow AI: until direct access is blocked, this system governs only its own traffic.
