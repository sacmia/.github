# Create a Sacmia FastAPI repository

Follow the [common repository guide](../NEW_REPOSITORY_GUIDE.md), using
[`sacmia/template-fastapi`](https://github.com/sacmia/template-fastapi).

## Setup

```bash
gh repo clone sacmia/REPOSITORY_NAME
cd REPOSITORY_NAME
git switch development
git pull origin development
git switch -c docs/project-setup
```

Replace project placeholders in `README.md`, `CLAUDE.md`,
`docs/PROJECT_DECISIONS.md`, and `.env.example`.

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
git commit -m "Configure project documentation and Claude instructions"
git push -u origin docs/project-setup
gh pr create --base development
```

## FastAPI verification

- [ ] `/health` works locally
- [ ] Ruff and pytest pass
- [ ] CI uses the shared Sacmia FastAPI workflow
- [ ] Database migrations are enabled in CI when the project adds persistence
- [ ] Docker image builds when deployment is introduced

