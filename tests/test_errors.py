import httpx
import pytest

from proxyhat import (
    AuthenticationError,
    NotFoundError,
    PermissionError,
    ProxyHat,
    ProxyHatError,
    RateLimitError,
    ValidationError,
)
from proxyhat.errors import APIError


class TestErrorHandling:
    def test_authentication_error(self, client: ProxyHat, mock_api):
        mock_api.get("/auth/user").mock(
            return_value=httpx.Response(
                401,
                json={"success": False, "description": "Unauthorized"},
            )
        )
        with pytest.raises(AuthenticationError) as exc_info:
            client.auth.user()
        assert exc_info.value.status_code == 401
        assert "Unauthorized" in exc_info.value.message

    def test_permission_error(self, client: ProxyHat, mock_api):
        mock_api.get("/auth/user").mock(
            return_value=httpx.Response(
                403,
                json={"success": False, "description": "Forbidden"},
            )
        )
        with pytest.raises(PermissionError) as exc_info:
            client.auth.user()
        assert exc_info.value.status_code == 403

    def test_not_found_error(self, client: ProxyHat, mock_api):
        mock_api.get("/sub-users/nonexistent").mock(
            return_value=httpx.Response(
                404,
                json={"success": False, "description": "Not Found"},
            )
        )
        with pytest.raises(NotFoundError) as exc_info:
            client.sub_users.get("nonexistent")
        assert exc_info.value.status_code == 404

    def test_validation_error(self, client: ProxyHat, mock_api):
        mock_api.post("/sub-users").mock(
            return_value=httpx.Response(
                422,
                json={
                    "success": False,
                    "description": "Validation Error",
                    "errors": {"name": ["Name is required"]},
                },
            )
        )
        with pytest.raises(ValidationError) as exc_info:
            client.sub_users.create(proxy_password="test")
        assert exc_info.value.status_code == 422
        assert exc_info.value.errors == {"name": ["Name is required"]}

    def test_rate_limit_error(self, client: ProxyHat, mock_api):
        mock_api.get("/sub-users").mock(
            return_value=httpx.Response(
                429,
                json={"success": False, "description": "Rate Limited"},
                headers={"retry-after": "30"},
            )
        )
        with pytest.raises(RateLimitError) as exc_info:
            client.sub_users.list()
        assert exc_info.value.status_code == 429
        assert exc_info.value.retry_after == 30

    def test_api_error(self, client: ProxyHat, mock_api):
        mock_api.get("/sub-users").mock(
            return_value=httpx.Response(
                500,
                json={"success": False, "description": "Internal Server Error"},
            )
        )
        with pytest.raises(APIError) as exc_info:
            client.sub_users.list()
        assert exc_info.value.status_code == 500

    def test_error_hierarchy(self):
        assert issubclass(AuthenticationError, ProxyHatError)
        assert issubclass(PermissionError, ProxyHatError)
        assert issubclass(NotFoundError, ProxyHatError)
        assert issubclass(ValidationError, ProxyHatError)
        assert issubclass(RateLimitError, ProxyHatError)
        assert issubclass(APIError, ProxyHatError)
