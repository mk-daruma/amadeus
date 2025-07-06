"""
amadeus - 音声秘書AI メインアプリケーション

FastAPI アプリケーションのエントリーポイントです。
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
from src.utils.logger import logger
from src.presentation.routers import health, conversation, audio

# FastAPI アプリケーション作成
app = FastAPI(
    title=settings.app_name,
    description="音声秘書AI for Raspberry Pi",
    version=settings.app_version,
    debug=settings.debug,
)

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーター登録
app.include_router(health.router, prefix=settings.api_v1_prefix)
app.include_router(conversation.router, prefix=settings.api_v1_prefix)
app.include_router(audio.router, prefix=settings.api_v1_prefix)


@app.on_event("startup")
async def startup_event():
    """アプリケーション起動時の処理"""
    logger.info(f"Starting {settings.app_name} v{settings.app_version}")
    logger.info(f"Debug mode: {settings.debug}")
    logger.info(f"API prefix: {settings.api_v1_prefix}")


@app.on_event("shutdown")
async def shutdown_event():
    """アプリケーション終了時の処理"""
    logger.info(f"Shutting down {settings.app_name}")


@app.get("/")
async def root():
    """ルートエンドポイント"""
    return {
        "message": f"{settings.app_name} voice assistant is running",
        "version": settings.app_version,
        "api_docs": "/docs",
        "health_check": f"{settings.api_v1_prefix}/health"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port,
        log_level=settings.log_level.lower()
    )