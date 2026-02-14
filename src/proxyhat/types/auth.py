from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class RegisterResponse:
    message: str
    access_token: str
    token_type: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RegisterResponse:
        return cls(
            message=data.get("message", ""),
            access_token=data.get("accessToken", ""),
            token_type=data.get("tokenType", ""),
        )


@dataclass
class LoginResponse:
    access_token: str
    token_type: str
    requires_2fa: bool = False

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> LoginResponse:
        return cls(
            access_token=data.get("accessToken", ""),
            token_type=data.get("tokenType", ""),
            requires_2fa=data.get("requires_2fa", False),
        )


@dataclass
class TrafficInfo:
    subscription: str | None
    subscription_starts_at: str | None
    subscription_expires_at: str | None
    regular_bytes: int
    regular_human: str
    subscription_bytes: int
    subscription_human: str
    total_bytes: int
    total_human: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TrafficInfo:
        return cls(
            subscription=data.get("subscription"),
            subscription_starts_at=data.get("subscription_starts_at"),
            subscription_expires_at=data.get("subscription_expires_at"),
            regular_bytes=data.get("regular_bytes", 0),
            regular_human=data.get("regular_human", ""),
            subscription_bytes=data.get("subscription_bytes", 0),
            subscription_human=data.get("subscription_human", ""),
            total_bytes=data.get("total_bytes", 0),
            total_human=data.get("total_human", ""),
        )


@dataclass
class User:
    uuid: str
    name: str
    email: str
    traffic: TrafficInfo

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> User:
        return cls(
            uuid=data.get("uuid", ""),
            name=data.get("name", ""),
            email=data.get("email", ""),
            traffic=TrafficInfo.from_dict(data.get("traffic", {})),
        )


@dataclass
class SupportedProvider:
    name: str
    slug: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SupportedProvider:
        return cls(
            name=data.get("name", ""),
            slug=data.get("slug", ""),
        )


@dataclass
class SocialAccount:
    provider: str
    email: str | None
    connected_at: str | None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SocialAccount:
        return cls(
            provider=data.get("provider", ""),
            email=data.get("email"),
            connected_at=data.get("connected_at"),
        )
