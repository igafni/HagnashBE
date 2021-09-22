from fastapi import APIRouter
from pydantic import BaseModel
from App.common.ElasticSearchAdapter.ElasticAdapter import ElasticAdapter, CONNECTION_STRING, API_KEY
from typing import Dict

INDEX_NAME = "places"

router = APIRouter()
es = ElasticAdapter(connection_string=CONNECTION_STRING, api_key=API_KEY, index=INDEX_NAME)


class Place(BaseModel):
    id: str
    name: str


def place_to_snippet(document: Dict):
    src = document["_source"]
    return {"id": src["id"], "name": src["name"], "description": src["description"],
            "images": src["images"], "facilities": src["facilities"]}


@router.get("/places/getPlace/{item_id}", tags=["places"])
async def get_place(item_id: str):
    es.connect()
    result = es.search_document({"query": {
        "match": {
            "id": item_id
        }
    }})['hits']['hits']
    es.close()
    return result


@router.get("/places/{text}", tags=["places"])
async def get_places_by_text(text: str):
    es.connect()
    result = es.search_document({"query": {
        "query_string": {
            "query": f"*{text}*"
        }
    }})['hits']['hits']
    es.close()
    places = map(place_to_snippet, result)
    return list(places)


@router.get("/places/", tags=["places"])
async def get_all_places():
    es.connect()
    result = es.search_document({'query': {
        'match_all': {}
    }})['hits']['hits']
    es.close()
    places = map(place_to_snippet, result)
    return list(places)
