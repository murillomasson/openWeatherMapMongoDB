# Open Weather Map API MongoDB, FastAPI
Aplicação realizada em FastAPI que busca latitude e longidade de uma cidade fornecida e, a partir dessas informações, retorna informações metereológicas e salva numa dada coleção no MongoDB.

Para rodar a aplicação, por favor, siga esses passos:

- Cadastre-se em Open Weather Map e retire uma chave de API na sessão de "consultas para 5 dias": https://openweathermap.org/
- Clone o repositório: 
```cmd
git clone https://github.com/murillomasson/openWeatherMapMongoDB.git
```
- Instale os requerimentos:
```cmd
pip install -r requirements.txt
```
- Registre-se em MongoDB Atlas: https://www.mongodb.com/cloud/atlas/register. Você pode seguir o tutorial de como criar um cluster e criar a conexão str: https://www.mongodb.com/docs/atlas/getting-started/
- Abra o arquivo _api.py_ e altere as duas primeiras variáveis:
1. `MONGO_CLIENT_URI` com a string obtida em MongoDB Atlas
2. `API_KEY` com a chave obtida em Open Weather Map
- Rode a aplicação no servidor local:
```cmd
uvicorn api:app --reload
```
- Pronto! Faça suas consultas alterando o campo _cidade_ no link abaixo, de acordo com sua cidade escolhida:
```cmd
http://127.0.0.1:8000/weather/{cidade}
```
- Você pode consultar a conexão ao banco de dados, acessando seu perfil no MongoDB > Database > Browse Collections ou então acessar MongoDB Compass a partir da URI gerada no seu perfil
