from app.models import User
from app.protocols.gateway import DatabaseGateway


class GetUser:
    """
    interactor to get user
    """

    def __init__(self, gateway: DatabaseGateway) -> None:
        self.gateway = gateway

    def execute(self) -> User:
        return self.gateway.get_user()
