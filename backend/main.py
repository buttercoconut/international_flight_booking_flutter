# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.flight_routes import router as flight_router
from .routes.booking_routes import router as booking_router

app = FastAPI(title="International Flight Booking API")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(flight_router)
app.include_router(booking_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the International Flight Booking API"}
