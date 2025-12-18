import os
from unittest.mock import patch, Mock

import pytest

from scripts import backup_dashboards


def test_fetch_dashboards_headers(monkeypatch):
    monkeypatch.setenv("GRAFANA_API_KEY", "testkey")
    monkeypatch.setenv("GRAFANA_URL", "http://test")
    mock_resp = Mock()
    mock_resp.json.return_value = [{"title": "d"}]
    mock_resp.raise_for_status = lambda: None
    with patch("scripts.backup_dashboards.requests.get", return_value=mock_resp) as mock_get:
        res = backup_dashboards.fetch_dashboards()
        mock_get.assert_called_once()
        assert res == [{"title": "d"}]
