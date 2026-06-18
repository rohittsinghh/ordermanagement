from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.order import (
    OrderCreate,
    OrderUpdate,
    OrderResponse
)

from app.services.order_service import OrderService
from app.repositories.order_repository import OrderRepository


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


def get_order_service() -> OrderService:

    repository = OrderRepository()

    return OrderService(repository)


@router.post(
    "/",
    response_model=OrderResponse
)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    service: OrderService = Depends(get_order_service)
):

    try:
        return service.create_order(
            db,
            order.model_dump()
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[OrderResponse]
)
def get_all_orders(
    db: Session = Depends(get_db),
    service: OrderService = Depends(get_order_service)
):

    return service.get_all_orders(db)


@router.get(
    "/{order_id}",
    response_model=OrderResponse
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    service: OrderService = Depends(get_order_service)
):

    order = service.get_order(
        db,
        order_id
    )

    if not order:

        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


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

    updated_order = service.update_order(
        db,
        order_id,
        order.model_dump(exclude_unset=True)
    )

    if not updated_order:

        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return updated_order


@router.delete(
    "/{order_id}"
)
def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
    service: OrderService = Depends(get_order_service)
):

    deleted_order = service.delete_order(
        db,
        order_id
    )

    if not deleted_order:

        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return {
        "message": "Order deleted successfully"
    }


@router.get(
    "/user/{user_id}",
    response_model=list[OrderResponse]
)
def get_orders_by_user(
    user_id: int,
    db: Session = Depends(get_db),
    service: OrderService = Depends(get_order_service)
):

    return service.get_orders_by_user(
        db,
        user_id
    )