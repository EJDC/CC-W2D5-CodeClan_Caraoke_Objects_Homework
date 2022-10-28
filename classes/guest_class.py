class Guest:
    def __init__(self, name, fav_song, fav_drink, singing_level, wallet):
        self.name = name
        self.fav_song = fav_song
        self.fav_drink = fav_drink
        self.singing_level = singing_level # 1 - 10
        self.intoxication_level = 0 # - some per drink! + some per food!
        self.total_score = 0
        self.wallet = wallet

    def decrease_wallet(self, amount):
        self.wallet -= amount

    def sing_song(self, song, room):
        self.total_score += self.score_song_attempt(song.difficulty)
        song.remove_from_playlist(song,room)


    # Song Score =
    # (Singing Level + Fav Song Bonus(5)) 
    # - (Intoxication Level + Song Difficulty)
    
    def score_song_attempt(self, difficulty):
        return (self.singing_level) - (self.intoxication_level + difficulty)

    def check_for_fav_song(self, room):
        if self.fav_song in room.playlist:
            return "Woop Woop!!!"
        else:
            return f"Get {self.fav_song.title} on that playlist!"