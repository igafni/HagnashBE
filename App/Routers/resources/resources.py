from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

router = APIRouter()


class Image(BaseModel):
    pass


@router.post("/resources/images", tags=["resources"])
async def get_all_comment(image: Image):
    image_dict = image.dict()
    pass
