from common.ElasticSearchAdapter.ElasticAdapter import ElasticAdapter, CONNECTION_STRING, API_KEY
import uuid

es = ElasticAdapter(connection_string=CONNECTION_STRING, api_key=API_KEY, index="places")
es.connect()
res = {
    "id": uuid.uuid4(),
    "name": "בעל חצור",
    "description": "היום ההר הוא שטח צבאי סגור ושוכן עליו בסיס של מערך הבקרה בחיל האוויר הישראלי שנבנה החל מ 1975 ותחילת בנייתו בגדר שהקימו חברי קבוצת העבודה שהקימה באותה שנה את היישוב הסמוך עפרה. במסגרת הדיונים עם הרשות הפלסטינית על הסדר הקבע, ישנה דרישה ישראלית שעל ההר תהיה תחנת התרעה ישראלית לפחות לחמש שנים.",
    "images": [
        {
            "path": "static/images/4f22b870-6e97-4e52-aa39-cf2ba7ce2c59.jpeg",
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
# es.update_document('6acbec39-1682-4033-a42f-6f29222297c2',)
# print(res['hits']['hits'][0]['_source'])
print(uuid.uuid4())

es.close()
