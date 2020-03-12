# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, current_loc):
        self.name = name,
        self.current_loc = current_loc

    def move(self, next_loc):
        self.current_loc = next_loc
