from abc import ABC, abstractmethod
from typing import List, Optional

from py_blog.schemas.articles import Article, ArticleCreate, ArticleUpdate
from py_blog.schemas.users import User, UserRegister


class IArticleRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Article]:
        pass

    @abstractmethod
    def get_by_id(self, post_id: int) -> Optional[Article]:
        pass

    @abstractmethod
    def create(self, post: ArticleCreate) -> Article:
        pass

    @abstractmethod
    def update(self, post_id: int, post: ArticleUpdate) -> Optional[Article]:
        pass

    @abstractmethod
    def delete(self, post_id: int) -> bool:
        pass


class IUserRepository(ABC):
    @abstractmethod
    def get_by_username(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    def create(self, user: UserRegister) -> User:
        pass
