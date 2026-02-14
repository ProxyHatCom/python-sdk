from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Country:
    code: str
    name: str
    availability: str
    connection_type: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Country:
        return cls(
            code=data.get("code", ""),
            name=data.get("name", ""),
            availability=data.get("availability", ""),
            connection_type=data.get("connection_type", ""),
        )


@dataclass
class Region:
    code: str
    name: str
    country_code: str
    availability: str | None = None
    connection_type: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Region:
        return cls(
            code=data.get("code", ""),
            name=data.get("name", ""),
            country_code=data.get("country_code", ""),
            availability=data.get("availability"),
            connection_type=data.get("connection_type"),
        )


@dataclass
class City:
    code: str
    name: str
    country_code: str
    region_code: str | None = None
    availability: str | None = None
    connection_type: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> City:
        return cls(
            code=data.get("code", ""),
            name=data.get("name", ""),
            country_code=data.get("country_code", ""),
            region_code=data.get("region_code"),
            availability=data.get("availability"),
            connection_type=data.get("connection_type"),
        )


@dataclass
class ISP:
    code: str
    name: str
    country_code: str
    availability: str | None = None
    connection_type: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ISP:
        return cls(
            code=data.get("code", ""),
            name=data.get("name", ""),
            country_code=data.get("country_code", ""),
            availability=data.get("availability"),
            connection_type=data.get("connection_type"),
        )


@dataclass
class Zipcode:
    code: str
    name: str
    country_code: str
    city_code: str | None = None
    availability: str | None = None
    connection_type: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Zipcode:
        return cls(
            code=data.get("code", ""),
            name=data.get("name", ""),
            country_code=data.get("country_code", ""),
            city_code=data.get("city_code"),
            availability=data.get("availability"),
            connection_type=data.get("connection_type"),
        )
