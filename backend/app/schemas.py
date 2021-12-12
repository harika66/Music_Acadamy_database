from typing import List
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Boolean

class UserInfoBase(BaseModel):
    is_student:bool
    is_teacher:bool
    name: str
    email: str
    phone: str


class UserInfo(UserInfoBase):
    user_id:int

    class Config:
        orm_mode = True

