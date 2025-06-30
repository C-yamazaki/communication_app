# test/test_cruds.py　DB層のテスト

import os
os.environ["TESTING"] = "true"

from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from cruds import create_user, get_users
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

# ユーザー登録のテスト
def test_create_user_success():
    db: Session = SessionLocal()

    user_in = UserCreate(
        nickname="テストユーザー",
        employee_code="EMP123",
        admin=False
    )

    user = create_user(db, user_in)

    assert user.id is not None
    assert user.nickname == "テストユーザー"
    assert user.employee_code == "EMP123"
    assert user.admin is False
    db.close()

# ユーザー登録の重複エラーのテスト
def test_create_user_duplicate():
    db: Session = SessionLocal()

    user1 = UserCreate(nickname="ユーザー1", employee_code="EMP999", admin=False)
    create_user(db, user1)

    user2 = UserCreate(nickname="ユーザー2", employee_code="EMP999", admin=True)
    
    try:
        create_user(db, user2)
        assert False, "重複エラーが起きるべきだった"
    except Exception as e:
        assert e.status_code == 400
        assert "すでに登録されています" in e.detail

    db.close()


# ユーザー一覧取得のテスト
def test_get_users_returns_all_users():
    db: Session = SessionLocal()
    # Arrange: ユーザーを2人登録
    create_user(db, UserCreate(nickname="ユーザーA", employee_code="EMP001", admin=False))
    create_user(db, UserCreate(nickname="ユーザーB", employee_code="EMP002", admin=True))

    # Act: ユーザー一覧を取得
    users = get_users(db)

    # Assert: 登録した2ユーザーが取得される
    assert len(users) == 2
    assert users[0].nickname == "ユーザーA"
    assert users[1].nickname == "ユーザーB"
