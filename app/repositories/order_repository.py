"""
Order Repository

Responsibilities
----------------
1. Perform all database operations related to orders.
2. Execute SQLAlchemy queries.
3. Commit successful transactions.
4. Roll back failed transactions.

The repository should NOT:
- Perform business validations.
- Raise HTTPException.
- Return JSONResponse.
"""

from sqlalchemy.orm import Session

from app.models.order import Order


class OrderRepository:

    # --------------------------------------------------
    # Create Order
    # --------------------------------------------------
    def create_order(
        self,
        db: Session,
        order_data: dict
    ) -> Order:

        try:

            order = Order(**order_data)

            db.add(order)

            db.commit()

            db.refresh(order)

            return order

        except Exception:

            # Undo the transaction if commit fails
            db.rollback()

            # Re-raise the exception
            raise

        finally:

            # Reserved for logging or cleanup
            pass

    # --------------------------------------------------
    # Get Order By ID
    # --------------------------------------------------
    def get_order(
        self,
        db: Session,
        order_id: int
    ) -> Order | None:

        try:

            return (
                db.query(Order)
                .filter(Order.id == order_id)
                .first()
            )

        except Exception:

            raise

        finally:

            pass

    # --------------------------------------------------
    # Get All Orders
    # --------------------------------------------------
    def get_all_orders(
        self,
        db: Session
    ) -> list[Order]:

        try:

            return db.query(Order).all()

        except Exception:

            raise

        finally:

            pass

    # --------------------------------------------------
    # Update Order
    # --------------------------------------------------
    def update_order(
        self,
        db: Session,
        order_id: int,
        update_data: dict
    ) -> Order | None:

        try:

            order = (
                db.query(Order)
                .filter(Order.id == order_id)
                .first()
            )

            if order is None:
                return None

            for key, value in update_data.items():
                setattr(order, key, value)

            db.commit()

            db.refresh(order)

            return order

        except Exception:

            db.rollback()

            raise

        finally:

            pass

    # --------------------------------------------------
    # Delete Order
    # --------------------------------------------------
    def delete_order(
        self,
        db: Session,
        order_id: int
    ) -> Order | None:

        try:

            order = (
                db.query(Order)
                .filter(Order.id == order_id)
                .first()
            )

            if order is None:
                return None

            db.delete(order)

            db.commit()

            return order

        except Exception:

            db.rollback()

            raise

        finally:

            pass

    # --------------------------------------------------
    # Get Orders By User ID
    # --------------------------------------------------
    def get_orders_by_user(
        self,
        db: Session,
        user_id: int
    ) -> list[Order]:

        try:

            return (
                db.query(Order)
                .filter(Order.user_id == user_id)
                .all()
            )

        except Exception:

            raise

        finally:

            pass