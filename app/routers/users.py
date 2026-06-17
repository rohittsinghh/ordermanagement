from fastapi import APIRouter, HTTPException

from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse
)

from app.services import user_service

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("", response_model=UserResponse)
def create_user(user: UserCreate):
    return user_service.create_user(user)


@router.get("", response_model=list[UserResponse])
def get_all_users():
    return user_service.get_all_users()


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):

    user = user_service.get_user(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_update: UserUpdate
):

    updated_user = user_service.update_user(
        user_id,
        user_update
    )

    if not updated_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return updated_user


@router.delete("/{user_id}")
def delete_user(user_id: int):

    deleted_user = user_service.delete_user(user_id)

    if not deleted_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }