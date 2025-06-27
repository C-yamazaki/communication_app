# Flutter × FastAPI × PostgreSQL サンプルプロジェクト

このプロジェクトは、Flutter（Web）をフロントエンドに、FastAPIをバックエンド、PostgreSQLをデータベースとして使用した全体統合のサンプル構成です。

---

## 前提条件（Macユーザー向け）

このプロジェクトはDockerを用いて構築されていますが、現在のところ **Mac環境での利用を前提**としています。

### 必要なツール

- [Docker Desktop for Mac](https://www.docker.com/ja-jp/)

> ※ Windowsでの使用は非推奨です。

---

## ディレクトリ構成

```
frontend/      # Flutter Webアプリケーション  
backend/       # FastAPI アプリケーション　(API)  
db/            # PostgreSQLと初期化スクリプト  
docker-compose.yml  # 各サービスの連携定義
```

---

## 使用技術

* Flutter 3.29.2（Webアプリ用）
* Python 3.12.4（FastAPI 0.110.1）
* PostgreSQL 15
* Docker & Docker Compose

---

## 起動方法・アクセスURL

```bash
docker-compose up -d
```

> フロントエンド (Flutter) は、ホットリロードの使用を実現するためbashシェルで起動しており、手動でFlutter Webサーバーを起動する必要があります。

Flutterのコンテナが起動したら、別ターミナルで以下を実行します:

```bash
docker compose exec flutter bash
flutter run -d web-server --web-hostname 0.0.0.0 --web-port 5000
```

ブラウザでアクセス:

* フロントエンド (Flutter Web) : [http://localhost:5001](http://localhost:5001)
* バックエンド (FastAPI Swagger UI) : [http://localhost:8001/docs](http://localhost:8001/docs)

---

## API エンドポイント例

* `GET /users` : 登録済みユーザー一覧を取得
* `POST /users` : 新しいユーザーを登録

---

## 環境変数

* `API_BASE_URL`: Flutterから通信するAPIのURL（docker-composeで自動設定されます）
* `DATABASE_URL`: FastAPIからPostgreSQLへの接続URL

---

## データベース初期化

初回起動時に、以下のスクリプトが自動実行されます:

* `init.sql`: DBとユーザー作成
* `init_tables.sql`: テーブルの定義

---

## 注意点

このリポジトリは教育・検証用途であり、本番環境での使用は推奨されません。

---