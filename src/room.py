# Implement a class to hold room information. This should have name and
# description attributes.
from colorama import Fore
from colorama import Style


class Room:
    def __init__(self, name, desc, n_to=None, e_to=None, s_to=None, w_to=None):
        self.name = name
        self.desc = desc
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to

    def __str__(self):
        return f"{Fore.GREEN}{self.name}{Style.RESET_ALL}\n{Fore.YELLOW}{self.desc}{Style.RESET_ALL}"
