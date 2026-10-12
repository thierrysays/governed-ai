# Instruction file: internal assistant

Status: working draft prepared for the owner. It decides nothing: it orders what is missing before `internal-assistant` can be approved, and it invents no person, model, threshold or legal citation. Use case sheet: `internal-assistant.md`. Classification: ADR 0003.

## 1. Status of the approval conditions

The six conditions come from the use case sheet. None is fully met today; condition 4 has a draft.

| Condition | Status | Evidence in the repository | Remaining work |
|---|---|---|---|
| 1. Named accountable person and system owner | Not met | `registry/systems.yaml`: `accountable` and `owner` are `to-be-assigned` | The owner designates both |
| 2. Approved model with a reference evaluation, cleared for `internal` | Not met | The system lists no model; the registry holds only synthetic examples | Choose a model (section 5), run the evaluation (section 6), record the reference |
| 3. Documented run of the evaluation cases, with thresholds | Not met | Nine synthetic cases in `evals/internal-assistant/cases.yaml`; no run, no threshold | The AI risk owner sets thresholds; the cases are run (section 6) |
| 4. Users informed that they interact with an AI system | Drafted | Draft notice in section 7.1 | Check the wording against the official text; show it in the interface |
| 5. Gateway in place, direct access to models blocked | Not met | Requirements contract only (`gateway/README.md`); no product chosen | Choose and deploy the gateway (ADR 0002 is still open) |
| 6. Data protection assessment with the DPO | Not started | Screening questions in section 3 | Answer them with the DPO, who decides what follows |

## 2. Decisions awaited from the owner

| Decision | Why it matters | Constraint or options |
|---|---|---|
| Accountable person | No approval without a named person | One named individual, not a function |
| System owner | Runs the system day to day (first line of defence) | A named individual or team lead |
| Supervision frequency and sample size | Defines the human oversight | To be set by the owner; no value is proposed here |
| Log retention period | Drives the privacy impact of sampled review | To be set with the DPO; shorter is safer |
| Evaluation thresholds and stop criteria | Without them the evaluation cannot pass or fail | To be set by the AI risk owner from the risk register (section 4) |
| Target cloud and gateway product | Blocks conditions 2 and 5 | ADR 0002 is open; requirements are in `gateway/README.md` |
| Scope of the document base | It is the real data perimeter | Which collections the assistant may read, each with a data class |

## 3. Data protection pre-assessment

These are screening questions, not legal conclusions. The DPO answers them and decides what follows, including whether a data protection impact assessment is required.

| Question | Why it is asked | Answer |
|---|---|---|
| Can users paste personal data about third parties into prompts? | Such data is out of scope for this system | To complete with the DPO |
| Do the logs contain personal data about employees (identity, prompt content)? | Logging is required (G6) and sampled review reads it | To complete with the DPO |
| Who can read the logs, and for how long? | Access and retention drive the privacy impact | To complete with the DPO |
| Which legal basis covers sampled review of conversations? | The review processes employees' data; the DPO establishes the basis, it is not assumed here | To complete with the DPO |
| How are employees informed of logging and review? | Prior information is a condition of approval (condition 4) | To complete with the DPO |
| Do the documents the assistant can read contain personal data? | Retrieval can surface it, even from an `internal` document | To complete with the DPO |
| Is a data protection impact assessment required? | Only the DPO can qualify it; the answers above feed that decision | To complete with the DPO |
| Which processors or sub-processors handle prompts and logs, and where? | The hosting region of the model and of the logs matters (section 5) | To complete with the DPO |

## 4. Risk register of the use case

The register is qualitative: no probability or impact score is set here. The AI risk owner rates each risk and derives the thresholds of section 6.

