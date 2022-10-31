class Bar:
    def __init__(self, drinks_inventory, food_inventory):
        self.drinks_inventory = drinks_inventory
        self.food_inventory = food_inventory

    def stock_check(self, guest):
        if guest.fav_drink in self.drinks_inventory and self.drinks_inventory[guest.fav_drink]["quantity"] > 0:
            return True
        else:
            return False

    def drinks_wallet_check(self, guest):
        if guest.wallet >= self.drinks_inventory[guest.fav_drink]["cost"]:
            return True
        else:
            return False
    
    def intoxication_check(self, guest):
        if guest.intoxication_level <= 10:
            return True
        else:
            return False
    
    def serve_fav_drink(self, guest, room):
        if self.stock_check(guest) and self.drinks_wallet_check(guest) and self.intoxication_check(guest):
            self.drinks_inventory[guest.fav_drink]["quantity"] -= 1
            guest.wallet -= self.drinks_inventory[guest.fav_drink]["cost"]
            guest.intoxication_level += self.drinks_inventory[guest.fav_drink]["strength"]
            room.till_value += self.drinks_inventory[guest.fav_drink]["cost"]
    
    