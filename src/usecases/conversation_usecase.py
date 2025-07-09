"""
会話ユースケース

会話処理のビジネスロジックを担当
"""

from src.domain.entities.conversation_session import ConversationSession
from src.domain.entities.message import Message
from src.domain.entities.messages import Messages
from src.domain.enums.message_roles import MessageRole
from src.domain.repositories.session_repository import SessionRepository
from src.infrastructure.gateways.agents_gateway import AgentsGateway


class ConversationUseCase:
    """会話ユースケース"""
    
    def __init__(
        self,
        session_repository: SessionRepository,
        agents_gateway: AgentsGateway
    ):
        self.session_repository = session_repository
        self.agents_gateway = agents_gateway
    
    async def process_user_message(
        self,
        session_id: str,
        user_id: str,
        user_message: str
    ) -> str:
        """
        ユーザーメッセージを処理する
        
        Args:
            session_id: セッションID
            user_id: ユーザーID
            user_message: ユーザーからのメッセージ
            
        Returns:
            str: AIからの応答メッセージ
        """
        # セッションを取得または作成
        session = self.session_repository.get(session_id)
        if session is None:
            session = ConversationSession(
                session_id=session_id,
                user_id=user_id
            )
        
        # ユーザーメッセージを追加
        user_msg = Message(
            role=MessageRole.USER,
            content=user_message
        )
        session.messages.items.append(user_msg)
        
        # AIによる応答を取得
        ai_response = await self.agents_gateway.process_conversation(session.messages)
        
        # AIメッセージを追加
        ai_msg = Message(
            role=MessageRole.ASSISTANT,
            content=ai_response
        )
        session.messages.items.append(ai_msg)
        
        # セッションを保存
        self.session_repository.save(session)
        
        return ai_response