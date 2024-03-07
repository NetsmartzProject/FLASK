from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter(
    prefix='/product',
    tags=['product']
)


products =["Apple","Orange","Phone"]

@router.get("/all")
def get_all_product():
    data= " ".join(products)
    return Response(content=data,media_type="text/plain")
    