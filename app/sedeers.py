import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from data_access.db.models.museum import Museum
from data_access.db.models.exhibit import Exhibit
from data_access.db.session import AsyncSessionLocal


async def seed_museums(db: AsyncSession):
    museums = [
        {"name": "National Museum of Kazakhstan", "city": "Astana", "founded_year": 2014},
        {"name": "Central State Museum", "city": "Almaty", "founded_year": 1931},
        {"name": "Karaganda Regional Museum", "city": "Karaganda", "founded_year": 1932},
    ]
    for museum_data in museums:
        result = await db.execute(
            select(Museum).where(Museum.name == museum_data["name"])
        )
        exists = result.scalar_one_or_none()
        if not exists:
            db.add(Museum(
                name=museum_data["name"],
                city=museum_data["city"],
                founded_year=museum_data["founded_year"]
            ))
    await db.commit()


async def seed_exhibits(db: AsyncSession):
    museum1 = (
        await db.execute(select(Museum).where(Museum.name == "National Museum of Kazakhstan"))
    ).scalar_one()

    museum2 = (
        await db.execute(select(Museum).where(Museum.name == "Central State Museum"))
    ).scalar_one()

    museum3 = (
        await db.execute(select(Museum).where(Museum.name == "Karaganda Regional Museum"))
    ).scalar_one()

    exhibits = [
        {"title": "Golden Man",          "era": "Saka Period",  "museum_id": museum1.id},
        {"title": "Ancient Petroglyphs", "era": "Bronze Age",   "museum_id": museum1.id},
        {"title": "Scythian Sword",      "era": "Iron Age",     "museum_id": museum2.id},
        {"title": "Silk Road Artifacts", "era": "Medieval",     "museum_id": museum2.id},
        {"title": "Soviet Documents",    "era": "20th Century", "museum_id": museum3.id},
        {"title": "Nomadic Jewelry",     "era": "Bronze Age",   "museum_id": museum3.id},
    ]
    for exhibit_data in exhibits:
        result = await db.execute(
            select(Exhibit).where(Exhibit.title == exhibit_data["title"])
        )
        exists = result.scalar_one_or_none()
        if not exists:
            db.add(Exhibit(
                title=exhibit_data["title"],
                era=exhibit_data["era"],
                museum_id=exhibit_data["museum_id"]
            ))
    await db.commit()


async def run_seeders(db: AsyncSession):
    await seed_museums(db)
    await seed_exhibits(db)


async def main():
    async with AsyncSessionLocal() as db:
        await run_seeders(db)


if __name__ == "__main__":
    asyncio.run(main())