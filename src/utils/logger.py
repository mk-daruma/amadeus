"""
ログ設定

アプリケーション全体のログ設定を管理します。
"""

import logging
import logging.handlers
import os
from pathlib import Path
from typing import Optional

from src.config import settings


def setup_logger(
    name: str = "amadeus",
    level: Optional[str] = None,
    log_file: Optional[str] = None,
) -> logging.Logger:
    """
    ログの設定を行います。
    
    Args:
        name: ログ名
        level: ログレベル
        log_file: ログファイルパス
    
    Returns:
        設定されたロガー
    """
    logger = logging.getLogger(name)
    
    # 既に設定済みの場合はそのまま返す
    if logger.handlers:
        return logger
    
    # ログレベル設定
    log_level = level or settings.log_level
    logger.setLevel(getattr(logging, log_level.upper()))
    
    # フォーマッター設定
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # コンソールハンドラー
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # ファイルハンドラー
    file_path = log_file or settings.log_file
    if file_path:
        # ログディレクトリ作成
        log_dir = Path(file_path).parent
        log_dir.mkdir(parents=True, exist_ok=True)
        
        # ローテーションハンドラー
        file_handler = logging.handlers.RotatingFileHandler(
            file_path,
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5,
            encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


# デフォルトロガー
logger = setup_logger()