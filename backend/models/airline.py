from pydantic import BaseModel

class AirlineBase(BaseModel):
    name: str
    country: str

class AirlineCreate(AirlineBase):
    pass

class Airline(AirlineBase):
    id: int

    class Config:
        orm_mode = True
