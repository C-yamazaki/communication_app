-- データベースを作成（存在しない場合のみ）
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_database WHERE datname = 'communication'
    ) THEN
        CREATE DATABASE communication WITH ENCODING 'UTF8' LC_COLLATE='en_US.utf8' LC_CTYPE='en_US.utf8' TEMPLATE=template0;
    END IF;
END $$;

-- 新しいユーザーを作成（存在しない場合のみ）
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_roles WHERE rolname = 'myuser'
    ) THEN
        CREATE ROLE myuser WITH LOGIN PASSWORD 'postgres';
    END IF;
END $$;

-- 作成したデータベースにユーザーを割り当てる
GRANT ALL PRIVILEGES ON DATABASE communication TO myuser;
