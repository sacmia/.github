# Create a new Sacmia FastAPI repository

Use this checklist whenever an administrator creates a FastAPI repository. Do not
start from a blank repository; the Sacmia template supplies Claude instructions,
Docker, CI, tests, security rules, and the standard branch workflow.

## GitHub website steps

1. Open [`sacmia/template-fastapi`](https://github.com/sacmia/template-fastapi).
2. Select **Use this template** → **Create a new repository**.
3. Set **Owner** to `sacmia`.
4. Enter the approved repository name and description.
5. Select **Private** unless the project owner explicitly approves public visibility.
6. Select **Include all branches**. This copies both `main` and `development`.
7. Select **Create repository**.

## Initial project setup

```bash
gh repo clone sacmia/REPOSITORY_NAME
cd REPOSITORY_NAME
git switch development
git pull origin development
git switch -c docs/project-setup
```

Replace project placeholders in:

- `README.md`
- `CLAUDE.md`
- `docs/PROJECT_DECISIONS.md`
- `.env.example`

Never place real credentials in these files. Add runtime credentials later through
GitHub **Settings → Secrets and variables → Actions**.

Commit the project setup and open a pull request into `development`:

```bash
git add .
git commit -m "Configure project documentation and Claude instructions"
git push -u origin docs/project-setup
gh pr create --base development
```

Another team member reviews and merges the pull request. Coding agents must not merge
their own pull requests.

## Administrator verification checklist

- [ ] Repository was created from `sacmia/template-fastapi`
- [ ] Visibility is correct
- [ ] `main` and `development` branches exist
- [ ] Default branch remains `main` (production)
- [ ] Feature pull requests target `development`
- [ ] CI appears under the **Actions** tab and passes on `development`
- [ ] `CLAUDE.md` placeholders are replaced
- [ ] No credentials or customer data were committed
- [ ] Human reviewer access is configured

## If `development` was not copied

If **Include all branches** was missed, create `development` from `main` before any
feature work:

```bash
git clone https://github.com/sacmia/REPOSITORY_NAME.git
cd REPOSITORY_NAME
git switch -c development
git push -u origin development
```

## Standard lifecycle

```text
feat/*, fix/*, docs/* → pull request → development → release pull request → main
```

`main` represents production. Merging `development` into `main` is an intentional
release step performed by the team.

