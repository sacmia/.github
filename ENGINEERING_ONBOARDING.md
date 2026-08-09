# Sacmia engineering onboarding

Send this page to every new developer. Complete the checklist with a team lead
before starting project work.

## Read in this order

1. This onboarding page.
2. [Sacmia engineering standards](SACMIA_ENGINEERING_STANDARDS.md).
3. [Security for developers](guides/SECURITY_FOR_DEVELOPERS.md).
4. [Contributing and Git workflow](CONTRIBUTING.md).
5. [AI-assisted development](guides/AI_ASSISTED_DEVELOPMENT.md).
6. [Code review and testing](guides/CODE_REVIEW_AND_TESTING.md).
7. The relevant technology guide: [FastAPI](guides/FASTAPI.md) or
   [Flutter](guides/FLUTTER.md).
8. The assigned project's `README.md`, `CLAUDE.md`, developer workflow, and
   feature specification.

## First-week checklist

### Access and security

- [ ] Use the company email account where one has been provided.
- [ ] Enable two-factor authentication on GitHub and other company accounts.
- [ ] Store credentials in the approved password manager, never in documentation.
- [ ] Confirm access only to the repositories and development systems needed.
- [ ] Join the team's approved communication and task-management tools.

New developers should not receive production access unless their role requires it
and a responsible owner approves it.

### Local setup

- [ ] Install Git, the GitHub CLI, an approved editor, and the required SDKs.
- [ ] Clone the assigned repository.
- [ ] Follow its local setup instructions without sharing secrets.
- [ ] Run the application and its automated checks locally.
- [ ] Ask a team member about any undocumented or failing step.

### Practice workflow

- [ ] Start from the latest `development` branch.
- [ ] Create a small `docs/`, `test/`, `feat/`, or `fix/` branch as assigned.
- [ ] Start a fresh, dedicated AI session for that branch and pull request.
- [ ] Make a focused change with AI assistance if useful.
- [ ] Review the complete diff and run the documented checks.
- [ ] Open a pull request into `development` and complete its template.
- [ ] Address review comments in the same AI session without resolving another
      person's comment silently.
- [ ] Review and manually test another safe development change with guidance.

## Ready for project work

A team lead should confirm that the developer can:

- explain the `feature branch -> development -> main` workflow;
- run the project and tests locally;
- use AI without sharing secrets or accepting changes blindly;
- open and review a focused pull request;
- distinguish local, development, and production environments; and
- report a security concern or exposed credential immediately.

Record completion in the company's approved onboarding tracker. Do not record
passwords, tokens, connection strings, or other secrets there.
