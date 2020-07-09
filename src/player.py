# Write a class to hold player information, e.g. what room they are in
# currently.
from colorama import Fore, Back, Style


class Player:
    def __init__(self, nickname, current_room=None):
        self.nickname = nickname
        self.current_room = current_room

    def __str__(self):
        return f"{Fore.BLACK}{Back.WHITE} {self.nickname} {Style.RESET_ALL}"

    def move_to(self, direction):
        def no_room():
            print(f'{Fore.RED}There is nothing there!{Style.RESET_ALL}')

        if direction.lower() == 'e':
            if self.current_room.w_to:
                self.current_room = self.current_room.w_to
                print(self.current_room)
            else:
                no_room()
        elif direction.lower() == 'w':
            if self.current_room.e_to:
                self.current_room = self.current_room.e_to
                print(self.current_room)
            else:
                no_room()
        elif direction.lower() == "n":
            if self.current_room.s_to:
                self.current_room = self.current_room.s_to
                print(self.current_room)
            else:
                no_room()

        elif direction.lower() == 's':
            if self.current_room.n_to:
                self.current_room = self.current_room.n_to
                print(self.current_room)
            else:
                no_room()

        else:
            print('Available directional commands: [s], [n], [e], [w]')
            print(f'{Fore.CYAN}For more, type "help"{Style.RESET_ALL}')
