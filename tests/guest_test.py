import unittest
from classes.guest_class import Guest
from classes.song_class import Song
from classes.room_class import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song = Song("Africa", "Toto", "Toto IV", "Pop", 4)
        self.song_2 = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", "Rock", 6)
        self.guest = Guest("Alistair", self.song, "Mohito", 7, 25.50)
        self.room = Room(1, "Nirvana", 3,  100.00, 5.00)

    def test_guest_has_name(self):
        self.assertEqual("Alistair", self.guest.name)
    
    def test_guest_has_favourite_song(self):
        self.assertEqual(self.song, self.guest.fav_song)
    
    def test_guest_has_favourite_drink(self):
        self.assertEqual("Mohito", self.guest.fav_drink)

    def test_guest_has_singing_level(self):
        self.assertEqual(7, self.guest.singing_level)

    def test_guest_has_wallet(self):
        self.assertEqual(25.50, self.guest.wallet)
    
    def test_decrease_wallet(self):
        self.guest.decrease_wallet(5)
        self.assertEqual(20.50, self.guest.wallet)

    def test_sing_song(self):
        self.song.add_to_playlist(self.song, self.room)
        self.guest.sing_song(self.song, self.room)
        self.assertEqual(0, len(self.room.playlist))

    def test_score_song_attempt(self):
        self.song.add_to_playlist(self.song, self.room)
        self.guest.sing_song(self.song, self.room)
        self.assertEqual(3, self.guest.total_score)
    
    def test_favourite_song_is_on_playlist(self):
        self.song.add_to_playlist(self.song, self.room)
        self.assertEqual("Woop Woop!!!",  self.guest.check_for_fav_song(self.room))
        
    def test_favourite_song_is_not_on_playlist(self):
        self.song.add_to_playlist(self.song_2, self.room)
        self.assertEqual("Get Africa on that playlist!",  self.guest.check_for_fav_song(self.room))
        


