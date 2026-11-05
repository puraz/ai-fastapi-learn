from pydantic import BaseModel, ConfigDict, Field

class ChatAliasRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    session_id: str | None = Field(default=None, alias="sessionId")
    user_id: str | None = Field(default=None, alias="userId")
    message: str

request1 = ChatAliasRequest(
    sessionId="c_10001",
    userId="u_10001",
    message="你好"
)

request2 = ChatAliasRequest(
    session_id="c_10002",
    user_id="u_10002",
    message="你好"
)

print(request1.model_dump())
print(request1.model_dump(by_alias=True))
print(request2.model_dump())