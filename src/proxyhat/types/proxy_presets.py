from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class ProxyPreset:
    id: str
    name: str
    data: dict[str, Any]
    created_at: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ProxyPreset:
        return cls(
            id=data.get("id", ""),
            name=data.get("name", ""),
            data=data.get("data", {}),
            created_at=data.get("created_at"),
        )
