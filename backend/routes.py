from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# import cruds, schemas, models
from database import get_db

import test.test_cruds as cruds, test.test_schemas as schemas, test.test_models as models


router = APIRouter()

# ユーザー一覧取得（GET）
# @router.get("/users", response_model=list[schemas.UserRead])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return cruds.get_users(db, skip=skip, limit=limit)

# ユーザー登録（POST）
@router.post("/users") #, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # email重複チェック（任意で）
    existing = db.query(models.User).filter(models.User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    return cruds.create_user(db, user)
