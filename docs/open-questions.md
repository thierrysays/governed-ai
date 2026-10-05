# Open questions

Items to be decided by the owner. None is resolved in code. French version: `open-questions_FR.md`.

1. Target cloud and identity provider (ADR 0002 stays proposed until answered).
2. Gateway product, or build on an open-source proxy (ADR 0002).
3. First use case chosen: internal assistant, limited risk (`docs/governance/use-cases/internal-assistant.md`). Still open: its accountable person and owner, the model, the supervision frequency, and the data protection assessment with the DPO.
4. Exact legal citations for the EU AI Act, GDPR and sector rules applicable to the first use case: to be taken from the official texts, not from this repository.
5. Evaluation thresholds and stop criteria: no numeric value is set here; they must come from the first use case's risk assessment.
6. Review of the French and English texts by the author: the two versions are written in parallel and must be proofread as a pair before any external use.
7. Licence of the public repository: decided on 2026-10-05, Apache-2.0 for code and CC BY 4.0 for documents and data (ADR 0004). Still open: confirmation of the wording by a legal adviser. The contribution process is defined in `CONTRIBUTING.md` (version 0.5.0).

8. Security reporting channel and code of conduct: decided on 2026-10-05, `SECURITY.md` and `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1), both reporting to the owner's email address. GitHub private vulnerability reporting was enabled on 2026-10-05 (confirmed by the owner). Still open: whether to replace the personal address with a dedicated one.
