# Identity

Principles (to be implemented according to the identity provider chosen, see `docs/open-questions.md`):

- Workload identities for agents and applications; no shared static secret.
- Delegation on behalf of the user (OAuth 2.x, on-behalf-of) with the minimum scope.
- Short-lived tokens, with rotation and revocation tested.
- Every agent has a named owner, recorded in `registry/systems.yaml`.
