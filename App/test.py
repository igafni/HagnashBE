from common.ElasticSearchAdapter.ElasticAdapter import ElasticAdapter, CONNECTION_STRING, API_KEY
import uuid

res = {
    "id": uuid.uuid4(),
    "name": "בית פלדמן",
    "description": "בית נופש על הים. בעל אוכלוסייה צעירה ותוססת,"
                   " חדר אוכל ברמת מסעדת מישלן בהובלת השף, מיכאל (<גפני לא לשכוח לשים שם משפחה>)."
                   " עובדה מעניינת - במיקום זה מתקיים קורס ממס בוגרים בהובלת סגל מפקדים מהמם",
    "images": ["ae990b18-df76-42c3-9400-71d7edc0b7f3"],
    "area": "השרון",
    "location": {"lon": "32.2999385", "lat": "34.8204612"},
    "facilities": ["music_room", "pool"],
    "guard_post": [{"type": "sit", "name": "שג",
                    "description": "אין הרבה תנועה במהלך השבוע, בעיקר תנועה של קורסיסטים, מידי פעם מגיעים ממסניקים "
                                   "חתיכים בלי אישור כניסה רכבי - מומלץ להכניס בכל זאת"},
                   {"type": "walk", "name": "פטרול",
                    "description": "בסיס קטן ככה שהפטרול קליל, מידי פעם ממסניקים רצים מסביב למגרש מומלץ להצטרף לריצה"}
                   ]
}
es = ElasticAdapter(connection_string=CONNECTION_STRING, api_key=API_KEY, index="places")
es.connect()
es.index_document(res)
es.close()
