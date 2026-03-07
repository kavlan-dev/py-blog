from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str


class UserRegister(UserBase):
    pass


class UserLogin(UserBase):
    pass


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
