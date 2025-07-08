"""
会話用ルーター

音声会話・テキスト会話のエンドポイントを提供します。
"""

from fastapi import APIRouter, HTTPException, File, UploadFile
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from src.utils.logger import logger

router = APIRouter(
    prefix="/conversation",
    tags=["conversation"],
)


class TextConversationRequest(BaseModel):
    """テキスト会話リクエスト"""
    message: str
    user_id: Optional[str] = None
    session_id: Optional[str] = None


class ConversationResponse(BaseModel):
    """会話レスポンス"""
    response: str
    timestamp: datetime
    session_id: Optional[str] = None


@router.post("/text", response_model=ConversationResponse)
async def text_conversation(request: TextConversationRequest):
    """テキストベースの会話"""
    logger.info(f"Text conversation request: {request.message}")
    
    # 将来的にはUseCaseに処理を委譲
    # 現在は仮実装
    response_text = f"受け取ったメッセージ: {request.message}"
    
    return ConversationResponse(
        response=response_text,
        timestamp=datetime.now(),
        session_id=request.session_id
    )


@router.post("/audio", response_model=ConversationResponse)
async def audio_conversation(
    audio_file: UploadFile = File(...),
    user_id: Optional[str] = None,
    session_id: Optional[str] = None,
):
    """音声ベースの会話"""
    logger.info(f"Audio conversation request: {audio_file.filename}")
    
    # 音声ファイルの検証
    if not audio_file.content_type.startswith("audio/"):
        raise HTTPException(
            status_code=400,
            detail="音声ファイルをアップロードしてください"
        )
    
    # 将来的には音声認識→会話処理→音声合成の流れを実装
    # 現在は仮実装
    response_text = f"音声ファイル '{audio_file.filename}' を受信しました"
    
    return ConversationResponse(
        response=response_text,
        timestamp=datetime.now(),
        session_id=session_id
    )


@router.get("/sessions/{session_id}/history")
async def get_conversation_history(session_id: str):
    """会話履歴取得"""
    logger.info(f"Conversation history request for session: {session_id}")
    
    # 将来的にはRepositoryから履歴を取得
    return {
        "session_id": session_id,
        "history": [],
        "message": "会話履歴機能は未実装です"
    }