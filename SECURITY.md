# Security policy

French version: `SECURITY_FR.md`.

## Supported versions

Only the current `main` branch is supported. Fixes are made on `main`; older versions are not patched.

## What to report

This repository holds policies, a registry validator and documents, and runs no service. A security issue here is one of the following:

- A policy flaw: a request that `policies/routing.rego` or `policies/actions.rego` allows although the registry says it should be denied, or a bypass of the human approval required for irreversible actions.
- A validator flaw: a registry or evaluation file that is invalid but passes `make validate`.
- A weakness in the CI workflow (`.github/workflows/`), such as unsafe handling of pull request input.
- A secret, credential or personal data committed to the repository or its history.

The following are out of scope: opinions on the content of governance documents (open an ordinary issue), vulnerabilities in third-party tools such as OPA or GitHub Actions (report them upstream), and the synthetic example entries in `registry/`.

## How to report

Do not open a public issue. Use GitHub private vulnerability reporting: open the Security tab of this repository and choose "Report a vulnerability", or go to https://github.com/thierrysays/governed-ai/security/advisories/new. Only the owner sees the report. If you cannot use GitHub, send it to conduct@glossolalie.pro instead. Write in English or French and include the affected file or rule, steps to reproduce (a failing input is ideal) and the impact you see.

## What to expect

The owner reads each report, assesses it and, if it is confirmed, fixes it on `main` and credits you if you wish. This is a one-person project: there is no fixed response time, no bounty and no service level. Please give the owner a reasonable time to fix the issue before you disclose it publicly.

## Good faith

Research limited to reading this public repository and running its code on your own machine is welcome. Do not test against systems you do not own. This policy does not grant legal immunity.
