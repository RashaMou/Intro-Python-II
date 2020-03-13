# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    def __init__(self, name, current_room):
        self.name = name,
        self.current_room = current_room
        self.items = ['rock', 'paper']


    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
        else:
            print("You cannot move in that direction. Try another one.")

    def view_inventory_items(self):
        if len(self.items) > 0:
            print('You have the following items in your inventory:')
            print(*self.items, sep = "\n")
            print("\nWhat would you like to do?\n")
            print ('\n')

    def add_inventory_item(self, item):
        self.items.append(item)
        print(f'You have added {item.name} to your inventory.\n')

    def drop_inventory_item(self, item):
        self.items.remove(item)
        print(f'You have dropped {item.name}.\n')
