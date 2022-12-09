import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

ROOT_URL = "https://www.billboard.com/charts/hot-100/"
scope = "playlist-modify-private"

date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
html = requests.get(f"{ROOT_URL}{date}").text

soup = BeautifulSoup(html, 'html.parser')
songs_html = soup.select('.o-chart-results-list__item h3#title-of-a-story')
songs = [song.text.strip() for song in songs_html]
artists = [song.find_next_sibling('span').text.strip() for song in songs_html]

# needed args are set as env variables
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user_id = sp.me()['id']

playlist_uris = []
for i, song in enumerate(songs):
  try:
    result = sp.search(q=f"{song} {artists[i]}", limit=1)['tracks']['items'][0]['uri']
  except IndexError:
    pass
  else:
    playlist_uris.append(result)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist['id'], items=playlist_uris)
print(f"Visit https://open.spotify.com/playlist/{playlist['id']} for your time travel playlist!")
