from fastapi import APIRouter, HTTPException, Path, Query, Body
from app.schemas.chat import ChatRequest, ChatResponse, GenerateTitleRequest, GenerateTitleResponse
from app.services.chat_service import chat_with_ai
from app.schemas.response import ApiResponse

router = APIRouter()

@router.post("/chat", response_model = ApiResponse[ChatResponse])
async def chat(request: ChatRequest) -> ApiResponse[ChatResponse]:
    res = await chat_with_ai(request)
    return ApiResponse(
        data = res
    )

@router.post("/conversations/{conversation_id}/chat", response_model = ApiResponse[ChatResponse])
async def chat_in_conversation(
    request: ChatRequest,
    conversation_id: str = Path(..., description = "会话id"),
    debug: bool = Query(default = False, description = "是否开启调试模式")
) -> ApiResponse[ChatResponse]:
    result = await chat_with_ai(request)
    if debug:
        result.trace_id = result.trace_id or "debug_trace"
    result.session_id = conversation_id
    return ApiResponse(
        data = result
    )


@router.post("/chat/title", response_model=ApiResponse[GenerateTitleResponse])
async def generate_chat_title(
    # message: str = Body(..., embed=True, min_length=1, description="用户第一条消息"),
    request: GenerateTitleRequest
) -> ApiResponse[GenerateTitleResponse]:
    title = request.message[:20]
    return ApiResponse[GenerateTitleResponse](
        data = GenerateTitleResponse(title = title)
    )
