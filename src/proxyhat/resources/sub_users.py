from __future__ import annotations

from typing import TYPE_CHECKING, Any

from proxyhat.types.sub_user import BulkDeleteResponse, ResetUsageResponse, SubUser

if TYPE_CHECKING:
    from proxyhat.async_client import AsyncProxyHat
    from proxyhat.client import ProxyHat


class SubUsersResource:
    def __init__(self, client: ProxyHat) -> None:
        self._client = client

    def list(self) -> list[SubUser]:
        data = self._client.request("GET", "/sub-users")
        if isinstance(data, list):
            return [SubUser.from_dict(item) for item in data]
        return []

    def create(
        self,
        *,
        proxy_password: str,
        is_traffic_limited: bool = False,
        traffic_limit: str | None = None,
        name: str | None = None,
        notes: str | None = None,
        sub_user_group_id: str | None = None,
    ) -> SubUser:
        body: dict[str, Any] = {
            "proxy_password": proxy_password,
            "is_traffic_limited": is_traffic_limited,
        }
        if traffic_limit is not None:
            body["traffic_limit"] = traffic_limit
        if name is not None:
            body["name"] = name
        if notes is not None:
            body["notes"] = notes
        if sub_user_group_id is not None:
            body["sub_user_group_id"] = sub_user_group_id

        data = self._client.request("POST", "/sub-users", json=body)
        return SubUser.from_dict(data)

    def get(self, id: str) -> SubUser:
        data = self._client.request("GET", f"/sub-users/{id}")
        return SubUser.from_dict(data)

    def update(
        self,
        id: str,
        *,
        proxy_password: str | None = None,
        is_traffic_limited: bool | None = None,
        traffic_limit: str | None = None,
        name: str | None = None,
        notes: str | None = None,
    ) -> SubUser:
        body: dict[str, Any] = {}
        if proxy_password is not None:
            body["proxy_password"] = proxy_password
        if is_traffic_limited is not None:
            body["is_traffic_limited"] = is_traffic_limited
        if traffic_limit is not None:
            body["traffic_limit"] = traffic_limit
        if name is not None:
            body["name"] = name
        if notes is not None:
            body["notes"] = notes

        data = self._client.request("PUT", f"/sub-users/{id}", json=body)
        return SubUser.from_dict(data)

    def delete(self, id: str) -> None:
        self._client.request("DELETE", f"/sub-users/{id}")

    def reset_usage(self, ids: list[str]) -> ResetUsageResponse:
        data = self._client.request("POST", "/sub-users/reset/usage", json={"ids": ids})
        return ResetUsageResponse.from_dict(data)

    def bulk_delete(self, ids: list[str]) -> BulkDeleteResponse:
        data = self._client.request("POST", "/sub-users/bulk-delete", json={"ids": ids})
        return BulkDeleteResponse.from_dict(data)

    def bulk_move_to_group(self, ids: list[str], group_id: str | None = None) -> Any:
        return self._client.request("POST", "/sub-users/bulk-move-to-group", json={"ids": ids, "group_id": group_id})


class AsyncSubUsersResource:
    def __init__(self, client: AsyncProxyHat) -> None:
        self._client = client

    async def list(self) -> list[SubUser]:
        data = await self._client.request("GET", "/sub-users")
        if isinstance(data, list):
            return [SubUser.from_dict(item) for item in data]
        return []

    async def create(
        self,
        *,
        proxy_password: str,
        is_traffic_limited: bool = False,
        traffic_limit: str | None = None,
        name: str | None = None,
        notes: str | None = None,
        sub_user_group_id: str | None = None,
    ) -> SubUser:
        body: dict[str, Any] = {
            "proxy_password": proxy_password,
            "is_traffic_limited": is_traffic_limited,
        }
        if traffic_limit is not None:
            body["traffic_limit"] = traffic_limit
        if name is not None:
            body["name"] = name
        if notes is not None:
            body["notes"] = notes
        if sub_user_group_id is not None:
            body["sub_user_group_id"] = sub_user_group_id

        data = await self._client.request("POST", "/sub-users", json=body)
        return SubUser.from_dict(data)

    async def get(self, id: str) -> SubUser:
        data = await self._client.request("GET", f"/sub-users/{id}")
        return SubUser.from_dict(data)

    async def update(
        self,
        id: str,
        *,
        proxy_password: str | None = None,
        is_traffic_limited: bool | None = None,
        traffic_limit: str | None = None,
        name: str | None = None,
        notes: str | None = None,
    ) -> SubUser:
        body: dict[str, Any] = {}
        if proxy_password is not None:
            body["proxy_password"] = proxy_password
        if is_traffic_limited is not None:
            body["is_traffic_limited"] = is_traffic_limited
        if traffic_limit is not None:
            body["traffic_limit"] = traffic_limit
        if name is not None:
            body["name"] = name
        if notes is not None:
            body["notes"] = notes

        data = await self._client.request("PUT", f"/sub-users/{id}", json=body)
        return SubUser.from_dict(data)

    async def delete(self, id: str) -> None:
        await self._client.request("DELETE", f"/sub-users/{id}")

    async def reset_usage(self, ids: list[str]) -> ResetUsageResponse:
        data = await self._client.request("POST", "/sub-users/reset/usage", json={"ids": ids})
        return ResetUsageResponse.from_dict(data)

    async def bulk_delete(self, ids: list[str]) -> BulkDeleteResponse:
        data = await self._client.request("POST", "/sub-users/bulk-delete", json={"ids": ids})
        return BulkDeleteResponse.from_dict(data)

    async def bulk_move_to_group(self, ids: list[str], group_id: str | None = None) -> Any:
        return await self._client.request(
            "POST", "/sub-users/bulk-move-to-group", json={"ids": ids, "group_id": group_id}
        )
