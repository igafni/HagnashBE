from fastapi import APIRouter
from pydantic import BaseModel
import uuid
from typing import Optional, Dict

from App.common.ElasticSearchAdapter.ElasticAdapter import ElasticAdapter, CONNECTION_STRING, API_KEY

INDEX_NAME = "comments"
router = APIRouter()
es = ElasticAdapter(connection_string=CONNECTION_STRING, api_key=API_KEY, index=INDEX_NAME)


class Comment(BaseModel):
    place_id: str
    user: str
    content: str
    rate: Optional[int]


def comment_to_snippet(comment):
    return comment["_source"]


@router.post("/comments/", tags=["comments"])
async def create_comment(comment: Comment):
    item_dict = comment.dict()
    item_dict["id"] = uuid.uuid4()
    es.connect()
    es.index_document(item_dict)
    es.close()


@router.get("/comments/{place_id}", tags=["comments"])
async def get_all_comment(place_id: str):
    es.connect()
    res = es.search_document({"query": {
        "match": {
            "place_id": place_id
        }
    }})
    es.close()
    comments = map(comment_to_snippet, res["hits"]["hits"])
    return list(comments)


@router.get("/rateAverage/{place_id}", tags=["comments"])
async def get_rate_average(place_id: str):
    es.connect()
    res = es.search_document({"query": {
        "match": {
            "place_id": place_id
        }},
        "aggs": {
            "avg_grade": {"avg": {"field": "rate"}}
        }
    })
    es.close()
    grade = res["aggregations"]["avg_grade"]["value"]
    if grade is not None:
        grade = round(grade, 1)
    return {"avg_grade": grade}


@router.delete("/comments/{comment_id}", tags=["comments"])
async def delete_comment(comment_id: str):
    es.connect()
    es.delete_document({"query": {
        "match": {
            "id": comment_id
        }
    }})
    es.close()
