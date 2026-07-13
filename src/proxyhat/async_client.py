from __future__ import annotations

from typing import Any

import httpx

from proxyhat._base_client import DEFAULT_BASE_URL, DEFAULT_TIMEOUT, BaseClientConfig, _parse_json_body
from proxyhat.connection import ProxyProtocol, build_connection_url
from proxyhat.resources.analytics import AsyncAnalyticsResource
from proxyhat.resources.auth import AsyncAuthResource
from proxyhat.resources.coupons import AsyncCouponsResource
from proxyhat.resources.email import AsyncEmailResource
from proxyhat.resources.locations import AsyncLocationsResource
from proxyhat.resources.payments import AsyncPaymentsResource
from proxyhat.resources.plans import AsyncPlansResource
from proxyhat.resources.profile import AsyncProfileResource
from proxyhat.resources.proxy_descriptors import AsyncProxyDescriptorsResource
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
        self.proxy_descriptors = AsyncProxyDescriptorsResource(self)
        self.profile = AsyncProfileResource(self)
        self.two_factor = AsyncTwoFactorResource(self)
        self.email = AsyncEmailResource(self)
        self.coupons = AsyncCouponsResource(self)
        self.plans = AsyncPlansResource(self)
        self.payments = AsyncPaymentsResource(self)

    async def connection_url(
        self,
        *,
        sub_user: str | None = None,
        country: str | None = None,
        region: str | None = None,
        city: str | None = None,
        sticky: bool | str | None = None,
        filter: str | None = None,
        protocol: ProxyProtocol = "http",
    ) -> str:
        """Return a ready-to-use residential proxy URL (see ``ProxyHat.connection_url``)."""
        users = await self.sub_users.list()
        want = sub_user.strip() if sub_user else None
        if want:
            chosen = next((s for s in users if s.uuid == want or s.name == want), None)
        else:
            usable = [
                s for s in users if not s.suspended_at and (s.traffic_limit == 0 or s.used_traffic < s.traffic_limit)
            ]
            chosen = usable[0] if usable else None
        if chosen is None or not chosen.proxy_username or not chosen.proxy_password:
            raise ValueError(
                f'No sub-user matched "{want}" (or it has no proxy credentials).'
                if want
                else "No usable sub-user found (all suspended or out of traffic). "
                "Create one, top up, or pass sub_user=."
            )
        return build_connection_url(
            username=chosen.proxy_username,
            password=chosen.proxy_password,
            country=country,
            region=region,
            city=city,
            sticky=sticky,
            filter=filter,
            protocol=protocol,
        )

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
