import email

from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:


    def create_user(
        self,
        db: Session,
        user_data: dict
    ) -> User:

        user = User(**user_data)

        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    def get_user_by_email(
    self,
    db: Session,
    email: str
) -> User | None:

     return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    def get_user(
        self,
        db: Session,
        user_id: int
    ) -> User | None:

        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    def get_all_users(
        self,
        db: Session
    ) -> list[User]:

        return db.query(User).all()

    def update_user(
        self,
        db: Session,
        user_id: int,
        update_data: dict
    ) -> User | None:

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
        db.refresh(user)

        return user

    def delete_user(
        self,
        db: Session,
        user_id: int
    ) -> User | None:

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
   