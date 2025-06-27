from fastapi import HTTPException
from sqlalchemy.orm import Session
from test.test_models import User
from schemas import UserCreate

# ユーザー新規登録
def test_create_user(db: Session, user: UserCreate):
    # 社員番号の重複チェック
    existing_user = db.query(User).filter(User.employee_code == user.employee_code).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="この社員コードはすでに登録されています")
    
    # ユーザーの新規登録
    new_user = User(
        nickname=user.nickname, 
        employee_code=user.employee_code,
        admin=user.admin
        )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# ユーザー一覧取得
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(User).offset(skip).limit(limit).all()
