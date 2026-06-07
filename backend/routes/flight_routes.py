"""FastAPI router for flight search and listing."""

from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from datetime import datetime

from ..models.flight import Flight, FlightCreate

router = APIRouter()

# In-memory store for demo purposes
_flights: List[Flight] = []

@router.get("/search", response_model=List[Flight])
async def search_flights(
    origin: str = Query(..., description="IATA code of origin"),
    destination: str = Query(..., description="IATA code of destination"),
    departure_date: datetime = Query(..., description="Departure date in ISO format"),
    passengers: int = Query(1, ge=1),
):
    # Simple filter logic; real implementation would call external API
    results = [f for f in _flights if f.origin == origin and f.destination == destination]
    return results

@router.post("/add", response_model=Flight)
async def add_flight(flight: FlightCreate):
    new_id = len(_flights) + 1
    new_flight = Flight(id=new_id + 1, **flight.dict())
    _flights.append(new_flight)
    return new_flight
