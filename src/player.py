# Write a class to hold player information, e.g. what room they are in
# currently.
from colorama import Fore, Back, Style
from item import Weapon, Item


class Player:
    def __init__(self, nickname, current_room=None, inventory=None, dmg=0):
        self.nickname = nickname
        self.current_room = current_room
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
        self.dmg = dmg

    def __str__(self):
        return f"{Fore.BLACK}{Back.WHITE} {self.nickname} ({self.dmg}) {Style.RESET_ALL}"

    def attack(self, unit):
        for monster in self.current_room.monsters:
            if monster.name == unit:
                unit = monster
                break
        if unit.health > self.dmg:
            unit.health -= self.dmg
        else:
            unit.dies_at(self.current_room)

    def show_inventory(self):
        if len(self.inventory) > 0:

            item_counts = dict.fromkeys(
                [item.name for item in self.inventory], 0)
            for item in self.inventory:
                if item.name in item_counts.keys():
                    item_counts.update(
                        {item.name: item_counts.get(item.name) + 1})

            player_inventory = 'Your inventory: ' + \
                ', '.join(
                    [f'{item}: {item_counts[item]}' for item in item_counts])
        else:
            player_inventory = 'No items in inventory'
        print(f'{Back.BLUE}{Fore.WHITE}{player_inventory}{Style.RESET_ALL}')

    def move_to(self, direction):
        def no_room():
            print(f'{Fore.RED}There is nothing there!{Style.RESET_ALL}')

        if direction.lower() == 'w':
            if self.current_room.w_to:
                self.current_room = self.current_room.w_to
                print(self.current_room)
            else:
                no_room()
        elif direction.lower() == 'e':
            if self.current_room.e_to:
                self.current_room = self.current_room.e_to
                print(self.current_room)
            else:
                no_room()
        elif direction.lower() == "s":
            if self.current_room.s_to:
                self.current_room = self.current_room.s_to
                print(self.current_room)
            else:
                no_room()

        elif direction.lower() == 'n':
            if self.current_room.n_to:
                self.current_room = self.current_room.n_to
                print(self.current_room)
            else:
                no_room()

        else:
            print(f'{Fore.RED}Sorry, no idea what that means!{Style.RESET_ALL}')
            print(f'{Fore.CYAN}Type "help" for available commands{Style.RESET_ALL}')
            print(self.current_room)
