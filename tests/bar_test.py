import unittest
from classes.bar_class import Bar

drinks_inventory = {"Henricks" : {"quantity": 3, "type": "Gin", "cost": 3.50},
                "Bombay Sapphire": {"quantity": 9,"type": "Gin", "cost": 3.50},
                "White Wine": {"quantity": 5,"type": "Wine", "cost": 3.50}}
                
class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar(drinks_inventory)
    
    def test_bar_has_drinks_inventory(self):
        self.assertEqual(drinks_inventory, self.bar.drinks_inventory)