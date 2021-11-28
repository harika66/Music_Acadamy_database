from sqlalchemy import Column, Integer, String
from database import Base

class UserInfo(Base):
    __tablename__ = "student_info"

    std_id = Column(Integer, primary_key = True, index = True)
    std_name = Column(String)
    course_name = Column(String)
    batch = Column(String)  
    tch_name = Column(String)
    fees = Column(Integer)