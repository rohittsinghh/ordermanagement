"""
Application Custom Exceptions

Responsibilities
----------------
- Define application-specific exceptions.
- Separate business logic from HTTP logic.
- Store both the HTTP status code and error message.
"""

from fastapi import status


class AppException(Exception):
    """
    Base class for all application exceptions.
    """

    def __init__(
        self,
        status_code: int,
        message: str
    ):

        self.status_code = status_code
        self.message = message

        super().__init__(message)


# --------------------------------------------------
# User Exceptions
# --------------------------------------------------

class UserNotFoundException(AppException):

    def __init__(self):

        super().__init__(
            status.HTTP_404_NOT_FOUND,
            "User not found."
        )


class UserAlreadyExistsException(AppException):

    def __init__(self):

        super().__init__(
            status.HTTP_409_CONFLICT,
            "User already exists."
        )


# --------------------------------------------------
# Order Exceptions
# --------------------------------------------------

class OrderNotFoundException(AppException):

    def __init__(self):

        super().__init__(
            status.HTTP_404_NOT_FOUND,
            "Order not found."
        )


class InvalidOrderQuantityException(AppException):

    def __init__(self):

        super().__init__(
            status.HTTP_400_BAD_REQUEST,
            "Order quantity must be greater than zero."
        )


# --------------------------------------------------
# Database Exception
# --------------------------------------------------

class DatabaseException(AppException):

    def __init__(self):

        super().__init__(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "A database error occurred."
        )