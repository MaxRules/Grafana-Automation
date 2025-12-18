# Grafana Automation

Simple starter workspace for Grafana automation tasks (dashboards backup/restore, provisioning helpers).

Defaults used:
- Python 3.11 + Poetry
- Dockerfile included
- GitHub Actions CI
- MIT license

Quick start

1. Install dependencies: `poetry install`
2. Set your Grafana env vars:
   - `GRAFANA_URL` (default: http://localhost:3000)
   - `GRAFANA_API_KEY`
3. Run sample script:

```bash
python scripts/backup_dashboards.py
```

Developing

- Run tests: `poetry run pytest -q`
- Lint: `poetry run flake8`

Contributing

Open an issue or PR with suggested improvements.

Badges

- CI: ![CI](https://github.com/MaxRules/Grafana-Automation/actions/workflows/ci.yml/badge.svg)
- Packages: ![Package](https://github.com/MaxRules/Grafana-Automation/packages)

Docs

See `docs/AUTH.md` and `docs/PROVISIONING.md` for notes about authentication and provisioning examples.

---

## Usage examples ✅

### Run the backup script

Export your Grafana credentials and run the example backup script locally:

```bash
export GRAFANA_URL=http://localhost:3000
export GRAFANA_API_KEY="<your_api_key>"
python scripts/backup_dashboards.py
```

(On Windows PowerShell use `setx GRAFANA_API_KEY "<your_api_key>"` or `$env:GRAFANA_API_KEY = "<your_api_key>"` for the session.)

### Docker Compose (local dev)

Start Grafana and the helper app together with Docker Compose:

```bash
# Provide GRAFANA_API_KEY via environment (or in a .env file)
docker-compose up -d --build
# Tail logs
docker-compose logs -f
```

The `app` service will use the `GRAFANA_URL` `http://grafana:3000` and `GRAFANA_API_KEY` from the environment.

### Makefile targets (shortcuts)

- `make install` — install project dependencies via Poetry
- `make test` — run `pytest`
- `make lint` — run `flake8`
- `make build` — build the local Docker image (`grafana-automation:local`)
- `make compose-up` — `docker-compose up -d --build`
- `make compose-down` — `docker-compose down`

Use these for local development and quick iteration.

---

## CI & Publishing ⚙️

This repository contains two GitHub Actions workflows:

- `.github/workflows/ci.yml` — runs on pushes/PRs to `main`, installs dependencies, runs tests and lints the code.
- `.github/workflows/publish.yml` — builds and publishes a multi-platform Docker image to GitHub Container Registry (GHCR) on pushes to `main` or when a tag `v*` is pushed.

Publishing notes:
- The publish workflow uses the repository's `GITHUB_TOKEN` by default to authenticate against `ghcr.io`.
- If you prefer Docker Hub or another registry, provide a `REGISTRY_PAT` secret and update the workflow accordingly.

**Secrets (you will configure these later)**
- `GRAFANA_API_KEY` — required for any workflow that interacts with Grafana APIs (backups, provisioning)
- `REGISTRY_PAT` — optional personal access token for non-GHCR registries

Add secrets in the repository Settings → Secrets & variables → Actions or with the GitHub CLI:

```bash
# example (requires gh CLI login):
gh secret set GRAFANA_API_KEY --body "<your_key>"
gh secret set REGISTRY_PAT --body "<your_registry_pat>"
```

> Note: I will not add or change repository secrets for you — configure them when ready.

---

## Pushing & setup to GitHub 📤

If you haven't yet added a remote, use:

```bash
git remote add origin https://github.com/<owner>/<repo>.git
git branch -M main
git push -u origin main
```

You already pushed this repository to `https://github.com/MaxRules/Grafana-Automation.git`.

---

## Files of interest 🗂️

- `scripts/backup_dashboards.py` — example backup script
- `tests/` — unit tests (run with `pytest`)
- `Dockerfile` — builds the `grafana-automation` image
- `docker-compose.yml` — local dev stack
- `Makefile` — helper targets (`install`, `test`, `lint`, `build`, `compose-up`)
- `.github/workflows/ci.yml` and `.github/workflows/publish.yml` — CI and publish workflows
- `docs/AUTH.md`, `docs/PROVISIONING.md` — auth and provisioning guidance

---

## Contributing

Contributions welcome — open an issue or PR with suggested improvements.
