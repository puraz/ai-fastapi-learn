from fastapi import APIRouter, Path, Query

from app.schemas.conversation import (
    ConversationCreateRequest,
    ConversationMessagesResponse,
    ConversationResponse,
)
from app.schemas.response import ApiResponse
from app.service.conversation_service import create_conversation, get_conversation_messages


router = APIRouter()

@router.post("/conversations", response_model = ApiResponse[ConversationResponse])
async def create_new_conversation(
    request: ConversationCreateRequest,
) -> ApiResponse[ConversationResponse]:
    result = await create_conversation(request)
    return ApiResponse[ConversationResponse](
        data = result
    )

@router.get("/conversations/{conversation_id}/messages", response_model = ApiResponse[ConversationMessagesResponse])
async def get_messages(
    conversation_id: str = Path(..., description = "会话 ID")
) -> ApiResponse[ConversationMessagesResponse]:
    result = await get_conversation_messages(conversation_id)

    return ApiResponse[ConversationMessagesResponse](
        data = result
    )
    