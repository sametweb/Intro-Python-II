from colorama import Fore, Back, Style


class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def on_take(self):
        print(f'{Back.BLUE}You picked up {self.name}{Style.RESET_ALL}')

    def on_drop(self):
        print(f'{Back.BLUE}You dropped {self.name}{Style.RESET_ALL}')

    def add_to_room(self, room):
        room.items.append(self)
        return room.items

    def remove_from_room(self, room):
        room.items.remove(self)
        return room.items

    def add_to_player(self, player):
        player.inventory.append(self)
        self.remove_from_room(player.current_room)
        self.on_take()
        return player.inventory

    def remove_from_player(self, player):
        player.inventory.remove(self)
        self.add_to_room(player.current_room)
        self.on_drop()
        return player.inventory


class Weapon(Item):
    def __init__(self, name, desc, dmg=30):
        super().__init__(name, desc)
        self.dmg = dmg

    def add_to_player(self, player):
        player.inventory.append(self)
        player.dmg += self.dmg
        self.remove_from_room(player.current_room)
        self.on_take()
        return player.inventory

    def remove_from_player(self, player):
        player.inventory.remove(self)
        player.dmg -= self.dmg
        self.add_to_room(player.current_room)
        self.on_drop()
        return player.inventory
