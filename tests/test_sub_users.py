import httpx
import pytest
import respx

from proxyhat import AsyncProxyHat, ProxyHat
from proxyhat.types.sub_user import BulkDeleteResponse, ResetUsageResponse, SubUser

SUB_USER_DATA = {
    "uuid": "su-001",
    "proxy_username": "user_abc123",
    "is_default_user": False,
    "is_traffic_limited": True,
    "used_traffic": 1073741824,
    "traffic_limit": 5368709120,
    "lifecycle_status": "Active",
    "name": "Main proxy",
    "notes": None,
    "sub_user_group_id": None,
    "created_at": "2026-01-20T10:00:00Z",
}


class TestSubUsersSync:
    def test_list(self, client: ProxyHat, mock_api):
        mock_api.get("/sub-users").mock(
            return_value=httpx.Response(
                200,
                json={"success": True, "payload": [SUB_USER_DATA]},
            )
        )
        result = client.sub_users.list()
        assert len(result) == 1
        assert isinstance(result[0], SubUser)
        assert result[0].uuid == "su-001"

    def test_create(self, client: ProxyHat, mock_api):
        mock_api.post("/sub-users").mock(
            return_value=httpx.Response(
                201,
                json={"success": True, "payload": SUB_USER_DATA},
            )
        )
        result = client.sub_users.create(
            proxy_password="pass123",
            is_traffic_limited=True,
            traffic_limit="5GB",
            name="Main proxy",
        )
        assert isinstance(result, SubUser)
        assert result.name == "Main proxy"

    def test_get(self, client: ProxyHat, mock_api):
        mock_api.get("/sub-users/su-001").mock(
            return_value=httpx.Response(
                200,
                json={"success": True, "payload": SUB_USER_DATA},
            )
        )
        result = client.sub_users.get("su-001")
        assert result.uuid == "su-001"

    def test_update(self, client: ProxyHat, mock_api):
        updated = {**SUB_USER_DATA, "name": "Updated proxy"}
        mock_api.put("/sub-users/su-001").mock(
            return_value=httpx.Response(
                200,
                json={"success": True, "payload": updated},
            )
        )
        result = client.sub_users.update("su-001", name="Updated proxy")
        assert result.name == "Updated proxy"

    def test_delete(self, client: ProxyHat, mock_api):
        mock_api.delete("/sub-users/su-001").mock(
            return_value=httpx.Response(200, json={"success": True, "payload": None})
        )
        client.sub_users.delete("su-001")

    def test_reset_usage(self, client: ProxyHat, mock_api):
        mock_api.post("/sub-users/reset/usage").mock(
            return_value=httpx.Response(
                200,
                json={"success": True, "payload": {"reset": 2}},
            )
        )
        result = client.sub_users.reset_usage(["su-001", "su-002"])
        assert isinstance(result, ResetUsageResponse)
        assert result.reset == 2

    def test_bulk_delete(self, client: ProxyHat, mock_api):
        mock_api.post("/sub-users/bulk-delete").mock(
            return_value=httpx.Response(
                200,
                json={
                    "success": True,
                    "payload": {
                        "requested": 2,
                        "deleted": 2,
                        "skipped": 0,
                        "not_found": 0,
                        "failed": 0,
                    },
                },
            )
        )
        result = client.sub_users.bulk_delete(["su-001", "su-002"])
        assert isinstance(result, BulkDeleteResponse)
        assert result.deleted == 2


class TestSubUsersAsync:
    @pytest.mark.asyncio
    async def test_list(self, async_client: AsyncProxyHat):
        with respx.mock(base_url="https://api.proxyhat.com/v1") as mock_api:
            mock_api.get("/sub-users").mock(
                return_value=httpx.Response(
                    200,
                    json={"success": True, "payload": [SUB_USER_DATA]},
                )
            )
            result = await async_client.sub_users.list()
            assert len(result) == 1
            assert result[0].proxy_username == "user_abc123"
        await async_client.close()
