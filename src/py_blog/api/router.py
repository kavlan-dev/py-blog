from typing import List

from fastapi import APIRouter, HTTPException, status

from py_blog.schemas.post import Post, PostCreate, PostUpdate
from py_blog.services.service import PostService


class PostRouter:
    def __init__(self, service: PostService):
        self.service = service
        self.router = APIRouter(prefix="/api/posts", tags=["posts"])
        self._setup_routes()

    def _setup_routes(self):
        @self.router.get("/", response_model=List[Post])
        async def get_all_posts():
            return self.service.get_all_posts()

        @self.router.get("/{post_id}", response_model=Post)
        async def get_post(post_id: int):
            post = self.service.get_post_by_id(post_id)
            if not post:
                raise HTTPException(status_code=404, detail="Post not found")
            return post

        @self.router.post("/", response_model=Post, status_code=status.HTTP_201_CREATED)
        async def create_post(post: PostCreate):
            return self.service.create_post(post)

        @self.router.put("/{post_id}", response_model=Post)
        async def update_post(post_id: int, post: PostUpdate):
            updated_post = self.service.update_post(post_id, post)
            if not updated_post:
                raise HTTPException(status_code=404, detail="Post not found")
            return updated_post

        @self.router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
        async def delete_post(post_id: int):
            success = self.service.delete_post(post_id)
            if not success:
                raise HTTPException(status_code=404, detail="Post not found")
            return None


def get_router(service: PostService) -> APIRouter:
    return PostRouter(service).router
