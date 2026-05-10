from pydantic import BaseModel
from datetime import datetime

class Booking(BaseModel):
    booking_id: str
    user_id: str
    flight_id: str
    booking_time: datetime
    status: str
    # Additional fields like seat, class, etc.
