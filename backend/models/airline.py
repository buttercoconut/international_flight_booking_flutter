# models/airline.py
from pydantic import BaseModel

class Airline(BaseModel):
    airline_id: str
    name: str
    country: str
    iata_code: str
