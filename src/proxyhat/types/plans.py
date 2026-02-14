from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class RegularPlan:
    id: str
    name: str
    gb: int
    price_per_gb: float
    price_total: float
    currency: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RegularPlan:
        return cls(
            id=data.get("id", ""),
            name=data.get("name", ""),
            gb=data.get("gb", 0),
            price_per_gb=data.get("price_per_gb", 0.0),
            price_total=data.get("price_total", 0.0),
            currency=data.get("currency", "USD"),
        )


@dataclass
class SubscriptionPlan:
    id: str
    name: str
    gb: int
    price_per_gb: float
    price_total: float
    period: str
    rollover_enabled: bool = False

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SubscriptionPlan:
        return cls(
            id=data.get("id", ""),
            name=data.get("name", ""),
            gb=data.get("gb", 0),
            price_per_gb=data.get("price_per_gb", 0.0),
            price_total=data.get("price_total", 0.0),
            period=data.get("period", ""),
            rollover_enabled=data.get("rollover_enabled", False),
        )


@dataclass
class PublicPricing:
    plans: list[Any]

    @classmethod
    def from_dict(cls, data: Any) -> PublicPricing:
        if isinstance(data, list):
            return cls(plans=data)
        return cls(plans=data.get("plans", []))
