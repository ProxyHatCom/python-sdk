# ProxyHat Python SDK

The official Python SDK for the [ProxyHat](https://proxyhat.com?utm_source=github&utm_medium=readme&utm_campaign=sdk-python&utm_content=hero) residential proxy API.

[![CI](https://github.com/ProxyHatCom/python-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/ProxyHatCom/python-sdk/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/proxyhat)](https://pypi.org/project/proxyhat/)
[![Python](https://img.shields.io/pypi/pyversions/proxyhat)](https://pypi.org/project/proxyhat/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Features

- **One-call proxy connection** — `client.connection_url()` turns your API key into a ready-to-use residential proxy URL
- Full coverage of the ProxyHat API
- Local gateway URL builder (`build_connection_url`) — no network needed
- Sync (`ProxyHat`) and async (`AsyncProxyHat`) clients
- Typed responses using dataclasses
- Comprehensive error handling with typed exceptions
- Pagination support for location endpoints

## Installation

```bash
pip install proxyhat
```

## Quick Start

```python
from proxyhat import ProxyHat

client = ProxyHat(api_key="ph_your_api_key")

# List sub-users
users = client.sub_users.list()
for user in users:
    print(user.proxy_username, user.lifecycle_status)

# Create a sub-user
new_user = client.sub_users.create(
    proxy_password="secure_pass",
    is_traffic_limited=True,
    traffic_limit="5GB",
    name="Scraper",
)
print(new_user.uuid)
```

### Async Usage

```python
import asyncio
from proxyhat import AsyncProxyHat

async def main():
    async with AsyncProxyHat(api_key="ph_your_api_key") as client:
        users = await client.sub_users.list()
        for user in users:
            print(user.proxy_username)

asyncio.run(main())
```

## Connecting to a proxy

From an API key to actually routing traffic in one call — the SDK looks up an active sub-user and builds the gateway URL for you:

```python
from proxyhat import ProxyHat

proxy = ProxyHat(api_key="ph_your_api_key")

# Rotating residential IP, US exit:
url = proxy.connection_url(country="us")
# → http://<user>-country-us:<pass>@gate.proxyhat.com:8080

# Sticky session (same IP for 30m), city-targeted, SOCKS5:
sticky = proxy.connection_url(country="de", city="berlin", sticky="30m", protocol="socks5")

# Use it with any HTTP client:
import httpx
resp = httpx.get("https://api.ipify.org", proxy=url)
```

**Offline builder** — if you already have a sub-user's credentials, build the URL with no network call:

```python
from proxyhat import build_connection_url

url = build_connection_url(username="ph-8f2a1c", password="PxSecret123", country="gb", filter="high")
```

**Server-built descriptor** — let the API assemble it (validates the sub-user is active):

```python
d = proxy.proxy_descriptors.create(
    sub_user_uuid=user.uuid,
    protocol="http",
    location={"country": "us", "city": "new_york"},
    session={"mode": "sticky", "ttl": "30m"},
)
print(d.url)
```

## Authentication

Get your API key from the [ProxyHat Dashboard](https://dashboard.proxyhat.com/register?utm_source=github&utm_medium=readme&utm_campaign=sdk-python&utm_content=signup).

See the [Authentication Guide](https://docs.proxyhat.com/authentication?utm_source=github&utm_medium=readme&utm_campaign=sdk-python&utm_content=auth-guide) for details.

## API Reference

| Resource | Methods |
|----------|---------|
| `client.auth` | `register`, `login`, `user`, `logout`, `supported_providers`, `social_accounts`, `disconnect_social`, `oauth_redirect` |
| `client.sub_users` | `list`, `create`, `get`, `update`, `delete`, `reset_usage`, `bulk_delete`, `bulk_move_to_group` |
| `client.sub_user_groups` | `list`, `create`, `get`, `update`, `delete` |
| `client.locations` | `countries`, `regions`, `cities`, `isps`, `zipcodes` |
| `client.analytics` | `traffic`, `traffic_total`, `requests`, `requests_total`, `domain_breakdown` |
| `client.proxy_presets` | `list`, `create`, `get`, `update`, `delete` |
| `client.proxy_descriptors` | `create` |
| `client.connection_url(...)` | build a ready proxy URL from an active sub-user |
| `client.profile` | `get_preferences`, `update_preferences`, `list_api_keys`, `create_api_key`, `delete_api_key`, `regenerate_api_key` |
| `client.two_factor` | `status`, `enable`, `confirm`, `disable`, `qr_code`, `recovery_codes`, `disable_by_recovery`, `change_password` |
| `client.email` | `request_change`, `confirm_change`, `cancel_change`, `resend_verification` |
| `client.coupons` | `validate`, `apply`, `redeem` |
| `client.plans` | `list_regular`, `list_subscriptions`, `get_regular`, `get_subscription`, `pricing_regular`, `pricing_subscriptions` |
| `client.payments` | `list`, `create`, `get`, `check`, `invoice`, `cryptocurrencies` |

## Error Handling

```python
from proxyhat import ProxyHat, ProxyHatError, NotFoundError, RateLimitError, ValidationError

client = ProxyHat(api_key="ph_your_api_key")

try:
    user = client.sub_users.get("nonexistent-id")
except NotFoundError as e:
    print(f"Not found: {e.message}")
except RateLimitError as e:
    print(f"Rate limited. Retry after {e.retry_after}s")
except ValidationError as e:
    print(f"Validation failed: {e.errors}")
except ProxyHatError as e:
    print(f"API error {e.status_code}: {e.message}")
```

See the [Error Handling Guide](https://docs.proxyhat.com/errors?utm_source=github&utm_medium=readme&utm_campaign=sdk-python&utm_content=error-handling) for the full list of error codes.

## Documentation

- [Getting Started](https://docs.proxyhat.com?utm_source=github&utm_medium=readme&utm_campaign=sdk-python&utm_content=getting-started)
- [API Reference](https://docs.proxyhat.com/api/auth?utm_source=github&utm_medium=readme&utm_campaign=sdk-python&utm_content=api-reference)
- [Full Documentation](https://docs.proxyhat.com?utm_source=github&utm_medium=readme&utm_campaign=sdk-python&utm_content=docs-home)

## Links

- [ProxyHat](https://proxyhat.com?utm_source=github&utm_medium=readme&utm_campaign=sdk-python&utm_content=links) — Residential & mobile proxy network
- [Dashboard](https://dashboard.proxyhat.com?utm_source=github&utm_medium=readme&utm_campaign=sdk-python&utm_content=links) — Manage proxies, sub-users, and API keys
- [GitHub](https://github.com/ProxyHatCom/python-sdk) — Source code & issue tracker

## License

MIT — see [LICENSE](LICENSE) for details.
