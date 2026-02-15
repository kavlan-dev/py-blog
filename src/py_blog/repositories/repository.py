from typing import List, Optional

from sqlalchemy.orm import Session

from py_blog.models.post import Post as PostModel
from py_blog.repositories.interfaces import BaseRepository
from py_blog.schemas.post import Post, PostCreate, PostUpdate


class PostRepository(BaseRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Post]:
        posts = self.db.query(PostModel).all()
        return [Post.model_validate(post) for post in posts]

    def get_by_id(self, post_id: int) -> Optional[Post]:
        post = self.db.query(PostModel).filter(PostModel.id == post_id).first()
        return Post.model_validate(post) if post else None

    def create(self, post: PostCreate) -> Post:
        db_post = PostModel(**post.model_dump())
        self.db.add(db_post)
        self.db.commit()
        self.db.refresh(db_post)
        return Post.model_validate(db_post)

    def update(self, post_id: int, post: PostUpdate) -> Optional[Post]:
        db_post = self.db.query(PostModel).filter(PostModel.id == post_id).first()
        if not db_post:
            return None

        for key, value in post.model_dump(exclude_unset=True).items():
            setattr(db_post, key, value)

        self.db.commit()
        self.db.refresh(db_post)
        return Post.model_validate(db_post)

    def delete(self, post_id: int) -> bool:
        post = self.db.query(PostModel).filter(PostModel.id == post_id).first()
        if not post:
            return False

        self.db.delete(post)
        self.db.commit()
        return True


def get_post_repository(db: Session) -> BaseRepository:
    return PostRepository(db)
