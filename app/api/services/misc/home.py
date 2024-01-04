from fastapi import status
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

router = APIRouter()


@router.get("/")
async def home(request: Request) -> JSONResponse:
    return JSONResponse({"message": "hello friend"}, status_code=status.HTTP_200_OK)
