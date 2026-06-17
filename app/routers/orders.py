from fastapi import APIRouter, HTTPException

from app.schemas.order import (
    OrderCreate,
    OrderUpdate,
    OrderResponse
)

from app.services import order_service

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("", response_model=OrderResponse)
def create_order(order: OrderCreate):

    new_order = order_service.create_order(order)

    if not new_order:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return new_order


@router.get("", response_model=list[OrderResponse])
def get_all_orders():
    return order_service.get_all_orders()


@router.get("/{order_id}",
            response_model=OrderResponse)
def get_order(order_id: int):

    order = order_service.get_order(order_id)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


@router.put("/{order_id}",
            response_model=OrderResponse)
def update_order(
    order_id: int,
    order_update: OrderUpdate
):

    updated_order = order_service.update_order(
        order_id,
        order_update
    )

    if not updated_order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return updated_order


@router.delete("/{order_id}")
def delete_order(order_id: int):

    deleted_order = order_service.delete_order(
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
def get_user_orders(user_id: int):

    return order_service.get_user_orders(user_id)