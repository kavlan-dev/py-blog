from py_blog.config import load_config
from py_blog.repositories.articles import get_article_repository
from py_blog.repositories.users import get_user_repository
from py_blog.services.articles import ArticleService
from py_blog.services.users import UserService
from py_blog.utils import security
from py_blog.utils.init_db import init_db
from py_blog.utils.logger import setup_logger

config = load_config()
security.init_secret_key(config.get_secret_key())

db = init_db(config.db.get_dsn())
article_repo = get_article_repository(db)
user_repo = get_user_repository(db)

article_service = ArticleService(article_repo)
user_service = UserService(user_repo)


def get_logger():
    return setup_logger()


def get_post_service() -> ArticleService:
    return article_service


def get_user_service() -> UserService:
    return user_service
