"""FastAPI application entry point.

The app imports the routers defined in the `routes` package and exposes
the API under the `/api` prefix. CORS middleware is added to allow
requests from the Flutter web client.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.flight_routes import router as flight_router
from .routes.booking_routes import router as booking_router

app = FastAPI(title="International Flight Booking API")

# Allow all origins for demo; tighten in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(flight_router, prefix="/api")
app.include_router(booking_router, prefix="/api")

@app.get("/health")
async def health_check():
    return {"status": "ok"}
