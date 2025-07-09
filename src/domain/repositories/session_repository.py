"""
セッションリポジトリインターフェース

会話セッションの永続化を担うリポジトリインターフェース
"""

from typing import Protocol, Optional

from src.domain.entities.conversation_session import ConversationSession


class SessionRepository(Protocol):
    """セッションリポジトリのインターフェース"""
    
    def save(self, session: ConversationSession) -> None:
        """セッションを保存"""
        ...
    
    def get(self, session_id: str) -> Optional[ConversationSession]:
        """セッションを取得"""
        ...
    
    def delete(self, session_id: str) -> None:
        """セッションを削除"""
        ...