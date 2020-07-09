from colorama import Fore, Back, Style


class Monster:
    def __init__(self, name='monster', health=100, dmg=10):
        self.name = name
        self.health = 100
        self.dmg = dmg

    def dies_at(self, room):
        room.remove_monster(self)
        print(f"{Fore.BLACK}{Back.GREEN}{self.name} dies!{Style.RESET_ALL}")
