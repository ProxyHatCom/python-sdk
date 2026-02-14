import httpx

from proxyhat import ProxyHat
from proxyhat.types.locations import Country


class TestLocationsSync:
    def test_countries(self, client: ProxyHat, mock_api):
        mock_api.get("/locations/countries").mock(
            return_value=httpx.Response(
                200,
                json={
                    "success": True,
                    "payload": [
                        {
                            "code": "US",
                            "name": "United States",
                            "availability": "high",
                            "connection_type": "residential",
                        }
                    ],
                },
            )
        )
        result = client.locations.countries(connection_type="residential", limit=50)
        assert len(result) == 1
        assert isinstance(result[0], Country)
        assert result[0].code == "US"

    def test_countries_with_pagination(self, client: ProxyHat, mock_api):
        mock_api.get("/locations/countries").mock(
            return_value=httpx.Response(
                200,
                json={"success": True, "payload": []},
            )
        )
        result = client.locations.countries(limit=10, offset=100)
        assert result == []

    def test_regions(self, client: ProxyHat, mock_api):
        mock_api.get("/locations/regions").mock(
            return_value=httpx.Response(
                200,
                json={
                    "success": True,
                    "payload": [
                        {"code": "CA", "name": "California", "country_code": "US"},
                    ],
                },
            )
        )
        result = client.locations.regions(country__code="US")
        assert len(result) == 1
        assert result[0].code == "CA"

    def test_cities(self, client: ProxyHat, mock_api):
        mock_api.get("/locations/cities").mock(
            return_value=httpx.Response(
                200,
                json={
                    "success": True,
                    "payload": [
                        {"code": "LA", "name": "Los Angeles", "country_code": "US"},
                    ],
                },
            )
        )
        result = client.locations.cities(country__code="US", region__code="CA")
        assert len(result) == 1

    def test_isps(self, client: ProxyHat, mock_api):
        mock_api.get("/locations/isps").mock(
            return_value=httpx.Response(
                200,
                json={
                    "success": True,
                    "payload": [
                        {"code": "att", "name": "AT&T", "country_code": "US"},
                    ],
                },
            )
        )
        result = client.locations.isps(country__code="US")
        assert len(result) == 1

    def test_zipcodes(self, client: ProxyHat, mock_api):
        mock_api.get("/locations/zipcodes").mock(
            return_value=httpx.Response(
                200,
                json={
                    "success": True,
                    "payload": [
                        {"code": "90001", "name": "90001", "country_code": "US"},
                    ],
                },
            )
        )
        result = client.locations.zipcodes(country__code="US", city__code="LA")
        assert len(result) == 1
