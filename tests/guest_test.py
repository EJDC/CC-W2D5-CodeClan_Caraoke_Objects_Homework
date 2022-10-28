import unittest
from classes.guest_class import Guest
from classes.song_class import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song = Song("Africa", "Toto", "Toto IV", "Pop", 8)
        self.guest = Guest("Alistair", self.song, "Mohito", 4, 25.50)
    
    def test_guest_has_name(self):
        self.assertEqual("Alistair", self.guest.name)
    
    def test_guest_has_favourite_song(self):
        self.assertEqual(self.song, self.guest.fav_song)
    
    def test_guest_has_favourite_drink(self):
        self.assertEqual("Mohito", self.guest.fav_drink)

    def test_guest_has_singing_level(self):
        self.assertEqual(4, self.guest.singing_level)

    def test_guest_has_wallet(self):
        self.assertEqual(25.50, self.guest.wallet)
    
    def test_decrease_wallet(self):
        self.guest.decrease_wallet(5)
        self.assertEqual(20.50, self.guest.wallet)