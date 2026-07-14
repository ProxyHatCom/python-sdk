"""ProxyHat Python SDK — official client for the ProxyHat residential proxy API."""

from proxyhat.async_client import AsyncProxyHat
from proxyhat.client import ProxyHat
from proxyhat.connection import (
    PROXYHAT_GATEWAY,
    PROXYHAT_PORT_HTTP,
    PROXYHAT_PORT_SOCKS5,
    build_connection_url,
    build_proxy_username,
)
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
    "PROXYHAT_GATEWAY",
    "PROXYHAT_PORT_HTTP",
    "PROXYHAT_PORT_SOCKS5",
    "APIError",
    "AsyncProxyHat",
    "AuthenticationError",
    "NotFoundError",
    "PermissionError",
    "ProxyHat",
    "ProxyHatError",
    "RateLimitError",
    "ValidationError",
    "build_connection_url",
    "build_proxy_username",
]

__version__ = "0.2.1"
