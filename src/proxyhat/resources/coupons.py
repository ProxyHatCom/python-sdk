from __future__ import annotations

from typing import TYPE_CHECKING, Any

from proxyhat.types.coupons import CouponResponse

if TYPE_CHECKING:
    from proxyhat.async_client import AsyncProxyHat
    from proxyhat.client import ProxyHat


class CouponsResource:
    def __init__(self, client: ProxyHat) -> None:
        self._client = client

    def validate(
        self,
        *,
        code: str,
        plan_id: str | None = None,
        order_sum: float | None = None,
        currency: str | None = None,
    ) -> CouponResponse:
        body: dict[str, Any] = {"code": code}
        if plan_id is not None:
            body["plan_id"] = plan_id
        if order_sum is not None:
            body["order_sum"] = order_sum
        if currency is not None:
            body["currency"] = currency
        data = self._client.request("POST", "/coupon/validate", json=body)
        return CouponResponse.from_dict(data)

    def apply(
        self,
        *,
        code: str,
        plan_id: str | None = None,
        order_sum: float | None = None,
        currency: str | None = None,
    ) -> CouponResponse:
        body: dict[str, Any] = {"code": code}
        if plan_id is not None:
            body["plan_id"] = plan_id
        if order_sum is not None:
            body["order_sum"] = order_sum
        if currency is not None:
            body["currency"] = currency
        data = self._client.request("POST", "/coupon/apply", json=body)
        return CouponResponse.from_dict(data)

    def redeem(self, *, code: str) -> CouponResponse:
        data = self._client.request("POST", "/coupon/redeem", json={"code": code})
        return CouponResponse.from_dict(data)


class AsyncCouponsResource:
    def __init__(self, client: AsyncProxyHat) -> None:
        self._client = client

    async def validate(
        self,
        *,
        code: str,
        plan_id: str | None = None,
        order_sum: float | None = None,
        currency: str | None = None,
    ) -> CouponResponse:
        body: dict[str, Any] = {"code": code}
        if plan_id is not None:
            body["plan_id"] = plan_id
        if order_sum is not None:
            body["order_sum"] = order_sum
        if currency is not None:
            body["currency"] = currency
        data = await self._client.request("POST", "/coupon/validate", json=body)
        return CouponResponse.from_dict(data)

    async def apply(
        self,
        *,
        code: str,
        plan_id: str | None = None,
        order_sum: float | None = None,
        currency: str | None = None,
    ) -> CouponResponse:
        body: dict[str, Any] = {"code": code}
        if plan_id is not None:
            body["plan_id"] = plan_id
        if order_sum is not None:
            body["order_sum"] = order_sum
        if currency is not None:
            body["currency"] = currency
        data = await self._client.request("POST", "/coupon/apply", json=body)
        return CouponResponse.from_dict(data)

    async def redeem(self, *, code: str) -> CouponResponse:
        data = await self._client.request("POST", "/coupon/redeem", json={"code": code})
        return CouponResponse.from_dict(data)
