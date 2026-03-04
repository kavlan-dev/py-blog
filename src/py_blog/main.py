from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from py_blog.routers.articles import get_router


app = FastAPI()

router = get_router()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
