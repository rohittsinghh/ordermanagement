# FastAPI classes used for creating routes and dependency injection
from fastapi import APIRouter, Depends

# SQLAlchemy database session
from sqlalchemy.orm import Session

# Dependency that provides a database session
from app.database.database import get_db

# Dependency that provides the UserService object
from app.core.dependencies import get_user_service

# Pydantic schemas for request validation and response serialization
from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse
)

# Service layer containing business logic
from app.services.user_service import UserService


# Router configuration
# All endpoints in this file will start with "/users"
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# -------------------------------------------------------
# Create User
# -------------------------------------------------------
@router.post(
    "/",
    response_model=UserResponse,
    status_code=201
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service)
):
    """
    Create a new user.

    Flow:
    Client
        ↓
    Router
        ↓
    UserService
        ↓
    UserRepository
        ↓
    PostgreSQL
    """

    return service.create_user(
        db,
        user.model_dump()
    )


# -------------------------------------------------------
# Get All Users
# -------------------------------------------------------
@router.get(
    "/",
    response_model=list[UserResponse]
)
def get_all_users(
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service)
):
    """
    Fetch all users from the database.
    """

    return service.get_all_users(db)


# -------------------------------------------------------
# Get User By ID
# -------------------------------------------------------
@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service)
):
    """
    Fetch a single user using its ID.
    """

    return service.get_user(
        db,
        user_id
    )


# -------------------------------------------------------
# Update User
# -------------------------------------------------------
@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service)
):
    """
    Update an existing user.
    Only the fields sent in the request will be updated.
    """

    return service.update_user(
        db,
        user_id,
        user.model_dump(exclude_unset=True)
    )


# -------------------------------------------------------
# Delete User
# -------------------------------------------------------
@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service)
):
    """
    Delete a user using its ID.
    """

    service.delete_user(
        db,
        user_id
    )

    return {
        "message": "User deleted successfully"
    }