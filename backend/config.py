"""Configuration for the backend service.

This module loads environment variables and provides a central place for
application settings such as database URLs, API keys, and other secrets.
"""

from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = Field(
        "postgresql://user:password@localhost:5432/international_flight_booking",
        env="DATABASE_URL",
    )

    # Amadeus API credentials (placeholder)
    AMADEUS_CLIENT_ID: str = Field("", env="AMADEUS_CLIENT_ID")
    AMADEUS_CLIENT_SECRET: str = Field("", env="AMADEUS_CLIENT_SECRET")

    # Stripe API key (placeholder)
    STRIPE_SECRET_KEY: str = Field("", env="STRIPE_SECRET_KEY")

    # Email service API key (placeholder)
    SENDGRID_API_KEY: str = Field("", env="SENDGRID_API_KEY")

    # Other settings
    DEBUG: bool = Field(False, env="DEBUG")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Instantiate a global settings object
settings = Settings()
