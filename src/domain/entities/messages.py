"""
メッセージリストエンティティ

メッセージの集合を表すドメインエンティティ
"""

from typing import List
from pydantic import BaseModel, Field

from .message import Message


class Messages(BaseModel):
    """メッセージリスト"""
    items: List[Message] = Field(default_factory=list)
    
    def to_string(self) -> str:
        """メッセージリストを文字列化"""
        return "[" + ", ".join(msg.to_string() for msg in self.items) + "]"