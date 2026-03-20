from pydantic import BaseModel
from uuid import UUID

class ExhibitCreate(BaseModel):
    title: str
    era: str
    museum_id: UUID

class ExhibitRead(BaseModel):
    id: UUID
    title: str
    era: str
    museum_id: UUID

    class Config:
        from_attributes = True