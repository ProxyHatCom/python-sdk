from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class ProxyDescriptor:
    """Server-built connection descriptor (POST /v1/proxy-descriptors)."""

    provider_id: str
    sub_user_uuid: str
    protocol: str
    filter: str
    host: str
    port: int
    username: str
    password: str
    url: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ProxyDescriptor:
        return cls(
            provider_id=data.get("provider_id", ""),
            sub_user_uuid=data.get("sub_user_uuid", ""),
            protocol=data.get("protocol", ""),
            filter=data.get("filter", ""),
            host=data.get("host", ""),
            port=data.get("port", 0),
            username=data.get("username", ""),
            password=data.get("password", ""),
            url=data.get("url", ""),
        )
