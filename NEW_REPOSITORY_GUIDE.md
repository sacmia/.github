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
7. Never commit credentials or customer data. Add runtime values through GitHub
   **Settings → Secrets and variables → Actions** when deployment is configured.
8. Run the stack's required local checks and open a pull request into `development`.
9. Another team member reviews and tests. Coding agents do not merge their own PRs.
10. Use `development → main` only as an intentional production release.

## Common verification checklist

- [ ] Correct Sacmia template was used
- [ ] Repository name, description, visibility, and access are correct
- [ ] Both `main` and `development` exist; `main` remains the production branch
- [ ] Template placeholders are replaced
- [ ] CI passes on `development`
- [ ] No secrets or customer data were committed
- [ ] Reviewers have access
- [ ] Environment and deployment details are documented without secret values

## Technology guides

- [FastAPI](guides/FASTAPI.md)
- [Flutter](guides/FLUTTER.md)

## Standard lifecycle

```text
feat/*, fix/*, docs/* → pull request → development → release pull request → main
```

