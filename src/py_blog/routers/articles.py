from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status

from py_blog.core.depends import get_post_service
from py_blog.schemas.articles import Article, ArticleCreate, ArticleUpdate
from py_blog.services.articles import ArticleService

router = APIRouter(prefix="/api/articles", tags=["posts"])


def get_article_router() -> APIRouter:
    return router


@router.get("", response_model=List[Article])
async def get_all_article(
    service: ArticleService = Depends(get_post_service),
) -> List[Article]:
    return service.get_all_posts()


@router.get("/{post_id}", response_model=Article)
async def get_article(
    post_id: int, service: ArticleService = Depends(get_post_service)
) -> Optional[Article]:
    post = service.get_post_by_id(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.post("", response_model=Article, status_code=status.HTTP_201_CREATED)
async def create_article(
    post: ArticleCreate, service: ArticleService = Depends(get_post_service)
) -> Article:
    return service.create_post(post)


@router.put("/{post_id}", response_model=Article)
async def update_article(
    post_id: int,
    post: ArticleUpdate,
    service: ArticleService = Depends(get_post_service),
) -> Article:
    updated_post = service.update_post(post_id, post)
    if not updated_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(
    post_id: int, service: ArticleService = Depends(get_post_service)
) -> None:
    success = service.delete_post(post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return None
