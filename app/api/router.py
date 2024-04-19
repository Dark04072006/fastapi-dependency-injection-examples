from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.depends_stub import Stub
from app.models import User
from app.usecases.get_user import GetUser

user_router = APIRouter()


@user_router.get("/")
def get_user(interactor: Annotated[GetUser, Depends(Stub(GetUser))]) -> User:
    return interactor.execute()
