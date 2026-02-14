from __future__ import annotations

from typing import Any

from proxyhat.errors import (
    APIError,
    AuthenticationError,
    NotFoundError,
    PermissionError,
    RateLimitError,
    ValidationError,
)

DEFAULT_BASE_URL = "https://api.proxyhat.com/v1"
DEFAULT_TIMEOUT = 30.0
USER_AGENT = "proxyhat-python/0.1.0"


def _build_headers(api_key: str | None) -> dict[str, str]:
    headers: dict[str, str] = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
    }
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    return headers


def _raise_for_status(status_code: int, body: Any, headers: Any) -> None:
    if 200 <= status_code < 300:
        return

    message = ""
    errors = None

    if isinstance(body, dict):
        message = body.get("description", "") or body.get("message", "")
        errors = body.get("errors")

    if not message:
        message = f"HTTP {status_code}"

    if status_code == 401:
        raise AuthenticationError(message=message, errors=errors)
    elif status_code == 403:
        raise PermissionError(message=message, errors=errors)
    elif status_code == 404:
        raise NotFoundError(message=message, errors=errors)
    elif status_code == 422:
        raise ValidationError(message=message, errors=errors)
    elif status_code == 429:
        retry_after = None
        retry_header = headers.get("retry-after") if hasattr(headers, "get") else None
        if retry_header:
            try:
                retry_after = int(retry_header)
            except (ValueError, TypeError):
                pass
        raise RateLimitError(message=message, errors=errors, retry_after=retry_after)
    else:
        raise APIError(message=message, status_code=status_code, errors=errors)


def _parse_json_body(response: Any) -> Any:
    """Attempt to parse response as JSON, return empty dict on failure."""
    content_type = response.headers.get("content-type", "")
    if "application/json" not in content_type:
        return {}
    try:
        return response.json()
    except Exception:
        return {}


class BaseClientConfig:
    """Shared configuration for sync and async clients."""

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    @property
    def headers(self) -> dict[str, str]:
        return _build_headers(self.api_key)

    def build_url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    @staticmethod
    def handle_response(status_code: int, body: Any, headers: Any) -> Any:
        _raise_for_status(status_code, body, headers)

        if isinstance(body, dict):
            if "payload" in body:
                return body["payload"]
            if "data" in body:
                return body["data"]
        return body
