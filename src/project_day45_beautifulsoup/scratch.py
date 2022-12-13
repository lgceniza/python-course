import requests
from bs4 import BeautifulSoup

page = requests.get('https://news.ycombinator.com/').text
soup = BeautifulSoup(page, 'html.parser')

stories = soup.select('.titleline>a')
titles = list(map(lambda s: s.getText(), stories))
links = list(map(lambda s: s.get('href'), stories))
scores = list(map(lambda s: int(s.text.split()[0]), soup.select('.subline .score')))

biggest_story_id = scores.index(max(scores))
print("Article:", titles[biggest_story_id])
print("Link:", links[biggest_story_id])
print(f"Score: {scores[biggest_story_id]} points")
