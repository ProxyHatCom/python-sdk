from __future__ import annotations

from typing import TYPE_CHECKING, Any

from proxyhat.types.analytics import DomainBreakdownResponse, TimeSeriesResponse, TotalResponse

if TYPE_CHECKING:
    from proxyhat.async_client import AsyncProxyHat
    from proxyhat.client import ProxyHat


def _analytics_body(
    period: str = "24h",
    start_date: str | None = None,
    end_date: str | None = None,
) -> dict[str, Any]:
    body: dict[str, Any] = {"period": period}
    body["start_date"] = start_date
    body["end_date"] = end_date
    return body


class AnalyticsResource:
    def __init__(self, client: ProxyHat) -> None:
        self._client = client

    def traffic(
        self,
        *,
        period: str = "24h",
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> TimeSeriesResponse:
        body = _analytics_body(period, start_date, end_date)
        data = self._client.request("POST", "/traffic", json=body)
        return TimeSeriesResponse.from_dict(data)

    def traffic_total(
        self,
        *,
        period: str = "24h",
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> TotalResponse:
        body = _analytics_body(period, start_date, end_date)
        data = self._client.request("POST", "/traffic/period-total", json=body)
        return TotalResponse.from_dict(data)

    def requests(
        self,
        *,
        period: str = "24h",
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> TimeSeriesResponse:
        body = _analytics_body(period, start_date, end_date)
        data = self._client.request("POST", "/requests", json=body)
        return TimeSeriesResponse.from_dict(data)

    def requests_total(
        self,
        *,
        period: str = "24h",
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> TotalResponse:
        body = _analytics_body(period, start_date, end_date)
        data = self._client.request("POST", "/requests/period-total", json=body)
        return TotalResponse.from_dict(data)

    def domain_breakdown(
        self,
        *,
        period: str = "24h",
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> DomainBreakdownResponse:
        body = _analytics_body(period, start_date, end_date)
        data = self._client.request("POST", "/domain-breakdown", json=body)
        return DomainBreakdownResponse.from_dict(data)


class AsyncAnalyticsResource:
    def __init__(self, client: AsyncProxyHat) -> None:
        self._client = client

    async def traffic(
        self,
        *,
        period: str = "24h",
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> TimeSeriesResponse:
        body = _analytics_body(period, start_date, end_date)
        data = await self._client.request("POST", "/traffic", json=body)
        return TimeSeriesResponse.from_dict(data)

    async def traffic_total(
        self,
        *,
        period: str = "24h",
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> TotalResponse:
        body = _analytics_body(period, start_date, end_date)
        data = await self._client.request("POST", "/traffic/period-total", json=body)
        return TotalResponse.from_dict(data)

    async def requests(
        self,
        *,
        period: str = "24h",
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> TimeSeriesResponse:
        body = _analytics_body(period, start_date, end_date)
        data = await self._client.request("POST", "/requests", json=body)
        return TimeSeriesResponse.from_dict(data)

    async def requests_total(
        self,
        *,
        period: str = "24h",
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> TotalResponse:
        body = _analytics_body(period, start_date, end_date)
        data = await self._client.request("POST", "/requests/period-total", json=body)
        return TotalResponse.from_dict(data)

    async def domain_breakdown(
        self,
        *,
        period: str = "24h",
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> DomainBreakdownResponse:
        body = _analytics_body(period, start_date, end_date)
        data = await self._client.request("POST", "/domain-breakdown", json=body)
        return DomainBreakdownResponse.from_dict(data)
