import httpx
import pytest
import respx

from proxyhat import AsyncProxyHat, ProxyHat
from proxyhat.types.auth import LoginResponse, RegisterResponse, User


class TestAuthSync:
    def test_register(self, client: ProxyHat, mock_api):
        mock_api.post("/auth/register").mock(
            return_value=httpx.Response(
                201,
                json={
                    "message": "Account created",
                    "accessToken": "tok_123",
                    "tokenType": "Bearer",
                },
            )
        )
        result = client.auth.register(
            name="Test User",
            email="test@example.com",
            password="secret123",
            password_confirmation="secret123",
        )
        assert isinstance(result, RegisterResponse)
        assert result.access_token == "tok_123"
        assert result.token_type == "Bearer"

    def test_login(self, client: ProxyHat, mock_api):
        mock_api.post("/auth/login").mock(
            return_value=httpx.Response(
                200,
                json={"accessToken": "tok_456", "tokenType": "Bearer"},
            )
        )
        result = client.auth.login(email="test@example.com", password="secret123")
        assert isinstance(result, LoginResponse)
        assert result.access_token == "tok_456"

    def test_user(self, client: ProxyHat, mock_api):
        mock_api.get("/auth/user").mock(
            return_value=httpx.Response(
                200,
                json={
                    "success": True,
                    "payload": {
                        "uuid": "usr-001",
                        "name": "Test User",
                        "email": "test@example.com",
                        "traffic": {
                            "subscription": None,
                            "subscription_starts_at": None,
                            "subscription_expires_at": None,
                            "regular_bytes": 1073741824,
                            "regular_human": "1 GB",
                            "subscription_bytes": 0,
                            "subscription_human": "0 B",
                            "total_bytes": 1073741824,
                            "total_human": "1 GB",
                        },
                    },
                },
            )
        )
        result = client.auth.user()
        assert isinstance(result, User)
        assert result.uuid == "usr-001"
        assert result.traffic.regular_bytes == 1073741824

    def test_logout(self, client: ProxyHat, mock_api):
        mock_api.post("/auth/logout").mock(return_value=httpx.Response(200, json={"success": True, "payload": None}))
        client.auth.logout()


class TestAuthAsync:
    @pytest.mark.asyncio
    async def test_login(self, async_client: AsyncProxyHat):
        with respx.mock(base_url="https://api.proxyhat.com/v1") as mock_api:
            mock_api.post("/auth/login").mock(
                return_value=httpx.Response(
                    200,
                    json={"accessToken": "tok_async", "tokenType": "Bearer"},
                )
            )
            result = await async_client.auth.login(email="test@example.com", password="secret123")
            assert result.access_token == "tok_async"
        await async_client.close()

    @pytest.mark.asyncio
    async def test_user(self, async_client: AsyncProxyHat):
        with respx.mock(base_url="https://api.proxyhat.com/v1") as mock_api:
            mock_api.get("/auth/user").mock(
                return_value=httpx.Response(
                    200,
                    json={
                        "success": True,
                        "payload": {
                            "uuid": "usr-async",
                            "name": "Async User",
                            "email": "async@example.com",
                            "traffic": {
                                "subscription": None,
                                "subscription_starts_at": None,
                                "subscription_expires_at": None,
                                "regular_bytes": 0,
                                "regular_human": "0 B",
                                "subscription_bytes": 0,
                                "subscription_human": "0 B",
                                "total_bytes": 0,
                                "total_human": "0 B",
                            },
                        },
                    },
                )
            )
            result = await async_client.auth.user()
            assert result.uuid == "usr-async"
        await async_client.close()
