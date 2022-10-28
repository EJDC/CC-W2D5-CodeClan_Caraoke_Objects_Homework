import unittest
from classes.room_class import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, "Nirvana", 7,  100.00, 5.00)
    
    def test_room_has_room_number(self):
        self.assertEqual(1, self.room.id)
    
    def test_room_has_room_name(self):
        self.assertEqual("Nirvana", self.room.name)
    
    def test_room_has_capacit(self):
        self.assertEqual(7, self.room.capacity)

    def test_room_till_has_value(self):
        self.assertEqual(100.00, self.room.till_value)
    
    def test_room_has_entry_fee(self):
        self.assertEqual(5, self.room.entry_fee)