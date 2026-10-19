from uuid import UUID

from pydantic import BaseModel, Field


class ChatbotAnswer(BaseModel):
    submission_id: UUID
    step_code: str = Field(min_length=1, max_length=50)
    comment: str = Field(default="", max_length=2000)
    score: int | None = Field(default=None, ge=1, le=5, strict=True)
    chat_history: list[str] = Field(default_factory=list, max_length=200)
