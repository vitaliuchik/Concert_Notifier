import ctypes
from collections import Counter


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0                                # count actual elements
        self._capacity = 1                         # default array capacity
        self._A = self._make_array(self._capacity) # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError( 'invalid index' )
        return self._A[k]                          # retrieve from array

    def append(self, obj):
        """Add object to end of the array.

        :param obj: object
        :return: None
        """
        if self._n == self._capacity:              # not enough room
            self._resize(2 * self._capacity)       # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):                          # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c)                    # new (bigger) array
        for k in range(self._n):                   # for each existing value
            B[k] = self._A[k]
        self._A = B                                # use the bigger array
        self._capacity = c

    def _make_array(self, c): # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)( )           # see ctypes documentation


class Playlist:
    """Represents playlist, contains song"""
    def __init__(self):
        """Creates an empty playlist."""
        self._playlist = DynamicArray()

    def append(self, track):
        """Appends song to playlist

        :param track: dict
        :return: None
        """
        title, artists = self._process_dict(track)
        if not self._has_song(title) and title and artists:
            self._playlist.append('{}:{}'.format(title, artists))

    def _has_song(self, title):
        """Checks if song is already in playlist"""
        for i in range(len(self._playlist)):
            song_name = self._playlist[i].split(':')[0]
            if song_name == title:
                return True
        return False

    def _process_dict(self, track):
        """Transforms song dictionary to title and artists string
        In Google Play Music, there are two possible different types
        of track dictionary, so this function handle both of them"""
        if 'trackId' in track.keys():
            title = track['trackId']
            artists = ','.join(track['track']['artistId'])
        elif 'storeId' in track.keys():
            title = track['storeId']
            artists = ','.join(track['artistId'])
        else:
            return (False, False)
        return (title, artists)

    def __str__(self):
        """Represents playlist in string"""
        result = 'Playlist:\n'
        for i in range(len(self._playlist)):
            result += self._playlist[i] + '\n'
        return result

    def top_n(self, n):
        """Returns list with n more popular user's artists

        :param n: int
        :return: artists: list
        """
        artists = DynamicArray()
        for i in range(len(self._playlist)):
            for artist in self._playlist[i].split(':')[1].split(','):
                artists.append(artist)
        counter = list(Counter(artists).items())
        counter.sort(key=lambda x: x[1], reverse=True)
        return [counter[i][0] for i in range(min(n, len(counter)))]
