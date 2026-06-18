from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.user import User
from app.models.order import Order

from app.routers import users
from app.routers import orders
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

app = FastAPI(
    title="Order Management System"
)

# Create tables (only if they don't already exist)
Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(orders.router)


@app.get("/")
def home():
    return {"message": "Order Management API Running"}