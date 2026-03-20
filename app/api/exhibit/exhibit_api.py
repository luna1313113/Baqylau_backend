from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.exhibit.exhibit_schemas import ExhibitCreate, ExhibitRead
from data_access.db.session import get_db
from data_access.exhibit.exhibit_repository import ExhibitRepository
from business_logic.exhibit.exhibit_service import ExhibitService

router = APIRouter()

def get_exhibit_service(db: AsyncSession = Depends(get_db)) -> ExhibitService:
    repo = ExhibitRepository(db)
    return ExhibitService(repo)

@router.get("/all", response_model=list[ExhibitRead])
async def get_exhibits(
    service: ExhibitService = Depends(get_exhibit_service),
):
    return await service.get_all()

@router.post("/", response_model=ExhibitRead, status_code=201)
async def create_exhibits(
    exhibit: ExhibitCreate,
    service: ExhibitService = Depends(get_exhibit_service)
):
    try:
        return await service.create_exhibit(exhibit)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))