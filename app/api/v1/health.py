from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/health")
async def health():
    return {
        "status": "ok",
        "services": "ai-agent-course",
        "version": "0.1.0"
    }

@router.get("/error-demo")
async def error_demo():
    raise HTTPException(
        status_code=400,
        detail="这是一个错误示例"
    )