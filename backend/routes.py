from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import cruds, schemas, models
from database import get_db
import os




router = APIRouter()

# ユーザー登録（POST）
@router.post("/users") #, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return cruds.create_user(db, user)


# ユーザー一覧取得（GET）
@router.get("/users", response_model=list[schemas.UserRead])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return cruds.get_users(db, skip=skip, limit=limit)

# テスト用：ユーザーデータを全削除（TESTING=trueのときのみ有効）
@router.delete("/test/clear-users")
def clear_users(db: Session = Depends(get_db)):
    if os.getenv("TESTING") == "true":
        db.query(models.User).delete()
        db.commit()
        return {"message": "All users deleted"}
    else:
        return {"message": "TESTINGモードでのみ有効"}
