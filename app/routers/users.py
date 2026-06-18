from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse
)

from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


def get_user_service() -> UserService:
    repository = UserRepository()
    return UserService(repository)


@router.post(
    "/",
    response_model=UserResponse
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service)
):
    return service.create_user(
        db,
        user.model_dump()
    )


@router.get(
    "/",
    response_model=list[UserResponse]
)
def get_all_users(
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service)
):
    return service.get_all_users(db)


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service)
):
    return service.get_user(
        db,
        user_id
    )


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
    return service.update_user(
        db,
        user_id,
        user.model_dump(exclude_unset=True)
    )


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service)
):
    return service.delete_user(
        db,
        user_id
    )