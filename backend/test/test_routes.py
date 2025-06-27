from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import test_cruds, test_schemas, test_models
from database import get_db

router = APIRouter()

# ユーザー一覧取得（GET）ß
# @router.get("/users", response_model=list[test_schemas.UserRead])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return test_cruds.get_users(db, skip=skip, limit=limit)

# ユーザー登録（POST）
@router.post("/users", response_model=test_schemas.UserRead)
def create_user(user: test_schemas.UserCreate, db: Session = Depends(get_db)):
    return test_cruds.create_user(db, user)

    # email重複チェック（任意で）
    # existing = db.query(test_models.User).filter(test_models.User.email == user.email).first()
    # if existing:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    # return test_cruds.create_user(db, user)
