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


@app.get("/weather/{city}", response_model=dict)
async def get_weather(city):
    geolocation = json.loads(
        requests.get(
                f"https://api.openweathermap.org/geo/1.0/direct?q={city}"
                f"&limit=5&appid={API_KEY}&lang={lang}"
            ).text
    )

    lat = str(geolocation[0]['lat'])
    lon = str(geolocation[0]['lon'])

    source = json.loads(
        requests.get(
                f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}"
                f"&appid={API_KEY}&lang={lang}&units=metric"
            ).text
    )

    json_data = json.dumps(
        source,
        ensure_ascii=False
    )

    data = json.loads(json_data)
    coll.insert_one(data)
    
    return source

