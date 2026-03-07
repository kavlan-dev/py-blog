from typing import Optional
from py_blog.repositories.interfaces import IUserRepository
from py_blog.schemas.users import UserRegister, User


class UserService:
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def get_user_by_username(self, username: str) -> Optional[User]:
        return self.repository.get_by_username(username)

    def create_user(self, user: UserRegister) -> User:
        return self.repository.create(user)
