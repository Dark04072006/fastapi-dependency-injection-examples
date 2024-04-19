from typing import Annotated, TypeVar

from fastapi import Depends, FastAPI

from app.adapters.gateway import MockDatabaseGateway
from app.protocols.gateway import DatabaseGateway
from app.usecases.get_user import GetUser

DependencyT = TypeVar("DependencyT")


def provide_db_gateway() -> DatabaseGateway:
    return MockDatabaseGateway()


def provide_interactor(gateway: Annotated[DatabaseGateway, Depends()]) -> GetUser:
    return GetUser(gateway=gateway)


def init_di(app: FastAPI) -> None:
    """Initialize dependencies"""

    app.dependency_overrides[DatabaseGateway] = provide_db_gateway
    app.dependency_overrides[GetUser] = provide_interactor
