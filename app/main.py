from fastapi import FastAPI

from app.api.services.misc.router import MISC_ROUTER

app = FastAPI()

app.include_router(MISC_ROUTER)
