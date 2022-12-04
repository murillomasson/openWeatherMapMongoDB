from pymongo import MongoClient
from fastapi import FastAPI
from datetime import datetime
import requests
import json

# preencha as informações referentes à URI do MongoDB e a chave da API
API_KEY = ""
lang = 'pt_br'
MONGO_CLIENT_URI = ""
DB = "weather"
COLL = "cities"

client = MongoClient(MONGO_CLIENT_URI)
db = client[DB]
coll = db[COLL]

app = FastAPI()


@app.get("/{city}", response_model=dict)
async def get_city(city):
    data = {}
    now = datetime.now()
    geolocation = json.loads(
        requests.get(
            f"https://api.openweathermap.org/geo/1.0/direct?q="
            f"{city}&limit=5&appid={API_KEY}&lang={lang}"
        ).text
    )
    source = json.loads(
        requests.get(
            "https://api.openweathermap.org/data/2.5/forecast?"
            "lat={}&lon={}&appid={}&lang={}&units=metric".format(
                str(geolocation[0]['lat']),
                str(geolocation[0]['lon']),
                API_KEY,
                lang,
            )
        ).text
    )

    for i in source["list"]:
        data[i["dt_txt"]] = [i]

    coll.insert_one(
        json.loads(
            json.dumps(
                {
                    "city": geolocation[0]["name"],
                    "date_time": now.strftime("%m/%d/%Y, %H:%M:%S"),
                    "data": data
                }
            )
        )
    )
    return {"city": geolocation[0]["name"], "date_time": now.strftime("%m/%d/%Y, %H:%M:%S"), "data": data}
