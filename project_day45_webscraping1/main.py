import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

website_html = requests.get(URL).text
soup = BeautifulSoup(website_html, 'html.parser')

with open('movies.txt', 'w') as f:
  for movie in reversed(soup.select('h3.title')):
    f.write(movie.text + '\n')
