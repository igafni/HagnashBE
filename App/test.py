from common.ElasticSearchAdapter.ElasticAdapter import ElasticAdapter, CONNECTION_STRING, API_KEY
import uuid

es = ElasticAdapter(connection_string=CONNECTION_STRING, api_key=API_KEY, index="places")
es.connect()
res = {
    "id": uuid.uuid4(),
    "name": "אביגיל",
    "description": "אביגיל הוא מאחז בתחום מועצה אזורית הר חברון. ממוקם על גבעה בין סוסיא למעון, נקרא על שמה של אביגיל, אשת נבל הכרמלי שעל פי המקרא התגוררה במעון המקראית שמזוהה באתר סמוך. "
                   "נקודה מעניינת - אביגיל בגימטריה זה  'אבטחה כבדה' ו'אבוטבול', צירוף מקרים?",
    "images": [
        {
            "path": "static/images/b990834f-cf72-494d-ada4-1913ff842c65.jpg",
            "description": "כניסה לאביגיל"
        },
        {
            "path": "static/images/8dac092d-fc28-4053-95fb-76f37d62bccd.jpg",
            "description": "מעיין חדש"
        },
        {
            "path": "static/images/b3567d2a-18db-4dc8-bcc8-bc031b1449de.jpg",
            "description": "המאחז"
        }
    ],
    "area": "יהודה",
    "location": {
        "lon": "31.4345152",
        "lat": "35.1836511"
    },
    "facilities": [
        "pool"
    ],
    "guard_post": [
        {
            "type": "walk",
            "name": "פטרול",
            "description": "הרבה עיזות, אתם עלולים למצוא את עצמכם צועקים על מקומיים לא לגנוב ארטישוקים"
        }
    ]
}

es.index_document(res)

# print(res['hits']['hits'][0]['_source'])
es.close()
