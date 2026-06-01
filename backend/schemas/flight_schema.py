"""Pydantic schemas for API request/response models.

The schemas are split into *request* and *response* variants to keep
validation clear.  They are used by the routers to validate incoming
data and to serialise database objects.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, EmailStr


# Airline schemas
class AirlineBase(BaseModel):
    name: str = Field(..., max_length=100)
    iata_code: str = Field(..., min_length=2, max_length=2)


class AirlineCreate(AirlineBase):
    pass


class AirlineRead(AirlineBase):
    id: int
    flights: List["FlightRead"] = []

    class Config:
        orm_mode = True


# Flight schemas
class FlightBase(BaseModel):
    flight_number: str = Field(..., max_length=10)
    departure_airport: str = Field(..., min_length=3, max_length=3)
    arrival_airport: str = Field(..., min_length=3, max_length=3)
    departure_time: datetime
    arrival_time: datetime
    status: Optional[str] = "scheduled"


class FlightCreate(FlightBase):
    airline_id: int


class FlightRead(FlightBase):
    id: int
    airline: AirlineRead
    bookings: List["BookingRead"] = []

    class Config:
        orm_mode = True


# User schemas
class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True


# Booking schemas
class BookingBase(BaseModel):
    passenger_name: str
    seat_number: Optional[str] = None
    price: float


class BookingCreate(BookingBase):
    flight_id: int


class BookingRead(BookingBase):
    id: int
    paid: bool
    user: UserRead
    flight: FlightRead

    class Config:
        orm_mode = True


__all__ = [
    "AirlineBase",
    "AirlineCreate",
    "AirlineRead",
    "FlightBase",
    "FlightCreate",
    "FlightRead",
    "UserBase",
    "UserCreate",
    "UserRead",
    "BookingBase",
    "BookingCreate",
    "BookingRead",
]
