import hashlib
from typing import Optional

from py_blog.repositories.interfaces import IUserRepository
from py_blog.schemas.users import User, UserLogin, UserRegister


class UserService:
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def get_user_by_username(self, username: str) -> Optional[User]:
        return self.repository.get_by_username(username)

    def authenticate_user(self, user: UserLogin) -> Optional[User]:
        db_user = self.repository.get_by_username(user.username)
        if (
            db_user
            and hashlib.sha256(user.password.encode("utf-8")).hexdigest()
            == db_user.password
        ):
            return db_user
        return None

    def create_user(self, user: UserRegister) -> User:
        hashed_password = hashlib.sha256(user.password.encode("utf-8")).hexdigest()
        user.password = hashed_password
        return self.repository.create(user)
