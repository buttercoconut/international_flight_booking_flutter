"""Pydantic model for Booking.
"""

from datetime import datetime
from pydantic import BaseModel, Field

class BookingBase(BaseModel):
    user_id: int = Field(..., example=1)
    flight_id: int = Field(..., example=42)
    passengers: int = Field(..., ge=1, le=9, example=1)
    total_price: float = Field(..., example=350.0)
    booking_time: datetime = Field(default_factory=datetime.utcnow)

class BookingCreate(BookingBase):
    pass

class BookingRead(BookingBase):
    id: int
