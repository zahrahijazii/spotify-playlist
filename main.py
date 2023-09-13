import bs4
import requests 
import spotipy 
from spotipy.oauth2 import SpotifyOAuth
import pprint


CLIENT_ID = "294aa54d502041afaa2b3190667a960c"
CLIENT_SECRET = "86c2c74dc9f64f71b45f9453cbaea351"
SPOTIFY_ENDPOINT ="https://api.spotify.com"
REDIRECT_URI = "http://example.com"

#Authentication:

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    cache_path="C:/Users/HP/Desktop/spotify-playlist/spotify-playlist/.cache",
    show_dialog=True,
    username="zahra hijazi"))


user_id = sp.current_user()["id"]



user_input = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + user_input)

billboard_webpage = response.text

soup = bs4.BeautifulSoup(billboard_webpage, "html.parser")

song_list = soup.select("li ul li h3")

song_names = [song_name.getText().strip() for song_name in song_list]

song_uris = []

for song_name in song_names:
    try:
        uri = sp.search(q=song_name)["tracks"]["items"][1]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song_name} is not found in Spotify. Skipped.")

#create playlist:
playlist = sp.user_playlist_create(
    user=user_id, 
    name=f"{user_input} Billboard 100",
    public=False
    )

playlist_id = playlist["id"]

sp.playlist_add_items(
    playlist_id=playlist_id,
    items=song_uris
    )

print("done")

# sp.user_playlist_add_tracks(
#     user=user_id,
#     playlist_id=





