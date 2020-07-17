# Implement a class to hold room information. This should have name and
# description attributes.
from colorama import Fore, Back, Style

class Room:
    def __init__(self, name, desc, items=None, monsters=None, n_to=None, e_to=None, s_to=None, w_to=None):
        self.name = name
        self.desc = desc
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to
        if items == None:
            self.items = []
        else:
            self.items = items
        if monsters == None:
            self.monsters = []
        else:
            self.monsters = monsters

    def __str__(self):
        if len(self.items) > 0:
            item_list = 'Items in room: ' + \
                ', '.join([item.name for item in self.items])
        else:
            item_list = 'No item in the room'

        if len(self.monsters) > 0:
            monster_list = 'Monsters in room: ' + \
                ', '.join(
                    [monster.name + f'({monster.health})' for monster in self.monsters])
        else:
            monster_list = 'No monster in the room'

        return f"{Fore.GREEN}{self.name}{Style.RESET_ALL}\n{Fore.YELLOW}{self.desc}\n{Fore.BLUE}{item_list}\n{Fore.WHITE}{Back.MAGENTA}{monster_list}{Style.RESET_ALL}"

    def remove_monster(self, monster):
        del self.monsters[self.monsters.index(monster)]
