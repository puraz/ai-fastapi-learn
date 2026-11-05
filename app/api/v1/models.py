from fastapi import APIRouter

router = APIRouter()

@router.get("/models")
async def list_models():
    return {
        "models": {
            "deepseek-chat",
            "qwen-plus",
            "gpt-4o-mini"
        }
    }