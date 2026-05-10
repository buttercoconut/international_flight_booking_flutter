from pydantic import BaseModel
from typing import List

class Flight(BaseModel):
    flight_id: str
    airline: str
    origin: str
    destination: str
    departure_time: str
    arrival_time: str
    price: float
    layovers: int
    duration_minutes: int
    seats_available: int
