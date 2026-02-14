from __future__ import annotations

from typing import Any

import httpx

from proxyhat._base_client import DEFAULT_BASE_URL, DEFAULT_TIMEOUT, BaseClientConfig, _parse_json_body
from proxyhat.resources.analytics import AnalyticsResource
from proxyhat.resources.auth import AuthResource
from proxyhat.resources.coupons import CouponsResource
from proxyhat.resources.email import EmailResource
from proxyhat.resources.locations import LocationsResource
from proxyhat.resources.payments import PaymentsResource
from proxyhat.resources.plans import PlansResource
from proxyhat.resources.profile import ProfileResource
from proxyhat.resources.proxy_presets import ProxyPresetsResource
from proxyhat.resources.sub_user_groups import SubUserGroupsResource
from proxyhat.resources.sub_users import SubUsersResource
from proxyhat.resources.two_factor import TwoFactorResource


class ProxyHat:
    """Synchronous client for the ProxyHat API."""

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> None:
        self._config = BaseClientConfig(api_key=api_key, base_url=base_url, timeout=timeout)
        self._http = httpx.Client(headers=self._config.headers, timeout=self._config.timeout)

        self.auth = AuthResource(self)
        self.sub_users = SubUsersResource(self)
        self.sub_user_groups = SubUserGroupsResource(self)
        self.locations = LocationsResource(self)
        self.analytics = AnalyticsResource(self)
        self.proxy_presets = ProxyPresetsResource(self)
        self.profile = ProfileResource(self)
        self.two_factor = TwoFactorResource(self)
        self.email = EmailResource(self)
        self.coupons = CouponsResource(self)
        self.plans = PlansResource(self)
        self.payments = PaymentsResource(self)

    def request(
        self,
        method: str,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> Any:
        url = self._config.build_url(path)
        # Filter out None params
        if params:
            params = {k: v for k, v in params.items() if v is not None}
        response = self._http.request(method, url, json=json, params=params)
        body = _parse_json_body(response)
        return self._config.handle_response(response.status_code, body, response.headers)

    def request_raw(
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
        return self._http.request(method, url, params=params)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> ProxyHat:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
