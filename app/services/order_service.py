from sqlalchemy.orm import Session

from app.repositories.order_repository import OrderRepository


class OrderService:

    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def create_order(
        self,
        db: Session,
        order_data: dict
    ):

        if order_data["quantity"] <= 0:
            raise ValueError("Quantity must be greater than 0")

        return self.order_repository.create_order(
            db,
            order_data
        )

    def get_order(
        self,
        db: Session,
        order_id: int
    ):

        return self.order_repository.get_order(
            db,
            order_id
        )

    def get_all_orders(
        self,
        db: Session
    ):

        return self.order_repository.get_all_orders(db)

    def update_order(
        self,
        db: Session,
        order_id: int,
        update_data: dict
    ):

        return self.order_repository.update_order(
            db,
            order_id,
            update_data
        )

    def delete_order(
        self,
        db: Session,
        order_id: int
    ):

        return self.order_repository.delete_order(
            db,
            order_id
        )

    def get_orders_by_user(
        self,
        db: Session,
        user_id: int
    ):

        return self.order_repository.get_orders_by_user(
            db,
            user_id
        )