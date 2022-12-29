from pymongo.errors import OperationFailure
from fastapi.testclient import TestClient
from weather import app, API_KEY, lang
from datetime import datetime
from fastapi import status
from icecream import ic
import requests
import pymongo
import pytest
import json

client = TestClient(app)

GEOLOCATION_JSON_EXAMPLE_01 = [
        {
            "name": "Porto Alegre",
            "local_names":
                {
                    "mk": "Порто Алегре", "th": "ปรอโตอเลกรี", "ru": "Порту-Алегри", "nl": "Porto Alegre",
                    "sv": "Porto Alegre", "ce": "Порту-Алегри", "ko": "포르투알레그리", "no": "Porto Alegre",
                    "en": "Porto Alegre", "ja": "ポルト・アレグレ", "de": "Porto Alegre", "kn": "ಪೋರ್ಟೊ ಅಲೆಗ್ರೇ",
                    "bg": "Порто Алегри", "oc": "Pôrto Alegre", "lv": "Portualegri", "ur": "پورتو الیگرے",
                    "mr": "पोर्तू अलेग्री", "el": "Πόρτο Αλέγκρε", "pl": "Porto Alegre", "eo": "Porto-Alegro",
                    "lt": "Porto Alegrė", "la": "Portus Alacer", "os": "Порту-Алегри", "tg": "Порту-Алегре",
                    "hy": "Պորտու Ալեգրի", "tr": "Porto Alegre", "kk": "Порту-Алегри", "ka": "პორტუ-ალეგრი",
                    "ar": "بورتو أليغري", "fa": "پورتو الگره", "fr": "Porto Alegre", "it": "Porto Alegre",
                    "uz": "Portu-Alegri", "be": "Порту-Алегры", "es": "Porto Alegre", "zh": "阿雷格里港",
                    "he": "פורטו אלגרה", "sr": "Порто Алегре", "pt": "Porto Alegre", "uk": "Порту-Алегрі",
                    "mn": "Порту-Алегри"
                },
            "lat": -30.0324999,
            "lon": -51.2303767,
            "country": "BR",
            "state": "Rio Grande do Sul"
        },
        {
            "name": "Porto Alegre",
            "lat": 0.0343796,
            "lon": 6.5352131,
            "country": "ST",
        },
        {
            "name": "Porto Alegre",
            "lat": -30.100916650000002,
            "lon": -51.18878818689657,
            "country": "BR",
            "state": "Rio Grande do Sul"
        },
        {
            "name": "Porto Alegre",
            "local_names":
                {
                    "es": "Porto Alegre"
                },
            "lat": 4.7871158000000005,
            "lon": -75.72443862149512,
            "country": "CO",
            "state": "Risaralda"
        },
        {
            "name": "Porto Alegre",
            "lat": -20.3501819,
            "lon": -44.0310914,
            "country": "BR",
            "state": "Minas Gerais"
        }
    ]

GEOLOCATION_API_JSON_EXAMPLE_01 = requests.get(
    f"https://api.openweathermap.org/geo/1.0/direct?q="
    f"porto_alegre&limit=5&appid={API_KEY}&lang={lang}"
)

GEOLOCATION_JSON_EXAMPLE_02 = [
    {
        "name": "Maringá", "local_names":
        {
            "zh": "馬林加",
            "sr": "Маринга",
            "ja": "マリンガ",
            "bg": "Маринга",
            "pt": "Maringá",
            "ko": "마링가",
            "ru": "Маринга",
            "la": "Maringa",
            "lt": "Maringa",
            "mk": "Маринга"
        },
        "lat": -23.425269,
        "lon": -51.9382078,
        "country": "BR",
        "state": "Paraná"
    },
    {
        "name": "Maringa",
        "lat": 10.0526283,
        "lon": 12.0438902,
        "country": "NG",
        "state": "Borno State"
    },
    {
        "name": "Bairro Maringa",
        "local_names":
            {
                "pt": "Bairro Maringa"
            },
        "lat": -9.416404,
        "lon": -40.5148675,
        "country": "BR",
        "state": "Bahia"
    },
    {
        "name": "Maringa",
        "lat": -1.714575,
        "lon": -48.6582867,
        "country": "BR",
        "state": "Pará"
    },
    {
        "name": "Maringa",
        "lat": -5.4744408,
        "lon": -48.119197,
        "country": "BR",
        "state": "Tocantins"
    }
]

GEOLOCATION_API_JSON_EXAMPLE_02 = requests.get(
    f"https://api.openweathermap.org/geo/1.0/direct?q="
    f"maringa&limit=5&appid={API_KEY}&lang={lang}"
)


@pytest.mark.asyncio
async def test_api_request_geolocation_verify_01() -> None:
    assert GEOLOCATION_API_JSON_EXAMPLE_01.status_code == status.HTTP_200_OK
    assert GEOLOCATION_API_JSON_EXAMPLE_01.json() == GEOLOCATION_JSON_EXAMPLE_01


@pytest.mark.asyncio
async def test_api_request_weather_verify_01() -> None:
    response = client.get("/porto_alegre")
    ic(response.json())
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_api_request_geolocation_verify_02() -> None:
    assert GEOLOCATION_API_JSON_EXAMPLE_02.status_code == status.HTTP_200_OK
    assert GEOLOCATION_API_JSON_EXAMPLE_02.json() == GEOLOCATION_JSON_EXAMPLE_02


@pytest.mark.asyncio
async def test_api_request_weather_verify_02() -> None:
    response = client.get("/maringa")
    ic(response.json())
    assert response.status_code == status.HTTP_200_OK


def database_connection_info():
    try:
        client = api.client
        print(client.server_info())

    except errors.ServerSelectionTimeoutError as error:
        print(error)

      
def count_doc():
    return print("O número atual de documentos na coleção '{}' do banco de dados '{}' é de {}.".format(
        api.COLL,
        api.DB,
        api.coll.count_documents({})
        )
    )


database_connection_info()
count_doc()
