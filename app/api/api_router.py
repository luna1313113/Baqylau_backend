from fastapi import APIRouter
from api.museum.museum_router import router as museum_router
from api.exhibit.exhibit_router import router as exhibit_router

api_router = APIRouter()

api_router.include_router(
    museum_router,
    prefix="/museum"
)

api_router.include_router(
    exhibit_router,
    prefix="/exhibit"
)