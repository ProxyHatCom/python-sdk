from __future__ import annotations

from typing import Any

import httpx

from proxyhat._base_client import DEFAULT_BASE_URL, DEFAULT_TIMEOUT, BaseClientConfig, _parse_json_body
from proxyhat.connection import ProxyProtocol, build_connection_url
from proxyhat.resources.analytics import AnalyticsResource
from proxyhat.resources.auth import AuthResource
from proxyhat.resources.coupons import CouponsResource
from proxyhat.resources.email import EmailResource
from proxyhat.resources.locations import LocationsResource
from proxyhat.resources.payments import PaymentsResource
from proxyhat.resources.plans import PlansResource
from proxyhat.resources.profile import ProfileResource
from proxyhat.resources.proxy_descriptors import ProxyDescriptorsResource
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
        self.proxy_descriptors = ProxyDescriptorsResource(self)
        self.profile = ProfileResource(self)
        self.two_factor = TwoFactorResource(self)
        self.email = EmailResource(self)
        self.coupons = CouponsResource(self)
        self.plans = PlansResource(self)
        self.payments = PaymentsResource(self)

    def connection_url(
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
        """Return a ready-to-use residential proxy URL.

        Looks up your sub-users, picks an active one with remaining traffic (or
        the one named by ``sub_user``), and builds the gateway URL locally.
        """
        users = self.sub_users.list()
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
