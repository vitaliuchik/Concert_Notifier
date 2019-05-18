from scripts import playlist_adt
import unittest


class TestPlaylistADT(unittest.TestCase):

    def setUp(self):
        self.playlist = playlist_adt.Playlist()
        self.songs = [{'track':{'artistId': ['artist1', 'artist2']},
                    'trackId': 'track1'},
                    {'artistId': ['artist1'], 'storeId': 'track2'},
                    {'track':{'artistId': ['artist1', 'artist2']}, 
                    'trackId': 'track1'}]

    def test_append(self):
        """"Testing method append()"""
        self.playlist.append(self.songs[0])
        self.assertEqual(str(self.playlist),
            'Playlist:\ntrack1:artist1,artist2\n')
        self.playlist.append(self.songs[1])
        self.assertEqual(str(self.playlist),
            'Playlist:\ntrack1:artist1,artist2\ntrack2:artist1\n')
        self.playlist.append(self.songs[2])
        self.assertEqual(str(self.playlist),
            'Playlist:\ntrack1:artist1,artist2\ntrack2:artist1\n')

    def test_top_n(self):
        """Testing method top_n()"""
        self.playlist.append(self.songs[0])
        self.playlist.append(self.songs[1])
        self.playlist.append(self.songs[2])
        self.assertEqual(self.playlist.top_n(1), ['artist1'])
        self.assertEqual(self.playlist.top_n(2), ['artist1', 'artist2'])

    def test_has_song(self):
        """Testing method has_song()"""
        self.playlist.append(self.songs[0])
        self.playlist.append(self.songs[1])
        self.playlist.append(self.songs[2])
        self.assertTrue(self.playlist._has_song('track2'))
        self.assertFalse(self.playlist._has_song('track3'))

    def test_process_dict(self):
        """Testing method process_dict()"""
        self.assertEqual(self.playlist._process_dict(self.songs[0]),
            ('track1', 'artist1,artist2'))


if __name__ == '__main__':
    unittest.main()