"""FastAPI router for booking operations."""

from fastapi import APIRouter, Depends, HTTPException
from typing import List

from ..models.booking import Booking, BookingCreate

router = APIRouter()

# In-memory store for demo purposes
_bookings: List[Booking] = []

@router.post("/create", response_model=Booking)
async def create_booking(booking: BookingCreate):
    new_id = len(_bookings) + 1
    new_booking = Booking(id=new_id, **booking.dict())
    _bookings.append(new_booking)
    return new_booking

@router.get("/user/{user_id}", response_model=List[Booking])
async def get_user_bookings(user_id: int):
    return [b for b in _bookings if b.user_id == user_id]
