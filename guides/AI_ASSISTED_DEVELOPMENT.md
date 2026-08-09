# AI-assisted development

Sacmia developers may use Claude, Codex, or another approved coding assistant.
The developer remains responsible for requirements, code, tests, security, and the
pull request. An AI-generated change is not automatically correct.

## Before asking the assistant to code

1. Start from the latest `development` branch and create the assigned feature branch.
2. Confirm that the work has acceptance criteria or an approved feature document.
3. Read the repository's `CLAUDE.md`, developer workflow, and relevant feature docs.
4. Check `git status` so unrelated local changes are not included.

Use a planning request first:

```text
Read CLAUDE.md, the developer workflow, the relevant feature specification, and
their linked documents fully. Do not write code yet. Inspect existing patterns,
propose a focused implementation and test plan, and list conflicts or unanswered
product questions. Do not invent unspecified behaviour.
```

Resolve important questions with the product owner or team lead before implementation.

## Ask for a complete, reviewable change

After the plan is approved, use a request such as:

```text
Implement the approved plan on the current feature branch. Follow existing project
patterns. Add tests for the acceptance criteria and migrations when required. Run
the documented checks and report their results, manual test steps, assumptions, and
remaining risks. Do not merge the pull request.
```

Keep one feature or fix in each session and pull request. Review tool requests before
approving them, especially changes involving dependencies, databases, cloud resources,
domains, deployments, or destructive commands.

## Information that must not be shared

Never paste passwords, tokens, private keys, connection strings, production data,
customer data, or confidential documents into an AI prompt. Use safe placeholders.
Do not give a coding assistant production, cloud-administrator, DNS, or secret-manager
access unless a responsible owner explicitly approves a necessary task.

## Before opening a pull request

- Inspect `git status` and the complete diff yourself.
- Confirm the change matches every acceptance criterion and contains no unrelated work.
- Run formatting, linting, tests, and migration checks documented by the repository.
- Manually test success, validation, authorization, and important failure paths.
- Check for secrets, unsafe logs, unnecessary dependencies, and generated artifacts.
- Write accurate PR notes; do not claim a check passed unless you saw it pass.

An assistant may draft code, tests, documentation, and a pull request. It must not
approve or merge its own work. A human reviewer and passing CI are required.

## Stop and ask for help when

- expected behaviour is missing or contradictory;
- the assistant proposes broad rewrites or unrelated changes;
- tests are removed, weakened, skipped, or written to confirm incorrect behaviour;
- credentials are hard-coded or sensitive data appears in logs;
- a destructive migration or production change is proposed; or
- the assistant says work is complete without showing verification evidence.

For more examples of using Codex to understand, build, test, and review software, see
the [official OpenAI developer guidance](https://developers.openai.com/).
