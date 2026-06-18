from sqlalchemy.orm import Session

from app.models.order import Order


class OrderRepository:

    def create_order(
        self,
        db: Session,
        order_data: dict
    ) -> Order:

        order = Order(**order_data)

        db.add(order)
        db.commit()
        db.refresh(order)

        return order

    def get_order(
        self,
        db: Session,
        order_id: int
    ) -> Order | None:

        return (
            db.query(Order)
            .filter(Order.id == order_id)
            .first()
        )

    def get_all_orders(
        self,
        db: Session
    ) -> list[Order]:

        return (
            db.query(Order)
            .all()
        )

    def update_order(
        self,
        db: Session,
        order_id: int,
        update_data: dict
    ) -> Order | None:

        order = (
            db.query(Order)
            .filter(Order.id == order_id)
            .first()
        )

        if not order:
            return None

        for key, value in update_data.items():
            setattr(order, key, value)

        db.commit()
        db.refresh(order)

        return order

    def delete_order(
        self,
        db: Session,
        order_id: int
    ) -> Order | None:

        order = (
            db.query(Order)
            .filter(Order.id == order_id)
            .first()
        )

        if not order:
            return None

        db.delete(order)
        db.commit()

        return order

    def get_orders_by_user(
        self,
        db: Session,
        user_id: int
    ) -> list[Order]:

        return (
            db.query(Order)
            .filter(Order.user_id == user_id)
            .all()
        )