# routes/flight_routes.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..models.flight import FlightSearchRequest, FlightSearchResponse, Flight

router = APIRouter(prefix="/flights", tags=["flights"])

# Dummy in-memory flight data for demo purposes
FAKE_FLIGHTS = [
    Flight(
        flight_id="FL123",
        airline="Delta",
        origin="JFK",
        destination="LHR",
        departure_time="2024-07-01T08:00:00Z",
        arrival_time="2024-07-01T20:00:00Z",
        duration_minutes=480,
        price=650.0,
        layovers=0,
        seats_available=10,
    ),
    Flight(
        flight_id="FL456",
        airline="British Airways",
        origin="JFK",
        destination="LHR",
        departure_time="2024-07-01T12:00:00Z",
        arrival_time="2024-07-01T22:00:00Z",
        duration_minutes=480,
        price=700.0,
        layovers=0,
        seats_available=5,
    ),
]

@router.post("/search", response_model=FlightSearchResponse)
async def search_flights(request: FlightSearchRequest):
    # In a real implementation, query the database or external API
    # Here we simply filter the FAKE_FLIGHTS list
    results = [f for f in FAKE_FLIGHTS if f.origin == request.origin and f.destination == request.destination]
    if not results:
        raise HTTPException(status_code=404, detail="No flights found")
    return FlightSearchResponse(flights=results)
