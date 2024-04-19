from typing import Protocol

from app.models import User


class DatabaseGateway(Protocol):
    """
    some protocol of adapter, in our case it's a db gateway
    """

    def get_user(self) -> User:
        """get a user"""
