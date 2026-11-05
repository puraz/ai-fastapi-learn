from pydantic import BaseModel, Field
from typing import Any, Generic, TypeVar

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    code: int = Field(default = 200, description = "业务状态码")
    message: str = Field(default = "success", description = "提示信息")
    data: T | None = Field(default=None, description="响应数据")

class ErrorResponse(BaseModel):
    code: int = Field(default=500, description="错误码")
    message: str = Field(..., description="错误信息")
    detail: str | None = Field(default=None, description="错误详情")