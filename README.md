# Sacmia engineering handbook

This is the home page for Sacmia's organization-wide engineering standards and
developer guides. Send this page to new developers so they can find the current
process from one place.

> [New developer? Start with the engineering onboarding guide.](ENGINEERING_ONBOARDING.md)

## Find the right guide

| I need to... | Follow this guide |
| --- | --- |
| Join Sacmia as a developer | [Engineering onboarding](ENGINEERING_ONBOARDING.md) |
| Join a project or start a feature | [Developer start steps](guides/AI_ASSISTED_DEVELOPMENT.md#start-here-steps-for-developers) |
| Start an AI-assisted feature session | [Copyable feature-start prompt](guides/AI_ASSISTED_DEVELOPMENT.md#copyable-prompt-to-start-a-feature) |
| Develop with any approved AI tool | [AI-assisted development](guides/AI_ASSISTED_DEVELOPMENT.md) |
| Create user flows, UX/UI specifications, or mockups | [Product design and mockups](guides/PRODUCT_DESIGN_AND_MOCKUPS.md) |
| Review a pull request or test a change | [Code review and testing](guides/CODE_REVIEW_AND_TESTING.md) |
| Work securely or handle credentials | [Security for developers](guides/SECURITY_FOR_DEVELOPERS.md) |
| Work on a FastAPI repository | [FastAPI guide](guides/FASTAPI.md) |
| Work on a Flutter repository | [Flutter guide](guides/FLUTTER.md) |
| Create or administer a repository | [New repository guide](NEW_REPOSITORY_GUIDE.md) |
| Report a security vulnerability | [Security policy](SECURITY.md) |

## Daily development workflow

Every feature or fix follows this path:

```text
assigned work -> feature branch -> dedicated AI session -> local tests
-> pull request to development -> human review and testing -> development server
-> intentional production release to main
```

Start with the detailed
[project and feature steps](guides/AI_ASSISTED_DEVELOPMENT.md#start-here-steps-for-developers).
The essential rule is:

```text
One feature or fix -> one branch -> one dedicated AI session -> one pull request
```

## Core standards

- [Sacmia engineering standards](SACMIA_ENGINEERING_STANDARDS.md)
- [Contributing and Git workflow](CONTRIBUTING.md)
- [Pull-request template](PULL_REQUEST_TEMPLATE.md)
- [Security policy](SECURITY.md)

Project documentation may add stricter requirements but must not weaken these common
security, review, branch, or release rules.

## Repository owners and administrators

Repository creation and administration are not normal feature-development duties.
Assigned owners or administrators should follow the
[new repository guide](NEW_REPOSITORY_GUIDE.md). New FastAPI repositories should be
created from `sacmia/template-fastapi`; other approved stack templates should be used
when available.

## How organization defaults work

Repositories without local overrides can inherit this repository's pull-request
template, issue templates, `CONTRIBUTING.md`, and `SECURITY.md` through GitHub.

`CLAUDE.md`, application scaffolding, CI caller files, deployment configuration,
branch protection, architecture, and product requirements remain repository-specific.
Shared engineering rules should also be available inside active repositories so any
approved AI coding assistant can read them locally.

When a common standard changes materially, update active repositories through reviewed
pull requests. Do not copy passwords, tokens, customer data, private architecture, or
project-specific confidential information into this public repository.
