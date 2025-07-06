"""
アプリケーション設定

環境変数とアプリケーション設定を管理します。
"""

from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """アプリケーション設定"""
    
    # アプリケーション基本設定
    app_name: str = Field(default="amadeus", description="アプリケーション名")
    app_version: str = Field(default="0.1.0", description="アプリケーションバージョン")
    debug: bool = Field(default=False, description="デバッグモード")
    
    # サーバー設定
    host: str = Field(default="0.0.0.0", description="サーバーホスト")
    port: int = Field(default=8000, description="サーバーポート")
    
    # API設定
    api_v1_prefix: str = Field(default="/api/v1", description="API v1 プレフィックス")
    
    # OpenAI設定
    openai_api_key: Optional[str] = Field(default=None, description="OpenAI API キー")
    openai_model: str = Field(default="gpt-4o-mini", description="OpenAI モデル")
    
    # Whisper設定
    whisper_model: str = Field(default="whisper-1", description="Whisper モデル")
    
    # VOICEVOX設定
    voicevox_api_url: str = Field(default="http://localhost:50021", description="VOICEVOX API URL")
    voicevox_speaker_id: int = Field(default=3, description="VOICEVOX スピーカーID（ずんだもん）")
    
    # Porcupine設定
    porcupine_access_key: Optional[str] = Field(default=None, description="Porcupine アクセスキー")
    porcupine_keyword: str = Field(default="computer", description="ウェイクワード")
    
    # 音声設定
    audio_sample_rate: int = Field(default=16000, description="音声サンプリングレート")
    audio_channels: int = Field(default=1, description="音声チャンネル数")
    audio_chunk_size: int = Field(default=1024, description="音声チャンクサイズ")
    
    # ログ設定
    log_level: str = Field(default="INFO", description="ログレベル")
    log_file: Optional[str] = Field(default=None, description="ログファイルパス")
    
    # CORS設定
    cors_origins: list[str] = Field(default=["*"], description="CORS許可オリジン")
    
    # データベース設定
    database_url: Optional[str] = Field(default=None, description="データベース接続URL")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


def get_settings() -> Settings:
    """設定インスタンスを取得"""
    return Settings()


# グローバル設定インスタンス
settings = get_settings()