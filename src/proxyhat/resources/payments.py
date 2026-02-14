from __future__ import annotations

from typing import TYPE_CHECKING, Any

import httpx

from proxyhat.types.payments import Cryptocurrency, Payment, PaymentCreateResponse, PaymentDetails

if TYPE_CHECKING:
    from proxyhat.async_client import AsyncProxyHat
    from proxyhat.client import ProxyHat


class PaymentsResource:
    def __init__(self, client: ProxyHat) -> None:
        self._client = client

    def list(self) -> list[Payment]:
        data = self._client.request("GET", "/payments")
        if isinstance(data, list):
            return [Payment.from_dict(item) for item in data]
        return []

    def create(
        self,
        *,
        type: str,
        plan_id: str,
        gate: str = "crypto",
        cryptocurrency_code: str,
        coupon_code: str | None = None,
    ) -> PaymentCreateResponse:
        body: dict[str, Any] = {
            "type": type,
            "plan_id": plan_id,
            "gate": gate,
            "cryptocurrency_code": cryptocurrency_code,
        }
        if coupon_code is not None:
            body["coupon_code"] = coupon_code
        data = self._client.request("POST", "/payments", json=body)
        return PaymentCreateResponse.from_dict(data)

    def get(self, id: str) -> PaymentDetails:
        data = self._client.request("GET", f"/payments/{id}")
        return PaymentDetails.from_dict(data)

    def check(self, id: str) -> PaymentDetails:
        data = self._client.request("GET", f"/payments/{id}/check")
        return PaymentDetails.from_dict(data)

    def invoice(self, id: str, *, format: str = "pdf") -> httpx.Response:
        return self._client.request_raw("GET", f"/payments/{id}/invoice", params={"format": format})

    def cryptocurrencies(self) -> list[Cryptocurrency]:
        data = self._client.request("GET", "/payments/cryptocurrencies")
        if isinstance(data, list):
            return [Cryptocurrency.from_dict(item) for item in data]
        return []


class AsyncPaymentsResource:
    def __init__(self, client: AsyncProxyHat) -> None:
        self._client = client

    async def list(self) -> list[Payment]:
        data = await self._client.request("GET", "/payments")
        if isinstance(data, list):
            return [Payment.from_dict(item) for item in data]
        return []

    async def create(
        self,
        *,
        type: str,
        plan_id: str,
        gate: str = "crypto",
        cryptocurrency_code: str,
        coupon_code: str | None = None,
    ) -> PaymentCreateResponse:
        body: dict[str, Any] = {
            "type": type,
            "plan_id": plan_id,
            "gate": gate,
            "cryptocurrency_code": cryptocurrency_code,
        }
        if coupon_code is not None:
            body["coupon_code"] = coupon_code
        data = await self._client.request("POST", "/payments", json=body)
        return PaymentCreateResponse.from_dict(data)

    async def get(self, id: str) -> PaymentDetails:
        data = await self._client.request("GET", f"/payments/{id}")
        return PaymentDetails.from_dict(data)

    async def check(self, id: str) -> PaymentDetails:
        data = await self._client.request("GET", f"/payments/{id}/check")
        return PaymentDetails.from_dict(data)

    async def invoice(self, id: str, *, format: str = "pdf") -> httpx.Response:
        return await self._client.request_raw("GET", f"/payments/{id}/invoice", params={"format": format})

    async def cryptocurrencies(self) -> list[Cryptocurrency]:
        data = await self._client.request("GET", "/payments/cryptocurrencies")
        if isinstance(data, list):
            return [Cryptocurrency.from_dict(item) for item in data]
        return []
