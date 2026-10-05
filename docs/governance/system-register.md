# System register: method

The machine-readable source of truth is `registry/systems.yaml`. This document holds the human justification for each classification.

## Sheet per system (to copy)

| Field | Content |
|---|---|
| Identifier | Same as in `registry/systems.yaml` |
| Purpose | Decision or task supported, users concerned |
| Risk class | `unacceptable`, `high`, `limited` or `minimal`, with the justification and the reference to the applicable text (exact citation to be taken from the official text) |
| Data processed | Data classes, presence of personal data, legal basis |
| Models and tools | References to the registry |
| Human oversight | Mode and control point |
| Accountable person | Named individual |
| Evaluation | Reference to the evaluation set and the stop criteria |
| Suspension conditions | Triggers and procedure |

## Registered systems

| Identifier | Status | Class | Sheet |
|---|---|---|---|
| `internal-assistant` | candidate | limited | `use-cases/internal-assistant.md`, ADR 0003 |

The `example-internal-assistant` registry entry is synthetic.
