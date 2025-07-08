# Docker Compose での amadeus 起動方法

このプロジェクトは Docker Compose を使用して FastAPI アプリケーション、データベース、VOICEVOX API サーバーを起動できます。

## 事前準備

1. 環境変数ファイルを作成：
```bash
cp .env.example .env
```

2. `.env` ファイルを編集して必要な API キーを設定：
   - `OPENAI_API_KEY`: OpenAI API キー
   - `PORCUPINE_ACCESS_KEY`: Porcupine ウェイクワード検出のアクセスキー

## 起動方法

### 1. すべてのサービスを起動
```bash
docker-compose up -d
```

### 2. ログを確認
```bash
# 全サービスのログを表示
docker-compose logs -f

# 特定のサービスのログを表示
docker-compose logs -f amadeus-api
docker-compose logs -f voicevox
docker-compose logs -f db
```

### 3. API にアクセス
- **FastAPI アプリケーション**: http://localhost:8000
- **FastAPI ドキュメント**: http://localhost:8000/docs
- **VOICEVOX API**: http://localhost:50021
- **PostgreSQL**: localhost:5432

## サービス構成

本プロジェクトでは以下のサービスが起動されます：

### amadeus-api
- **ポート**: 8000
- **機能**: FastAPI アプリケーション（音声秘書 AI のメイン API）
- **依存関係**: db, voicevox

### db
- **ポート**: 5432
- **機能**: PostgreSQL データベース
- **データベース名**: amadeus
- **ユーザー**: amadeus

### voicevox
- **ポート**: 50021
- **機能**: VOICEVOX 音声合成 API サーバー
- **使用モデル**: CPU版（開発用）

## 開発用コマンド

### サービスの停止
```bash
docker-compose down
```

### 完全にクリーンアップ（データベースデータも削除）
```bash
docker-compose down -v
```

### 特定のサービスのみ起動
```bash
# FastAPI アプリケーションのみ起動
docker-compose up amadeus-api

# VOICEVOX サーバーのみ起動
docker-compose up voicevox

# データベースのみ起動
docker-compose up db
```

### イメージを再ビルド
```bash
# 全サービスを再ビルド
docker-compose build

# 特定のサービスのみ再ビルド
docker-compose build amadeus-api

# キャッシュを使わずに再ビルド
docker-compose build --no-cache
```

### 開発時の便利コマンド

```bash
# サービスの状態を確認
docker-compose ps

# 実行中のコンテナに接続
docker-compose exec amadeus-api bash

# データベースに接続
docker-compose exec db psql -U amadeus -d amadeus

# VOICEVOX API の動作確認
curl http://localhost:50021/version
```

## トラブルシューティング

### ポート競合エラー
既に 8000 番ポートが使用されている場合：
```bash
# 使用中のプロセスを確認
lsof -i :8000

# docker-compose.yml でポート番号を変更
```

### 依存関係エラー
```bash
# イメージを再ビルド
docker-compose build --no-cache amadeus-api
```

### VOICEVOX API の起動に時間がかかる場合
VOICEVOX API サーバーは初回起動時にモデルのダウンロードを行うため、しばらく時間がかかります。
```bash
# ログで起動状況を確認
docker-compose logs -f voicevox
```

### 音声処理時のエラー
音声処理（PyAudio）を使用する場合、Dockerコンテナ内でのオーディオデバイスアクセスが制限されることがあります。
本格的な音声処理はRaspberry Pi上で実行することを前提としています。

## 次のステップ

1. **API の動作確認**: http://localhost:8000/docs でAPIドキュメントを確認
2. **VOICEVOX の動作確認**: http://localhost:50021 でVOICEVOX APIを確認
3. **開発環境での音声処理テスト**: 音声処理機能は段階的に追加
4. **Raspberry Pi へのデプロイ**: 本番環境での音声処理対応