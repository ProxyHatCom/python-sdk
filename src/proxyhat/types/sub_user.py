from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class SubUser:
    uuid: str
    proxy_username: str
    is_default_user: bool
    is_traffic_limited: bool
    used_traffic: int
    traffic_limit: int
    lifecycle_status: str
    name: str | None
    notes: str | None
    sub_user_group_id: str | None
    created_at: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SubUser:
        return cls(
            uuid=data.get("uuid", ""),
            proxy_username=data.get("proxy_username", ""),
            is_default_user=data.get("is_default_user", False),
            is_traffic_limited=data.get("is_traffic_limited", False),
            used_traffic=data.get("used_traffic", 0),
            traffic_limit=data.get("traffic_limit", 0),
            lifecycle_status=data.get("lifecycle_status", ""),
            name=data.get("name"),
            notes=data.get("notes"),
            sub_user_group_id=data.get("sub_user_group_id"),
            created_at=data.get("created_at", ""),
        )


@dataclass
class ResetUsageResponse:
    reset: int

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ResetUsageResponse:
        return cls(reset=data.get("reset", 0))


@dataclass
class BulkDeleteResponse:
    requested: int
    deleted: int
    skipped: int
    not_found: int
    failed: int

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> BulkDeleteResponse:
        return cls(
            requested=data.get("requested", 0),
            deleted=data.get("deleted", 0),
            skipped=data.get("skipped", 0),
            not_found=data.get("not_found", 0),
            failed=data.get("failed", 0),
        )
