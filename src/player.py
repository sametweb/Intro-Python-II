# Write a class to hold player information, e.g. what room they are in
# currently.
from colorama import Fore, Back, Style


class Player:
    def __init__(self, nickname, current_room=None, inventory=None):
        self.nickname = nickname
        self.current_room = current_room
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def __str__(self):
        return f"{Fore.BLACK}{Back.WHITE} {self.nickname} {Style.RESET_ALL}"

    def show_inventory(self):
        if len(self.inventory) > 0:

            item_counts = dict.fromkeys(
                [item.name for item in self.inventory], 0)
            for item in self.inventory:
                if item.name in item_counts.keys():
                    item_counts.update(
                        {item.name: item_counts.get(item.name) + 1})

            print(str(item_counts))

            player_inventory = 'Items: ' + \
                ', '.join([item.name for item in self.inventory])
        else:
            player_inventory = 'No items'
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
