import uuid

from app.repositories.conversation_repository import conversation_repository
from app.schemas.conversation import (
    ConversationCreateRequest,
    ConversationMessagesResponse,
    ConversationResponse,
)


async def create_conversation(request: ConversationCreateRequest) -> ConversationResponse:
    conversation_id = f"c_{uuid.uuid4().hex[:8]}"

    res = await conversation_repository.create(
        conversation_id = conversation_id,
        request = request
    )
    return ConversationResponse(
        conversation_id = res.get("conversation_id"),
        title=res.get("title")
    )

async def get_conversation_messages(
    conversation_id: str
) -> ConversationMessagesResponse:
    messages = await conversation_repository.get_messages(conversation_id)
    return ConversationMessagesResponse(
        conversation_id=conversation_id,
        messages=messages
    )