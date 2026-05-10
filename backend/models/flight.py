from pydantic import BaseModel
from datetime import datetime

class Flight(BaseModel):
    flight_id: str
    airline: str
    origin: str
    destination: str
    departure_time: datetime
    arrival_time: datetime
    price: float
    layovers: int
    duration_minutes: int
    # Additional fields can be added as needed
