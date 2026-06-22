from fastapi import Depends

from app.repositories.user_repository import UserRepository
from app.repositories.order_repository import OrderRepository

from app.services.user_service import UserService
from app.services.order_service import OrderService


# ------------------------
# Repository Dependencies
# ------------------------

def get_user_repository() -> UserRepository:
    return UserRepository()


def get_order_repository() -> OrderRepository:
    return OrderRepository()


# ------------------------
# Service Dependencies
# ------------------------

def get_user_service(
    repository: UserRepository = Depends(get_user_repository)
) -> UserService:

    return UserService(repository)


def get_order_service(
    repository: OrderRepository = Depends(get_order_repository)
) -> OrderService:

    return OrderService(repository)