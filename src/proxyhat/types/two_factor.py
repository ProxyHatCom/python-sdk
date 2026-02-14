from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class TwoFactorStatus:
    enabled: bool

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TwoFactorStatus:
        return cls(enabled=data.get("enabled", False))


@dataclass
class TwoFactorEnableResponse:
    qr: str
    secret: str
    recovery_codes: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TwoFactorEnableResponse:
        return cls(
            qr=data.get("qr", ""),
            secret=data.get("secret", ""),
            recovery_codes=data.get("recovery_codes", []),
        )


@dataclass
class RecoveryCodes:
    codes: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RecoveryCodes:
        return cls(codes=data if isinstance(data, list) else data.get("codes", []))
