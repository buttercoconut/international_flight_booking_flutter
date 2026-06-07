"""Pydantic models for Flight entity."""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class FlightBase(BaseModel):
    flight_number: str = Field(..., example="AA123")
    airline_id: int
    origin: str = Field(..., example="JFK")
    destination: str = Field(..., example="LHR")
    departure_time: datetime
    arrival_time: datetime
    price: float
    currency: str = Field(..., example="USD")
    layovers: int = Field(0, ge=0)

class FlightCreate(FlightBase):
    pass

class Flight(FlightBase):
    id: int

    class Config:
        orm_mode = True
