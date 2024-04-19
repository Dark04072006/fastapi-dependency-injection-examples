from fastapi import FastAPI

from app.api.router import user_router
from app.main.di import init_di


def create_app() -> FastAPI:
    """application factory"""

    app = FastAPI()

    app.include_router(user_router)

    init_di(app)

    return app
