from room import Room
from player import Player
import os
import sys
import time
import textwrap

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

#### HELPERS ###

wrapper = textwrap.TextWrapper(width=50)


def type(phrase):
    for character in phrase:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)


### INITIALIZE PLAYER ###


def start_game():
    os.system('clear')

    question1 = "Hello, what's your name?\n"
    type(question1)

    player_name = input('> ')
    player1 = Player(player_name, 'outside')
    print(player1.print_location())
    os.system('clear')

    welcome = 'Welcome, ' + player_name + '. \n'
    type(welcome)

    def prompt():
        location = room[player1.current_room].description + '\n'
        prompt_action = 'What would you like to do? \n'

        type(location)
        type(prompt_action)


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
    if option.lower() == 'play' or 'p':
        start_game()
    elif option.lower() == 'help' or 'h':
        help_menu()
    elif option.lower() == 'quit' or 'q':
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit', 'p', 'h', 'q']:
        print('Please enter a valid command')
        option = input('> ')
        if option.lower() == 'play' or 'p':
            start_game()
        elif option.lower() == 'help' or 'h':
            help_menu()
        elif option.lower() == 'quit' or 'q':
            sys.exit()


def help_menu():
    print('########################################')
    print('## Welcome to ESCAPE FROM MONKEY CAVE ##')
    print('########################################')
    print('- Placeholder for help -')
    title_screen_selections()


### START ###
title_screen()
