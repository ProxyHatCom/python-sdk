from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Coupon:
    id: str
    code: str
    type: str
    data: Any
    discount: float | None = None
    final_amount: float | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Coupon:
        return cls(
            id=data.get("id", ""),
            code=data.get("code", ""),
            type=data.get("type", ""),
            data=data.get("data"),
            discount=data.get("discount"),
            final_amount=data.get("final_amount"),
        )


@dataclass
class CouponResponse:
    success: bool
    coupon: Coupon | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CouponResponse:
        coupon_data = data.get("coupon")
        return cls(
            success=data.get("success", False),
            coupon=Coupon.from_dict(coupon_data) if coupon_data else None,
        )
