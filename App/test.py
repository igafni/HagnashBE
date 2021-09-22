from common.ElasticSearchAdapter.ElasticAdapter import ElasticAdapter, CONNECTION_STRING, API_KEY
import uuid

es = ElasticAdapter(connection_string=CONNECTION_STRING, api_key=API_KEY, index="places")
es.connect()
res = {
    "id": uuid.uuid4(),
    "name": "עתניאל",
    "description": "יש גדר אז אין יותר מדי על מה לשמור",
    "images": [
      {
        "path": "static/images/4afe1868-82f3-43b3-b4b0-71a083e3b359.jpg",
        "description": "ברוכים הבאים"
      },
        {
        "path": "static/images/d8a1fe3f-861c-4cff-ac7c-246f9610f720.jpg",
        "description": "עושים כיף"
        }
    ],
    "area": "יהודה",
    "location": {
      "lon": "31.4388597",
      "lat": "35.0223552"
    },
    "facilities": [
      "music_room"
    ],
    "guard_post": [
      {
        "type": "sit",
        "name": "שג",
        "description": "לפעמים הרבשצ בודק"
      }
    ]
  }

es.index_document(res)


#print(res['hits']['hits'][0]['_source'])
print(uuid.uuid4())

es.close()
