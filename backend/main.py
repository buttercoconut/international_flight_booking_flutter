"""Main FastAPI application.

The app imports the routers defined in ``routers`` and exposes a
single ``/docs`` endpoint for Swagger UI.  The database tables are
created automatically on startup using the ``Base.metadata.create_all``
method.  In a production setting you would normally use Alembic for
migrations, but for this example the simple approach keeps the
project lightweight.
"""

from __future__ import annotations

import asyncio
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine

from .config import settings
from .database import engine
from .models import Base
from .routers import flight_routes, auth_routes

app = FastAPI(title="International Flight Booking API", version="0.1.0")

# Register routers
app.include_router(flight_routes.router)
app.include_router(auth_routes.router)

# ---------------------------------------------------------------
# Startup / shutdown events
# ---------------------------------------------------------------

@app.on_event("startup")
async def on_startup():
    # Create tables if they don't exist – this is fine for a demo
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# ---------------------------------------------------------------
# Health check
# ---------------------------------------------------------------

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# ---------------------------------------------------------------
# Run with: uvicorn backend.main:app --reload
# ---------------------------------------------------------------

__all__ = ["app"]
