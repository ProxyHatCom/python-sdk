"""ProxyHat gateway connection helpers.

The API resources manage your account; these helpers turn a sub-user's
``proxy_username`` / ``proxy_password`` into a ready-to-use proxy URL, building
the gateway username with ProxyHat's targeting grammar. Everything here is
offline (no network) — see https://docs.proxyhat.com/connecting.
"""

from __future__ import annotations

import secrets
from typing import Literal
from urllib.parse import quote

PROXYHAT_GATEWAY = "gate.proxyhat.com"
PROXYHAT_PORT_HTTP = 8080
PROXYHAT_PORT_SOCKS5 = 1080

ProxyProtocol = Literal["http", "socks5"]


def _slug(value: str) -> str:
    return "_".join(value.strip().lower().split())


def build_proxy_username(
    base: str,
    *,
    country: str | None = None,
    region: str | None = None,
    city: str | None = None,
    sticky: bool | str | None = None,
    filter: str | None = None,
) -> str:
    """Build a gateway username from a base ``proxy_username`` plus targeting tokens.

    Fixed order: ``<base>-country-<iso>[-region-<slug>][-city-<slug>]``
    ``[-sid-<16hex>-ttl-<dur>]-filter-<tier>``.

    ``sticky``: ``True`` → 30m default; a string sets the TTL ("30m"/"12h");
    omit / ``False`` for a fresh rotating IP per request.
    """
    parts = [base.strip(), "country", (country or "any").strip().lower()]

    if region and region.strip().lower() != "any":
        parts += ["region", _slug(region)]
    if city:
        parts += ["city", _slug(city)]
    if sticky is not None and sticky is not False:
        if sticky is True:
            ttl = "30m"
        else:
            raw = str(sticky).strip()
            ttl = "30m" if raw.lower() in ("", "true", "1", "yes", "on") else raw
        parts += ["sid", secrets.token_hex(8), "ttl", ttl]
    if isinstance(filter, str):
        tier = filter.strip().lower()
        if tier.startswith("filter-"):
            tier = tier[len("filter-") :]
        if tier and tier != "none":
            parts += ["filter", tier]

    return "-".join(parts)


def build_connection_url(
    *,
    username: str,
    password: str,
    country: str | None = None,
    region: str | None = None,
    city: str | None = None,
    sticky: bool | str | None = None,
    filter: str | None = None,
    protocol: ProxyProtocol = "http",
) -> str:
    """Build a full proxy connection URL for the ProxyHat gateway.

    Example: ``http://<user>-country-us:<pass>@gate.proxyhat.com:8080``.
    """
    port = PROXYHAT_PORT_SOCKS5 if protocol == "socks5" else PROXYHAT_PORT_HTTP
    user = build_proxy_username(
        username,
        country=country,
        region=region,
        city=city,
        sticky=sticky,
        filter=filter,
    )
    return f"{protocol}://{quote(user, safe='')}:{quote(password, safe='')}@{PROXYHAT_GATEWAY}:{port}"
