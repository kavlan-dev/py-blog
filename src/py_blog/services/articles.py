from typing import List, Optional

from py_blog.repositories.interfaces import IArticleRepository
from py_blog.schemas.articles import Article, ArticleCreate, ArticleUpdate


class ArticleService:
    def __init__(self, repository: IArticleRepository):
        self.repository = repository

    def get_all_posts(self) -> List[Article]:
        return self.repository.get_all()

    def get_post_by_id(self, post_id: int) -> Optional[Article]:
        return self.repository.get_by_id(post_id)

    def create_post(self, post: ArticleCreate) -> Article:
        return self.repository.create(post)

    def update_post(self, post_id: int, post: ArticleUpdate) -> Optional[Article]:
        return self.repository.update(post_id, post)

    def delete_post(self, post_id: int) -> bool:
        return self.repository.delete(post_id)
