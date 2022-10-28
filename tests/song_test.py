import unittest
from classes.song_class import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Africa", "Toto", "Toto IV", "Pop", 8)
    
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