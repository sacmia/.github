# SACMIA GitHub defaults

This public repository provides GitHub-specific organization defaults: community
health files, issue and pull-request templates, reusable workflows, workflow templates,
and the public organization profile.

It is **not** an engineering-policy source. The private
[`sacmia-engineering`](https://github.com/sacmia/sacmia-engineering) repository is the
single source of truth for SACMIA engineering governance, architecture profiles,
standards, ADRs, and repository templates. Authorized collaborators should start there
and then follow the local instructions in the repository they are changing.

## Contents

| Path | Purpose |
| --- | --- |
| [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/) | Organization-default issue forms |
| [`.github/workflow-templates/`](.github/workflow-templates/) | Starter callers for approved reusable CI |
| [`.github/workflows/`](.github/workflows/) | Reusable FastAPI and Flutter CI mechanisms |
| [`PULL_REQUEST_TEMPLATE.md`](PULL_REQUEST_TEMPLATE.md) | Profile-neutral pull-request checklist |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Concise public contribution defaults |
| [`SECURITY.md`](SECURITY.md) | Private vulnerability-reporting instructions |
| [`profile/README.md`](profile/README.md) | Public organization profile |
| [`sacmia.yml`](sacmia.yml) | Engineering v1.1.0 adoption metadata and checks |

## How organization defaults work

Repositories without local overrides can inherit this repository's pull-request
template, issue templates, `CONTRIBUTING.md`, and `SECURITY.md` through GitHub.

`AGENTS.md`, `CLAUDE.md`, `sacmia.yml`, application scaffolding, CI caller files,
deployment configuration, branch policy, architecture, and product requirements remain
repository-specific. A local file overrides an organization default where GitHub
supports inheritance.

This repository MUST link to the engineering standard instead of duplicating it. Do not
copy passwords, tokens, customer data, private architecture, or product-specific
confidential information into this public repository.
