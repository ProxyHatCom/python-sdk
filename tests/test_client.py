import pytest

from proxyhat import AsyncProxyHat, ProxyHat


class TestClientInit:
    def test_sync_client_defaults(self):
        client = ProxyHat(api_key="ph_test")
        assert client._config.api_key == "ph_test"
        assert client._config.base_url == "https://api.proxyhat.com/v1"
        assert client._config.timeout == 30.0
        client.close()

    def test_sync_client_custom(self):
        client = ProxyHat(api_key="ph_test", base_url="https://custom.api.com/v2", timeout=60.0)
        assert client._config.base_url == "https://custom.api.com/v2"
        assert client._config.timeout == 60.0
        client.close()

    def test_sync_client_context_manager(self):
        with ProxyHat(api_key="ph_test") as client:
            assert client._config.api_key == "ph_test"

    @pytest.mark.asyncio
    async def test_async_client_context_manager(self):
        async with AsyncProxyHat(api_key="ph_test") as client:
            assert client._config.api_key == "ph_test"

    def test_resource_initialization(self):
        client = ProxyHat(api_key="ph_test")
        assert hasattr(client, "auth")
        assert hasattr(client, "sub_users")
        assert hasattr(client, "sub_user_groups")
        assert hasattr(client, "locations")
        assert hasattr(client, "analytics")
        assert hasattr(client, "proxy_presets")
        assert hasattr(client, "profile")
        assert hasattr(client, "two_factor")
        assert hasattr(client, "email")
        assert hasattr(client, "coupons")
        assert hasattr(client, "plans")
        assert hasattr(client, "payments")
        client.close()

    def test_headers_include_auth(self):
        client = ProxyHat(api_key="ph_secret_key")
        headers = client._config.headers
        assert headers["Authorization"] == "Bearer ph_secret_key"
        assert "User-Agent" in headers
        client.close()

    def test_base_url_trailing_slash_stripped(self):
        client = ProxyHat(api_key="ph_test", base_url="https://api.example.com/v1/")
        assert client._config.base_url == "https://api.example.com/v1"
        client.close()
