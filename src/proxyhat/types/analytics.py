from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class TimeSeriesResponse:
    labels: list[str] = field(default_factory=list)
    data: list[int] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TimeSeriesResponse:
        return cls(
            labels=data.get("labels", []),
            data=data.get("data", []),
        )


@dataclass
class TotalResponse:
    total: int = 0

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TotalResponse:
        return cls(total=data.get("total", 0))


@dataclass
class DomainBreakdownItem:
    domain: str
    bandwidth: int
    requests: int

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DomainBreakdownItem:
        return cls(
            domain=data.get("domain", ""),
            bandwidth=data.get("bandwidth", 0),
            requests=data.get("requests", 0),
        )


@dataclass
class DomainBreakdownResponse:
    items: list[DomainBreakdownItem] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DomainBreakdownResponse:
        return cls(
            items=[DomainBreakdownItem.from_dict(item) for item in data.get("items", [])],
        )
