from app.core.config import settings

def test_get_settings():
    assert settings.app_name == "AI Agent Course API"
    assert settings.supported_model_list == [
        "deepseek-chat",
        "qwen-plus",
        "gpt-4o-mini",
    ]