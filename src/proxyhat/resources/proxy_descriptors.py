from __future__ import annotations

from typing import TYPE_CHECKING, Any

from proxyhat.types.proxy_descriptor import ProxyDescriptor

if TYPE_CHECKING:
    from proxyhat.async_client import AsyncProxyHat
    from proxyhat.client import ProxyHat


def _body(
    sub_user_uuid: str,
    protocol: str,
    location: dict[str, Any] | None,
    session: dict[str, Any] | None,
    filter: str | None,
) -> dict[str, Any]:
    body: dict[str, Any] = {"sub_user_uuid": sub_user_uuid, "protocol": protocol}
    if location is not None:
        body["location"] = location
    if session is not None:
        body["session"] = session
    if filter is not None:
        body["filter"] = filter
    return body


class ProxyDescriptorsResource:
    def __init__(self, client: ProxyHat) -> None:
        self._client = client

    def create(
        self,
        *,
        sub_user_uuid: str,
        protocol: str = "http",
        location: dict[str, Any] | None = None,
        session: dict[str, Any] | None = None,
        filter: str | None = None,
    ) -> ProxyDescriptor:
        data = self._client.request(
            "POST", "/proxy-descriptors", json=_body(sub_user_uuid, protocol, location, session, filter)
        )
        return ProxyDescriptor.from_dict(data)


class AsyncProxyDescriptorsResource:
    def __init__(self, client: AsyncProxyHat) -> None:
        self._client = client

    async def create(
        self,
        *,
        sub_user_uuid: str,
        protocol: str = "http",
        location: dict[str, Any] | None = None,
        session: dict[str, Any] | None = None,
        filter: str | None = None,
    ) -> ProxyDescriptor:
        data = await self._client.request(
            "POST", "/proxy-descriptors", json=_body(sub_user_uuid, protocol, location, session, filter)
        )
        return ProxyDescriptor.from_dict(data)
