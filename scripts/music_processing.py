from gmusicapi import Mobileclient
from playlist_adt import Playlist
from parsing import Parser


class Analyser:
    """Analyser for Google Play Music"""

    def analyse(self, device_id, artists_number):
        """The main method that analysis Google Play Music account,
        and returns results of parsing concert.ua

        :param device_id: str
        :param artists_number: int
        :return: results: list
        """

        api = Mobileclient()
        try:
            artists_number = int(artists_number)
            device_id = str(device_id)
        except ValueError:
            return - 1
        api.oauth_login(str(device_id))

        main_playlist = Playlist()

        library = api.get_all_songs()
        for song in library:
            main_playlist.append(song)

        playlists = api.get_all_user_playlist_contents()
        for playlist in playlists:
            for song in playlist['tracks']:
                main_playlist.append(song)

        top = main_playlist.top_n(artists_number)
        artists = []
        for artist_id in top:
            artist = api.get_artist_info(include_albums=False, artist_id=artist_id, max_rel_artist=0, max_top_tracks=0)
            artists.append(artist['name'])

        results = []
        for artist in artists:
                parse_result = Parser().parse(artist)
                if parse_result:
                    results.append(parse_result)

        return results
