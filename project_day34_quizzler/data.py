import requests

NUMBER_OF_QUESTIONS = 10

resp = requests.get(f'https://opentdb.com/api.php?amount={NUMBER_OF_QUESTIONS}&type=boolean')
resp.raise_for_status()

question_data = resp.json()['results']
