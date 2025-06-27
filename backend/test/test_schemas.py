from pydantic import BaseModel, EmailStr

# ユーザー登録用（POSTリクエスト）
class UserCreate(BaseModel):
    nickname: str
    employee_code: str
    admin: bool

# ユーザー表示用（レスポンス）
# class UserRead(BaseModel):
#     id: int
#     name: str
#     email: EmailStr

#     class Config:
#         from_attributes = True
