from room import Room
from player import Player
from item import Item
import os
import sys
import time
import textwrap


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

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

### Initialize Items

sword = Item('sword', 'weapon', 'A sharp steel blade')
food = Item('food', 'sustenance', "Not delicious, but it'll do")
twine = Item('twine', 'resource', 'Can be used to craft things')
wood = Item('wood', 'resource', 'Can be used to craft things' )
herbs = Item('herbs', 'resource', 'Medicinal herbs to restore health')

### Add items to room
room['outside'].items = sword, twine

#### HELPERS ###

wrapper = textwrap.TextWrapper(width=50)


def typewriter(phrase):
    for character in phrase:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.001)

def help_menu():
    print('\n#############################')
    print('##        Help Menu        ##')
    print('#############################\n')
    print('Travel:       (n)orth, (s)outh, (e)ast, (w)est.')
    print('Inventory:    (v)iew items in a room, check your (i)nventory, (take) an item, (drop) an item, (examine) an item .')
    print('Help:         (h)')
    print('\n')

def unknown_command_options():
    print('Unknown command, please try again. You can also press (h) for help, or (q) to quit. \n')
    action = input('>>>> ')
    if action == 'q':
        sys.exit()
    elif action == 'h':
        help_menu()

### START GAME ###

def player_inventory_loop():
    player.view_inventory_items()
    action = input('>>>> ')
    cmd = action.split(' ') ## gives us a list
    if cmd[0] == 'examine':
        for item in player.items:
            if item.name == cmd[1]:
                idx = player.items.index(item)
                player.items[idx].examine_item()
                break
                room_loop()
            else:
                print('Unknown item. Please try again.')
                break
    elif cmd[0] == 'drop':
        for item in player.current_room.items:
            if item.name == cmd[1]:
                idx = player.items.index(item)
                player.drop_inventory_item(player.current_room.items[idx])
                ## add inventory item to room
                player.current_room.add_items_to_room(player.current_room.items[idx])
                break
                print('\n')
                room_loop()
            else:
                print('Unknown item. Please try again.')
                break
    if cmd[0] == 'c':
            room_loop()

def room_inventory_loop():
    player.current_room.view_room_items()
    action = input('>>>> ')
    cmd = action.split(' ')
    if cmd[0] == 'examine':
        for item in player.current_room.items:
            if item.name == cmd[1]:
                idx = player.current_room.items.index(item)
                player.current_room.items[idx].examine_item()
                break
                room_loop()
            else:
                print('Unknown item. Please try again.')
                break
    elif cmd[0] == 'take':
        for item in player.current_room.items:
            if item.name == cmd[1]:
                idx = player.current_room.items.index(item)
                player.add_inventory_item(player.current_room.items[idx])
                player.current_room.remove_item(player.current_room.items[idx])
                break
                print('\n')
                room_loop()
            else:
                print('Unknown item. Please try again.')
                break
    if cmd[0] == 'c':
            room_loop()


def start_game():
    help_menu()

    question1 = "Hello, what's your name?\n"
    typewriter(question1)

    player_name = input('>>>> ')
    print('\n')
    global player
    player = Player(player_name, room['outside'])
    welcome = 'Welcome, ' + player_name + '.'

    typewriter(welcome)
    print('\n')

    game_loop()

def action_loop():
    acceptable_inputs = ['n', 's', 'w', 'e', 'v', 'i']
    print('\n')
    action = input('>>>> ')
    while action not in acceptable_inputs:
        unknown_command_options()
    if action in acceptable_inputs[:4]:
        player.travel(action)
    elif action == 'i':
        player_inventory_loop()
    elif action == 'v':
        room_inventory_loop()



def room_loop():
    print('\n')
    typewriter('You are now in the ' + player.current_room.name + '.\n')
    typewriter(player.current_room.description + '.\n')
    print('\n')
    typewriter('You can (v)iew items in this location, or go in one of these directions:\n')
    print(player.current_room.get_exits_string())

### GAME LOOP ####

def game_loop():
    while True:
        room_loop()
        action_loop()









#### Title Screen ####


def title_screen():
    os.system('clear')
    print('#########################################')
    print('## Welcome to ESCAPE FROM MONKEY CAVE! ##')
    print('#########################################')
    print('                - (P)lay -           ')
    print('                - (H)elp -           ')
    print('                - (Q)uit -           ')
    print('        Creative Commons by Rasha    ')
    title_screen_selections()


def title_screen_selections():
    option = input('> ')
    if option.lower() == 'p':
        start_game()
    elif option.lower() == 'h':
        help_menu_start()
    elif option.lower() == 'q':
        sys.exit()
    while option.lower() not in ['p', 'h', 'q']:
        print('Please enter a valid command')
        option = input('> ')
        if option.lower() == 'p':
            start_game()
        elif option.lower() == 'h':
            os.system('clear')
            help_menu_start()
        elif option.lower() == 'q':
            sys.exit()


def help_menu_start():
    print('########################################')
    print('## Welcome to ESCAPE FROM MONKEY CAVE ##')
    print('########################################')
    print('- Placeholder for help -')
    title_screen_selections()


### START ###
title_screen()
