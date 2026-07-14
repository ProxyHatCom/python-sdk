# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.1] - 2026-07-14

### Fixed

- `User-Agent` header now derives from the installed package version (`proxyhat-python/0.2.1`) instead of a hardcoded `0.1.0` string, so it can no longer drift.

## [0.2.0] - 2026-07-13

### Added

- **Proxy connection helpers** — turn an API key or sub-user credentials into a ready proxy URL:
  - `client.connection_url(...)` (sync + async) — picks an active sub-user and builds the gateway URL
  - `build_connection_url()` / `build_proxy_username()` — offline gateway URL/username builder
  - `client.proxy_descriptors.create()` — server-built connection descriptor (`POST /v1/proxy-descriptors`)
- `SubUser.proxy_password` and `SubUser.suspended_at` fields

## [0.1.0] - 2026-02-13

### Added

- Initial release of the ProxyHat Python SDK
- Sync (`ProxyHat`) and async (`AsyncProxyHat`) clients
- Full coverage of ProxyHat API v1 endpoints
- Typed responses using dataclasses
- Comprehensive error handling with typed exceptions
- Pagination support for location endpoints
