# Authentication & Secrets 🔐

This document explains recommended ways to authenticate to Grafana for automation.

Environment variables
- GRAFANA_URL — e.g. `http://localhost:3000` (default)
- GRAFANA_API_KEY — Grafana API Key with **Viewer** or **Editor** scope depending on actions

Creating an API key
1. In Grafana: Configuration → API Keys → Add API Key
2. Select a name and minimum required role (Viewer/Editor/Admin)
3. Store the key securely; you won't be able to view it again

Security best practices
- Use least-privilege API keys (Viewer for read-only backups, Editor if you create/update dashboards)
- Store secrets in GitHub Actions secrets, Azure Key Vault, or a Kubernetes Secret

GitHub Actions example
- Add a repository secret named `GRAFANA_API_KEY`
- Reference it in workflows:
  - name: Run backup
    env:
      GRAFANA_API_KEY: ${{ secrets.GRAFANA_API_KEY }}

Curl example
curl -H "Authorization: Bearer $GRAFANA_API_KEY" "$GRAFANA_URL/api/search"
