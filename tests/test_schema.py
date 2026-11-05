"""ChatRequest / ChatMessage 的 schema 校验测试。

运行（项目根目录）：
    uv run pytest
    uv run pytest tests/test_schema.py -v
"""

import pytest
from pydantic import ValidationError

from app.schemas.chat import ChatMessage, ChatRequest, MessageRole


def make_messages() -> list[ChatMessage]:
    return [
        ChatMessage(role=MessageRole.SYSTEM, content="你是一个专业 AI 助手"),
        ChatMessage(role=MessageRole.USER, content="什么是 AI Agent？"),
    ]


def test_chat_request_serialization():
    request = ChatRequest(
        messages=make_messages(),
        model="deepseek-chat",
        temperature=0.7,
        stream=False,
    )

    data = request.model_dump()

    assert data["model"] == "deepseek-chat"
    assert data["temperature"] == 0.7
    assert data["stream"] is False
    assert data["session_id"] is None
    assert [m["role"] for m in data["messages"]] == [
        MessageRole.SYSTEM,
        MessageRole.USER,
    ]
    assert data["messages"][1]["content"] == "什么是 AI Agent？"


def test_role_enum_accepts_plain_string():
    message = ChatMessage(role="user", content="hi")
    assert message.role == MessageRole.USER


def test_messages_must_not_be_empty():
    with pytest.raises(ValidationError):
        ChatRequest(messages=[])


def test_message_content_must_not_be_empty():
    with pytest.raises(ValidationError):
        ChatMessage(role=MessageRole.USER, content="")


@pytest.mark.parametrize("model", ["deepseek-chat", "qwen-plus", "gpt-4o-mini"])
def test_supported_models_are_accepted(model):
    request = ChatRequest(messages=make_messages(), model=model)
    assert request.model == model


def test_unsupported_model_is_rejected():
    with pytest.raises(ValidationError) as exc_info:
        ChatRequest(messages=make_messages(), model="gpt-5")
    assert "不支持的模型" in str(exc_info.value)


@pytest.mark.parametrize("temperature", [-0.1, 2.1])
def test_temperature_out_of_range_is_rejected(temperature):
    with pytest.raises(ValidationError):
        ChatRequest(messages=make_messages(), temperature=temperature)


def test_extra_field_is_forbidden():
    with pytest.raises(ValidationError):
        ChatRequest(messages=make_messages(), foo=1)
