from fastapi import APIRouter
from pydantic import BaseModel
from App.common.ElasticSearchAdapter.ElasticAdapter import ElasticAdapter, CONNECTION_STRING, API_KEY

PLACES_INDEX = "places"

router = APIRouter()


class Place(BaseModel):
    id: str
    name: str


@router.get("/places/{item_id}", tags=["places"])
async def get_place(item_id: int):
    return {"item_id": item_id}

@router.get("/places/{text}", tags=["places"])
async def get_places_by_text(text: str):
    es = ElasticAdapter(connection_string=CONNECTION_STRING, api_key=API_KEY, index=PLACES_INDEX)
    es.connect()
    res = es.search_document({"query": {
        "query_string": {
            "query": f"*{text}*"
        }
    }})
    es.close()
    return res['hits']['hits']

@router.get("/places/", tags=["places"])
async def get_all_places():
    es = ElasticAdapter(connection_string=CONNECTION_STRING, api_key=API_KEY, index=PLACES_INDEX)
    es.connect()
    res = es.search_document({'query': {
        'match_all': {}
    }})
    es.close()
    return res['hits']['hits']

