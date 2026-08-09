# Sacmia engineering standards

These are common defaults for Sacmia repositories. Project-specific documentation
may add stricter rules but must not silently weaken security, review, or release rules.

## Git and releases

- Work on a short-lived branch such as `feat/<name>`, `fix/<name>`, or `docs/<name>`.
- Open pull requests into `development`; never push directly to `development` or `main`.
- Require at least one human review and passing CI before merge.
- Merge `development` into `main` only as an intentional production release.
- Never let a coding agent merge its own pull request.

## Generated code and human responsibility

- Coding agents must read the repository's `CLAUDE.md` and feature specification first.
- Use one dedicated AI session for each feature branch and pull request. Keep review
  fixes in that session and start a fresh session for unrelated work. A replacement
  session must first re-read the current documentation, branch diff, pull request,
  and review comments.
- Do not invent unspecified product behavior; record the question and obtain a decision.
- Every behavior change needs proportionate automated tests and manual acceptance notes.
- Humans remain responsible for review, security decisions, and functional testing.

## Security

- Never commit or log passwords, tokens, private keys, connection strings, or real
  customer data. Use environment variables and the platform's encrypted secret store.
- Authenticate and authorize on the server. Client-side hiding is not authorization.
- Validate untrusted input and use explicit response schemas to avoid data leakage.
- Use least-privilege service accounts and separate development from production.
- Production credentials, databases, buckets, domains, and test accounts must never be
  reused from development.

## Cost-conscious scalable design

- Keep APIs stateless; durable state belongs in an approved shared datastore.
- Treat container filesystems as temporary; store media in approved object storage.
- Reuse bounded database pools, keep transactions short, and prevent N+1 queries.
- Paginate collection endpoints with server-enforced defaults and maximums.
- Make retryable writes idempotent through keys or database uniqueness constraints.
- Add indexes for demonstrated query paths in the same migration as the feature.
- Use structured, security-safe logs and configurable operational limits.
- Do not add paid services, Redis, replicas, queues, Kubernetes, microservices, or
  multiple regions without explicit approval and measured need.

## Quality

- Keep business logic outside transport/UI handlers and make it unit-testable.
- Match established project patterns instead of introducing duplicate approaches.
- Run formatting, linting, tests, and migration checks before opening a pull request.
- Keep pull requests focused and document acceptance criteria, tests, assumptions,
  migration impact, security impact, and manual test steps.
