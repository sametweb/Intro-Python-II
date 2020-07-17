from room import Room
from player import Player
from item import Item, Weapon
from monster import Monster
from colorama import Fore, Style
from os import system, name

# Declare all the rooms

sword = Weapon("sword", "you can slay your enemy with this")
mana = Item("mana", "you can cast spells with this")
heal = Item("heal", "you can heal your health with this")

roshan = Monster('Roshan')
creep = Monster('Creep')

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [sword], [roshan, creep]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [mana]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [heal]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [mana, sword, heal]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#


def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


player_name = ""

clear_screen()

while len(player_name) < 1:
    player_name = input('Please enter a nickname: ')

# Make a new player object that is currently in the 'outside' room.
new_player = Player(player_name, room['outside'])

clear_screen()

print('Welcome', new_player)


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

is_playing = True

print(new_player.current_room)

while is_playing:

    command = input('What do you want to do? ')

    if(command == 'q'):
        is_playing = False
        break

    clear_screen()

    if(command == 'help' or command == 'h'):
        print('[s] for south')
        print('[n] for north')
        print('[e] for east')
        print('[w] for west')
        print('get [item_name] for picking up items')
        print('take [item_name] for picking up items')
        print('drop [item_name] for dropping items')
        print('attack [unit_name] for attacking monsters')

        print(new_player.current_room)

    elif command == 'i' or command == 'inventory':
        new_player.show_inventory()
        print(new_player.current_room)

    else:
        command = command.split(' ')
        if len(command) == 1:
            print(new_player)
            command = command[0]
            new_player.move_to(command)

        elif len(command) == 2:
            if command[0] == 'get' or command[0] == 'take':
                requested_item = command[1]

                for item in new_player.current_room.items:
                    if item.name == requested_item:
                        requested_item = item
                        break

                if type(requested_item) != str:
                    requested_item.add_to_player(new_player)
                else:
                    print('Item not here')
            elif command[0] == 'drop':
                dropping_item = command[1]
                for item in new_player.inventory:
                    if item.name == dropping_item:
                        dropping_item = item
                        break
                    else:
                        requested_item = None
                if isinstance(dropping_item, Item) or isinstance(dropping_item, Weapon):
                    dropping_item.remove_from_player(new_player)
                else:
                    print("You can't drop what you don't have!")

            elif command[0] == 'attack':
                unit = command[1]
                new_player.attack(unit)
            print(new_player)
            print(new_player.current_room)
