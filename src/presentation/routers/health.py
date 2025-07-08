"""
ヘルスチェック用ルーター

アプリケーションの状態確認用のエンドポイントを提供します。
"""

from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

from src.config import settings
from src.utils.logger import logger

router = APIRouter(
    prefix="/health",
    tags=["health"],
)


class HealthResponse(BaseModel):
    """ヘルスチェックレスポンス"""
    status: str
    timestamp: datetime
    version: str
    app_name: str


@router.get("/", response_model=HealthResponse)
async def health_check():
    """基本的なヘルスチェック"""
    logger.info("Health check requested")
    
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now(),
        version=settings.app_version,
        app_name=settings.app_name
    )


@router.get("/detailed")
async def detailed_health_check():
    """詳細なヘルスチェック"""
    logger.info("Detailed health check requested")
    
    # 将来的にはデータベース接続、外部API接続などをチェック
    checks = {
        "database": "not_implemented",
        "openai_api": "not_implemented",
        "voicevox_api": "not_implemented",
        "audio_system": "not_implemented",
    }
    
    return {
        "status": "healthy",
        "timestamp": datetime.now(),
        "version": settings.app_version,
        "app_name": settings.app_name,
        "checks": checks
    }