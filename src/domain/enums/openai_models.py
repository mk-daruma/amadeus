"""
OpenAI モデル列挙型

使用可能なOpenAI APIモデルの定義
"""

from enum import Enum


class OpenAIModel(str, Enum):
    """OpenAI APIで使用可能なモデル"""
    
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_4O = "gpt-4o"
    GPT_4_TURBO = "gpt-4-turbo"
    GPT_3_5_TURBO = "gpt-3.5-turbo"