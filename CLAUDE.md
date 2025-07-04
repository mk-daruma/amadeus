# CLAUDE.md

このファイルは、Claude Code (claude.ai/code) がこのリポジトリでコードを扱う際のガイダンスを **日本語** で提供します。

## プロジェクト概要

本プロジェクト「amadeus」は **Clean Architecture** 原則に従った **Python / FastAPI** アプリケーションです。

## 開発環境

- **Python 3.11 以降** のランタイム
- **FastAPI** Web フレームワーク
- 開発ツール: `git`, `zsh`, `fzf`, `gh` (GitHub CLI), `jq`
- ネットワークユーティリティ: `iptables`, `ipset`, `iproute2`, `dnsutils`
- VS Code 拡張: Python, Pylint, Black (保存時に自動フォーマット)
- **Claude Code CLI** をグローバルインストール済み

## リポジトリ構成

- Clean Architecture に従った FastAPI アプリケーション
- Python 開発用に設定された **devcontainer**
- `main` ブランチで初期化された Git リポジトリ

## アーキテクチャ規約

このプロジェクトは Clean Architecture の原則に従い、以下のレイヤを持ちます。

### レイヤ構成

1. **Entity** – コアとなるビジネスエンティティとドメインモデル
2. **UseCase** – アプリケーションのビジネスロジック
3. **Gateway** – 外部システムとのインターフェース
4. **Repository** – データ永続化のインターフェース
5. **Router** – FastAPI ルーティングとリクエスト処理

### アーキテクチャガイドライン

- **依存性ルール**: 依存は内向きにのみ向ける。外側のレイヤは内側に依存できるが、その逆は不可。
- **Entity レイヤ**: 外部依存のない純粋なビジネスロジックを含む。
- **UseCase レイヤ**: Entity と Repository / Gateway インターフェースを用いてビジネス処理を調整する。
- **Repository / Gateway**: インターフェースを UseCase レイヤに定義し、実装は Infrastructure レイヤに配置する。
- **Router レイヤ**: HTTP 処理を担当し、UseCase に処理を委譲する。

### ディレクトリ構成

```text
src/
├── domain/
│   ├── entities/      # ビジネスエンティティ (Pydantic ドメインモデル)
│   └── repositories/  # Repository インターフェース (Protocol クラス)
├── usecases/          # アプリケーションビジネスロジック
├── infrastructure/
│   ├── repositories/  # Repository 実装
│   ├── gateways/      # 外部サービス実装
│   └── database/      # DB 接続およびモデル
├── presentation/
│   ├── routers/       # FastAPI ルータ
│   └── schemas/       # リクエスト／レスポンス用 Pydantic モデル
└── main.py            # FastAPI アプリケーションのエントリポイント
```

### 開発指針

- データのバリデーションとシリアライズには **Pydantic** を使用する。
- Repository インターフェースには Python の **Protocol** を用いる。
- FastAPI 依存は **presentation** 層のみに限定する。
- FastAPI の `Depends()` を使った依存性注入を活用する。
- **pytest** を用いて各レイヤを個別にテストする。
- ドメインと UseCase レイヤではフレームワーク依存を避ける。
- コード全体に **型ヒント** を徹底する。

### FastAPI 固有ガイドライン

- Router は薄く保ち、処理を UseCase に委譲する。
- リクエスト／レスポンススキーマにはドメインエンティティとは分離した **Pydantic** モデルを使用する。
- Repository 実装の注入には FastAPI の依存性注入機構を利用する。
- エラーは適切な **HTTP ステータスコード** でハンドリングする。
- I/O 操作には **async/await** を用いる。

## 開発ノート

- devcontainer には Claude Code がプリインストールされており、完全な開発環境を提供する。
- VS Code は Pylint と Black により保存時自動フォーマットが行われる。
- ネットワーク機能はネットワーク関連開発が可能なように設定済み。
- 新規コードは常に Clean Architecture 原則に従うこと。
- FastAPI の機能を活用しつつ、レイヤ間の境界を明確に保つこと。

---

### 会話言語に関する指示

**以降、Claude Code との対話は必ず日本語で行ってください。**
