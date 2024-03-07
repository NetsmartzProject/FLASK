from fastapi import APIRouter, Response, status, Depends
from enum import Enum
from typing import List
from schemas import ArticleBase,ArticleDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_articles

router = APIRouter(
    prefix='/article',
    tags=['article']
)

# Create Articles
@router.post("/",response_model=ArticleDisplay)
def create_article(request:ArticleBase,db: Session=Depends(get_db)):
    return db_articles.create_article(db,request)


@router.get("/{id}",response_model=ArticleDisplay)
def get_article(id: int,db: Session=Depends(get_db)):
    return db_articles.get_article(db,id)
