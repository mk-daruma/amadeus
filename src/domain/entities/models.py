"""
AIモデル定義

使用可能なAIモデルのEnum定義
"""

from enum import Enum


class OpenAIModel(str, Enum):
    """OpenAI APIで使用可能なモデル"""
    
    GPT_4O_MINI = "gpt-4o-mini"