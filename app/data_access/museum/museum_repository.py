from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from data_access.db.models.museum import Museum


class MuseumRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[Museum]:
        result = await self.db.execute(select(Museum))
        return result.scalars().all()

    async def get_by_id(self, museum_id: str) -> Museum | None:
        result = await self.db.execute(select(Museum).where(Museum.id == museum_id))
        return result.scalar_one_or_none()

    async def create(self, name: str, city: str, founded_year: int) -> Museum:
        museum = Museum(name=name, city=city, founded_year=founded_year)
        self.db.add(museum)
        await self.db.commit()
        await self.db.refresh(museum)
        return museum