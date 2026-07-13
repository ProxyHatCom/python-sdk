import re

import httpx
import pytest

from proxyhat import ProxyHat, build_connection_url, build_proxy_username


class TestBuildProxyUsername:
    def test_defaults_country_any(self):
        assert build_proxy_username("ph-8f2a1c") == "ph-8f2a1c-country-any"

    def test_country_region_city_filter_order(self):
        assert (
            build_proxy_username("ph-1", country="US", region="California", city="Los Angeles", filter="high")
            == "ph-1-country-us-region-california-city-los_angeles-filter-high"
        )

    def test_sticky_session_16_hex(self):
        assert re.fullmatch(r"ph-1-country-any-sid-[0-9a-f]{16}-ttl-30m", build_proxy_username("ph-1", sticky="30m"))
        assert build_proxy_username("ph-1", sticky=True).endswith("-ttl-30m")

    def test_rotating_has_no_session(self):
        assert "-sid-" not in build_proxy_username("ph-1", country="de")

    def test_filter_none_and_prefix(self):
        assert build_proxy_username("ph-1", filter="none") == "ph-1-country-any"
        got = build_proxy_username("ph-1", filter="filter-high-speed-fast")
        assert got == "ph-1-country-any-filter-high-speed-fast"


class TestBuildConnectionUrl:
    def test_http_default_port(self):
        assert (
            build_connection_url(username="ph-1", password="pw", country="us")
            == "http://ph-1-country-us:pw@gate.proxyhat.com:8080"
        )

    def test_socks5_port(self):
        assert (
            build_connection_url(username="ph-1", password="pw", protocol="socks5")
            == "socks5://ph-1-country-any:pw@gate.proxyhat.com:1080"
        )

    def test_encodes_credentials(self):
        assert "p%40s%3As@gate.proxyhat.com" in build_connection_url(username="ph-1", password="p@s:s")


def _sub_user(**kw):
    base = {
        "uuid": "u1",
        "proxy_username": "abc",
        "proxy_password": "pw",
        "is_default_user": False,
        "is_traffic_limited": True,
        "used_traffic": 1,
        "traffic_limit": 100,
        "lifecycle_status": "Active",
        "name": None,
        "notes": None,
        "sub_user_group_id": None,
        "created_at": "2026-01-01T00:00:00Z",
        "suspended_at": None,
    }
    base.update(kw)
    return base


class TestConnectionUrl:
    def test_picks_active_and_builds(self, client: ProxyHat, mock_api):
        mock_api.get("/sub-users").mock(
            return_value=httpx.Response(200, json={"success": True, "payload": [_sub_user()]})
        )
        assert client.connection_url(country="gb") == "http://abc-country-gb:pw@gate.proxyhat.com:8080"

    def test_skips_suspended_and_out_of_traffic(self, client: ProxyHat, mock_api):
        mock_api.get("/sub-users").mock(
            return_value=httpx.Response(
                200,
                json={
                    "success": True,
                    "payload": [
                        _sub_user(uuid="s", proxy_username="susp", suspended_at="2026-01-01"),
                        _sub_user(uuid="o", proxy_username="over", used_traffic=100, traffic_limit=100),
                        _sub_user(uuid="g", proxy_username="good", traffic_limit=0, used_traffic=9),
                    ],
                },
            )
        )
        assert "good-country-any" in client.connection_url()

    def test_raises_when_none_usable(self, client: ProxyHat, mock_api):
        mock_api.get("/sub-users").mock(
            return_value=httpx.Response(
                200,
                json={"success": True, "payload": [_sub_user(used_traffic=100, traffic_limit=100)]},
            )
        )
        with pytest.raises(ValueError, match="No usable sub-user"):
            client.connection_url()
