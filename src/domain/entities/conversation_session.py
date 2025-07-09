"""
会話セッションエンティティ

会話セッションを表すドメインエンティティ
"""

from datetime import datetime
from pydantic import BaseModel, Field

from .messages import Messages


class ConversationSession(BaseModel):
    """会話セッション"""
    session_id: str
    user_id: str
    messages: Messages = Field(default_factory=Messages)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)