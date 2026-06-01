from pydantic import BaseModel
from datetime import datetime

class BookingBase(BaseModel):
    user_id: int
    flight_id: int
    passengers: int
    booking_time: datetime

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int
    status: str

    class Config:
        orm_mode = True
