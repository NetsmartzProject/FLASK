from typing import List
from pydantic import BaseModel

class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True

class Course(BaseModel):
    AuthorName: str
    SkillName: str
    ReactJs: bool

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    password: str
    articles: List[Article] = []
    courses: List[Course] = []

    class Config:
        orm_mode = True

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    AuthorName: str
    SkillName: str
    ReactJs: bool
    user_course_id: int

class CourseDisplay(BaseModel):
    AuthorName: str
    SkillName: str
    ReactJs: bool

    class Config:
        orm_mode = True


#  EXAMPLE OF CREATING SCHEMA 

# from pydantic import BaseModel
# from typing import List


# class Article(BaseModel):
#     title: str
#     content: str
#     published: bool

#     class config:
#         orm_mode = True


# class Course(BaseModel):
#     AuthorName: str
#     SkillName: str
#     ReactJs: bool

#     class config:
#         orm_mode = True


# class UserBase(BaseModel):
#     username: str
#     email: str
#     password: str


# class UserDisplay(BaseModel):
#     username: str
#     email: str
#     password: str
#     items: List[Article] = []
#     courses: List[Course] = []

#     class Config:
#         orm_mode = True


# # User Inside ArticleDisplay


# class User(BaseModel):
#     id: int
#     username: str

#     class config:
#         orm_mode = True


# class COURSE(BaseModel):
#     id: int
#     username: str

#     class config:
#         orm_mode = True


# class ArticleBase(BaseModel):
#     title: str
#     content: str
#     published: bool
#     creator_id: int


# class ArticleDisplay(BaseModel):
#     title: str
#     content: str
#     published: bool
#     user: User

#     class config:
#         orm_mode = True


# class CourseBase(BaseModel):
#     AuthorName: str
#     SkillName: str
#     ReactJs: bool
#     user_course_id: int


# class CourseDisplay(BaseModel):
#     AuthorName: str
#     SkillName: str
#     ReactJs: bool
#     user: COURSE

#     class config:
#         orm_mode = True


