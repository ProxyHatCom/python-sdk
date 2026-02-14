from __future__ import annotations

from typing import TYPE_CHECKING, Any

from proxyhat.types.profile import APIKey, Preferences

if TYPE_CHECKING:
    from proxyhat.async_client import AsyncProxyHat
    from proxyhat.client import ProxyHat


class ProfileResource:
    def __init__(self, client: ProxyHat) -> None:
        self._client = client

    def get_preferences(self) -> Preferences:
        data = self._client.request("GET", "/profile/preferences")
        return Preferences.from_dict(data)

    def update_preferences(self, **preferences: Any) -> Preferences:
        data = self._client.request("PUT", "/profile/preferences", json=preferences)
        return Preferences.from_dict(data)

    def list_api_keys(self) -> list[APIKey]:
        data = self._client.request("GET", "/profile/api-keys")
        if isinstance(data, list):
            return [APIKey.from_dict(item) for item in data]
        return []

    def create_api_key(self, *, name: str | None = None) -> APIKey:
        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        data = self._client.request("POST", "/profile/api-keys", json=body)
        return APIKey.from_dict(data)

    def delete_api_key(self, id: str) -> None:
        self._client.request("DELETE", f"/profile/api-keys/{id}")

    def regenerate_api_key(self, id: str) -> APIKey:
        data = self._client.request("POST", f"/profile/api-keys/{id}/regenerate")
        return APIKey.from_dict(data)


class AsyncProfileResource:
    def __init__(self, client: AsyncProxyHat) -> None:
        self._client = client

    async def get_preferences(self) -> Preferences:
        data = await self._client.request("GET", "/profile/preferences")
        return Preferences.from_dict(data)

    async def update_preferences(self, **preferences: Any) -> Preferences:
        data = await self._client.request("PUT", "/profile/preferences", json=preferences)
        return Preferences.from_dict(data)

    async def list_api_keys(self) -> list[APIKey]:
        data = await self._client.request("GET", "/profile/api-keys")
        if isinstance(data, list):
            return [APIKey.from_dict(item) for item in data]
        return []

    async def create_api_key(self, *, name: str | None = None) -> APIKey:
        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        data = await self._client.request("POST", "/profile/api-keys", json=body)
        return APIKey.from_dict(data)

    async def delete_api_key(self, id: str) -> None:
        await self._client.request("DELETE", f"/profile/api-keys/{id}")

    async def regenerate_api_key(self, id: str) -> APIKey:
        data = await self._client.request("POST", f"/profile/api-keys/{id}/regenerate")
        return APIKey.from_dict(data)
