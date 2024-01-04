import time
import json
from datetime import datetime

from fastapi.requests import Request
from starlette.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware

class CustomResponse(Response):
    def __init__(self, content, **kwargs):
        super().__init__(content, **kwargs)
        self._body = content  # Store the original content here

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Start the timer
        start_time = time.time()

        # Log the request
        request_body = b""
        request_body = await request.body()
        log_details = {
            "time": datetime.now().isoformat(),
            "request_method": request.method,
            "request_url": str(request.url),
            "request_user_agent": str(request.headers.get("User-Agent")),
            "request_body": request_body.decode("utf-8"),
        }
        print("Request:", json.dumps(log_details, indent=2))

        # Call the next middleware or route handler
        response = await call_next(request)

        try:
            content = await response.body()
        except AttributeError:
            content = None

        custom_response = CustomResponse(
            content=content,
            status_code=response.status_code,
            headers=dict(response.headers),
        )

        # Calculate response time
        process_time = (time.time() - start_time) * 1000  # convert to ms

        # Log the response
        log_details = {
            "time": datetime.now().isoformat(),
            "response_status": custom_response.status_code,
            "response_time_ms": process_time,
            "response_headers": str(request.headers.get("User-Agent", None)),
            "response_body": str(custom_response.body),
        }
        print("Response:", json.dumps(log_details, indent=2))

        return response