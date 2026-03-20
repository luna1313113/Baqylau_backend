from data_access.museum.museum_repository import MuseumRepository


class MuseumService:
    def __init__(self, repo: MuseumRepository):
        self.repo = repo

    async def get_all(self):
        return await self.repo.get_all()

    async def get_by_id(self, museum_id: str):
        return await self.repo.get_by_id(museum_id)

    async def create(self, data):
        return await self.repo.create(
            name=data.name,
            city=data.city,
            founded_year=data.founded_year
        )