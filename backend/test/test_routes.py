# APIルートのテスト

import os
os.environ["TESTING"] = "true"  # SQLiteのインメモリDBを使用

from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

from main import create_app
from database import Base, get_db  # engine は使わない

# テスト用のインメモリDBを使用
TEST_DATABASE_URL = "sqlite:///:memory:"
test_engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool )
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

# テーブル作成（重要：test_engine を使う！）
Base.metadata.create_all(bind=test_engine)

# テスト用DBセッションに差し替え
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# FastAPI アプリ作成 → 依存関係を上書き
app = create_app()
app.dependency_overrides[get_db] = override_get_db

#　テストクライアント作成
client = TestClient(app)

# ユーザー登録（POST）
def test_create_user():
    response = client.post(
        "/users",
        json={
            "nickname": "テストユーザー",
            "employee_code": "EMP001",
            "admin": False
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nickname"] == "テストユーザー"
    assert data["employee_code"] == "EMP001"
    assert data["admin"] is False
    assert "id" in data

def test_create_user_duplicate():
    payload = {
        "nickname": "重複ユーザー",
        "employee_code": "EMP001",  # 上と同じ
        "admin": True
    }
    response = client.post("/users", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "この社員コードはすでに登録されています"


# ユーザー一覧取得（GET）
client = TestClient(app)

def test_get_users_route_returns_users_list():
    # Arrange: 前のデータを削除する（テスト用エンドポイントがある場合）
    client.delete("/test/clear-users")  # もしくは直接DBクリアロジックをテスト用に用意
    
    # Arrange: ユーザーをAPI経由で2人登録
    client.post("/users", json={"nickname": "ユーザーC", "employee_code": "EMP003", "admin": False})
    client.post("/users", json={"nickname": "ユーザーD", "employee_code": "EMP004", "admin": True})

    # Act: GETリクエストで一覧取得
    response = client.get("/users")

    # Assert: ステータスコード・中身の確認
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["nickname"] == "ユーザーC"
    assert data[1]["employee_code"] == "EMP004"
