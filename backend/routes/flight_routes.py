from fastapi import APIRouter, HTTPException
from ..models.flight import Flight
from datetime import datetime

router = APIRouter()

# Mock data store
_flights = [
    Flight(
        flight_id="FL123",
        airline="Air Korea",
        origin="ICN",
        destination="LHR",
        departure_time=datetime(2024, 10, 1, 10, 0),
        arrival_time=datetime(2024, 10, 1, 20, 0),
        price=350.0,
        layovers=0,
        duration_minutes=600,
    ),
    Flight(
        flight_id="FL456",
        airline="British Airways",
        origin="ICN",
        destination="LHR",
        departure_time=datetime(2024, 10, 1, 12, 0),
        arrival_time=datetime(2024, 10, 1, 22, 0),
        price=400.0,
        layovers=1,
        duration_minutes=720,
    ),
]

@router.get("/search", response_model=list[Flight])
async def search_flights(origin: str, destination: str, date: str, passengers: int = 1):
    # Simplified search logic
    results = [f for f in _flights if f.origin == origin and f.destination == destination]
    if not results:
        raise HTTPException(status_code=404, detail="No flights found")
    return results
