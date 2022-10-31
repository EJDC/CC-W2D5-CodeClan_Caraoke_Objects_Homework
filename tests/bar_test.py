import unittest
from classes.bar_class import Bar
from classes.guest_class import Guest
from classes.song_class import Song
from classes.room_class import Room
from dicts.menu import drinks_inventory
from dicts.menu import food_inventory
                
class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar(drinks_inventory, food_inventory)
        self.song = Song("Africa", "Toto", "Toto IV", "Pop", 4)
        self.guest = Guest("Alistair", self.song, "Neck Oil", 7, 25.50)
        self.guest_2 = Guest("Sarah", self.song, "Beans", 6, 14.50)
        self.guest_3 = Guest("Alice", self.song, "Stella Artois", 4, 12.50)
        self.guest_4 = Guest("Sally", self.song, "Pinot Noir", 4, 1)
        self.guest_5 = Guest("Billy", self.song, "Chardonnay", 4, 10.00)

        self.room = Room(1, "Nirvana", 3,  100.00, 5.00)
    
    def test_bar_has_drinks_inventory(self):
        self.assertEqual(drinks_inventory, self.bar.drinks_inventory)

    def test_bar_has_accessible_drinks_inventory(self):
        self.assertEqual(3, self.bar.drinks_inventory["Henricks"]["quantity"])

    def test_bar_has_food_inventory(self):
        self.assertEqual(food_inventory, self.bar.food_inventory)

    def test_bar_has_accessible_food_inventory(self):
        self.assertEqual(9, self.bar.food_inventory["Fries"]["quantity"])
    
    def test_bar_cannot_serve_fav_drink_due_to_lack_of_funds(self):
        self.bar.serve_fav_drink(self.guest_4, self.room)
        self.assertEqual(8, self.bar.drinks_inventory["Pinot Noir"]["quantity"])
        self.assertEqual(1, self.guest_4.wallet)
        self.assertEqual(0, self.guest_4.intoxication_level)
        self.assertEqual(100, self.room.till_value)

    def test_bar_cannot_serve_fav_drink_not_in_dictionary(self):
        self.bar.serve_fav_drink(self.guest_2, self.room)
        self.assertEqual(14.50, self.guest_2.wallet)
        self.assertEqual(0, self.guest_2.intoxication_level)
        self.assertEqual(100, self.room.till_value)

    def test_bar_cannot_serve_fav_drink_not_in_stock(self):
        self.bar.serve_fav_drink(self.guest_3, self.room)
        self.assertEqual(12.50, self.guest_3.wallet)
        self.assertEqual(0, self.guest_3.intoxication_level)
        self.assertEqual(100, self.room.till_value)

    def test_bar_cannot_serve_fav_drink_due_to_intoxication(self):
        self.guest_5.intoxication_level += 11
        self.bar.serve_fav_drink(self.guest_5, self.room)
        self.assertEqual(5, self.bar.drinks_inventory["Chardonnay"]["quantity"])
        self.assertEqual(10, self.guest_5.wallet)
        self.assertEqual(11, self.guest_5.intoxication_level)
        self.assertEqual(100, self.room.till_value)

    def test_bar_can_serve_fav_drink(self):
        self.bar.serve_fav_drink(self.guest, self.room)
        self.assertEqual(3, self.bar.drinks_inventory["Neck Oil"]["quantity"])
        self.assertEqual(21, self.guest.wallet)
        self.assertEqual(1, self.guest.intoxication_level)
        self.assertEqual(104.50, self.room.till_value)


    