from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# テスト環境判定（TESTING=true のときSQLiteのインメモリを使用）
TESTING = os.environ.get("TESTING") == "true"

if TESTING:
    DATABASE_URL = "sqlite:///:memory:"
    CONNECT_ARGS = {"check_same_thread": False}
else:
    DATABASE_URL = os.environ.get("DATABASE_URL") or "postgresql://myuser:postgres@localhost/communication"
    CONNECT_ARGS = {}
    
    # DB接続用エンジン
engine = create_engine(DATABASE_URL, echo=True, connect_args=CONNECT_ARGS)


# 環境変数からDATABASE_URLを取得
# DATABASE_URL = os.environ.get("DATABASE_URL") or "postgresql://myuser:postgres@localhost/communication"

# DB接続用エンジン
# engine = create_engine(DATABASE_URL, echo=True)

# セッションファクトリ
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ベースクラス（models.pyで継承する）
Base = declarative_base()

# FastAPIのDependsで使えるセッション取得関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
