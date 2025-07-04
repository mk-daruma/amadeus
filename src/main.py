"""
amadeus - 音声秘書AI メインアプリケーション

FastAPI アプリケーションのエントリーポイントです。
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="amadeus",
    description="音声秘書AI for Raspberry Pi",
    version="0.1.0",
)

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 開発用設定
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """ヘルスチェック用エンドポイント"""
    return {"message": "amadeus voice assistant is running"}


@app.get("/health")
async def health_check():
    """ヘルスチェック"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)