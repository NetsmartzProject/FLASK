
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db.database import Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship

class DBUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship("DbArticle", back_populates='user')
    coursed = relationship("DbCourse", back_populates='user')

class DbArticle(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("DBUser", back_populates='items')

class DbCourse(Base):
    __tablename__ = "course"
    id = Column(Integer, primary_key=True, index=True)
    AuthorName = Column(String)
    SkillName = Column(String)
    ReactJs = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("DBUser", back_populates='coursed')


