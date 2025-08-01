import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth


class Spotify:
    def __init__(self):
        self.user_id = None
        self.sp = None
        pass

    def authenticate_spotify(self):
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri="http://127.0.0.1:8000/callback",
                client_id="6f0d20b938954fd7a229cc9b8431f12a",
                client_secret="74e4d171d885450983338dac9d4ce1aa",
                show_dialog=True,
                cache_path="token.txt"
            )
        )

        self.user_id = sp.current_user()["id"]
        self.sp = sp

    def spotify_create_play_list(self, title_text_list, singer):
        song_list = []
        for title in zip(title_text_list, singer):
            result = self.sp.search(q=f"'{title}'", type='track')
            try:
                song_track = result['tracks']['items'][0]['uri']
                song_list.append(song_track)
            except IndexError:
                print(f"Title track for {title} not found in Spotify")

        # Create play list
        play_list = self.sp.user_playlist_create(self.user_id, "Country Slay", public=False, collaborative=False,
                                                 description="")
        self.sp.playlist_add_items(play_list['id'], song_list, None)
