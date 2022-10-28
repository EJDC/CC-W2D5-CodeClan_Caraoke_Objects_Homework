class Song:
    def __init__(self, title, artist, album, genre, difficulty):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.difficulty = difficulty

    def add_to_playlist(self, song, room):
        room.playlist.append(song)
    
    def remove_from_playlist(self, song, room):
        room.playlist.remove(song)

    def clear_playlist(self, room):
        # print (room.playlist[0].title)
        room.playlist.clear()


    # print (f"Guest {self.guests[0].name} checked into {self.name}")
