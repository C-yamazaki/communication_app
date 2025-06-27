# Python ベースイメージを使用
FROM python:3.12.4-slim

# ビルドに必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    build-essential gcc curl libpq-dev \
    && pip install --upgrade pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを設定（アプリケーションのコードを管理するディレクトリ）
WORKDIR /backend

# 依存関係をインストール（キャッシュ削減のためのオプション付き）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコピー（アプリケーション全体をコンテナに配置）
COPY . ./

# ポートを公開（FastAPIのデフォルトポートを開放）
EXPOSE 8000

# FastAPI アプリを起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


