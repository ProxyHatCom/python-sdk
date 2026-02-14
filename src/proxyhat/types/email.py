from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class EmailChangeResponse:
    message: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> EmailChangeResponse:
        return cls(message=data.get("message", ""))
