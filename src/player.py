# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, nickname, room=None):
        self.nickname = nickname
        self.room = room

    def current_room(self):
        print("Current Room:", self.room.name)
        print(self.room.desc)

    def __str__(self):
        return "{}".format(self.nickname)
