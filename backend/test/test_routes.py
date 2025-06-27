import os
os.environ["TESTING"] = "true"  # SQLiteのインメモリDBを使用

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from main import create_app
from database import Base, engine, get_db

# テスト用のインメモリDBを使用
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# テーブル作成
Base.metadata.create_all(bind=engine)

# FastAPIの依存関係を上書き
app = create_app()

# テスト用DBセッションを使うよう差し替え
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


# テストクライアント作成（FastAPIアプリを実際に起動せずに叩く）
client = TestClient(create_app())

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
    # 同じ employee_code を再登録して 400 を期待
    payload = {
        "nickname": "重複ユーザー",
        "employee_code": "EMP001",  # 上と同じ
        "admin": True
    }
    response = client.post("/users", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Employee code already exists"






    # email重複チェック（任意で）
    # existing = db.query(test_models.User).filter(test_models.User.email == user.email).first()
    # if existing:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    # return test_cruds.create_user(db, user)



# ユーザー一覧取得（GET）
# # @router.get("/users", response_model=list[test_schemas.UserRead])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return test_cruds.get_users(db, skip=skip, limit=limit)