| Risk | Description | Controls in the repository | Open point |
|---|---|---|---|
| Purpose drift | The assistant becomes a tool for decisions about people | Reclassification triggers (ADR 0003); cases `ia-scope-001` and `ia-scope-002` | Detection relies on sampled review |
| Mislabelled documents | Documents above the ceiling become readable by the assistant | Data class ceilings in `policies/routing.rego` | Quality of document labels is not measured |
| Prompt injection through documents | Embedded instructions are treated as commands | Cases `ia-inj-001` and `ia-inj-002`; gateway filtering (G4) | The gateway is not deployed |
| Personal data leakage | Third-party or employee data is exposed | Cases `ia-leak-001` and `ia-leak-002`; data classes | Filtering depends on the gateway |
| Invented answers | A rule or figure is invented when no source exists | Cases `ia-ground-001` and `ia-ground-002` | Thresholds are not set |
| Shadow AI | Staff bypass the platform | Requirement G1 and network isolation (`infra/`) | Not implemented |
| Log exposure | Logs reveal the content of employees' conversations | Immutable logging (G6) | Retention and access rules are undecided |
| Model jurisdiction | Prompts are processed outside the intended jurisdiction | Region and class clearance in `registry/models.yaml` | No model is chosen |

## 5. Model admission criteria

The criteria are vendor-neutral. No provider is named, and no claim about any provider is made here: each criterion needs evidence supplied by the provider.

| Criterion | Evidence required | Pass condition |
|---|---|---|
| Hosting region | The provider's documentation of where prompts are processed | The region matches the policy set by the owner and the DPO |
| Data class clearance | The owner's decision recorded in `allowed_data_classes` | Clearance covers `internal` only if the DPO agrees |
| Use of inputs for training | A written contractual statement from the provider | Inputs are not used to train the provider's models, confirmed in writing |
| Retention by the provider | A written contractual statement | Retention is compatible with the DPO's decision |
| Evaluation | A run of the nine cases in both languages (section 6) | The thresholds set by the AI risk owner are met |
| Logging compatibility | A test through the gateway | Requests and decisions are logged (G6), with sensitive data masked |
| Exit plan | A documented replacement path | Another approved model or provider can take over without changing the policies |

## 6. Evaluation protocol

1. Preconditions: the gateway is in place and the model is a registry candidate.
2. Run each of the nine cases of `evals/internal-assistant/cases.yaml` in English and in French, through the gateway.
3. Record, for each case: model, date, language, the output, the verdict (conform, non-conform, to review) and the reviewer's name.
4. A case passes only if the expected behaviour is met in both languages.
5. The number of repetitions and the pass thresholds are set by the AI risk owner; no value is proposed here.
6. Store the results under `evals/internal-assistant/` and reference them in `evaluation_ref` (`make validate` checks that the referenced file exists).
7. Any change of model, prompt or policy requires a new run.

## 7. Supervision and information of users

### 7.1 Draft notice to users

> You are interacting with an AI assistant. It can make mistakes: check important answers against their source. Your conversations are logged, and a sample may be reviewed to check the quality and compliance of the assistant. Do not enter personal data about other people, nor documents classified above "internal". The assistant does not make or recommend decisions about individuals.

This wording is a proposal. It must be checked against the official text of the transparency obligation and validated by the DPO before it is shown.

### 7.2 Sampled supervision

Proposed principles, to be confirmed by the owner and the DPO: the reviewers are named; the reviewed content is limited to what the review needs; the sample is not aimed at particular individuals; the findings are used to improve the system, not to assess employees. Frequency and sample size are decisions of the owner (section 2).

## 8. Next steps

1. The owner designates the accountable person and the system owner.
2. The owner and the DPO answer the screening questions (section 3).
3. The owner chooses the target cloud and the gateway product, which closes ADR 0002.
4. The AI risk owner rates the risks (section 4) and sets the thresholds.
5. A model is selected against the admission criteria (section 5) and the evaluation is run (section 6).
6. When all six conditions are met, the owner may ask for `internal-assistant` to be set to `approved`. That decision is the owner's alone.
