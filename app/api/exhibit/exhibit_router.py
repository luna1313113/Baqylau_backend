from fastapi import APIRouter
from . import exhibit_api

router = APIRouter()
router = APIRouter(
    prefix="/exhibit"
)

router.include_router(
    exhibit_api.router,
    tags=["exhibits"]
)