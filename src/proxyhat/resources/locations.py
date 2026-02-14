from __future__ import annotations

from typing import TYPE_CHECKING, Any

from proxyhat.types.locations import ISP, City, Country, Region, Zipcode

if TYPE_CHECKING:
    from proxyhat.async_client import AsyncProxyHat
    from proxyhat.client import ProxyHat


def _location_params(
    limit: int | None = None,
    offset: int | None = None,
    name: str | None = None,
    connection_type: str | None = None,
    **kwargs: Any,
) -> dict[str, Any]:
    params: dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if name is not None:
        params["name"] = name
    if connection_type is not None:
        params["connection_type"] = connection_type
    params.update({k: v for k, v in kwargs.items() if v is not None})
    return params


class LocationsResource:
    def __init__(self, client: ProxyHat) -> None:
        self._client = client

    def countries(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        name: str | None = None,
        connection_type: str | None = None,
    ) -> list[Country]:
        params = _location_params(limit=limit, offset=offset, name=name, connection_type=connection_type)
        data = self._client.request("GET", "/locations/countries", params=params)
        if isinstance(data, list):
            return [Country.from_dict(item) for item in data]
        return []

    def regions(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        name: str | None = None,
        connection_type: str | None = None,
        country__code: str | None = None,
    ) -> list[Region]:
        params = _location_params(
            limit=limit, offset=offset, name=name, connection_type=connection_type, country__code=country__code
        )
        data = self._client.request("GET", "/locations/regions", params=params)
        if isinstance(data, list):
            return [Region.from_dict(item) for item in data]
        return []

    def cities(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        name: str | None = None,
        connection_type: str | None = None,
        country__code: str | None = None,
        region__code: str | None = None,
    ) -> list[City]:
        params = _location_params(
            limit=limit,
            offset=offset,
            name=name,
            connection_type=connection_type,
            country__code=country__code,
            region__code=region__code,
        )
        data = self._client.request("GET", "/locations/cities", params=params)
        if isinstance(data, list):
            return [City.from_dict(item) for item in data]
        return []

    def isps(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        name: str | None = None,
        connection_type: str | None = None,
        country__code: str | None = None,
    ) -> list[ISP]:
        params = _location_params(
            limit=limit, offset=offset, name=name, connection_type=connection_type, country__code=country__code
        )
        data = self._client.request("GET", "/locations/isps", params=params)
        if isinstance(data, list):
            return [ISP.from_dict(item) for item in data]
        return []

    def zipcodes(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        name: str | None = None,
        connection_type: str | None = None,
        country__code: str | None = None,
        city__code: str | None = None,
    ) -> list[Zipcode]:
        params = _location_params(
            limit=limit,
            offset=offset,
            name=name,
            connection_type=connection_type,
            country__code=country__code,
            city__code=city__code,
        )
        data = self._client.request("GET", "/locations/zipcodes", params=params)
        if isinstance(data, list):
            return [Zipcode.from_dict(item) for item in data]
        return []


class AsyncLocationsResource:
    def __init__(self, client: AsyncProxyHat) -> None:
        self._client = client

    async def countries(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        name: str | None = None,
        connection_type: str | None = None,
    ) -> list[Country]:
        params = _location_params(limit=limit, offset=offset, name=name, connection_type=connection_type)
        data = await self._client.request("GET", "/locations/countries", params=params)
        if isinstance(data, list):
            return [Country.from_dict(item) for item in data]
        return []

    async def regions(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        name: str | None = None,
        connection_type: str | None = None,
        country__code: str | None = None,
    ) -> list[Region]:
        params = _location_params(
            limit=limit, offset=offset, name=name, connection_type=connection_type, country__code=country__code
        )
        data = await self._client.request("GET", "/locations/regions", params=params)
        if isinstance(data, list):
            return [Region.from_dict(item) for item in data]
        return []

    async def cities(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        name: str | None = None,
        connection_type: str | None = None,
        country__code: str | None = None,
        region__code: str | None = None,
    ) -> list[City]:
        params = _location_params(
            limit=limit,
            offset=offset,
            name=name,
            connection_type=connection_type,
            country__code=country__code,
            region__code=region__code,
        )
        data = await self._client.request("GET", "/locations/cities", params=params)
        if isinstance(data, list):
            return [City.from_dict(item) for item in data]
        return []

    async def isps(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        name: str | None = None,
        connection_type: str | None = None,
        country__code: str | None = None,
    ) -> list[ISP]:
        params = _location_params(
            limit=limit, offset=offset, name=name, connection_type=connection_type, country__code=country__code
        )
        data = await self._client.request("GET", "/locations/isps", params=params)
        if isinstance(data, list):
            return [ISP.from_dict(item) for item in data]
        return []

    async def zipcodes(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        name: str | None = None,
        connection_type: str | None = None,
        country__code: str | None = None,
        city__code: str | None = None,
    ) -> list[Zipcode]:
        params = _location_params(
            limit=limit,
            offset=offset,
            name=name,
            connection_type=connection_type,
            country__code=country__code,
            city__code=city__code,
        )
        data = await self._client.request("GET", "/locations/zipcodes", params=params)
        if isinstance(data, list):
            return [Zipcode.from_dict(item) for item in data]
        return []
