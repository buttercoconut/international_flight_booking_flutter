from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from datetime import datetime
from ..models.flight import Flight, FlightCreate
from ..config import settings

router = APIRouter()

# In-memory flight store for demo purposes
_flights: List[Flight] = []

# Seed some flights
_flights.append(Flight(id=1, flight_number="AA101", airline_id=1, origin="JFK", destination="LHR", departure_time=datetime(2024, 10, 1, 8, 0), arrival_time=datetime(2024, 10, 1, 20, 0), price=750.0, seats_available=150))
_flights.append(Flight(id=2, flight_number="BA202", airline_id=2, origin="JFK", destination="LHR", departure_time=datetime(2024, 10, 1, 9, 0), arrival_time=datetime(2024, 10, 1, 21, 0), price=800.0, seats_available=120))

@router.get("/search", response_model=List[Flight])
async def search_flights(
    origin: str = Query(..., description="Departure airport code"),
    destination: str = Query(..., description="Arrival airport code"),
    date: datetime = Query(..., description="Flight date"),
    passengers: int = Query(1, ge=1, description="Number of passengers"),
):
    """Simple flight search filtering the in-memory list."""
    results = [f for f in _flights if f.origin == origin and f.destination == destination and f.departure_time.date() == date.date()]
    if not results:
        raise HTTPException(status_code=404, detail="No flights found")
    return results
