from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.museum.museum_schemas import MuseumCreate, MuseumResponse
from data_access.db.session import get_db
from data_access.museum.museum_repository import MuseumRepository
from business_logic.museum.museum_service import MuseumService

router = APIRouter()


def get_museum_service(db: AsyncSession = Depends(get_db)) -> MuseumService:
    repo = MuseumRepository(db)
    return MuseumService(repo)


@router.get("/all", response_model=list[MuseumResponse])
async def get_museums(
    service: MuseumService = Depends(get_museum_service)
):
    return await service.get_all()


@router.get("/{museum_id}", response_model=MuseumResponse)
async def get_museum(
    museum_id: str,
    service: MuseumService = Depends(get_museum_service)
):
    museum = await service.get_by_id(museum_id)
    if not museum:
        raise HTTPException(status_code=404, detail="Museum not found")
    return museum


@router.post("/", response_model=MuseumResponse, status_code=201)
async def create_museum(
    data: MuseumCreate,
    service: MuseumService = Depends(get_museum_service)
):
    return await service.create(data)