from data_access.exhibit.exhibit_repository import ExhibitRepository


class ExhibitService:
    def __init__(self, repo: ExhibitRepository):
        self.repo = repo

    async def get_all(self):
        return await self.repo.get_all()

    async def create_exhibit(self, data):
        return await self.repo.create(
            title=data.title,
            era=data.era,
            museum_id=data.museum_id
        )