from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from py_blog.core.depends import get_user_service
from py_blog.core.security import create_jwt_token, get_user_from_token
from py_blog.schemas.users import UserRegister
from py_blog.services.users import UserService

router = APIRouter(prefix="/api/auth", tags=["users"])


def get_user_router() -> APIRouter:
    return router


@router.post("/login")
def login(
    user: OAuth2PasswordRequestForm = Depends(),
    service: UserService = Depends(get_user_service),
):
    db_user = service.get_user_by_username(user.username)
    if not db_user:
        raise HTTPException(status_code=404, detail="user not found")
    if user.password != db_user.password:
        raise HTTPException(status_code=401, detail="invalid credentials")
    token = create_jwt_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/register")
def register(user: UserRegister, service: UserService = Depends(get_user_service)):
    return service.create_user(user)


@router.get("/about_me")
async def about_me(
    current_user: str = Depends(get_user_from_token),
    service: UserService = Depends(get_user_service),
):
    """
    Этот маршрут защищен и требует токен. Если токен действителен, мы возвращаем информацию о пользователе.
    """
    user = service.get_user_by_username(current_user)
    if not user:
        return {"error": "User not found"}
    return user
