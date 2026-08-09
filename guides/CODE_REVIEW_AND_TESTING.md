# Code review and testing

Human review and testing are required even when AI produced the code and CI passed.
The author owns the change; the reviewer owns the approval decision.

## Author checklist

Before requesting review:

- Re-read the acceptance criteria and inspect the complete diff.
- Remove unrelated changes, debugging code, unsafe logs, and generated files.
- Add or update automated tests for success, validation, authorization, and failures.
- Run the repository's formatting, linting, tests, and migration checks locally.
- Manually test through the repository's documented interface.
- Complete the PR description with test evidence, assumptions, migrations, security
  impact, and clear reviewer steps.

For APIs, use the generated Swagger/OpenAPI interface for normal manual checks.
Postman or Insomnia may be used when saved requests, environment variables, or repeated
test sequences are useful. Manual API checks do not replace automated tests.

## Reviewer checklist

Review in this order:

1. Read the feature document and acceptance criteria.
2. Confirm the PR is focused and targets `development`.
3. Inspect the implementation, tests, migrations, dependencies, and configuration.
4. Check authentication, role permissions, validation, error handling, and data exposure.
5. Confirm API responses use intended schemas and do not leak internal or answer data.
6. Look for unsafe database queries, missing indexes, unbounded lists, and retry problems.
7. Confirm CI passed, then run proportionate local and manual tests yourself.
8. Approve only when the behaviour and evidence are clear.

AI can produce convincing but incorrect code and tests. Check that tests assert the
required product behaviour rather than merely matching the implementation.

## Useful review feedback

Make each comment specific and actionable. State:

- what can fail or violate a requirement;
- where it occurs;
- the expected behaviour; and
- a reproducible example when helpful.

Use **Request changes** for issues that must be fixed before merge. Use **Comment**
for non-blocking suggestions. Authors should reply to feedback and let the reviewer
resolve the discussion after verifying the update.

## After merge to development

Test the deployed development version using safe development accounts and data.
Verify the feature's main flow, permissions, validation, and regression-sensitive
areas. Record the result on the PR or approved test tracker.

If a problem is found, create a focused fix branch from the latest `development`.
Do not patch `development` or `main` directly. Promotion from `development` to `main`
is a separate production release decision.
