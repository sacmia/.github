# Create a Sacmia FastAPI repository

Follow the [common repository guide](../NEW_REPOSITORY_GUIDE.md), using
[`sacmia/template-fastapi`](https://github.com/sacmia/template-fastapi).

## Setup

```bash
gh repo clone sacmia/REPOSITORY_NAME
cd REPOSITORY_NAME
git switch development
git pull --ff-only origin development
git switch -c docs/project-setup
```

Replace project placeholders in `README.md`, `AGENTS.md`, `CLAUDE.md`,
`docs/developer-workflow.md`, `docs/PROJECT_DECISIONS.md`, and `.env.example`.

The project developer workflow must cover macOS/Linux and Windows commands when the
team uses those systems, plus the project-specific AI start prompt and review checklist.

Run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
ruff check .
pytest
```

When persistence is added, initialize SQLAlchemy and Alembic, test against PostgreSQL,
and set `run-migrations: true` in `.github/workflows/ci.yml`.

```bash
git add .
git commit -m "Configure project documentation and AI instructions"
git push -u origin docs/project-setup
gh pr create --base development
```

## FastAPI verification

- [ ] `/health` works locally
- [ ] Ruff and pytest pass
- [ ] `AGENTS.md` and the project developer workflow route all approved AI tools to
      the same plan-before-code and human-review process
- [ ] Local setup is documented for every operating system used by the team
- [ ] CI uses the shared Sacmia FastAPI workflow
- [ ] Database migrations are enabled in CI when the project adds persistence
- [ ] Docker image builds when deployment is introduced
