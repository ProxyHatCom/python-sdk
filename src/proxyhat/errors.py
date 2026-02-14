from __future__ import annotations

from typing import Any


class ProxyHatError(Exception):
    """Base exception for all ProxyHat SDK errors."""

    message: str
    status_code: int | None
    errors: Any

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        errors: Any = None,
    ) -> None:
        self.message = message
        self.status_code = status_code
        self.errors = errors
        super().__init__(message)


class AuthenticationError(ProxyHatError):
    """Raised on 401 Unauthorized responses."""

    def __init__(self, message: str = "Unauthorized", errors: Any = None) -> None:
        super().__init__(message, status_code=401, errors=errors)


class PermissionError(ProxyHatError):
    """Raised on 403 Forbidden responses."""

    def __init__(self, message: str = "Forbidden", errors: Any = None) -> None:
        super().__init__(message, status_code=403, errors=errors)


class NotFoundError(ProxyHatError):
    """Raised on 404 Not Found responses."""

    def __init__(self, message: str = "Not Found", errors: Any = None) -> None:
        super().__init__(message, status_code=404, errors=errors)


class ValidationError(ProxyHatError):
    """Raised on 422 Unprocessable Entity responses. Includes field-level errors."""

    def __init__(self, message: str = "Validation Error", errors: Any = None) -> None:
        super().__init__(message, status_code=422, errors=errors)


class RateLimitError(ProxyHatError):
    """Raised on 429 Too Many Requests responses."""

    retry_after: int | None

    def __init__(
        self,
        message: str = "Rate Limited",
        errors: Any = None,
        retry_after: int | None = None,
    ) -> None:
        super().__init__(message, status_code=429, errors=errors)
        self.retry_after = retry_after


class APIError(ProxyHatError):
    """Raised for all other HTTP errors (500, etc.)."""

    def __init__(self, message: str = "API Error", status_code: int = 500, errors: Any = None) -> None:
        super().__init__(message, status_code=status_code, errors=errors)
