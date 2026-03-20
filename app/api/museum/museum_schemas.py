from pydantic import BaseModel
from uuid import UUID

class MuseumCreate(BaseModel):
    name: str
    city: str
    founded_year: int

class MuseumResponse(BaseModel):
    id: UUID
    name: str
    city: str
    founded_year: int

    class Config:
        from_attributes = True