from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from py_blog.depends import get_logger, get_user_service
from py_blog.schemas.users import User, UserLogin, UserRegister
from py_blog.services.users import UserService
from py_blog.utils.security import create_jwt_token, get_user_from_token

router = APIRouter(prefix="/api/auth", tags=["users"])


def get_user_router() -> APIRouter:
    return router


@router.post("/login", status_code=status.HTTP_200_OK)
def login(
    user: UserLogin,
    logger=Depends(get_logger),
    service: UserService = Depends(get_user_service),
):
    db_user = service.authenticate_user(user)
    if not db_user:
        logger.info(f"User not found: {user.username}")
        return JSONResponse(
            {"detail": "user not found"}, status_code=status.HTTP_404_NOT_FOUND
        )
    logger.info(f"Login successful for user: {user.username}")
    token = create_jwt_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@router.post(
    "/register", response_model=UserRegister, status_code=status.HTTP_201_CREATED
)
def register(
    user: UserRegister,
    logger=Depends(get_logger),
    service: UserService = Depends(get_user_service),
):
    logger.info(f"Registering new user: {user.username}")
    return service.create_user(user)


@router.get("/about_me", response_model=User, status_code=status.HTTP_200_OK)
async def about_me(
    current_user: str = Depends(get_user_from_token),
    logger=Depends(get_logger),
    service: UserService = Depends(get_user_service),
):
    user = service.get_user_by_username(current_user)
    if not user:
        logger.info(f"User not found: {current_user}")
        return JSONResponse(
            {"error": "User not found"}, status_code=status.HTTP_404_NOT_FOUND
        )
    logger.info(f"About me requested for user: {current_user}")
    return user
