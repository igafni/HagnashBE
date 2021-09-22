from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Comment(BaseModel):
    comment_id: str
    item_id: str
    user: str
    text: str


@router.post("/comments/", tags=["comments"])
async def create_comment(comment: Comment):
    item_dict = comment.dict()
    return item_dict


@router.get("/comments/{item_id}", tags=["comments"])
async def get_all_comment():
    pass


@router.delete("/comments/{comment_id}", tags=["comments"])
async def delete_comment():
    pass
