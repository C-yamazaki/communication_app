# Dart ベースの公式イメージを使用（Flutterの環境構築用）
FROM dart:stable AS build

# 必要なツールをインストール（gitやcurlなどFlutter環境に必要なものをセットアップ）
RUN apt-get update && apt-get install -y git curl unzip xz-utils && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Flutter SDK を指定バージョンでクローン
RUN git clone --branch 3.29.2 https://github.com/flutter/flutter.git /flutter

# バージョン確認（任意）
RUN /flutter/bin/flutter --version

# Flutter をパスに追加（Dart SDKも含む）
ENV PATH="/flutter/bin:/flutter/bin/cache/dart-sdk/bin:${PATH}"

# Flutter 環境をセットアップ（必要なキャッシュや依存関係を準備）
RUN flutter doctor && flutter precache --web

# 作業ディレクトリを設定（アプリケーションのコードを配置するためのディレクトリ）
WORKDIR /frontend

# ソースコードをコピー
COPY . ./

# 依存関係を解決
RUN flutter pub get

# --- 以下は開発用の設定 ---

# 開発用に EXPOSE を設定（FlutterのデフォルトWebサーバー用ポート）
EXPOSE 5000

# 開発用のコマンド（コンテナ上では手動でFlutter実行）
CMD ["bash"]
# →コンテナに入ったら「flutter run -d web-server --web-hostname 0.0.0.0 --web-port 5000」で実行
