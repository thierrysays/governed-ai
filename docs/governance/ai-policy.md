# AI policy (draft, to be validated by the COMEX or CODIR)

Status: draft. No clause is in force until approved by the competent management body.

## 1. Purpose and scope
This policy governs the design, acquisition, deployment and operation of AI systems, including agents and the tools they call. It applies to every use that goes through the platform, and the platform is the only authorised path (see `gateway/README.md`).

## 2. Principles
1. **Registry first**: a model, tool or system that is not in the registry (`registry/`) is not authorised.
2. **Classification before use**: every system receives a risk class (`unacceptable`, `high`, `limited`, `minimal`), justified in `system-register.md`. A system classed `unacceptable` is never approved.
3. **Named accountability**: every system has a designated accountable person (`accountable` field). No approval without one.
4. **Human oversight**: mandatory for high-risk systems and for any irreversible agent action.
5. **Data**: a model receives only the data classes it is cleared for (`allowed_data_classes`).
6. **Continuous evaluation**: no model or prompt enters production without a versioned evaluation (`evals/`). Thresholds are set by the risk assessment of each use case.
7. **Traceability**: every request and every policy decision is logged (`observability/`).
8. **Withdrawal**: every system has a suspension condition and a decommissioning plan.

## 3. Exceptions
An exception is written, dated, time-bound and approved by the AI risk owner. It is recorded in the registry and never granted verbally.

## 4. Review
Reviewed at least annually by the CODIR and after any significant incident. Structural decisions go through an ADR.
