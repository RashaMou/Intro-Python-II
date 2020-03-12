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


def typewriter(phrase):
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
    typewriter(question1)

    player_name = input('> ')
    global player
    current_location = room['outside']
    player = Player(player_name, current_location)
    os.system('clear')

    welcome = 'Welcome, ' + player_name + '. \n'
    typewriter(welcome)

    move_loop()


### GAME LOOP ####

def move_input():
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


def move_loop():
    location_name = 'You are now in the ' + player.current_location.name + '.\n'
    location_description = player.current_location.description + '.\n'
    prompt_move_action = 'Where would you like to go? \n'
    typewriter(location_name)
    typewriter(location_description)
    typewriter(prompt_move_action)
    move_input()


def player_move(action):
    # direction = action + '_to'
    # if hasattr(player.current_location, direction):
    #     player.current_location = player.current_location.direction
    if action == 'n':
        if hasattr(player.current_location, 'n_to'):
            player.move(player.current_location.n_to)
            move_loop()
        else:
            print('You cannot move there from here. Try another direction')
            move_input()
    elif action == 's':
        if hasattr(player.current_location, 's_to'):
            player.move(player.current_location.s_to)
            move_loop()
        else:
            print('You cannot move there from here. Try another direction')
            move_input()
    elif action == 'w':
        if hasattr(player.current_location, 'w_to'):
            player.move(player.current_location.w_to)
            move_loop()
        else:
            print('You cannot move there from here. Try another direction')
            move_input()
    elif action == 'e':
        if hasattr(player.current_location, 'e_to'):
            player.move(player.current_location.e_to)
            move_loop()
        else:
            print('You cannot move there from here. Try another direction')
            move_input()


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
