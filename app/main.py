from fastapi import FastAPI,Query

from app.api.v1.api import api_router
from app.api.v1.health import router as health_router
from app.api.v1.chat import router as chat_router
from app.api.v1.models import router as models_router
from app.api.v1.conversation import router as conversations_router
from app.api.v1.rag import router as rag_router
from app.core.config import settings

app = FastAPI(
    title = settings.app_name,
    description="Python + FastAPI + LLM + Agent 开发实战",
    version = settings.app_version,
    debug=settings.debug
)

app.include_router(api_router, prefix=settings.api_v1_prefix)

@app.get("/")
async def root():
    return {
        "message": settings.app_name,
        "env": settings.app_env,
        "version": settings.app_version,
    }


@app.get("/get_user/{user_id}")
async def get_user(user_id: int):
    return {
        "user_id": user_id,
        "user_name": f"用户：{user_id}"
    }

@app.get("/search")
async def search(
    q: str = Query(..., min_length = 1, max_length = 1000, description="搜索关键词"),
    page: int = Query(default = 1, ge = 1, description="页码"),
    page_size: int = Query(default = 10, ge = 1, le = 100, description = "每页数量")
):
    return {
           "q": q,
           "page": page,
           "page_size": page_size
    }

