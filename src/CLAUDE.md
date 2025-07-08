# 開発用ドキュメント - amadeus

amadeus（音声秘書AI）の開発に関する技術的な指針とブランチ戦略をまとめています。

## フェーズ1: 基本会話機能の開発戦略

### 推奨ブランチ戦略

#### 1. 基盤構築ブランチ
- `feature/project-structure` - Clean Architecture基盤
- `feature/fastapi-setup` - FastAPI基本設定とmain.py
- `feature/environment-config` - 環境変数・設定管理

#### 2. 音声処理コアブランチ
- `feature/audio-io-test` - 音声入出力テスト
- `feature/agents-sdk-integration` - agents SDK + 4o-mini連携
- `feature/wake-word-detection` - ウェイクワード検出（pvporcupine）
- `feature/speech-recognition` - 音声認識（Whisper API）
- `feature/voice-synthesis` - 音声合成（VOICEVOX）

#### 3. 統合・テストブランチ
- `feature/audio-pipeline` - 音声処理パイプライン統合
- `feature/conversation-loop` - 会話ループ実装

#### 4. 品質向上ブランチ
- `feature/testing-setup` - テスト環境構築
- `feature/error-handling` - エラーハンドリング強化
- `feature/logging` - ログ機能

### 推奨開発順序

1. **基盤構築フェーズ** (1-2週間)
   - Clean Architecture ディレクトリ構造
   - FastAPI基本設定
   - 環境変数管理

2. **コア機能開発フェーズ** (3-4週間)
   - agents SDK + 4o-mini 基本対話
   - 音声入出力テスト
   - ウェイクワード検出
   - 音声認識・合成

3. **統合・テストフェーズ** (1-2週間)
   - 音声処理パイプライン
   - 会話ループ統合

## Clean Architecture 実装ガイド

### ディレクトリ構造

```
src/
├── domain/
│   ├── entities/          # ドメインエンティティ
│   │   ├── conversation.py    # 会話エンティティ
│   │   ├── audio_data.py      # 音声データエンティティ
│   │   └── user_context.py    # ユーザーコンテキスト
│   └── repositories/      # リポジトリインターフェース
│       ├── conversation_repository.py
│       ├── audio_repository.py
│       └── user_context_repository.py
├── usecases/             # ユースケース
│   ├── conversation_usecase.py    # 会話処理
│   ├── audio_processing_usecase.py # 音声処理
│   └── wake_word_usecase.py       # ウェイクワード検出
├── infrastructure/       # 外部システム実装
│   ├── repositories/     # リポジトリ実装
│   │   ├── file_conversation_repository.py
│   │   └── memory_audio_repository.py
│   ├── gateways/         # 外部API実装
│   │   ├── openai_gateway.py      # OpenAI API
│   │   ├── voicevox_gateway.py    # VOICEVOX API
│   │   └── agents_sdk_gateway.py  # agents SDK
│   └── database/         # データベース（将来対応）
├── presentation/         # API・UI層
│   ├── routers/          # FastAPI ルーター
│   │   ├── conversation_router.py
│   │   └── audio_router.py
│   └── schemas/          # リクエスト・レスポンススキーマ
│       ├── conversation_schemas.py
│       └── audio_schemas.py
└── main.py              # FastAPI アプリケーション
```

### 実装方針

#### Domain Layer
- **Entities**: Pydanticモデルでドメインロジック
- **Repositories**: Protocol（abc）でインターフェース定義
- 外部依存なし、純粋なビジネスロジック

#### UseCase Layer
- ビジネスロジックの調整
- Repository・Gatewayインターフェースに依存
- 音声処理フローの制御

#### Infrastructure Layer
- 外部システムとの実際の通信
- OpenAI API、VOICEVOX API、agents SDK
- ファイル・メモリベースの永続化

#### Presentation Layer
- FastAPI ルーターとスキーマ
- HTTP エンドポイントの定義
- UseCase への委譲

### 技術スタック詳細

#### 音声処理
- **ウェイクワード**: `pvporcupine` 
- **音声認識**: `openai` (Whisper API)
- **音声合成**: `requests` + VOICEVOX API
- **会話AI**: `agents-sdk` + OpenAI 4o-mini

#### Web フレームワーク
- **FastAPI**: 非同期対応、自動ドキュメント生成
- **Pydantic**: データバリデーション、スキーマ定義
- **uvicorn**: ASGI サーバー

#### 音声処理ライブラリ
- **pyaudio**: 音声入出力
- **wave**: WAV ファイル処理
- **numpy**: 音声データ処理

### 開発時の注意点

1. **依存性の方向**: 常に内側（Domain）に向ける
2. **インターフェース分離**: 各レイヤーは抽象に依存
3. **テスト容易性**: モックやスタブで外部依存を置換
4. **型安全性**: 全てのコードに型ヒント必須
5. **非同期処理**: 音声処理・API呼び出しは async/await

### 環境設定

```bash
# 必要な環境変数
OPENAI_API_KEY=your_openai_api_key
VOICEVOX_API_URL=http://localhost:50021
PORCUPINE_ACCESS_KEY=your_porcupine_key
```

### テスト戦略

- **Unit Tests**: 各レイヤーの単体テスト
- **Integration Tests**: API・音声処理の統合テスト
- **E2E Tests**: 会話フロー全体のテスト

この開発戦略により、段階的かつ安全に音声秘書AIの実装を進めることができます。