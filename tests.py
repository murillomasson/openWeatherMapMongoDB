from datetime import datetime
from pymongo import errors
import requests
import json
import api


def database_connection_info():
    try:
        client = api.client
        print(client.server_info())

    except errors.ServerSelectionTimeoutError as error:
        print(error)


def check_api(city):
    now = datetime.now()
    geolocation = json.loads(
        requests.get(
            f"https://api.openweathermap.org/geo/1.0/direct?q="
            f"{city}&limit=5&appid={api.API_KEY}&lang={api.lang}"
        ).text
    )
    return print("API retornou como teste uma consulta para '{}' em {} e obteve sucesso.".format(
        str(geolocation[0]["name"]),
        now.strftime("%m/%d/%Y, às %H:%M:%S")
        )
    )


def count_doc():
    return print("O número atual de documentos na coleção '{}' do banco de dados '{}' é de {}.".format(
        api.COLL,
        api.DB,
        api.coll.count_documents({})
        )
    )


database_connection_info()
check_api(city="Maringá")
check_api(city="LONDON")
check_api(city="porto_alegre")
count_doc()
