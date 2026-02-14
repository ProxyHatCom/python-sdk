from __future__ import annotations

from typing import TYPE_CHECKING, Any

from proxyhat.types.auth import LoginResponse, RegisterResponse, SocialAccount, SupportedProvider, User

if TYPE_CHECKING:
    from proxyhat.async_client import AsyncProxyHat
    from proxyhat.client import ProxyHat


class AuthResource:
    def __init__(self, client: ProxyHat) -> None:
        self._client = client

    def register(
        self,
        *,
        name: str,
        email: str,
        password: str,
        password_confirmation: str,
        referral_code: str | None = None,
        utm_source: str | None = None,
        utm_medium: str | None = None,
        utm_campaign: str | None = None,
    ) -> RegisterResponse:
        body: dict[str, Any] = {
            "name": name,
            "email": email,
            "password": password,
            "password_confirmation": password_confirmation,
        }
        if referral_code is not None:
            body["referral_code"] = referral_code
        if utm_source is not None:
            body["utm_source"] = utm_source
        if utm_medium is not None:
            body["utm_medium"] = utm_medium
        if utm_campaign is not None:
            body["utm_campaign"] = utm_campaign

        data = self._client.request("POST", "/auth/register", json=body)
        return RegisterResponse.from_dict(data)

    def login(
        self,
        *,
        email: str,
        password: str,
        twofa_code: str | None = None,
    ) -> LoginResponse:
        body: dict[str, Any] = {"email": email, "password": password}
        if twofa_code is not None:
            body["twofa_code"] = twofa_code
        data = self._client.request("POST", "/auth/login", json=body)
        return LoginResponse.from_dict(data)

    def user(self) -> User:
        data = self._client.request("GET", "/auth/user")
        return User.from_dict(data)

    def logout(self) -> None:
        self._client.request("POST", "/auth/logout")

    def supported_providers(self) -> list[SupportedProvider]:
        data = self._client.request("GET", "/auth/supported-providers")
        if isinstance(data, list):
            return [SupportedProvider.from_dict(item) for item in data]
        return []

    def social_accounts(self) -> list[SocialAccount]:
        data = self._client.request("GET", "/auth/social-accounts")
        if isinstance(data, list):
            return [SocialAccount.from_dict(item) for item in data]
        return []

    def disconnect_social(self, provider: str) -> None:
        self._client.request("DELETE", f"/auth/social-accounts/{provider}")

    def oauth_redirect(self, provider: str) -> Any:
        return self._client.request("GET", f"/auth/{provider}/redirect")


class AsyncAuthResource:
    def __init__(self, client: AsyncProxyHat) -> None:
        self._client = client

    async def register(
        self,
        *,
        name: str,
        email: str,
        password: str,
        password_confirmation: str,
        referral_code: str | None = None,
        utm_source: str | None = None,
        utm_medium: str | None = None,
        utm_campaign: str | None = None,
    ) -> RegisterResponse:
        body: dict[str, Any] = {
            "name": name,
            "email": email,
            "password": password,
            "password_confirmation": password_confirmation,
        }
        if referral_code is not None:
            body["referral_code"] = referral_code
        if utm_source is not None:
            body["utm_source"] = utm_source
        if utm_medium is not None:
            body["utm_medium"] = utm_medium
        if utm_campaign is not None:
            body["utm_campaign"] = utm_campaign

        data = await self._client.request("POST", "/auth/register", json=body)
        return RegisterResponse.from_dict(data)

    async def login(
        self,
        *,
        email: str,
        password: str,
        twofa_code: str | None = None,
    ) -> LoginResponse:
        body: dict[str, Any] = {"email": email, "password": password}
        if twofa_code is not None:
            body["twofa_code"] = twofa_code
        data = await self._client.request("POST", "/auth/login", json=body)
        return LoginResponse.from_dict(data)

    async def user(self) -> User:
        data = await self._client.request("GET", "/auth/user")
        return User.from_dict(data)

    async def logout(self) -> None:
        await self._client.request("POST", "/auth/logout")

    async def supported_providers(self) -> list[SupportedProvider]:
        data = await self._client.request("GET", "/auth/supported-providers")
        if isinstance(data, list):
            return [SupportedProvider.from_dict(item) for item in data]
        return []

    async def social_accounts(self) -> list[SocialAccount]:
        data = await self._client.request("GET", "/auth/social-accounts")
        if isinstance(data, list):
            return [SocialAccount.from_dict(item) for item in data]
        return []

    async def disconnect_social(self, provider: str) -> None:
        await self._client.request("DELETE", f"/auth/social-accounts/{provider}")

    async def oauth_redirect(self, provider: str) -> Any:
        return await self._client.request("GET", f"/auth/{provider}/redirect")
