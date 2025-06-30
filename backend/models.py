from sqlalchemy import Column, Integer, String ,Boolean
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, nullable=False)
    employee_code = Column(String, unique=True, index=True, nullable=False)
    admin = Column(Boolean, default=False)  # 0:一般ユーザー, 1:管理者

    # email = Column(String, unique=True, index=True, nullable=False)
