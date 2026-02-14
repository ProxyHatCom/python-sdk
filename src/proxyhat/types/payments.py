from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class PaymentCreateResponse:
    success: bool
    payment_id: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> PaymentCreateResponse:
        return cls(
            success=data.get("success", False),
            payment_id=data.get("payment_id", ""),
        )


@dataclass
class CryptoInfo:
    code: str
    currency: str
    network: str
    icon: str | None = None
    label: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CryptoInfo:
        return cls(
            code=data.get("code", ""),
            currency=data.get("currency", ""),
            network=data.get("network", ""),
            icon=data.get("icon"),
            label=data.get("label"),
        )


@dataclass
class PaymentDetails:
    pay_address: str
    crypto_amount: float
    amount_usd: float
    crypto: CryptoInfo
    status: str
    tx_hash: str | None = None
    expires_at: str | None = None
    completed_at: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> PaymentDetails:
        return cls(
            pay_address=data.get("pay_address", ""),
            crypto_amount=data.get("crypto_amount", 0.0),
            amount_usd=data.get("amount_usd", 0.0),
            crypto=CryptoInfo.from_dict(data.get("crypto", {})),
            status=data.get("status", ""),
            tx_hash=data.get("tx_hash"),
            expires_at=data.get("expires_at"),
            completed_at=data.get("completed_at"),
        )


@dataclass
class Payment:
    id: str
    type: str
    status: str
    amount: float | None = None
    currency: str | None = None
    created_at: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Payment:
        return cls(
            id=data.get("id", ""),
            type=data.get("type", ""),
            status=data.get("status", ""),
            amount=data.get("amount"),
            currency=data.get("currency"),
            created_at=data.get("created_at"),
        )


@dataclass
class Cryptocurrency:
    code: str
    currency: str
    network: str
    icon: str | None = None
    label: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Cryptocurrency:
        return cls(
            code=data.get("code", ""),
            currency=data.get("currency", ""),
            network=data.get("network", ""),
            icon=data.get("icon"),
            label=data.get("label"),
        )
