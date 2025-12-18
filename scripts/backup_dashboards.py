#!/usr/bin/env python3
"""Simple Grafana backup helper (example).

Reads `GRAFANA_URL` and `GRAFANA_API_KEY` from environment and lists dashboards.
"""

import os
import argparse
from typing import Optional

import requests

GRAFANA_URL = os.environ.get("GRAFANA_URL", "http://localhost:3000")


def fetch_dashboards(folder: Optional[str] = None):
    """Fetch dashboards via Grafana search API.

    Raises RuntimeError if API key missing.
    """
    api_key = os.environ.get("GRAFANA_API_KEY")
    if not api_key:
        raise RuntimeError("GRAFANA_API_KEY not set")
    headers = {"Authorization": f"Bearer {api_key}"}
    params = {}
    if folder:
        params["folderIds"] = folder
    resp = requests.get(f"{GRAFANA_URL}/api/search", headers=headers, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", help="Folder ID to filter dashboards")
    args = parser.parse_args()
    dashboards = fetch_dashboards(args.folder)
    for d in dashboards:
        print(d)


if __name__ == "__main__":
    main()
