# PostgreSQL 15 ベースイメージ
FROM postgres:15

# 初期化スクリプトとテーブル作成スクリプトを設定
COPY init.sql /docker-entrypoint-initdb.d/init.sql
COPY init_tables.sql /docker-entrypoint-initdb.d/init_tables.sql

# デフォルトのPostgreSQLエントリーポイントを使う
CMD ["postgres"]
