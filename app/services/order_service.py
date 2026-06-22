"""
Order Service

Responsibilities:
- Perform business validations.
- Call repository methods.
- Raise custom exceptions.
- Do NOT interact with HTTP or FastAPI.
"""

from sqlalchemy.orm import Session

from app.repositories.order_repository import OrderRepository

from app.exceptions.custom_exceptions import (
    OrderNotFoundException,
    InvalidOrderQuantityException
)


class OrderService:

    def __init__(self, order_repository: OrderRepository):
        """
        Inject the OrderRepository.
        """
        self.order_repository = order_repository

    # ----------------------------------------------------
    # Create Order
    # ----------------------------------------------------
    def create_order(
        self,
        db: Session,
        order_data: dict
    ):

        # Business validation
        if order_data["quantity"] <= 0:
            raise InvalidOrderQuantityException()

        return self.order_repository.create_order(
            db,
            order_data
        )

    # ----------------------------------------------------
    # Get Order
    # ----------------------------------------------------
    def get_order(
        self,
        db: Session,
        order_id: int
    ):

        order = self.order_repository.get_order(
            db,
            order_id
        )

        if not order:
            raise OrderNotFoundException()

        return order

    # ----------------------------------------------------
    # Get All Orders
    # ----------------------------------------------------
    def get_all_orders(
        self,
        db: Session
    ):

        return self.order_repository.get_all_orders(db)

    # ----------------------------------------------------
    # Update Order
    # ----------------------------------------------------
    def update_order(
        self,
        db: Session,
        order_id: int,
        update_data: dict
    ):

        # Ensure order exists
        self.get_order(
            db,
            order_id
        )

        return self.order_repository.update_order(
            db,
            order_id,
            update_data
        )

    # ----------------------------------------------------
    # Delete Order
    # ----------------------------------------------------
    def delete_order(
        self,
        db: Session,
        order_id: int
    ):

        # Ensure order exists
        self.get_order(
            db,
            order_id
        )

        return self.order_repository.delete_order(
            db,
            order_id
        )

    # ----------------------------------------------------
    # Get Orders By User
    # ----------------------------------------------------
    def get_orders_by_user(
        self,
        db: Session,
        user_id: int
    ):

        return self.order_repository.get_orders_by_user(
            db,
            user_id
        )