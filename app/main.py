"""
Main Entry Point
"""

from fastapi import FastAPI

# -----------------------------
# Routers
# -----------------------------
from app.routers.users import router as user_router
from app.routers.orders import router as order_router

# -----------------------------
# Custom Exception Handlers
# -----------------------------
from app.exceptions.custom_exceptions import AppException
from app.exceptions.handlers import (
    app_exception_handler,
    global_exception_handler
)

# -----------------------------
# Create FastAPI Application
# -----------------------------
app = FastAPI(
    title="Order Management API",
)

# -----------------------------
# Register Global Exception Handlers
# -----------------------------
app.add_exception_handler(
    AppException,
    app_exception_handler
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)

# -----------------------------
# Register Routers
# -----------------------------
app.include_router(user_router)

app.include_router(order_router)

# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def root():

    return {
        "message": "Welcome to Order Management API"
    }