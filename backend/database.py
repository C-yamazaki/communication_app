from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# 環境変数からDATABASE_URLを取得
DATABASE_URL = os.environ.get("DATABASE_URL") or "postgresql://myuser:postgres@localhost/communication"

# DB接続用エンジン
engine = create_engine(DATABASE_URL, echo=True)

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
