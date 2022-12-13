import requests
from datetime import datetime

APP_ID = "8193e15c"
API_KEY = "c6ef5923cb9a86edda24d8067fb8416a"
NUTRITIONIX_QUERY_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_API_KEY = "5f63d88d6a5f59f13e75a95b326711bf"
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_API_KEY}/workoutSheet/workouts"

NUTRITIONIX_HEADERS = {
  "x-app-id": APP_ID,
  "x-app-key": API_KEY,
  "x-remote-user-id": "0"
}


nutritionix_data = { "query": "" }

nutritionix_data['query'] = input('What exercises did you do today? ')
r = requests.post(url=NUTRITIONIX_QUERY_ENDPOINT, headers=NUTRITIONIX_HEADERS, data=nutritionix_data)
print(r)

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")
for exercise in r.json()['exercises']:
  sheety_data = {
    "workout": {
      "date": date,
      "time": time,
      "exercise": exercise['name'].title(),
      "duration": exercise['duration_min'],
      "calories": exercise['nf_calories']
    }
  }

  r = requests.post(url=SHEETY_ENDPOINT, json=sheety_data)
  print(r)
