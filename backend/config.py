"""Application configuration using Pydantic BaseSettings.

This module centralises all environment variables required by the
backend.  It is intentionally lightweight so that the rest of the
application can import ``settings`` without pulling in heavy
dependencies.

Typical variables:

* ``DATABASE_URL`` – PostgreSQL connection string.
* ``SECRET_KEY`` – JWT signing key.
* ``ALGORITHM`` – JWT algorithm (HS256 by default).
* ``ACCESS_TOKEN_EXPIRE_MINUTES`` – token lifetime.
* ``ENV`` – ``development`` / ``production``.

The values are loaded from the environment and can be overridden by a
`.env` file in the project root.
"""

from __future__ import annotations

from datetime import timedelta
from pathlib import Path

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Application settings.

    The class inherits from :class:`pydantic.BaseSettings` which
    automatically reads environment variables and supports a ``.env``
    file.
    """

    # Database
    DATABASE_URL: str = Field(
        ...,
        description="PostgreSQL connection URL, e.g. postgres://user:pass@localhost/dbname",
    )

    # JWT
    SECRET_KEY: str = Field(
        ...,
        description="Secret key used to sign JWT tokens.",
    )
    ALGORITHM: str = Field("HS256", description="JWT signing algorithm.")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(
        30,
        description="Access token lifetime in minutes.",
    )

    # Environment
    ENV: str = Field("development", description="Application environment.")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instantiate a single global settings object
settings = Settings()

# Helper for token expiration
access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

__all__ = ["settings", "access_token_expires"]
