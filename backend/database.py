"""Database connection and session management.

Uses SQLAlchemy 2.0 style ``create_async_engine`` and ``async_sessionmaker``.
The engine is created once and reused across the application.
"""

from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from .config import settings

# Create the async engine.  ``asyncpg`` is the async driver for PostgreSQL.
engine: AsyncEngine = create_async_engine(settings.DATABASE_URL, echo=False, future=True)

# Async session factory
async_session: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSession
)

# Dependency for path operations
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

__all__ = ["engine", "async_session", "get_session"]
