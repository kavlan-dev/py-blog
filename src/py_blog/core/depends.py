from py_blog.core.config import get_settings
from py_blog.repositories.articles import get_article_repository
from py_blog.services.articles import ArticleService
from py_blog.core.init_db import init_db

config = get_settings()
db = init_db(config.get_database_url())
repository = get_article_repository(db)


def get_post_service() -> ArticleService:
    return ArticleService(repository)
