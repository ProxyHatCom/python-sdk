import httpx

from proxyhat import ProxyHat
from proxyhat.types.analytics import DomainBreakdownResponse, TimeSeriesResponse, TotalResponse


class TestAnalyticsSync:
    def test_traffic(self, client: ProxyHat, mock_api):
        mock_api.post("/traffic").mock(
            return_value=httpx.Response(
                200,
                json={
                    "success": True,
                    "payload": {
                        "labels": ["2026-01-14", "2026-01-15"],
                        "data": [1073741824, 2147483648],
                    },
                },
            )
        )
        result = client.analytics.traffic(period="7d")
        assert isinstance(result, TimeSeriesResponse)
        assert len(result.labels) == 2
        assert result.data[0] == 1073741824

    def test_traffic_total(self, client: ProxyHat, mock_api):
        mock_api.post("/traffic/period-total").mock(
            return_value=httpx.Response(
                200,
                json={"success": True, "payload": {"total": 3221225472}},
            )
        )
        result = client.analytics.traffic_total(period="30d")
        assert isinstance(result, TotalResponse)
        assert result.total == 3221225472

    def test_requests(self, client: ProxyHat, mock_api):
        mock_api.post("/requests").mock(
            return_value=httpx.Response(
                200,
                json={
                    "success": True,
                    "payload": {
                        "labels": ["2026-01-14"],
                        "data": [50000],
                    },
                },
            )
        )
        result = client.analytics.requests(period="24h")
        assert isinstance(result, TimeSeriesResponse)

    def test_domain_breakdown(self, client: ProxyHat, mock_api):
        mock_api.post("/domain-breakdown").mock(
            return_value=httpx.Response(
                200,
                json={
                    "success": True,
                    "payload": {
                        "items": [
                            {"domain": "example.com", "bandwidth": 1073741824, "requests": 15000},
                        ]
                    },
                },
            )
        )
        result = client.analytics.domain_breakdown(period="7d")
        assert isinstance(result, DomainBreakdownResponse)
        assert len(result.items) == 1
        assert result.items[0].domain == "example.com"
