from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class Place(BaseModel):
    id: str
    name: str


@router.post("/places/{item_id}", tags=["places"])
async def get_place(item_id: int):
    return {"item_id": item_id}


@router.get("/places/", tags=["places"])
async def get_all_places():
    return []
