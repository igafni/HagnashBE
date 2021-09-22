from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    id: str
    name: str


@router.post("/items/{item_id}", tags=["items"])
async def get_item(item_id: int):
    return {"item_id": item_id}


@router.get("/items/", tags=["items"])
async def get_all_items():
    return []
