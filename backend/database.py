from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# テスト環境判定（TESTING=true のときSQLiteのインメモリを使用）
TESTING = os.environ.get("TESTING") == "true"

if TESTING:
    DATABASE_URL = "sqlite:///./test.db"    #"sqlite:///:memory:の一時的からファイルベース化に変更"
    CONNECT_ARGS = {"check_same_thread": False}
else:
    # 本番環境のデータベースURL
    DATABASE_URL = os.environ.get("DATABASE_URL") or "postgresql://myuser:postgres@localhost/communication"
    CONNECT_ARGS = {}
    
    # DB接続用エンジン
engine = create_engine(DATABASE_URL, echo=True, connect_args=CONNECT_ARGS)



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
    