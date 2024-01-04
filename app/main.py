from fastapi import FastAPI

from app.api.services.misc.router import MISC_ROUTER

from app.middleware.logging_middleware import LoggingMiddleware

app = FastAPI()

# Add custom logging middleware
app.add_middleware(LoggingMiddleware)

app.include_router(MISC_ROUTER)
