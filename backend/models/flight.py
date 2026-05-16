from pydantic import BaseModel, Field
from datetime import datetime

class Flight(BaseModel):
    flight_id: str = Field(..., description="Unique flight identifier")
    airline: str = Field(..., description="Airline name")
    origin: str = Field(..., description="IATA code of origin airport")
    destination: str = Field(..., description="IATA code of destination airport")
    departure_time: datetime = Field(..., description="Scheduled departure time (UTC)")
    arrival_time: datetime = Field(..., description="Scheduled arrival time (UTC)")
    price: float = Field(..., description="Ticket price in USD")
    layovers: int = Field(..., description="Number of layovers")
    duration_minutes: int = Field(..., description="Total flight duration in minutes")

    class Config:
        orm_mode = True
