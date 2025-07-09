"""
メッセージエンティティ

会話メッセージを表すドメインエンティティ
"""

from datetime import datetime
from pydantic import BaseModel, Field

from src.domain.enums.message_roles import MessageRole


class Message(BaseModel):
    """会話メッセージ"""
    role: MessageRole
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)
    
    def to_string(self) -> str:
        """辞書形式を文字列に変換"""
        return f'{{"role": "{self.role.value}", "content": "{self.content}"}}'