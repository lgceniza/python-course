import requests

PARAMS = {
  'amount': 10,
  'type': 'boolean'
}

resp = requests.get(f'https://opentdb.com/api.php', params=PARAMS)
resp.raise_for_status()

question_data = resp.json()['results']
