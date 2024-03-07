from fastapi import APIRouter,Query,Body,Path
from pydantic import BaseModel
from typing import Optional,List,Dict



router =APIRouter(
    prefix='/blog',
    tags=['blog']
)

class Image(BaseModel):
    url:str
    alias:str

class BlogModel(BaseModel):
    title:str
    content:str
    nb_comments:int
    published: Optional[bool]
    tags:List[str] = []
    metadata:Dict[str,str]={'key': 'val1'}
    image:Optional[Image]=None

@router.post('/new/{id}')
def create_blog(blog:BlogModel,id: int, version: int=1):
    return {
        'id':id,
        'data':blog,
        'version':version
        }

## Request Body --> Read request body as JSON , Data Validation, Data Conversion 


##  REQUEST BODY WITH PARAMETERS we have path and Query Parameters

## @router.post('/new/{id}') 
# def create_blog(blog:BlogModel,id:int,version:int=1):


# @router.post('/new/{id}/comment')
# def create_comment(blog: BlogModel,id: int,
#         comment_id: int=Query(None,
#              title:"Id of the comment",
#              description:"Some description for comment_id ",                     
#         )
#         ):
#     return{
#         'body':blog,
#         'id':id,
#         "comment_id":comment_id
#     }

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(
    blog: BlogModel,
    id: int,
    comment_title: int = Query(
        None,
        title="Title of the comment",
        description="Some description for comment_title",
        alias="Comment_title",
        deprecated=True
    ),
    content:str = Body(...,
             min_length=14,
             regex="^[a-z\s]+$"),
            v:Optional[List[str]] =Query(['1.0','1.1','1.2','1.3']),
            comment_id: int = Path(..., gt=5, le=10)
                                         
):
    return {
        'body': blog,
        'id': id,
        "comment_title": comment_title,
        "content":content,
        "version":v,
        "comment_id":comment_id
    }
    
def required_functionality():
    return {'message':'Learning fastAPI is important '}


# Parameter metaData 
# Add title and Description Just like Adding title and description in Query 
# Add alias 
# Add deprecation 
# comment_id:int = Query(None, deprecated=True)
# Validators : validate data passes to parameters 

## Multiple Values -->
# for query parameters 