
from sqlalchemy.orm import Session
from schemas import UserInfo

import models, schemas


def get_user_by_username(db: Session, name: str):
    return db.query(models.UserInfo).filter(models.UserInfo.name == name).first()

# Function to store data into database
def create_user(db: Session, user: schemas.UserInfoBase):
    db_user = models.UserInfo(is_student = user.is_student, is_teacher = user.is_teacher,name=user.name, email=user.email,phone=user.phone)
    
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except:
        print("Create User Failed")
        return None
    return db_user

# Function to get list of students info
def get_students(db: Session):
    return db.query(models.UserInfo).all()