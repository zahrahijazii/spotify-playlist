import bs4
import requests 
import spotipy 
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = "294aa54d502041afaa2b3190667a960c"
CLIENT_SECRET = "86c2c74dc9f64f71b45f9453cbaea351"
SPOTIFY_ENDPOINT ="https://api.spotify.com"
REDIRECT_URI = "http://example.com"

#Authentication:

sp_oauth = SpotifyOAuth(
    scope="playlist-modify-private",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI)

token_info = sp_oauth.get_access_token()

if not token_info:
    auth_url = sp_oauth.get_authorize_url()
    print(f'Please visit this URL to authorize the application: {auth_url}')
    response = input('Enter the URL you were redirected to: ')
    token_info = sp_oauth.get_access_token(response)

sp = spotipy.Spotify(auth_manager=token_info["access_token"])


user_input = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + user_input)

billboard_webpage = response.text

soup = bs4.BeautifulSoup(billboard_webpage, "html.parser")

song_list = soup.select("li ul li h3")

song_names = [song_name.getText().strip() for song_name in song_list]
print(song_names)
