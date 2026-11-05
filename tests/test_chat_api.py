"""POST /api/v1/chat 的集成测试，需要本地服务在 8000 端口运行。

先启动服务：
    uv run uvicorn app.main:app --reload
再跑测试：
    uv run pytest                     # 服务没起时自动 skip
    uv run pytest -m "not integration" # 只跑不依赖服务的用例
"""

import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"
URL = f"{BASE_URL}/api/v1/chat"

pytestmark = pytest.mark.integration


def server_is_up() -> bool:
    try:
        requests.get(f"{BASE_URL}/docs", timeout=1)
    except requests.RequestException:
        return False
    return True


@pytest.fixture(scope="module")
def server():
    if not server_is_up():
        pytest.skip("服务未启动：uv run uvicorn app.main:app --reload")


def test_chat_endpoint(server):
    payload = {
        "messages": [
            {"role": "system", "content": "你是一个专业 AI 助手"},
            {"role": "user", "content": "什么是 RAG？"},
        ],
        "model": "deepseek-chat",
        "temperature": 0.7,
        "stream": False,
    }

    resp = requests.post(URL, json=payload, timeout=60)

    assert resp.status_code == 200
    body = resp.json()

    # ApiResponse 统一信封：{code, message, data}
    assert body["code"] == 200
    data = body["data"]
    assert data["model"] == "deepseek-chat"
    assert data["session_id"]
    assert "RAG" in data["answer"]
