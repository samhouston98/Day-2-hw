class Karaoke:
    def __init__(self, guests, songs, rooms):
        self.guests = guests
        self.songs = songs
        self.rooms = rooms

    def check_in_guests_to_rooms(self, guests, rooms):
        self.rooms += self.guests
