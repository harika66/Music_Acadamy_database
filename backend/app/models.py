from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Boolean
from database import Base

class UserInfo(Base):
    __tablename__ = "user_info"

    user_id = Column(Integer, primary_key = True, index = True)
    is_student = Column(Boolean)
    is_teacher = Column(Boolean)
    name = Column(String)
    email = Column(String)
    phone = Column(String)  