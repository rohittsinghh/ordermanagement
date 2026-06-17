from fastapi import FastAPI
from app.routers.users import router as user_router
from app.routers.orders import router as order_router

app = FastAPI(
    title="Order Management API"
)
app.include_router(order_router)

app.include_router(user_router)


@app.get("/")
def home():
    return {
        "message": "Order Management API is running"
    }