from db.models import DbCourse
from schemas import CourseBase
from sqlalchemy.orm.session import Session
from fastapi import HTTPException,status
from router.exception import StoryException
from sqlalchemy.orm import joinedload


def create_course(db:Session,request:CourseBase):
    new_course = DbCourse (
        AuthorName=request.AuthorName,
        SkillName=request.SkillName,
        ReactJs=request.ReactJs,
        user_id=request.user_course_id
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course.user)
    return new_course



def get_course(db: Session, id: int):
    course = (
        db.query(DbCourse)
        .options(joinedload(DbCourse.user))  # Include the related user
        .filter(DbCourse.id == id)
        .first()
    )
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Course with id {id} not found')
    return course

