from abc import ABC, abstractmethod
from typing import List, Optional

from py_blog.schemas.post import Post, PostCreate, PostUpdate


class BaseRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Post]:
        pass

    @abstractmethod
    def get_by_id(self, post_id: int) -> Optional[Post]:
        pass

    @abstractmethod
    def create(self, post: PostCreate) -> Post:
        pass

    @abstractmethod
    def update(self, post_id: int, post: PostUpdate) -> Optional[Post]:
        pass

    @abstractmethod
    def delete(self, post_id: int) -> bool:
        pass
