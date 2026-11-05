from fastapi import FastAPI,Query

from app.api.v1.api import api_router
from app.core.config import settings

def create_app() -> FastAPI:
    fast_app = FastAPI(
        title=settings.app_name,
        description="Python + FastAPI + LLM + Agent 开发实战",
        version=settings.app_version,
        debug=settings.debug
    )

    fast_app.include_router(api_router, prefix=settings.api_v1_prefix)

    @fast_app.get("/")
    async def root():
        return {
            "message": settings.app_name,
            "env": settings.app_env,
            "version": settings.app_version,
        }

    return fast_app

app = create_app()
