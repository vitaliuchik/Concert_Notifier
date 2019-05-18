from PlaylistADT import Playlist
import unittest


class TestPlaylistADT(unittest.TestCase):

    def setUp(self):
        self.playlist = Playlist()
        self.songs = [{'track':{'artistId': ['artist1', 'artist2']},
                    'trackId': 'track1'},
                    {'artistId': ['artist1'], 'storeId': 'track2'},
                    {'track':{'artistId': ['artist1', 'artist2']}, 
                    'trackId': 'track1'}]

    def test_append(self):
        self.playlist.append(self.songs[0])
        self.assertEqual(str(self.playlist), \
            'Playlist:\ntrack1:artist1,artist2\n')
        self.playlist.append(self.songs[1])
        self.assertEqual(str(self.playlist), \
            'Playlist:\ntrack1:artist1,artist2\ntrack2:artist1\n')
        self.playlist.append(self.songs[2])
        self.assertEqual(str(self.playlist), \
            'Playlist:\ntrack1:artist1,artist2\ntrack2:artist1\n')

    def test_top_n(self):
        self.playlist.append(self.songs[0])
        self.playlist.append(self.songs[1])
        self.playlist.append(self.songs[2])
        self.assertEqual(self.playlist.top_n(1), ['artist1'])
        self.assertEqual(self.playlist.top_n(2), ['artist1', 'artist2'])

    def test_has_song(self):
        self.playlist.append(self.songs[0])
        self.playlist.append(self.songs[1])
        self.playlist.append(self.songs[2])
        self.assertTrue(self.playlist._has_song('track2'))
        self.assertFalse(self.playlist._has_song('track3'))

    def test_process_dict(self):
        self.assertEqual(self.playlist._process_dict(self.songs[0]), \
            ('track1', 'artist1,artist2'))
    


if __name__ == '__main__':
    unittest.main()