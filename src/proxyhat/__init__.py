"""ProxyHat Python SDK — official client for the ProxyHat residential proxy API."""

from proxyhat.async_client import AsyncProxyHat
from proxyhat.client import ProxyHat
from proxyhat.errors import (
    APIError,
    AuthenticationError,
    NotFoundError,
    PermissionError,
    ProxyHatError,
    RateLimitError,
    ValidationError,
)

__all__ = [
    "APIError",
    "AsyncProxyHat",
    "AuthenticationError",
    "NotFoundError",
    "PermissionError",
    "ProxyHat",
    "ProxyHatError",
    "RateLimitError",
    "ValidationError",
]

__version__ = "0.1.0"
