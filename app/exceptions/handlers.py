"""
Global Exception Handlers

Responsibilities
----------------
- Convert custom exceptions into JSON responses.
- Return consistent API responses.
- Handle unexpected server errors.
"""

from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import AppException


# --------------------------------------------------
# Handle Application Exceptions
# --------------------------------------------------

async def app_exception_handler(
    request: Request,
    exc: AppException
):

    return JSONResponse(

        status_code=exc.status_code,

        content={
            "success": False,
            "message": exc.message
        }
    )


# --------------------------------------------------
# Handle Unexpected Exceptions
# --------------------------------------------------

async def global_exception_handler(
    request: Request,
    exc: Exception
):

    return JSONResponse(

        status_code=500,

        content={
            "success": False,
            "message": "Internal Server Error"
        }
    )