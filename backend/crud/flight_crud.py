"""CRUD helpers for the main domain entities.

Each function receives an async SQLAlchemy session and performs the
necessary database operations.  The functions are intentionally
stateless so that they can be reused across routers and tests.
"""

from __future__ import annotations

from typing import List, Optional

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Airline, Flight, User, Booking
from ..schemas.flight_schema import (
    AirlineCreate,
    AirlineRead,
    FlightCreate,
    FlightRead,
    UserCreate,
    UserRead,
    BookingCreate,
    BookingRead,
)

# ---------------------------------------------------------------------------
# Airline CRUD
# ---------------------------------------------------------------------------

async def create_airline(db: AsyncSession, airline_in: AirlineCreate) -> Airline:
    airline = Airline(**airline_in.model_dump())
    db.add(airline)
    await db.flush()
    return airline

async def get_airline(db: AsyncSession, airline_id: int) -> Optional[Airline]:
    result = await db.execute(select(Airline).where(Airline.id == airline_id))
    return result.scalar_one_or_none()

async def list_airlines(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Airline]:
    result = await db.execute(select(Airline).offset(skip).limit(limit))
    return result.scalars().all()

# ---------------------------------------------------------------------------
# Flight CRUD
# ---------------------------------------------------------------------------

async def create_flight(db: AsyncSession, flight_in: FlightCreate) -> Flight:
    flight = Flight(**flight_in.model_dump())
    db.add(flight)
    await db.flush()
    return flight

async def get_flight(db: AsyncSession, flight_id: int) -> Optional[Flight]:
    result = await db.execute(select(Flight).where(Flight.id == flight_id))
    return result.scalar_one_or_none()

async def list_flights(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Flight]:
    result = await db.execute(select(Flight).offset(skip).limit(limit))
    return result.scalars().all()

# ---------------------------------------------------------------------------
# User CRUD
# ---------------------------------------------------------------------------

async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
    user = User(email=user_in.email, hashed_password=user_in.password)
    db.add(user)
    await db.flush()
    return user

async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    result = await db.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()

async def get_user(db: AsyncSession, user_id: int) -> Optional[User]:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()

# ---------------------------------------------------------------------------
# Booking CRUD
# ---------------------------------------------------------------------------

async def create_booking(db: AsyncSession, booking_in: BookingCreate, user_id: int) -> Booking:
    booking = Booking(**booking_in.model_dump(), user_id=user_id)
    db.add(booking)
    await db.flush()
    return booking

async def get_booking(db: AsyncSession, booking_id: int) -> Optional[Booking]:
    result = await db.execute(select(Booking).where(Booking.id == booking_id))
    return result.scalar_one_or_none()

async def list_bookings(db: AsyncSession, user_id: int, skip: int = 0, limit: int = 100) -> List[Booking]:
    result = await db.execute(
        select(Booking).where(Booking.user_id == user_id).offset(skip).limit(limit)
    )
    return result.scalars().all()

# ---------------------------------------------------------------------------
# Exports
# ---------------------------------------------------------------------------

__all__ = [
    "create_airline",
    "get_airline",
    "list_airlines",
    "create_flight",
    "get_flight",
    "list_flights",
    "create_user",
    "get_user_by_email",
    "get_user",
    "create_booking",
    "get_booking",
    "list_bookings",
]
