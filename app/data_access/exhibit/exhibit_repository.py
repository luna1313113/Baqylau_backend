from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from data_access.db.models.exhibit import Exhibit


class ExhibitRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[Exhibit]:
        result = await self.db.execute(select(Exhibit))
        return result.scalars().all()

    async def create(self, title: str, era: str, museum_id) -> Exhibit:
        exhibit = Exhibit(title=title, era=era, museum_id=museum_id)
        self.db.add(exhibit)
        await self.db.commit()
        await self.db.refresh(exhibit)
        return exhibit