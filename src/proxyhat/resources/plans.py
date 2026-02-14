from __future__ import annotations

from typing import TYPE_CHECKING, Any

from proxyhat.types.plans import RegularPlan, SubscriptionPlan

if TYPE_CHECKING:
    from proxyhat.async_client import AsyncProxyHat
    from proxyhat.client import ProxyHat


class PlansResource:
    def __init__(self, client: ProxyHat) -> None:
        self._client = client

    def list_regular(self) -> list[RegularPlan]:
        data = self._client.request("GET", "/regular-options")
        if isinstance(data, list):
            return [RegularPlan.from_dict(item) for item in data]
        return []

    def list_subscriptions(self) -> list[SubscriptionPlan]:
        data = self._client.request("GET", "/subscription-plans")
        if isinstance(data, list):
            return [SubscriptionPlan.from_dict(item) for item in data]
        return []

    def get_regular(self, name: str) -> RegularPlan:
        data = self._client.request("GET", f"/plans/regular/{name}")
        return RegularPlan.from_dict(data)

    def get_subscription(self, name: str) -> SubscriptionPlan:
        data = self._client.request("GET", f"/plans/subscription/{name}")
        return SubscriptionPlan.from_dict(data)

    def pricing_regular(self) -> list[Any]:
        data = self._client.request("GET", "/pricing/regular")
        if isinstance(data, list):
            return data
        return []

    def pricing_subscriptions(self) -> list[Any]:
        data = self._client.request("GET", "/pricing/subscriptions")
        if isinstance(data, list):
            return data
        return []


class AsyncPlansResource:
    def __init__(self, client: AsyncProxyHat) -> None:
        self._client = client

    async def list_regular(self) -> list[RegularPlan]:
        data = await self._client.request("GET", "/regular-options")
        if isinstance(data, list):
            return [RegularPlan.from_dict(item) for item in data]
        return []

    async def list_subscriptions(self) -> list[SubscriptionPlan]:
        data = await self._client.request("GET", "/subscription-plans")
        if isinstance(data, list):
            return [SubscriptionPlan.from_dict(item) for item in data]
        return []

    async def get_regular(self, name: str) -> RegularPlan:
        data = await self._client.request("GET", f"/plans/regular/{name}")
        return RegularPlan.from_dict(data)

    async def get_subscription(self, name: str) -> SubscriptionPlan:
        data = await self._client.request("GET", f"/plans/subscription/{name}")
        return SubscriptionPlan.from_dict(data)

    async def pricing_regular(self) -> list[Any]:
        data = await self._client.request("GET", "/pricing/regular")
        if isinstance(data, list):
            return data
        return []

    async def pricing_subscriptions(self) -> list[Any]:
        data = await self._client.request("GET", "/pricing/subscriptions")
        if isinstance(data, list):
            return data
        return []
