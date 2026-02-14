from __future__ import annotations

from typing import TYPE_CHECKING, Any

from proxyhat.types.two_factor import RecoveryCodes, TwoFactorEnableResponse, TwoFactorStatus

if TYPE_CHECKING:
    from proxyhat.async_client import AsyncProxyHat
    from proxyhat.client import ProxyHat


class TwoFactorResource:
    def __init__(self, client: ProxyHat) -> None:
        self._client = client

    def status(self) -> TwoFactorStatus:
        data = self._client.request("GET", "/profile/2fa/status")
        return TwoFactorStatus.from_dict(data)

    def enable(self) -> TwoFactorEnableResponse:
        data = self._client.request("POST", "/profile/2fa/enable")
        return TwoFactorEnableResponse.from_dict(data)

    def confirm(self, *, code: str) -> Any:
        return self._client.request("POST", "/profile/2fa/confirm", json={"code": code})

    def disable(self, *, twofa_code: str) -> Any:
        return self._client.request("POST", "/profile/2fa/disable", json={"twofa_code": twofa_code})

    def qr_code(self) -> TwoFactorEnableResponse:
        data = self._client.request("GET", "/profile/2fa/qr-code")
        return TwoFactorEnableResponse.from_dict(data)

    def recovery_codes(self) -> RecoveryCodes:
        data = self._client.request("GET", "/profile/2fa/recovery-codes")
        return RecoveryCodes.from_dict(data)

    def disable_by_recovery(self, *, recovery_code: str) -> Any:
        return self._client.request(
            "POST", "/profile/2fa/disable-by-recovery-code", json={"recovery_code": recovery_code}
        )

    def change_password(
        self,
        *,
        current_password: str,
        password: str,
        password_confirmation: str,
        twofa_code: str | None = None,
    ) -> Any:
        body: dict[str, Any] = {
            "current_password": current_password,
            "password": password,
            "password_confirmation": password_confirmation,
        }
        if twofa_code is not None:
            body["twofa_code"] = twofa_code
        return self._client.request("POST", "/profile/password", json=body)


class AsyncTwoFactorResource:
    def __init__(self, client: AsyncProxyHat) -> None:
        self._client = client

    async def status(self) -> TwoFactorStatus:
        data = await self._client.request("GET", "/profile/2fa/status")
        return TwoFactorStatus.from_dict(data)

    async def enable(self) -> TwoFactorEnableResponse:
        data = await self._client.request("POST", "/profile/2fa/enable")
        return TwoFactorEnableResponse.from_dict(data)

    async def confirm(self, *, code: str) -> Any:
        return await self._client.request("POST", "/profile/2fa/confirm", json={"code": code})

    async def disable(self, *, twofa_code: str) -> Any:
        return await self._client.request("POST", "/profile/2fa/disable", json={"twofa_code": twofa_code})

    async def qr_code(self) -> TwoFactorEnableResponse:
        data = await self._client.request("GET", "/profile/2fa/qr-code")
        return TwoFactorEnableResponse.from_dict(data)

    async def recovery_codes(self) -> RecoveryCodes:
        data = await self._client.request("GET", "/profile/2fa/recovery-codes")
        return RecoveryCodes.from_dict(data)

    async def disable_by_recovery(self, *, recovery_code: str) -> Any:
        return await self._client.request(
            "POST", "/profile/2fa/disable-by-recovery-code", json={"recovery_code": recovery_code}
        )

    async def change_password(
        self,
        *,
        current_password: str,
        password: str,
        password_confirmation: str,
        twofa_code: str | None = None,
    ) -> Any:
        body: dict[str, Any] = {
            "current_password": current_password,
            "password": password,
            "password_confirmation": password_confirmation,
        }
        if twofa_code is not None:
            body["twofa_code"] = twofa_code
        return await self._client.request("POST", "/profile/password", json=body)
