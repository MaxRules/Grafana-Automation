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
