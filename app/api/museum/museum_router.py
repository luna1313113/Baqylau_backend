from fastapi import APIRouter
from . import museum_api

router = APIRouter()
router = APIRouter(
    prefix="/museum"
)
router.include_router(
    museum_api.router,
    tags=["museums"]
)