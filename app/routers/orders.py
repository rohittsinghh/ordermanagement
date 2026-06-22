# FastAPI classes used for routing and dependency injection
from fastapi import APIRouter, Depends

# SQLAlchemy database session
from sqlalchemy.orm import Session

# Database dependency
from app.database.database import get_db

# Service dependency
from app.core.dependencies import get_order_service

# Pydantic schemas
from app.schemas.order import (
    OrderCreate,
    OrderUpdate,
    OrderResponse
)

# Business logic layer
from app.services.order_service import OrderService


# Router configuration
router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


# -------------------------------------------------------
# Create Order
# -------------------------------------------------------
@router.post(
    "/",
    response_model=OrderResponse,
    status_code=201
)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    service: OrderService = Depends(get_order_service)
):
    """
    Create a new order.
    """

    return service.create_order(
        db,
        order.model_dump()
    )


# -------------------------------------------------------
# Get All Orders
# -------------------------------------------------------
@router.get(
    "/",
    response_model=list[OrderResponse]
)
def get_all_orders(
    db: Session = Depends(get_db),
    service: OrderService = Depends(get_order_service)
):
    """
    Fetch all orders.
    """

    return service.get_all_orders(db)


# -------------------------------------------------------
# Get Order By ID
# -------------------------------------------------------
@router.get(
    "/{order_id}",
    response_model=OrderResponse
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    service: OrderService = Depends(get_order_service)
):
    """
    Fetch a single order using its ID.
    """

    return service.get_order(
        db,
        order_id
    )


# -------------------------------------------------------
# Update Order
# -------------------------------------------------------
@router.put(
    "/{order_id}",
    response_model=OrderResponse
)
def update_order(
    order_id: int,
    order: OrderUpdate,
    db: Session = Depends(get_db),
    service: OrderService = Depends(get_order_service)
):
    """
    Update an existing order.
    Only the fields provided in the request are updated.
    """

    return service.update_order(
        db,
        order_id,
        order.model_dump(exclude_unset=True)
    )


# -------------------------------------------------------
# Delete Order
# -------------------------------------------------------
@router.delete("/{order_id}")
def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
    service: OrderService = Depends(get_order_service)
):
    """
    Delete an order using its ID.
    """

    service.delete_order(
        db,
        order_id
    )

    return {
        "message": "Order deleted successfully"
    }


# -------------------------------------------------------
# Get Orders By User ID
# -------------------------------------------------------
@router.get(
    "/user/{user_id}",
    response_model=list[OrderResponse]
)
def get_orders_by_user(
    user_id: int,
    db: Session = Depends(get_db),
    service: OrderService = Depends(get_order_service)
):
    """
    Fetch all orders belonging to a specific user.
    """

    return service.get_orders_by_user(
        db,
        user_id
    )