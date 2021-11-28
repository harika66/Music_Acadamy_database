
from sqlalchemy.orm import Session
from schemas import UserInfo

import models, schemas


def get_user_by_username(db: Session, std_name: str):
    return db.query(models.UserInfo).filter(models.UserInfo.std_name == std_name).first()


def create_user(db: Session, user: schemas.UserInfoBase):
    db_user = models.UserInfo(std_name=user.std_name, course_name=user.course_name,batch=user.batch,tch_name=user.tch_name,fees=user.fees)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Function to get list of students info
def get_students(db: Session):
    return db.query(models.UserInfo).all()