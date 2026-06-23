"""
User Service

Responsibilities:
- Perform business logic.
- Validate user data.
- Call the repository layer.
- Raise custom exceptions when business rules fail.

The service should NOT know anything about FastAPI or HTTP.
"""

from app.utils.decorators import log_execution_time
from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository

from app.exceptions.custom_exceptions import (
    UserAlreadyExistsException,
    UserNotFoundException
)


class UserService:

    def __init__(self, user_repository: UserRepository):
        """
        Inject the UserRepository.

        Dependency Injection allows us to easily replace
        the repository for testing or future implementations.
        """
        self.user_repository = user_repository

    # ----------------------------------------------------
    # Create User
    # ----------------------------------------------------
    @log_execution_time
    def create_user(
        self,
        db: Session,
        user_data: dict
    ):

        # Check whether the email already exists
        existing_user = self.user_repository.get_user_by_email(
            db,
            user_data["email"]
        )

        if existing_user:
            raise UserAlreadyExistsException()

        # Create new user
        return self.user_repository.create_user(
            db,
            user_data
        )

    # ----------------------------------------------------
    # Get User
    # ----------------------------------------------------
    @log_execution_time

    def get_user(
        self,
        db: Session,
        user_id: int
    ):

        user = self.user_repository.get_user(
            db,
            user_id
        )

        if not user:
            raise UserNotFoundException()

        return user

    # ----------------------------------------------------
    # Get All Users
    # ----------------------------------------------------
    @log_execution_time
    def get_all_users(
        self,
        db: Session
    ):

        return self.user_repository.get_all_users(db)

    # ----------------------------------------------------
    # Update User
    # ----------------------------------------------------
    @log_execution_time
    def update_user(
        self,
        db: Session,
        user_id: int,
        update_data: dict
    ):

        # Check if user exists
        self.get_user(
            db,
            user_id
        )

        return self.user_repository.update_user(
            db,
            user_id,
            update_data
        )

    # ----------------------------------------------------
    # Delete User
    # ----------------------------------------------------
    def delete_user(
        self,
        db: Session,
        user_id: int
    ):

        # Check if user exists
        self.get_user(
            db,
            user_id
        )

        return self.user_repository.delete_user(
            db,
            user_id
        )