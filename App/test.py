from common.ElasticSearchAdapter.ElasticAdapter import ElasticAdapter, CONNECTION_STRING, API_KEY
import uuid

es = ElasticAdapter(connection_string=CONNECTION_STRING, api_key=API_KEY, index="places")
es.connect()
res = {
    "id": uuid.uuid4(),
    "name": "אביגיל",
    "description": "אביגיל הוא מאחז בתחום מועצה אזורית הר חברון. ממוקם על גבעה בין סוסיא למעון, נקרא על שמה של אביגיל, אשת נבל הכרמלי שעל פי המקרא התגוררה במעון המקראית שמזוהה באתר סמוך.",
    "images": [
            {
                "path": "static/images/0342b617-6c84-4fe6-9b9d-02c20bbedf33.jpg",
                "description": "בעל חצור"
            }
        ],
    "area": "בנימין",
    "location": {
        "lon": "31.9794618",
        "lat": "35.2706896"
    },
    "facilities": [
        "gym"
    ],
    "guard_post": [
        {
            "type": "sit",
            "name": "שג",
            "description": "לא מפריעים לך בכלל"
        }
    ]
}

es.index_document(res)

# print(res['hits']['hits'][0]['_source'])
es.close()
