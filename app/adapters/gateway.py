from app.models import User
from app.protocols.gateway import DatabaseGateway


class MockDatabaseGateway(DatabaseGateway):
    """
    implementation of db gateway
    """

    def get_user(self) -> User:
        return User(id=1, name="some_user")
