from typing import List, Optional

from py_blog.repositories.interfaces import BaseRepository
from py_blog.schemas.post import Post, PostCreate, PostUpdate


class PostService:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def get_all_posts(self) -> List[Post]:
        return self.repository.get_all()

    def get_post_by_id(self, post_id: int) -> Optional[Post]:
        return self.repository.get_by_id(post_id)

    def create_post(self, post: PostCreate) -> Post:
        return self.repository.create(post)

    def update_post(self, post_id: int, post: PostUpdate) -> Optional[Post]:
        return self.repository.update(post_id, post)

    def delete_post(self, post_id: int) -> bool:
        return self.repository.delete(post_id)


def get_post_service(repository: BaseRepository) -> PostService:
    return PostService(repository)
