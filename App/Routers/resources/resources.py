from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Image(BaseModel):
    pass


@router.get("/resources/images/{image_id}", tags=["resources"])
async def get_image():
    return


@router.post("/resources/images", tags=["resources"])
async def get_all_comment(image: Image):
    image_dict = image.dict()
    pass
