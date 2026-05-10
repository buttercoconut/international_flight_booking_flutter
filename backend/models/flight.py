"""Pydantic models for the flight domain.

These models are used for request/response validation and for serialising
database rows when returning data to the client.
"""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

class FlightBase(BaseModel):
    flight_number: str = Field(..., example="AA1234")
    airline_code: str = Field(..., example="AA")
    departure_airport: str = Field(..., example="JFK")
    arrival_airport: str = Field(..., example="LHR")
    departure_time: datetime = Field(..., example="2024-07-01T08:00:00Z")
    arrival_time: datetime = Field(..., example="2024-07-01T20:00:00Z")
    price: float = Field(..., example=350.0)
    currency: str = Field(..., example="USD")
    layovers: int = Field(..., example=0)

class FlightCreate(FlightBase):
    pass

class FlightRead(FlightBase):
    id: int

class FlightSearchRequest(BaseModel):
    origin: str = Field(..., example="JFK")
    destination: str = Field(..., example="LHR")
    departure_date: str = Field(..., example="2024-07-01")
    passengers: int = Field(..., ge=1, le=9, example=1)

class FlightSearchResponse(BaseModel):
    flights: List[FlightRead]

# For database ORM mapping (SQLAlchemy) – kept minimal for brevity
# In a real project you would use declarative_base() and define tables.
