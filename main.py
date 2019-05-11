from gmusicapi import Mobileclient
from PlaylistADT import Playlist
import parsing

if __name__ == '__main__':
    api = Mobileclient()

    api.oauth_login('3284f2013409fe11')

    main_playlist = Playlist()

    library = api.get_all_songs()
    for song in library:
        main_playlist.append(song)

    playlists = api.get_all_user_playlist_contents()
    for playlist in playlists:
        for song in playlist['tracks']:
            main_playlist.append(song)

    top = main_playlist.top_n(5)
    artists = []
    for artist_id in top:
        artist = api.get_artist_info(include_albums=False, artist_id=artist_id, max_rel_artist=0, max_top_tracks=0)
        artists.append(artist['name'])

    for artist in artists:
            print(parsing.parser(artist))