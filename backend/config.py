from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "International Flight Booking"
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/flightdb"
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
