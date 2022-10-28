class Room:
    def __init__(self, id, name, capacity, till_value, entry_fee):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.till_value = till_value
        self.entry_fee = entry_fee
        self.guests = []
        self.playlist = []

    def add_to_room(self, guest):
        self.guests.append(guest)
        # print (f"Guest {self.guests[0].name} checked into {self.name}")

    def capacity_check(self, capacity):
        if len(self.guests) < capacity:
            return True
        else:
            return False
    
    def wallet_check(self, guest):
        if self.entry_fee <= guest.wallet:
            return True
        else:
            return False

    def increase_till(self, amount):
        self.till_value += amount

    def check_in(self, guest):
        if self.capacity_check(self.capacity) == True and self.wallet_check(guest) == True:
            self.add_to_room(guest)
            guest.decrease_wallet(self.entry_fee)
            self.increase_till(self.entry_fee)
        else:
            return "Cannot Checkin!"
    
    def check_out(self, guest):
        self.guests.remove(guest)

    def clear_room(self):
        self.guests.clear()