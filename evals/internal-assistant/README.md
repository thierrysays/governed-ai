# Internal assistant evaluation

`cases.yaml`: synthetic cases by category (prompt injection, data leakage, out of scope, grounding in sources, oversight). Each case exists in English and in French, because the assistant must be tested in both languages. The validator (`make validate`) checks the structure, the link to the system, the presence of both languages and the synthetic marker.

What this set does not do: it sets no pass threshold and is not an evaluation in itself. It fixes the scenarios to run. The execution engine, thresholds and sampling remain to be defined (see `docs/open-questions.md`). A model can be approved in the registry (`evaluation_ref`) only after a documented run of these cases.
