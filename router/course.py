from enum import Enum
from typing import List
from schemas import CourseBase,CourseDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import ab_course
from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter(
    prefix='/course',
    tags=['course']
)


@router.post("/", response_model=CourseDisplay)
def create_course(request: CourseBase, db: Session = Depends(get_db)):
    return ab_course.create_course(db, request)


@router.get("/{id}", response_model=CourseDisplay)
def get_course(id: int, db: Session = Depends(get_db)):
    course_data = ab_course.get_course(db, id)
    if not course_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Course with id {id} not found')
    
    user_data = {
        "id": course_data.user.id,
        "username": course_data.user.username,
    }
    return {
        "AuthorName": course_data.AuthorName,
        "SkillName": course_data.SkillName,
        "ReactJs": course_data.ReactJs,
        "user": user_data
    }


