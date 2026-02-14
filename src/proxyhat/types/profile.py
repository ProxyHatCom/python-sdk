from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Preferences:
    data: dict[str, Any]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Preferences:
        return cls(data=data)


@dataclass
class APIKey:
    id: str
    name: str | None
    plain_text_token: str | None = None
    created_at: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> APIKey:
        return cls(
            id=data.get("id", ""),
            name=data.get("name"),
            plain_text_token=data.get("plain_text_token"),
            created_at=data.get("created_at"),
        )
