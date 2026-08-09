# AI-assisted development

Sacmia developers may use any AI coding assistant approved by Sacmia. Claude and
Codex are examples, not requirements. These rules apply equally to every AI tool.
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

## Required workflow: one feature, one AI session

Use this rule for every approved AI coding assistant, regardless of product or vendor:

```text
One feature or fix -> one branch -> one dedicated AI session -> one pull request
```

- Start a fresh AI session after creating or switching to the assigned branch.
- Ask the assistant to read the current repository documentation before planning or
  changing files. Repository documentation and the current branch are the source of
  truth, not memories from an earlier session.
- Keep planning, implementation, tests, documentation, and pull-request creation for
  that feature in its dedicated session.
- Continue review feedback and fixes in the same session while that pull request is
  open.
- Start a new session for a different feature, branch, or pull request. Do not combine
  unrelated work to save time.

If a session is lost, becomes unreliable, or grows too large, a replacement session
may continue the same branch and pull request. Before acting, it must re-read the
repository instructions, inspect the branch status and complete diff, read the pull
request and review comments, and restate the remaining scope.

This keeps requirements and changes traceable, reduces confusion from outdated
decisions, and makes it easier for another developer to continue the work safely.

### Copyable prompt to start a feature

Replace the text inside `<angle brackets>`, then paste this as the first message in a
new session, task, thread, or chat in the approved AI coding assistant being used.
This guide uses **AI session** as the common name for all of those terms.

```text
You are helping me work on <FEATURE OR FIX NAME> in the <REPOSITORY NAME> repository.
Repository path: <LOCAL REPOSITORY PATH>
Required branch: <feat/... OR fix/...>
Pull-request target: development

Before changing any file:
1. Confirm the repository path, current branch, and git status. Stop if the branch is
   wrong or if unrelated changes could be overwritten.
2. Read the current Sacmia engineering standards and AI-assisted development guide:
   - https://github.com/sacmia/.github/blob/main/SACMIA_ENGINEERING_STANDARDS.md
   - https://github.com/sacmia/.github/blob/main/guides/AI_ASSISTED_DEVELOPMENT.md
   If you cannot access them, tell me before continuing.
3. Read this repository's README.md, CLAUDE.md, CONTRIBUTING.md, developer workflow,
   architecture documents, feature specification, acceptance criteria, and every
   relevant document linked from them. If a named file does not exist, say so.
4. Treat the current organization standards and repository documentation as the source
   of truth. Project rules may be stricter, but must not weaken Sacmia security, review,
   branch, or release rules.
5. Inspect the existing code and tests for established patterns.

Do not implement anything yet. Give me:
- your understanding of the requested scope and acceptance criteria;
- conflicts, missing decisions, assumptions, or security concerns;
- a focused implementation and test plan;
- the files and migrations likely to change; and
- the validation and manual testing you will perform.

Do not invent requirements, expose credentials, include unrelated changes, merge a
pull request, or push directly to development or main. Wait for my approval after
showing the plan.
```

For a brand-new repository, its owner or administrator must first follow the
[new repository guide](../NEW_REPOSITORY_GUIDE.md) and create the baseline project
documentation. Developers should use the prompt above only after the repository is
ready and a feature with acceptance criteria has been assigned.

### Example

A developer is assigned **Admin: create a test shell**.

1. The developer updates `development` and creates `feat/admin-create-test-shell`.
2. They start a new session in their approved AI coding assistant and give it the
   repository path.
3. They ask it to read `CLAUDE.md`, the developer workflow, architecture documents,
   and the feature specification before proposing a plan.
4. After the plan is approved, they use that session to implement and test only the
   test-shell feature and open one pull request into `development`.
5. A reviewer requests another authorization test. They return to the same session
   because the request belongs to the same pull request.
6. Their next assignment is **Candidate registration**. They create a different branch
   and start a new AI session; they do not continue in the test-shell session.

If the original session becomes unavailable during step 5, they may start a replacement
session on the same branch with this request:

```text
Continue the open pull request for this branch. Before changing anything, read the
repository instructions and relevant feature documents, inspect git status and the
complete branch diff, and read the pull request and all review comments. Summarize
the implemented scope and remaining review work, then wait for my approval.
```

## Ask for a complete, reviewable change

After the plan is approved, use a request such as:

```text
Implement the approved plan on the current feature branch. Follow existing project
patterns. Add tests for the acceptance criteria and migrations when required. Run
the documented checks and report their results, manual test steps, assumptions, and
remaining risks. Do not merge the pull request.
```

Review tool requests before approving them, especially changes involving dependencies,
databases, cloud resources, domains, deployments, or destructive commands.

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

Also follow the official documentation for the approved AI tool being used, but never
use tool-specific guidance to weaken Sacmia or project rules.
