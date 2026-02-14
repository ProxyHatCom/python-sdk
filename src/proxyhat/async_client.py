from __future__ import annotations

from typing import Any

import httpx

from proxyhat._base_client import DEFAULT_BASE_URL, DEFAULT_TIMEOUT, BaseClientConfig, _parse_json_body
from proxyhat.resources.analytics import AsyncAnalyticsResource
from proxyhat.resources.auth import AsyncAuthResource
from proxyhat.resources.coupons import AsyncCouponsResource
from proxyhat.resources.email import AsyncEmailResource
from proxyhat.resources.locations import AsyncLocationsResource
from proxyhat.resources.payments import AsyncPaymentsResource
from proxyhat.resources.plans import AsyncPlansResource
from proxyhat.resources.profile import AsyncProfileResource
from proxyhat.resources.proxy_presets import AsyncProxyPresetsResource
from proxyhat.resources.sub_user_groups import AsyncSubUserGroupsResource
from proxyhat.resources.sub_users import AsyncSubUsersResource
from proxyhat.resources.two_factor import AsyncTwoFactorResource


class AsyncProxyHat:
    """Asynchronous client for the ProxyHat API."""

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> None:
        self._config = BaseClientConfig(api_key=api_key, base_url=base_url, timeout=timeout)
        self._http = httpx.AsyncClient(headers=self._config.headers, timeout=self._config.timeout)

        self.auth = AsyncAuthResource(self)
        self.sub_users = AsyncSubUsersResource(self)
        self.sub_user_groups = AsyncSubUserGroupsResource(self)
        self.locations = AsyncLocationsResource(self)
        self.analytics = AsyncAnalyticsResource(self)
        self.proxy_presets = AsyncProxyPresetsResource(self)
        self.profile = AsyncProfileResource(self)
        self.two_factor = AsyncTwoFactorResource(self)
        self.email = AsyncEmailResource(self)
        self.coupons = AsyncCouponsResource(self)
        self.plans = AsyncPlansResource(self)
        self.payments = AsyncPaymentsResource(self)

    async def request(
        self,
        method: str,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> Any:
        url = self._config.build_url(path)
        if params:
            params = {k: v for k, v in params.items() if v is not None}
        response = await self._http.request(method, url, json=json, params=params)
        body = _parse_json_body(response)
        return self._config.handle_response(response.status_code, body, response.headers)

    async def request_raw(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
    ) -> httpx.Response:
        """Make a request and return the raw httpx.Response (for binary downloads)."""
        url = self._config.build_url(path)
        if params:
            params = {k: v for k, v in params.items() if v is not None}
        return await self._http.request(method, url, params=params)

    async def close(self) -> None:
        await self._http.aclose()

    async def __aenter__(self) -> AsyncProxyHat:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()
