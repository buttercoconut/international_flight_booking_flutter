"""Pydantic model for Airline.
"""

from pydantic import BaseModel, Field

class AirlineBase(BaseModel):
    code: str = Field(..., example="AA")
    name: str = Field(..., example="American Airlines")

class AirlineRead(AirlineBase):
    id: int
