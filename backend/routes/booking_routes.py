from fastapi import APIRouter, HTTPException
from ..models.booking import Booking
from datetime import datetime

router = APIRouter()

# Mock booking store
_bookings = []

@router.post("/create", response_model=Booking)
async def create_booking(user_id: str, flight_id: str):
    booking = Booking(
        booking_id="BK" + datetime.utcnow().strftime("%Y%m%d%H%M%S"),
        user_id=user_id,
        flight_id=flight_id,
        booking_time=datetime.utcnow(),
        status="confirmed",
    )
    _bookings.append(booking)
    return booking
