from __future__ import annotations

from typing import TYPE_CHECKING, Any

from proxyhat.types.proxy_presets import ProxyPreset

if TYPE_CHECKING:
    from proxyhat.async_client import AsyncProxyHat
    from proxyhat.client import ProxyHat


class ProxyPresetsResource:
    def __init__(self, client: ProxyHat) -> None:
        self._client = client

    def list(self) -> list[ProxyPreset]:
        data = self._client.request("GET", "/proxy-presets")
        if isinstance(data, list):
            return [ProxyPreset.from_dict(item) for item in data]
        return []

    def create(self, *, name: str, data: dict[str, Any]) -> ProxyPreset:
        result = self._client.request("POST", "/proxy-presets", json={"name": name, "data": data})
        return ProxyPreset.from_dict(result)

    def get(self, id: str) -> ProxyPreset:
        data = self._client.request("GET", f"/proxy-presets/{id}")
        return ProxyPreset.from_dict(data)

    def update(self, id: str, *, name: str | None = None, data: dict[str, Any] | None = None) -> ProxyPreset:
        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if data is not None:
            body["data"] = data
        result = self._client.request("PUT", f"/proxy-presets/{id}", json=body)
        return ProxyPreset.from_dict(result)

    def delete(self, id: str) -> None:
        self._client.request("DELETE", f"/proxy-presets/{id}")


class AsyncProxyPresetsResource:
    def __init__(self, client: AsyncProxyHat) -> None:
        self._client = client

    async def list(self) -> list[ProxyPreset]:
        data = await self._client.request("GET", "/proxy-presets")
        if isinstance(data, list):
            return [ProxyPreset.from_dict(item) for item in data]
        return []

    async def create(self, *, name: str, data: dict[str, Any]) -> ProxyPreset:
        result = await self._client.request("POST", "/proxy-presets", json={"name": name, "data": data})
        return ProxyPreset.from_dict(result)

    async def get(self, id: str) -> ProxyPreset:
        data = await self._client.request("GET", f"/proxy-presets/{id}")
        return ProxyPreset.from_dict(data)

    async def update(self, id: str, *, name: str | None = None, data: dict[str, Any] | None = None) -> ProxyPreset:
        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if data is not None:
            body["data"] = data
        result = await self._client.request("PUT", f"/proxy-presets/{id}", json=body)
        return ProxyPreset.from_dict(result)

    async def delete(self, id: str) -> None:
        await self._client.request("DELETE", f"/proxy-presets/{id}")
