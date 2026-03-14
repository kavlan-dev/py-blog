import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from py_blog.routers.articles import get_article_router
from py_blog.routers.users import get_user_router

app = FastAPI()

app.include_router(get_article_router())
app.include_router(get_user_router())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
