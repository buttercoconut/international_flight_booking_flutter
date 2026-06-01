from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..models.booking import Booking, BookingCreate
from datetime import datetime

router = APIRouter()

# In-memory booking store
_bookings: List[Booking] = []

@router.post("/create", response_model=Booking)
async def create_booking(booking: BookingCreate):
    new_id = len(_bookings) + 1
    new_booking = Booking(id=new_id, **booking.dict(), status="confirmed", booking_time=datetime.utcnow())
    _bookings.append(new_booking)
    return new_booking

@router.get("/list", response_model=List[Booking])
async def list_bookings():
    return _bookings
