"""Pydantic models for Booking entity."""

from pydantic import BaseModel, Field
from datetime import datetime

class BookingBase(BaseModel):
    user_id: int
    flight_id: int
    passengers: int = Field(..., ge=1)
    booking_time: datetime
    total_price: float

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True
