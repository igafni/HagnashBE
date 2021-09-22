from common.ElasticSearchAdapter.ElasticAdapter import ElasticAdapter, CONNECTION_STRING, API_KEY
import uuid

es = ElasticAdapter(connection_string=CONNECTION_STRING, api_key=API_KEY, index="places")
es.connect()
# res = {
#     "id": uuid.uuid4(),
#     "name": "כפר עציון",
#     "description": "יישוב ממש נחמד",
#     "images": [{
#         "path": "static/images/906c4c97-d129-498b-a49a-815e78a8f7e1.jpg",
#         "description": "היישוב"
#     }],
#     "area": "גוש עציון",
#     "location": {"lon": "31.6492899", "lat": "35.1106856"},
#     "facilities": ["music_room"],
#     "guard_post": [{"type": "sit", "name": "שג",
#                     "description": "יש מזגן טוב"},
#                    {"type": "walk", "name": "פטרול",
#                     "description": "אין גדר אז צריך להיות חדים בלילה"}
#                    ]
# }
# es.index_document(res)
# res1 = es.search_document({"query": {
#     "query_string": {
#         "query": "*בית*"
#     }
# }})
res = es.search_document({"query": {
        "match": {
            "id": "56d020b5-e2c2-4c3c-8f97-4d6784b4ece4"
        }
    }})
print(res['hits']['hits'][0]['_source'])
es.close()
