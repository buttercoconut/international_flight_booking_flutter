"""Utility functions for password hashing and JWT token creation.

The implementation uses ``passlib`` for hashing and ``python-jose`` for
JWT handling.  The functions are intentionally small so that they can
be unit‑tested in isolation.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any

from jose import jwt
from passlib.context import CryptContext

from ..config import settings

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Return a bcrypt hash of the given password."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a stored hash."""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict[str, Any], expires_delta: timedelta | None = None) -> str:
    """Create a JWT access token.

    Parameters
    ----------
    data:
        Payload data (usually ``{"sub": user_id}``).
    expires_delta:
        Optional custom expiration.  If omitted, the default from
        ``settings.ACCESS_TOKEN_EXPIRE_MINUTES`` is used.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


__all__ = ["hash_password", "verify_password", "create_access_token"]
