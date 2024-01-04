from fastapi.routing import APIRouter

from app.api.services.misc import home

MISC_ROUTER = APIRouter()
MISC_ROUTER.include_router(home.router)
