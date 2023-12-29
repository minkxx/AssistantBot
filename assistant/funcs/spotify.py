import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class spotiSearch:
    def __init__(self, spotify_client_id:str, spotify_client_secret:str):
        client_credentials_manager = (SpotifyClientCredentials(spotify_client_id, spotify_client_secret))
        self.spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        self.regex = r"^(https:\/\/open.spotify.com\/)(.*)$"

    def validUrl(self, url:str):
        if re.search(self.regex, url):
            return True
        else:
            return False

    def getTrack(self, url:str):
        if ("track" in url.split("/")) and (self.validUrl(url)):
            track = self.spotify.track(url)
            info = track["name"]
            for artist in track["artists"]:
                fetched = f' {artist["name"]}'
                if "Various Artists" not in fetched:
                    info += fetched
            return info
        else:
            return "Not a valid spotify track"
        
    def getAlbum(self, url:str):
        if ("album" in url.split("/")) and (self.validUrl(url)):
            album = self.spotify.album(url)
            albumName = album["name"]
            results = []
            for item in album["tracks"]["items"]:
                info = item["name"]
                for artist in item["artists"]:
                    fetched = f' {artist["name"]}'
                    if "Various Artists" not in fetched:
                        info += fetched
                results.append(info)
            return albumName, results
        else:
            return "Not a valid spotify track", "Not a valid spotify track"
        
    def getPlaylist(self, url:str):
        if ("playlist" in url.split("/")) and (self.validUrl(url)):
            playlist = self.spotify.playlist(url)
            playlistName = playlist["name"]
            results = []
            for item in playlist["tracks"]["items"]:
                music_track = item["track"]
                info = music_track["name"]
                for artist in music_track["artists"]:
                    fetched = f' {artist["name"]}'
                    if "Various Artists" not in fetched:
                        info += fetched
                results.append(info)
            return playlistName, results
        else:
            return "Not a valid spotify track", "Not a valid spotify track"