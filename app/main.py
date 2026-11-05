from fastapi import FastAPI,Query

from app.api.v1.health import router as health_router
from app.api.v1.chat import router as chat_router
from app.api.v1.models import router as models_router
from app.api.v1.conversation import router as conversations_router
from app.api.v1.rag import router as rag_router

app = FastAPI(
    title = "我的api文档",
    description="Python + FastAPI + LLM + Agent 开发实战",
    version = "1.0.1"
)

app.include_router(health_router, prefix = "/api/v1", tags = ["Health"])
app.include_router(chat_router, prefix = "/api/v1", tags = ["Chat"])
app.include_router(models_router, prefix = "/api/v1", tags = ["Models"])
app.include_router(conversations_router, prefix = "/api/v1", tags = ["Conversations"])
app.include_router(rag_router, prefix = "/api/v1", tags = ["RAG"])

@app.get("/")
async def root():
    return {
        "message": "hello world"
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

