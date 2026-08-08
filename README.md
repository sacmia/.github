# Sacmia organization standards

This public repository provides safe organization-wide GitHub defaults and reusable
CI workflows. It must never contain credentials, customer data, private architecture,
or project-specific business rules.

## What is inherited automatically

Repositories without local overrides can use the pull-request template, issue
templates, `CONTRIBUTING.md`, and `SECURITY.md` from this repository.

## What is not inherited automatically

`CLAUDE.md`, application scaffolding, CI caller files, deployment configuration, and
branch protection are repository-specific. Create new FastAPI repositories from
`sacmia/template-fastapi`, then fill in the project-specific sections.

Shared engineering rules live in `SACMIA_ENGINEERING_STANDARDS.md`. Stack templates
copy these rules so coding agents can read them locally. When the common standard
changes materially, update active repositories through reviewed pull requests.

## Administrator runbooks

- [Create a new Sacmia FastAPI repository](NEW_FASTAPI_REPOSITORY_GUIDE.md)
