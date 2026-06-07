"""Pydantic models for Airline entity."""

from pydantic import BaseModel, Field

class AirlineBase(BaseModel):
    name: str = Field(..., example="American Airlines")
    iata_code: str = Field(..., example="AA")

class AirlineCreate(AirlineBase):
    pass

class Airline(AirlineBase):
    id: int

    class Config:
        orm_mode = True
