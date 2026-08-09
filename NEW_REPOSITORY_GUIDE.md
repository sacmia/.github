# Create a new Sacmia repository

This is the common administrator checklist for every Sacmia technology. Follow it
first, then follow the relevant technology guide.

## Common steps

1. Confirm the approved project name, repository name, owner, visibility, and technical
   stack with the project owner.
2. Open the matching `sacmia/template-*` repository and select **Use this template** →
   **Create a new repository**. Do not start from a blank repository.
3. Set **Owner** to `sacmia` and select **Private** unless public visibility is
   explicitly approved.
4. Select **Include all branches** so `main` and `development` are copied.
5. Clone the repository, switch to `development`, and create `docs/project-setup`.
6. Replace all template placeholders in `README.md`, `CLAUDE.md`, environment examples,
   and project-decision documentation.
7. Add complete local-development instructions: prerequisites and versions, environment
   setup, dependency services, migrations, sample data, run/stop commands, ports, tests,
   linting, builds, and common errors.
8. Record the approved application technology and database. The local environment must
   use the same database engine and a compatible major version.
9. Decide whether Docker is required. Prefer Docker Compose for databases and related
   backend dependencies; document a native workflow when Docker is not appropriate.
10. Never commit credentials or customer data. Add runtime values through GitHub
   **Settings → Secrets and variables → Actions** when deployment is configured.
11. Run the stack's required local checks and open a pull request into `development`.
12. Another team member reviews and tests. Coding agents do not merge their own PRs.
13. Use `development → main` only as an intentional production release.

## Required repository settings

- Keep `main` as the production and default branch.
- Keep the long-lived `development` branch available for feature integration.
- Do not enable automatic deletion of pull-request head branches when release pull
  requests use `development` as the head; GitHub may delete `development` after merge.
- Require pull requests, human review, and passing CI where the organization plan
  supports those controls. Otherwise enforce the same workflow through review policy.
- Grant the minimum repository role each person needs.
- Configure environments and secrets separately for development and production.

## Common verification checklist

- [ ] Correct Sacmia template was used
- [ ] Repository name, description, visibility, and access are correct
- [ ] Both `main` and `development` exist; `main` remains the production branch
- [ ] Template placeholders are replaced
- [ ] CI passes on `development`
- [ ] No secrets or customer data were committed
- [ ] Reviewers have access
- [ ] Environment and deployment details are documented without secret values
- [ ] Local setup, run, stop, migration, test, and build commands are complete
- [ ] Database engine/version and isolated test-database rules are documented
- [ ] Docker usage or the approved native alternative is documented
- [ ] Automatic head-branch deletion cannot remove `development`

## Technology guides

- [FastAPI](guides/FASTAPI.md)
- [Flutter](guides/FLUTTER.md)

## Standard lifecycle

```text
feat/*, fix/*, docs/* → pull request → development → release pull request → main
```
