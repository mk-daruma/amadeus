"""
OpenAI Agents SDK Gateway

OpenAI Agents SDKを使用した会話処理ゲートウェイ実装
"""

import os
from agents import Agent, Runner

from src.domain.enums.openai_models import OpenAIModel
from src.domain.entities.messages import Messages
from src.utils.logger import logger


class AgentsGateway:
    """OpenAI Agents SDKを使用した会話処理ゲートウェイ"""
    
    def __init__(
        self,
        api_key: str,
        model: OpenAIModel,
        instructions: str,
        agent_name: str = "Assistant"
    ):
        """
        Agents Gatewayの初期化
        
        Args:
            api_key: OpenAI API キー
            model: 使用するモデル
            instructions: エージェントの指示プロンプト
            agent_name: エージェントの名前
        """
        # OpenAI API キーの設定
        os.environ["OPENAI_API_KEY"] = api_key
        
        # 音声秘書エージェントの初期化
        self.voice_assistant_agent = Agent(
            name=agent_name,
            instructions=instructions,
            model=model.value,
        )
        
        logger.info("Agents Gateway initialized with model: %s", model.value)
    
    async def process_conversation(
        self, 
        messages: Messages
    ) -> str:
        """
        会話履歴を含めてメッセージを処理する
        
        Args:
            messages: 会話履歴（Messagesエンティティ）
            
        Returns:
            str: エージェントからの応答メッセージ
            
        Raises:
            Exception: API呼び出しに失敗した場合
        """
        try:
            logger.info("Processing conversation with messages")
            
            # Agents SDKを使用して会話を処理
            result = Runner.run_sync(
                agent=self.voice_assistant_agent,
                messages=messages.to_string()
            )
            
            # レスポンスを取得
            response_text = str(result.messages[-1].content) if result.messages else "申し訳ございませんが、応答を生成できませんでした。"
            
            logger.info(
                "Conversation processed successfully - Response length: %d",
                len(response_text)
            )
            
            return response_text
            
        except Exception as e:
            logger.error(
                "Failed to process conversation: %s",
                str(e),
                exc_info=True
            )
            raise Exception(f"会話処理中にエラーが発生しました: {str(e)}")