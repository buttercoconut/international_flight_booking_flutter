# routes/booking_routes.py
from fastapi import APIRouter, Depends, HTTPException
from ..models.booking import Booking
from ..models.flight import Flight

router = APIRouter(prefix="/bookings", tags=["bookings"])

# In-memory storage for demo
FAKE_BOOKINGS = []

@router.post("/create", response_model=Booking)
async def create_booking(booking: Booking):
    # In a real system, validate flight availability, deduct seats, etc.
    FAKE_BOOKINGS.append(booking)
    return booking

@router.get("/list", response_model=list[Booking])
async def list_bookings():
    return FAKE_BOOKINGS
