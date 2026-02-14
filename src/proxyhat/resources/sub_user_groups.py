from __future__ import annotations

from typing import TYPE_CHECKING, Any

from proxyhat.types.sub_user_groups import SubUserGroup

if TYPE_CHECKING:
    from proxyhat.async_client import AsyncProxyHat
    from proxyhat.client import ProxyHat


class SubUserGroupsResource:
    def __init__(self, client: ProxyHat) -> None:
        self._client = client

    def list(self) -> list[SubUserGroup]:
        data = self._client.request("GET", "/sub-user-groups")
        if isinstance(data, list):
            return [SubUserGroup.from_dict(item) for item in data]
        return []

    def create(self, *, name: str, description: str | None = None) -> SubUserGroup:
        body: dict[str, Any] = {"name": name}
        if description is not None:
            body["description"] = description
        data = self._client.request("POST", "/sub-user-groups", json=body)
        return SubUserGroup.from_dict(data)

    def get(self, id: str) -> SubUserGroup:
        data = self._client.request("GET", f"/sub-user-groups/{id}")
        return SubUserGroup.from_dict(data)

    def update(self, id: str, *, name: str | None = None, description: str | None = None) -> SubUserGroup:
        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if description is not None:
            body["description"] = description
        data = self._client.request("PUT", f"/sub-user-groups/{id}", json=body)
        return SubUserGroup.from_dict(data)

    def delete(self, id: str) -> None:
        self._client.request("DELETE", f"/sub-user-groups/{id}")


class AsyncSubUserGroupsResource:
    def __init__(self, client: AsyncProxyHat) -> None:
        self._client = client

    async def list(self) -> list[SubUserGroup]:
        data = await self._client.request("GET", "/sub-user-groups")
        if isinstance(data, list):
            return [SubUserGroup.from_dict(item) for item in data]
        return []

    async def create(self, *, name: str, description: str | None = None) -> SubUserGroup:
        body: dict[str, Any] = {"name": name}
        if description is not None:
            body["description"] = description
        data = await self._client.request("POST", "/sub-user-groups", json=body)
        return SubUserGroup.from_dict(data)

    async def get(self, id: str) -> SubUserGroup:
        data = await self._client.request("GET", f"/sub-user-groups/{id}")
        return SubUserGroup.from_dict(data)

    async def update(self, id: str, *, name: str | None = None, description: str | None = None) -> SubUserGroup:
        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if description is not None:
            body["description"] = description
        data = await self._client.request("PUT", f"/sub-user-groups/{id}", json=body)
        return SubUserGroup.from_dict(data)

    async def delete(self, id: str) -> None:
        await self._client.request("DELETE", f"/sub-user-groups/{id}")
