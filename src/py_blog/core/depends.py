from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from py_blog.api.router import get_router
from py_blog.core.config import get_settings
from py_blog.repositories.repository import get_post_repository
from py_blog.services.service import get_post_service
from py_blog.utils.init_db import init_db


def get_app():
    config = get_settings()
    db = init_db(config.DATABASE_URL)
    repository = get_post_repository(db)
    service = get_post_service(repository)
    router = get_router(service)

    app = FastAPI()
    app.include_router(router)

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.state.db = db

    return app
