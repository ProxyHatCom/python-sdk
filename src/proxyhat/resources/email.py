from __future__ import annotations

from typing import TYPE_CHECKING, Any

from proxyhat.types.email import EmailChangeResponse

if TYPE_CHECKING:
    from proxyhat.async_client import AsyncProxyHat
    from proxyhat.client import ProxyHat


class EmailResource:
    def __init__(self, client: ProxyHat) -> None:
        self._client = client

    def request_change(self, *, email: str, twofa_code: str | None = None) -> EmailChangeResponse:
        body: dict[str, Any] = {"email": email}
        if twofa_code is not None:
            body["twofa_code"] = twofa_code
        data = self._client.request("POST", "/profile/email/request-change", json=body)
        return EmailChangeResponse.from_dict(data)

    def confirm_change(self, *, token: str) -> EmailChangeResponse:
        data = self._client.request("POST", "/profile/email/confirm-change", json={"token": token})
        return EmailChangeResponse.from_dict(data)

    def cancel_change(self) -> EmailChangeResponse:
        data = self._client.request("POST", "/profile/email/cancel-change")
        return EmailChangeResponse.from_dict(data)

    def resend_verification(self) -> EmailChangeResponse:
        data = self._client.request("POST", "/profile/email/resend-verification")
        return EmailChangeResponse.from_dict(data)


class AsyncEmailResource:
    def __init__(self, client: AsyncProxyHat) -> None:
        self._client = client

    async def request_change(self, *, email: str, twofa_code: str | None = None) -> EmailChangeResponse:
        body: dict[str, Any] = {"email": email}
        if twofa_code is not None:
            body["twofa_code"] = twofa_code
        data = await self._client.request("POST", "/profile/email/request-change", json=body)
        return EmailChangeResponse.from_dict(data)

    async def confirm_change(self, *, token: str) -> EmailChangeResponse:
        data = await self._client.request("POST", "/profile/email/confirm-change", json={"token": token})
        return EmailChangeResponse.from_dict(data)

    async def cancel_change(self) -> EmailChangeResponse:
        data = await self._client.request("POST", "/profile/email/cancel-change")
        return EmailChangeResponse.from_dict(data)

    async def resend_verification(self) -> EmailChangeResponse:
        data = await self._client.request("POST", "/profile/email/resend-verification")
        return EmailChangeResponse.from_dict(data)
