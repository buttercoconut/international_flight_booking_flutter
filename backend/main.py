from fastapi import FastAPI
from .routes import flight_routes, booking_routes, payment_routes
from .config import settings

app = FastAPI(title=settings.APP_NAME)

app.include_router(flight_routes.router, prefix="/flights", tags=["flights"])
app.include_router(booking_routes.router, prefix="/bookings", tags=["bookings"])
app.include_router(payment_routes.router, prefix="/payments", tags=["payments"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to International Flight Booking API"}
