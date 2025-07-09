"""
メッセージ役割列挙型

会話メッセージの役割定義
"""

from enum import Enum


class MessageRole(str, Enum):
    """メッセージの役割"""
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"