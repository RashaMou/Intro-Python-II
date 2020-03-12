# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, current_location):
        self.name = name,
        self.current_location = current_location

    def move(self, next_location):
        self.current_location = next_location
