# models/booking.py
from pydantic import BaseModel
from typing import List

class Booking(BaseModel):
    booking_id: str
    user_id: str
    flight_id: str
    passengers: int
    total_price: float
    status: str  # e.g., 'confirmed', 'cancelled'
    booking_time: str  # ISO 8601
