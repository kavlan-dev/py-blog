from py_blog.core import security
from py_blog.core.config import get_settings
from py_blog.core.init_db import init_db
from py_blog.repositories.articles import get_article_repository
from py_blog.repositories.users import get_user_repository
from py_blog.services.articles import ArticleService
from py_blog.services.users import UserService

config = get_settings()
security.init_secret_key(config.get_secret_key())

db = init_db(config.get_database_url())
article_repo = get_article_repository(db)
user_repo = get_user_repository(db)


def get_post_service() -> ArticleService:
    return ArticleService(article_repo)


def get_user_service() -> UserService:
    return UserService(user_repo)
