import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

client_id = os.getenv("d36d17f7f40d4aa18ecbbb12278f8be3")
client_secret = os.getenv("432339d8e9cd4a089f9003c0c82becd7")

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)
