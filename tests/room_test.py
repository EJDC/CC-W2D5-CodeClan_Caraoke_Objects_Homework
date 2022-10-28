import unittest
from classes.room_class import Room
from classes.song_class import Song
from classes.guest_class import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, "Nirvana", 3,  100.00, 5.00)

        self.song = Song("Africa", "Toto", "Toto IV", "Pop", 8)

        self.guest = Guest("Alistair", self.song, "Mohito", 2, 25.50)
        self.guest_2 = Guest("Bob", self.song, "Red Wine", 5, 4.20)
        self.guest_3 = Guest("Charlie", self.song, "Beer", 6, 30.20)
        self.guest_4 = Guest("Emma", self.song, "White Wine", 7, 60.40)

# Initisation Tests

    def test_room_has_room_number(self):
        self.assertEqual(1, self.room.id)
    
    def test_room_has_room_name(self):
        self.assertEqual("Nirvana", self.room.name)
    
    def test_room_has_capacity(self):
        self.assertEqual(3, self.room.capacity)

    def test_room_till_has_value(self):
        self.assertEqual(100.00, self.room.till_value)
    
    def test_room_has_entry_fee(self):
        self.assertEqual(5, self.room.entry_fee)

# Basic Add to Room Test
    def test_add_to_room_guest(self):
        self.room.add_to_room(self.guest)
        self.assertEqual(1, len(self.room.guests))
    
# Room Capacity and Affordability Tests
    def test_room_has_space(self):
        self.assertEqual(True, self.room.capacity_check(self.room.capacity))

    def test_room_has_no_space(self):
        self.room.add_to_room(self.guest)
        self.room.add_to_room(self.guest_2)
        self.room.add_to_room(self.guest_3)
        self.room.add_to_room(self.guest_4)
        self.assertEqual(False, self.room.capacity_check(self.room.capacity))

    def test_guest_can_pay_entry(self):
        self.assertEqual(True, self.room.wallet_check(self.guest))

    def test_guest_cannot_afford_entry(self):
        self.assertEqual(False, self.room.wallet_check(self.guest_2))

# Till Test
    def increase_till(self):
        self.room.increase_till(5)
        self.assertEqual(105, self.room.till_value)

# Checkin Tests
    def test_guest_cannot_be_checked_in_due_to_capacity(self):
        self.room.add_to_room(self.guest)
        self.room.add_to_room(self.guest_2)
        self.room.add_to_room(self.guest_3)
        self.assertEqual("Cannot Checkin!", self.room.check_in(self.guest_4))

    def test_guest_cannot_be_checked_in_due_to_insufficient_funds(self):
        self.assertEqual("Cannot Checkin!", self.room.check_in(self.guest_2))
    
    def test_guest_can_be_checked_in(self):
        self.room.check_in(self.guest)
        self.assertEqual(1, len(self.room.guests))
        self.assertEqual(20.50, self.guest.wallet)
        self.assertEqual(105, self.room.till_value)

# Checkout Tests
    def test_check_out_guest(self):
        self.room.check_in(self.guest)
        self.room.check_out(self.guest)
        self.assertEqual(0, len(self.room.guests))
    
    def test_check_out_all_guests(self):
        self.room.check_in(self.guest)
        self.room.check_in(self.guest_2)
        self.room.clear_room()
        self.assertEqual(0, len(self.room.guests))
