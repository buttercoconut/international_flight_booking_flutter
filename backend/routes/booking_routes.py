"""FastAPI routes for booking and payment.

These endpoints are placeholders. In a production system you would
persist bookings to a database, integrate with Stripe for payment,
and send confirmation emails via SendGrid.
"""

from fastapi import APIRouter, Depends, HTTPException
from typing import List

from ..config import settings
from ..models.booking import BookingCreate, BookingRead

router = APIRouter(prefix="/bookings", tags=["bookings"])

# In-memory store for demo purposes
_bookings: List[BookingRead] = []

@router.post("/", response_model=BookingRead)
async def create_booking(booking: BookingCreate):
    # In a real app, validate flight existence, seat availability, etc.
    new_id = len(_bookings) + 1
    booking_read = BookingRead(**booking.dict(), id=new_id)
    _bookings.append(booking_read)
    return booking_read

@router.get("/", response_model=List[BookingRead])
async def list_bookings():
    return _bookings

# Payment endpoint – stubbed
@router.post("/pay", response_model=dict)
async def pay_booking(booking_id: int):
    # In a real system, create a Stripe PaymentIntent, confirm payment,
    # and update booking status.
    for b in _bookings:
        if b.id == booking_id:
            return {"status": "paid", "booking_id": booking_id}
    raise HTTPException(status_code=404, detail="Booking not found")
