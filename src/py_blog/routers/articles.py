from typing import List

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from py_blog.core.depends import get_logger, get_post_service
from py_blog.core.security import get_user_from_token
from py_blog.schemas.articles import Article, ArticleCreate, ArticleUpdate
from py_blog.services.articles import ArticleService

router = APIRouter(prefix="/api/articles", tags=["posts"])


def get_article_router() -> APIRouter:
    return router


@router.get("", response_model=List[Article], status_code=status.HTTP_200_OK)
async def get_all_article(
    logger=Depends(get_logger),
    service: ArticleService = Depends(get_post_service),
) -> List[Article]:
    logger.info("Getting all articles")
    return service.get_all_posts()


@router.get("/{post_id}", response_model=Article, status_code=status.HTTP_200_OK)
async def get_article(
    post_id: int,
    logger=Depends(get_logger),
    service: ArticleService = Depends(get_post_service),
):
    post = service.get_post_by_id(post_id)
    if not post:
        logger.info(f"Article not found: {post_id}")
        return JSONResponse(
            {"detail": "Article not found"}, status_code=status.HTTP_404_NOT_FOUND
        )
    logger.info(f"Getting article: {post_id}")
    return post


@router.post("", response_model=Article, status_code=status.HTTP_201_CREATED)
async def create_article(
    post: ArticleCreate,
    logger=Depends(get_logger),
    current_user: str = Depends(get_user_from_token),
    service: ArticleService = Depends(get_post_service),
) -> Article:
    logger.info(f"Creating article: {post.title}")
    return service.create_post(post)


@router.put("/{post_id}", response_model=Article, status_code=status.HTTP_200_OK)
async def update_article(
    post_id: int,
    post: ArticleUpdate,
    logger=Depends(get_logger),
    current_user: str = Depends(get_user_from_token),
    service: ArticleService = Depends(get_post_service),
):
    updated_post = service.update_post(post_id, post)
    if not updated_post:
        logger.info(f"Article not found: {post_id}")
        return JSONResponse(
            {"detail": "Article not found"}, status_code=status.HTTP_404_NOT_FOUND
        )
    logger.info(f"Updating article: {post_id}")
    return updated_post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(
    post_id: int,
    logger=Depends(get_logger),
    current_user: str = Depends(get_user_from_token),
    service: ArticleService = Depends(get_post_service),
):
    success = service.delete_post(post_id)
    if not success:
        logger.info(f"Article not found: {post_id}")
        return JSONResponse(
            {"detail": "Article not found"}, status_code=status.HTTP_404_NOT_FOUND
        )
    logger.info(f"Deleting article: {post_id}")
    return None
