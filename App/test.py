from common.ElasticSearchAdapter.ElasticAdapter import ElasticAdapter, CONNECTION_STRING, API_KEY
import uuid

es = ElasticAdapter(connection_string=CONNECTION_STRING, api_key=API_KEY, index="places")
es.connect()
res = {
    "id": "a8095769-7628-4e4a-a623-ba0c36c767e5",
    "name": "כפר עציון",
    "description": " כפר עציון שבגוש עציון מושך אליו נופשים מכל הסוגים. זוגות, משפחות וקבוצות דתיים ושאינם דתיים באים מידי שנה ונהנים, וחיילים שאינם תמיד נהנים.",
    "images": [
        {
            "path": "static/images/906c4c97-d129-498b-a49a-815e78a8f7e1.jpg",
            "description": "היישוב"
        },
        {
            "path": "static/images/96708126-0039-4b35-a984-a72bb4abb707.jpg",
            "description": "מאהל"
        }
    ],
    "area": "גוש עציון",
    "location": {
        "lon": "31.6492899",
        "lat": "35.1106856"
    },
    "facilities": [
        "music_room"
    ],
    "guard_post": [
        {
            "type": "sit",
            "name": "שג",
            "description": "יש מזגן טוב"
        },
        {
            "type": "walk",
            "name": "פטרול",
            "description": "אין גדר אז צריך להיות חדים בלילה"
        }
    ]
}

es.index_document(res)

# print(res['hits']['hits'][0]['_source'])
es.close()
