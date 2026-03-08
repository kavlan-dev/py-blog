from py_blog.core import security
from py_blog.core.config import load_config
from py_blog.core.init_db import init_db
from py_blog.core.logger import setup_logger
from py_blog.repositories.articles import get_article_repository
from py_blog.repositories.users import get_user_repository
from py_blog.services.articles import ArticleService
from py_blog.services.users import UserService


def init_app():
    config = load_config()
    security.init_secret_key(config.get_secret_key())

    db = init_db(config.db.get_dsn())
    global article_repo
    article_repo = get_article_repository(db)
    global user_repo
    user_repo = get_user_repository(db)


def get_logger():
    return setup_logger()


def get_post_service() -> ArticleService:
    return ArticleService(article_repo)


def get_user_service() -> UserService:
    return UserService(user_repo)
