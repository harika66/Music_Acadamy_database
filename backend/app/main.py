from typing import List

import uvicorn
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import models, schemas, crud
from database import engine, SessionLocal
from utils import check_phone,check_email
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency

@app.get('/')
def index():
    return {"Msg":"Hello world"}

def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/user", response_model=schemas.UserInfo)
def create_user(user: schemas.UserInfoBase, db: Session = Depends(get_db)):
    
    db_user = crud.get_user_by_username(db, name=user.name)
    if db_user:
        print("Error: Duplicate user creation")
        raise HTTPException(status_code=400, detail="Username already registered")
    
    phone = check_phone(user.phone)
    print(phone)
    if phone==None:
        print("Error: Invalid phone number format")
        raise HTTPException(status_code=400, detail="Invalid Phone Number")
    else:
        user.phone = phone

    email = check_email(user.email)
    if email==None:
        print("Error: Invalid email id format")
        raise HTTPException(status_code=400, detail="Invalid email id")
    else:
        user.email = email

    return crud.create_user(db=db, user=user)


@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    data = crud.get_students(db=db)
    response = {"data":data}
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)
