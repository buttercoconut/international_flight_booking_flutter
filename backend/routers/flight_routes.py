"""FastAPI routers for the flight booking API.

Each router focuses on a single resource type and uses the CRUD
helpers defined in ``crud/flight_crud.py``.  The routers are
intentionally lightweight – they only orchestrate request
validation, database interaction and response serialisation.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_session
from ..crud.flight_crud import (
    create_airline,
    get_airline,
    list_airlines,
    create_flight,
    get_flight,
    list_flights,
    create_booking,
    get_booking,
    list_bookings,
)
from ..schemas.flight_schema import (
    AirlineCreate,
    AirlineRead,
    FlightCreate,
    FlightRead,
    BookingCreate,
    BookingRead,
)

router = APIRouter(prefix="/flights", tags=["flights"])

# Airline endpoints
@router.post("/airlines", response_model=AirlineRead, status_code=status.HTTP_201_CREATED)
async def create_airline_endpoint(
    airline_in: AirlineCreate, db: AsyncSession = Depends(get_session)
):
    airline = await create_airline(db, airline_in)
    await db.commit()
    return airline

@router.get("/airlines", response_model=list[AirlineRead])
async def list_airlines_endpoint(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)):
    airlines = await list_airlines(db, skip, limit)
    return airlines

@router.get("/airlines/{airline_id}", response_model=AirlineRead)
async def get_airline_endpoint(airline_id: int, db: AsyncSession = Depends(get_session)):
    airline = await get_airline(db, airline_id)
    if not airline:
        raise HTTPException(status_code=404, detail="Airline not found")
    return airline

# Flight endpoints
@router.post("/", response_model=FlightRead, status_code=status.HTTP_201_CREATED)
async def create_flight_endpoint(flight_in: FlightCreate, db: AsyncSession = Depends(get_session)):
    flight = await create_flight(db, flight_in)
    await db.commit()
    return flight

@router.get("/", response_model=list[FlightRead])
async def list_flights_endpoint(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)):
    flights = await list_flights(db, skip, limit)
    return flights

@router.get("/{flight_id}", response_model=FlightRead)
async def get_flight_endpoint(flight_id: int, db: AsyncSession = Depends(get_session)):
    flight = await get_flight(db, flight_id)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight

# Booking endpoints
@router.post("/bookings", response_model=BookingRead, status_code=status.HTTP_201_CREATED)
async def create_booking_endpoint(
    booking_in: BookingCreate, user_id: int, db: AsyncSession = Depends(get_session)
):
    booking = await create_booking(db, booking_in, user_id)
    await db.commit()
    return booking

@router.get("/bookings", response_model=list[BookingRead])
async def list_bookings_endpoint(user_id: int, skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)):
    bookings = await list_bookings(db, user_id, skip, limit)
    return bookings

@router.get("/bookings/{booking_id}", response_model=BookingRead)
async def get_booking_endpoint(booking_id: int, db: AsyncSession = Depends(get_session)):
    booking = await get_booking(db, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

__all__ = ["router"]
