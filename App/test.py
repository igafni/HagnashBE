from common.ElasticSearchAdapter.ElasticAdapter import ElasticAdapter, CONNECTION_STRING, API_KEY
import uuid

es = ElasticAdapter(connection_string=CONNECTION_STRING, api_key=API_KEY, index="places")
es.connect()
res = {
    "id": "56d020b5-e2c2-4c3c-8f97-4d6784b4ece4",
    "name": "בית פלדמן",
    "description": "בית נופש על הים. בעל אוכלוסייה צעירה ותוססת, חדר אוכל ברמת מסעדת מישלן בהובלת השף, מיכאל (גפני לא לשכוח לשים שם משפחה). עובדה מעניינת - במיקום זה מתקיים קורס ממס בוגרים בהובלת סגל מפקדים מהמם",
    "images": [
        {
            "path": "static/images/ae990b18-df76-42c3-9400-71d7edc0b7f3%20.jpg",
            "description": "הבריכה"
        },
        {
            "path": "static/images/97eb36d7-e3a3-41bf-affd-c8962c26e7c8.jpg",
            "description": "חדר האוכל"
        },
        {
            "path": "static/images/0b50f160-824e-4354-bac2-fa0e49e62096.jpg",
            "description": "אולם אברהם"
        },
        {
            "path": "static/images/709d521a - a664 - 4ec1 - 931b - 292a6b8e2909.jpg",
            "description": "נוף וזה"
        }
    ],
    "area": "השרון",
    "location": {
        "lon": "32.3036575",
        "lat": "34.8430392"
    },
    "facilities": [
        "music_room",
        "pool"
    ],
    "guard_post": [
        {
            "type": "sit",
            "name": "שג",
            "description": "אין הרבה תנועה במהלך השבוע, בעיקר תנועה של קורסיסטים, מידי פעם מגיעים ממסניקים חתיכים בלי אישור כניסה רכבי - מומלץ להכניס בכל זאת"
        },
        {
            "type": "walk",
            "name": "פטרול",
            "description": "בסיס קטן ככה שהפטרול קליל, מידי פעם ממסניקים רצים מסביב למגרש מומלץ להצטרף לריצה"
        }
    ]
}

es.index_document(res)

# print(res['hits']['hits'][0]['_source'])
es.close()
