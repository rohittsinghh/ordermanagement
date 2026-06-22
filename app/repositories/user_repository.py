"""
User Repository

Responsibilities:
-----------------
- Perform all database operations related to users.
- Execute SQLAlchemy queries.
- Manage database transactions.
- Rollback transactions when an error occurs.

The repository should NOT:
- Perform business validations.
- Raise HTTPException.
- Return JSON responses.
"""

from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    # ----------------------------------------------------
    # Create User
    # ----------------------------------------------------
    def create_user(
        self,
        db: Session,
        user_data: dict
    ) -> User:

        try:
            user = User(**user_data)

            db.add(user)

            db.commit()

            # Refresh the instance with the latest database state
            # This populates any DB-generated fields (e.g., id, defaults,
            # server-side timestamps) onto the SQLAlchemy model instance.
            db.refresh(user)

            return user

        except Exception:
            # Undo the transaction if commit fails
            db.rollback()

            # Re-raise the original exception
            raise

        finally:
            # Reserved for logging/cleanup if needed
            pass

    # ----------------------------------------------------
    # Get User By ID
    # ----------------------------------------------------
    def get_user(
        self,
        db: Session,
        user_id: int
    ) -> User | None:

        try:
            return (
                db.query(User)
                .filter(User.id == user_id)
                .first()
            )

        except Exception:
            raise

        finally:
            pass

    # ----------------------------------------------------
    # Get User By Email
    # ----------------------------------------------------
    def get_user_by_email(
        self,
        db: Session,
        email: str
    ) -> User | None:

        try:
            return (
                db.query(User)
                .filter(User.email == email)
                .first()
            )

        except Exception:
            raise

        finally:
            pass

    # ----------------------------------------------------
    # Get All Users
    # ----------------------------------------------------
    def get_all_users(
        self,
        db: Session
    ) -> list[User]:

        try:
            return db.query(User).all()

        except Exception:
            raise

        finally:
            pass

    # ----------------------------------------------------
    # Update User
    # ----------------------------------------------------
    def update_user(
        self,
        db: Session,
        user_id: int,
        update_data: dict
    ) -> User | None:

        try:
            user = (
                db.query(User)
                .filter(User.id == user_id)
                .first()
            )

            if not user:
                return None

            for key, value in update_data.items():
                setattr(user, key, value)

            db.commit()

            # Refresh the instance with the latest database state
            # Ensures any DB-side changes are loaded into the model
            db.refresh(user)

            return user

        except Exception:
            db.rollback()
            raise

        finally:
            pass

    # ----------------------------------------------------
    # Delete User
    # ----------------------------------------------------
    def delete_user(
        self,
        db: Session,
        user_id: int
    ) -> User | None:

        try:
            user = (
                db.query(User)
                .filter(User.id == user_id)
                .first()
            )

            if not user:
                return None

            db.delete(user)

            db.commit()

            return user

        except Exception:
            db.rollback()
            raise

        finally:
            pass