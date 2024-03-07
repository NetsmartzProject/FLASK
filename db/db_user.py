

from sqlalchemy.orm.session import Session
from schemas import UserBase, ArticleBase, CourseBase,  Article, Course, UserDisplay
from db.models import DBUser,DbArticle,DbCourse
from db.hash import Hash
from fastapi import HTTPException,status
from sqlalchemy.orm import joinedload


def create_user(db: Session, request: UserBase):
    new_user = DBUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    
    db.add(new_user)
    db.commit()
    return new_user

def get_all_users(db: Session):
    return db.query(DBUser).all()


def get_user(db: Session,id: int):
    user= db.query(DBUser).filter(DBUser.id == id).first()
    if not user:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} Not Found ')
    return user

# This approach is also working

# def get_user_articles_and_courses(db: Session, user_id: int):
#     user = db.query(DBUser).filter(DBUser.id == user_id).first()
#     if not user:
#         return None
    
#     articles = db.query(DbArticle).filter(DbArticle.user_id == user_id).all()
#     courses = db.query(DbCourse).filter(DbCourse.user_id == user_id).all()

#     articles_list = []
#     for article in articles:
#         article_dict = article.__dict__
#         article_dict.pop('_sa_instance_state')  # Remove SQLAlchemy state
#         articles_list.append(article_dict)

#     courses_list = []
#     for course in courses:
#         course_dict = course.__dict__
#         course_dict.pop('_sa_instance_state')  # Remove SQLAlchemy state
#         courses_list.append(course_dict)

#     return UserDisplay(
#         username=user.username,
#         email=user.email,
#         password=user.password,
#         articles=articles_list,
#         courses=courses_list
#     )

# This approach is also working

def get_user_articles_and_courses(db: Session, user_id: int) -> UserDisplay:
    user = db.query(DBUser).filter(DBUser.id == user_id).first()
    
    if not user:
        return None
    
    # Fetch articles and courses directly from user relationship properties
    articles = [DbArticle.__dict__ for DbArticle in user.items]
    courses = [DbCourse.__dict__ for DbCourse in user.coursed]

    # Remove internal state information from dictionaries
    for article in articles:
        article.pop('_sa_instance_state', None)
    
    for course in courses:
        course.pop('_sa_instance_state', None)

    return UserDisplay(
        username=user.username,
        email=user.email,
        password=user.password,
        articles=articles,
        courses=courses
    )


def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DBUser).filter(DBUser.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} Not Found ')

    # Update only the fields that are provided in the request
    if request.username:
        user.username = request.username
    if request.email:
        user.email = request.email
    if request.password:
        user.password = Hash.bcrypt(request.password)

    db.commit()
    return "ok"



def delete_user(db: Session,id: int):
    user=db.query(DBUser).filter(DBUser.id==id).first()
    if not user:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} Not Found ')

    db.delete(user)
    db.commit()
    return "ok"

