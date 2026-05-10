"""FastAPI routes for flight search.

This module implements a simple flight search endpoint that calls a stubbed
service. In a real implementation you would call the Amadeus/Sabre API
and map the response to the FlightRead model.
"""

from fastapi import APIRouter, Depends, HTTPException
from typing import List

from ..config import settings
from ..models.flight import FlightRead, FlightSearchRequest

router = APIRouter(prefix="/flights", tags=["flights"])

# Stubbed flight service – replace with real API client
class FlightService:
    def search(self, request: FlightSearchRequest) -> List[FlightRead]:
        # In a real scenario, validate request, call external API, parse
        # and return a list of FlightRead objects.
        # Here we just return a static list for demonstration.
        dummy_flight = FlightRead(
            id=1,
            flight_number="AA1234",
            airline_code="AA",
            departure_airport=request.origin,
            arrival_airport=request.destination,
            departure_time="2024-07-01T08:00:00Z",
            arrival_time="2024-07-01T20:00:00Z",
            price=350.0,
            currency="USD",
            layovers=0,
        )
        return [dummy_flight]

# Dependency that would normally provide a DB session or an API client
async def get_flight_service() -> FlightService:
    return FlightService()

@router.post("/search", response_model=List[FlightRead])
async def search_flights(
    request: FlightSearchRequest,
    service: FlightService = Depends(get_flight_service),
):
    try:
        flights = service.search(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return flights
