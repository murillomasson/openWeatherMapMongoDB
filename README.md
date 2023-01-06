# Open Weather Map API 
## MongoDB, FastAPI
FastAPI app that searches for latitude and longitude of a given city and, from this information, returns meteorological information and saves it in a given collection in MongoDB.
To run the application, please follow the next steps:

- Sign up for Open Weather Map and collect an API Key in the "3 hour forecast: 5 days" session: https://openweathermap.org/
- Clone the repository: 
```cmd
git clone https://github.com/murillomasson/openWeatherMapMongoDB.git
```

- Install all the requirements:
```cmd
cd openWeatherMapMongoDB
```
```cmd
pip install -r requirements.txt
```

- Sign up in MongoDB Atlas: https://www.mongodb.com/cloud/atlas/register or Log-in: https://account.mongodb.com/account/login.
You can check here how to create a cluster and make a str connection:
https://www.mongodb.com/docs/atlas/getting-started/

- Open _api.py_ and modify:
1. `MONGO_CLIENT_URI` with your MongoDB Atlas string
2. `API_KEY` with your API Key from Open Weather Map

- Run the application on localhost:
```cmd
uvicorn api:app --reload
```

- It's ready! Make your queries changing the field _city_:
```cmd
https://127.0.0.1:8000/{city}
```

- You can check your database connection:
1. Accessing your Mongo's profile > Database > Browser Collections
2. _MongoDB Compass_ using your generated URI (`MONGO_CLIENT_URI`)

- To run the tests:
```cmd
pdm run pytest -ssvv tests.py
```
