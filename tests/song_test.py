import unittest
from classes.song_class import Song
from classes.room_class import Room

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Africa", "Toto", "Toto IV", "Pop", 8)
        self.song_2 = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", "Rock", 6)

        self.room = Room(1, "Nirvana", 3,  100.00, 5.00)

    
    def test_song_has_title(self):
        self.assertEqual("Africa", self.song.title)
    
    def test_song_has_artist(self):
        self.assertEqual("Toto", self.song.artist)

    def test_song_has_album(self):
        self.assertEqual("Toto IV", self.song.album)
    
    def test_song_has_genre(self):
        self.assertEqual("Pop", self.song.genre)

    def test_song_has_singing_difficulty(self):
        self.assertEqual(8, self.song.difficulty)

    def test_add_song_to_playlist(self):
        self.song.add_to_playlist(self.song, self.room)
        self.assertEqual(1, len(self.room.playlist))
        self.assertEqual(self.song, self.room.playlist[0])
    
    def test_remove_song_from_playlist(self):
        self.song.add_to_playlist(self.song, self.room)
        self.song.remove_from_playlist(self.song, self.room)
        self.assertEqual(0, len(self.room.playlist))
    
    def test_clear_playlist(self):
        self.song.add_to_playlist(self.song, self.room)
        self.song.add_to_playlist(self.song_2, self.room)
        self.song.clear_playlist(self.room)
        self.assertEqual(0, len(self.room.playlist))

