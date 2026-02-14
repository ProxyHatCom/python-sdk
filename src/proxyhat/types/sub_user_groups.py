from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class SubUserGroup:
    id: str
    name: str
    description: str | None
    sub_users_count: int
    created_at: str
    sub_users: list[Any] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SubUserGroup:
        return cls(
            id=data.get("id", ""),
            name=data.get("name", ""),
            description=data.get("description"),
            sub_users_count=data.get("sub_users_count", 0),
            created_at=data.get("created_at", ""),
            sub_users=data.get("sub_users", []),
        )
