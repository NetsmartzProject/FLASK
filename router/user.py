from fastapi import APIRouter,Depends
from schemas import UserBase,UserDisplay ,CourseDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from typing import List
from fastapi import HTTPException, status


router = APIRouter(
    prefix="/user",
    tags=['User']
)

#CREATE USER 

@router.post("/",response_model=UserDisplay)
def create_user(request: UserBase,db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


#Read All User 
@router.get("/",response_model=List[UserDisplay])
def get_all_users(db: Session =Depends(get_db)):
    return db_user.get_all_users(db)

#  GET ALL DETAILS OF USER 
@router.get("/user/{user_id}/articles-and-courses", response_model=UserDisplay)
def get_user_articles_and_courses(user_id: int, db: Session = Depends(get_db)):
    user = db_user.get_user_articles_and_courses(db, user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail=f'User with id {user_id} not found')



@router.get("/{user_id}",response_model=UserDisplay)
def get_user(id: int,db: Session=Depends(get_db)):
    return db_user.get_user(db,id)


@router.post('/{id}/update')
def update_user(id: int,request: UserBase,db: Session=Depends(get_db)):
    return db_user.update_user(db,id,request)  

@router.get('/delete/{id}')
def delete_user(id: int,db: Session=Depends(get_db)):
    return db_user.delete_user(db,id)  