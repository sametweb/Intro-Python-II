from colorama import Fore, Back, Style


class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def add_to_room(self, room):
        room.items.append(self)
        return room.items

    def remove_from_room(self, room):
        room.items.remove(self)
        return room.items

    def add_to_player(self, player):
        player.inventory.append(self)
        self.remove_from_room(player.current_room)
        print(f'{Back.BLUE}You picked up {self.name}{Style.RESET_ALL}')
        return player.inventory

    def remove_from_player(self, player):
        player.inventory.remove(self)
        self.add_to_room(player.current_room)
        print(f'{Back.BLUE}You dropped {self.name}{Style.RESET_ALL}')
        return player.inventory
