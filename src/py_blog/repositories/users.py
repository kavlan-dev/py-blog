from typing import Optional

from sqlalchemy.orm import Session

from py_blog.models.users import User as UserModel
from py_blog.repositories.interfaces import IUserRepository
from py_blog.schemas.users import User, UserRegister


class UserRepository(IUserRepository):
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_username(self, username: str) -> Optional[User]:
        user = self.db.query(UserModel).filter(UserModel.username == username).first()
        return User.model_validate(user) if user else None

    def create(self, user: UserRegister) -> User:
        db_user = UserModel(**user.model_dump())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return User.model_validate(db_user)


def get_user_repository(db: Session) -> IUserRepository:
    return UserRepository(db)
