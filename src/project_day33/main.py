import requests
from datetime import datetime

MY_LAT = 14.423880
MY_LONG = 120.940819

def is_ISS_overhead():
  response = requests.get('http://api.open-notify.org/iss-now.json')
  response.raise_for_status()
  iss_position = {'latitude': float(response.json()['iss_position']['latitude']),
                  'longitude': float(response.json()['iss_position']['longitude'])}
  
  my_position = {'latitude': MY_LAT, 'longitude': MY_LONG}

  return all(list(map(lambda _: abs(iss_position[_]-my_position[_]) <= 5, my_position)))

def is_night():
  params = {'lat': MY_LAT, 'lng': MY_LONG, 'formatted': 0}

  response = requests.get('https://api.sunrise-sunset.org/json', params=params)
  response.raise_for_status()
  day_times = response.json()['results']
  sunrise = int(day_times['sunrise'].split('T')[1].split(':')[0])
  sunset = int(day_times['sunset'].split('T')[1].split(':')[0])

  time_now = datetime.now().hour

  return time_now >= sunset or time_now <= sunrise

if is_ISS_overhead() and is_night():
  print("LOOK UP!")
