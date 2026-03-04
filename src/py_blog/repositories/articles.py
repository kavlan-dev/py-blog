from typing import List, Optional

from sqlalchemy.orm import Session

from py_blog.models.articles import Article as ArticleModel
from py_blog.repositories.interfaces import IArticleRepository
from py_blog.schemas.articles import Article, ArticleCreate, ArticleUpdate


class ArticleRepository(IArticleRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Article]:
        posts = self.db.query(ArticleModel).all()
        return [Article.model_validate(post) for post in posts]

    def get_by_id(self, post_id: int) -> Optional[Article]:
        post = self.db.query(ArticleModel).filter(ArticleModel.id == post_id).first()
        return Article.model_validate(post) if post else None

    def create(self, post: ArticleCreate) -> Article:
        db_post = ArticleModel(**post.model_dump())
        self.db.add(db_post)
        self.db.commit()
        self.db.refresh(db_post)
        return Article.model_validate(db_post)

    def update(self, post_id: int, post: ArticleUpdate) -> Optional[Article]:
        db_post = self.db.query(ArticleModel).filter(ArticleModel.id == post_id).first()
        if not db_post:
            return None

        for key, value in post.model_dump(exclude_unset=True).items():
            setattr(db_post, key, value)

        self.db.commit()
        self.db.refresh(db_post)
        return Article.model_validate(db_post)

    def delete(self, post_id: int) -> bool:
        post = self.db.query(ArticleModel).filter(ArticleModel.id == post_id).first()
        if not post:
            return False

        self.db.delete(post)
        self.db.commit()
        return True


def get_article_repository(db: Session) -> IArticleRepository:
    return ArticleRepository(db)
