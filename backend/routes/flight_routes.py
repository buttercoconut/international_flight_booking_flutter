from fastapi import APIRouter, Query, HTTPException
from typing import List
from datetime import datetime
from models.flight import Flight

router = APIRouter()

# Dummy data store
_dummy_flights = [
    Flight(
        flight_id="FL123",
        airline="Delta",
        origin="JFK",
        destination="LHR",
        departure_time=datetime(2024, 6, 15, 22, 0),
        arrival_time=datetime(2024, 6, 16, 10, 0),
        price=850.0,
        layovers=0,
        duration_minutes=420,
    ),
    Flight(
        flight_id="FL456",
        airline="British Airways",
        origin="JFK",
        destination="LHR",
        departure_time=datetime(2024, 6, 15, 23, 30),
        arrival_time=datetime(2024, 6, 16, 11, 30),
        price=900.0,
        layovers=1,
        duration_minutes=480,
    ),
]

@router.get("/flights", response_model=List[Flight])
async def search_flights(
    origin: str = Query(..., description="IATA code of origin airport"),
    destination: str = Query(..., description="IATA code of destination airport"),
    date: datetime = Query(..., description="Departure date (YYYY-MM-DD)"),
    passengers: int = Query(1, ge=1, le=9, description="Number of passengers"),
):
    """Search for flights matching the criteria.
    In a real implementation this would query an external airline API or a database.
    """
    results = [f for f in _dummy_flights if f.origin == origin and f.destination == destination and f.departure_time.date() == date.date()]
    if not results:
        raise HTTPException(status_code=404, detail="No flights found for the given criteria")
    return results
