import requests

API_KEY = "03f9f463059988291b289cc8a65cccb3"
LAT = 14.423880
LONG = 120.940819
API_URL = "http://api.openweathermap.org/data/2.5/weather"
PARAMS = {
  'lat': LAT,
  'lon': LONG,
  'appid': API_KEY
}

resp = requests.get(API_URL, params=PARAMS)
resp.raise_for_status()

weather = resp.json()
print(f"Your location: {weather['sys']['country']}")
print(f"Max temp: {round(weather['main']['temp_max']-273.15, 2)}C")
print(f"Min temp: {round(weather['main']['temp_min']-273.15, 2)}C")
print(f"Description: {weather['weather'][0]['main']}")
