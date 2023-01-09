# Open Weather Map API 
## MongoDB, FastAPI
FastAPI app that searches for latitude and longitude of a given city and, from this information, returns meteorological information and saves it in a given collection in MongoDB.
_It is advisable that you create a virtual environment to run the application below (the application has been tested on Windows)._

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
- Click on:
1. _Build a database_
2. _Create_ (in _shared_, for basic configuration options)
3. _Create Cluster_
- Choose an _username_ and a _password_
- Click on: 
4. _Add My Current IP Address_
5. _Finish and close_
6. _Connect_
7. _Connect using MongoDB Compass_
- Then copy the connection string

- Open _api.py_ and modify:
1. `MONGO_CLIENT_URI` with your MongoDB Atlas string, changing the password in URI to your choosen one
2. `API_KEY` with your API Key from Open Weather Map

- Run the application on localhost:
```cmd
uvicorn api:app --reload
```

- It's ready! Make your queries changing the field _city_:
```cmd
https://127.0.0.1:8000/{city}
```
_(your queries must not have accents and spacing is done with an underscore)_

- You can check your database connection:
1. Accessing your Mongo's profile > _Database > Browser Collections_
_Or:_
2. Accessing _MongoDB Compass_ with your generated URI (`MONGO_CLIENT_URI`)

- To run the tests:
```cmd
cd openWeatherMapMongoDB
```
```cmd
pdm init
```
```cmd
pdm run pytest -ssvv tests.py
```
