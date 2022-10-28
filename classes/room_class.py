class Room:
    def __init__(self, id, name, capacity, till_value, entry_fee):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.till_value = till_value
        self.entry_fee = entry_fee
        self.guests = []
        self.songs = []