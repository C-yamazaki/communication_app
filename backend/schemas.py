from pydantic import BaseModel, ConfigDict

# ユーザー登録用（POSTリクエスト）
class UserCreate(BaseModel):
    nickname: str
    employee_code: str
    admin: bool

# ユーザー表示用（レスポンス）
class UserRead(BaseModel):
    id: int
    nickname: str
    employee_code: str
    admin: bool

    model_config = ConfigDict(from_attributes=True)
