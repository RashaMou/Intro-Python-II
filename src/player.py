# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, current_room):
        self.name = name,
        self.current_room = current_room

    def move(self, next_room):
        self.current_room = next_room

    def print_location(self):
        return f"You are now {self.current_room}"
