
from fastapi import FastAPI
from router import blog_post
from router import blog_get
from router import user
from router import article
from router import product
from router import course

from db import models
from db.database import engine
from fastapi.responses import JSONResponse
from router.exception import StoryException
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from starlette.responses import PlainTextResponse
from fastapi import FastAPI, HTTPException


app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_post.router)
app.include_router(blog_get.router)
app.include_router(product.router)
app.include_router(course.router)
# Define an endpoint with a tag
@app.get("/hii/{id}", tags=["hii"])
def index(id: int):
    return "Hello World"

@app.get("/hello",tags=["hello"])
def Hello():
    return "Hey, Whats'Up"

@app.exception_handler(StoryException)
def story_exception_handler(request:Request,exc:StoryException):
    return JSONResponse(
        status_code=418,    
        content={'detail':exc.name}
    )
    
    
# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400)


models.Base.metadata.create_all(engine)



## REQUEST BODY 

## POST Method , PYdantic BaseModel 

## class BlogModel(BaseMOdel):
## title:str
## content:str
## published:optional(bool)


## FastAPI will convert the Data 
#@router.post('/new)
#def create_blog(blog:BlogModel):
#return blog


## PARAMETER METADATA 

## information displayed in docs , Using the Query,Path and Body imports ,Set default value 

# comment_id: int = Query(None) 


