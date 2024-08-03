import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bilboard_scrap import date
from bilboard_scrap import song_names

scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    client_id="c_id",
    client_secret="c_secret",
    redirect_uri="http://example.com",
    cache_path="token.txt"
))

user_id = sp.current_user()["id"]



song_urls=[]
year=date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_urls.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
print(song_urls)

create_playlist = sp.user_playlist_create(user=user_id,name=f"{date} - Bilboard",public=True,description="Top 100")

sp.playlist_add_items(playlist_id=create_playlist["id"],items= song_urls, position=None)