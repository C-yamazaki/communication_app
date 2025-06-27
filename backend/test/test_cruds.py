# test/test_cruds.py

import os
os.environ["TESTING"] = "true"

from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import cruds
from schemas import UserCreate
from models import User


def setup_module(module):
    # モジュールの最初でテーブル作成（1回のみ）
    Base.metadata.create_all(bind=engine)

def teardown_function(function):
    # 各テスト後にDBをクリア
    db = SessionLocal()
    db.query(User).delete()
    db.commit()
    db.close()

def test_create_user_success():
    db: Session = SessionLocal()

    user_in = UserCreate(
        nickname="テストユーザー",
        employee_code="EMP123",
        admin=False
    )

    user = cruds.create_user(db, user_in)

    assert user.id is not None
    assert user.nickname == "テストユーザー"
    assert user.employee_code == "EMP123"
    assert user.admin is False
    db.close()


def test_create_user_duplicate():
    db: Session = SessionLocal()

    user1 = UserCreate(nickname="ユーザー1", employee_code="EMP999", admin=False)
    cruds.create_user(db, user1)

    user2 = UserCreate(nickname="ユーザー2", employee_code="EMP999", admin=True)
    
    try:
        cruds.create_user(db, user2)
        assert False, "重複エラーが起きるべきだった"
    except Exception as e:
        assert e.status_code == 400
        assert "すでに登録されています" in str(e.detail)

    db.close()
