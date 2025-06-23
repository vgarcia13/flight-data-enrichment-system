from datetime import datetime
from typing import List
from pydantic import BaseModel, Field


class FlightLeg(BaseModel):
    origin: str
    destination: str
    departure_time: datetime
    arrival_time: datetime
    flight_number: str
    aircraft_type: str
    cabin_type: str
    duration: int
    layover_time: str
    distance: int

class FlightData(BaseModel):
    id: str
    travel_class: str
    origin: str
    destination: str
    departure_time: datetime
    arrival_time: datetime
    flight_numbers: List[str] = Field(default_factory=list)
    legs: List[FlightLeg] = Field(default_factory=list)
    last_seen: datetime
