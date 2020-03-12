from room import Room
from player import Player
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


#### HELPERS ###

wrapper = textwrap.TextWrapper(width=50)


def type(phrase):
    for character in phrase:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)


def help_menu():
    print('To move, type (n)orth (s)outh (e)ast or (w)est to move in that direction.')

### START GAME ###


def start_game():
    os.system('clear')
    print('##################')
    print("## Let's begin! ##")
    print('##################')
    os.system('clear')

    question1 = "Hello, what's your name?\n"
    type(question1)

    player_name = input('> ')
    global player
    current_location = room['outside']
    player = Player(player_name, current_location)
    os.system('clear')

    welcome = 'Welcome, ' + player_name + '. \n'
    type(welcome)
    location_description = player.current_loc.description + '\n'
    type(location_description)

    os.system('clear')


### GAME LOOP ####


def move_loop():

    prompt_action = 'Where would you like to go? \n'

    type(location_description)
    type(prompt_action)

    action = input('> ')
    acceptable_directions = ['n', 's', 'w', 'e']
    while action.lower() not in acceptable_directions:
        print('Unknown direction, please try again. You can also press (h) for help, or (q) to quit. \n')
        action = input('> ')
    if action.lower() == 'q':
        sys.exit()
    if action.lower() == 'h':
        help_menu()
    if action.lower() in acceptable_directions:
        player_move(action.lower())


def player_move(action):
    if action == 'n':
        player.current_room = player.current_location.n_to
        print(player.current_location.n_to)


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
