class Guest:
    def __init__(self, name, fav_song, fav_drink, singing_level, wallet):
        self.name = name
        self.fav_song = fav_song
        self.fav_drink = fav_drink
        self.singing_level = singing_level
        self.intoxication_level = 0
        self.score = 0
        self.wallet = wallet

    def decrease_wallet(self, amount):
        self.wallet -= amount
