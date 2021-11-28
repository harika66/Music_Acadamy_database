from typing import List
from pydantic import BaseModel

class UserInfoBase(BaseModel):
    std_name: str
    course_name: str
    batch: str
    tch_name: str
    fees: int 


class UserInfo(UserInfoBase):
    std_id: int

    class Config:
        orm_mode = True

