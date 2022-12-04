from fastapi import FastAPI
import json
import requests
from pymongo import MongoClient

# preencha as informações referentes à URI do MongoDB e a chave da API

MONGO_CLIENT_URI = ""
API_KEY = ""
DB = "weather"
COLL = "cities"
lang = 'pt_br'

app = FastAPI()
client = MongoClient(MONGO_CLIENT_URI)
db = client[DB]
coll = db[COLL]


@app.get("/{city}", response_model=dict)
async def get_weather(city):
    data = {}
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
        data[i["dt_txt"], geolocation[0]["name"]] = [i]
    
    coll.insert_one(
        json.loads(
            json.dumps(
                {
                    "city": geolocation[0]["name"],
                    "timestamp": source["list"][0]["dt_txt"],
                    "data": data
                }
            )
        )
    )

    return data
