"""FastAPI application entry point for International Flight Booking backend."""

from fastapi import FastAPI
from .routes import flight_routes, booking_routes, payment_routes

app = FastAPI(title="International Flight Booking API")

# Include routers
app.include_router(flight_routes.router, prefix="/flights", tags=["flights"])
app.include_router(booking_routes.router, prefix="/bookings", tags=["bookings"])
app.include_router(payment_routes.router, prefix="/payments", tags=["payments"])

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}
