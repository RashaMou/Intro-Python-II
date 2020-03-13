# Implement a class to hold room information. This should have name and
# description attributes.


class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = []

    def view_room_items(self):
        if len(self.items) > 0:
            print('\n')
            print('This room contains the following items: \n')
            for item in self.items:
                print(item.name)
            print("\nEnter an item's name to (examine) it or (take) it, or enter (c) to continue.\n")
            print ('\n')
        else:
            print('This room has no items.')

    def add_items_to_room(self, item_name):
        self.items.append(item_name)
        print(f'You have added {item_name} to the {self.name} \n')

    def get_exits_string(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits

    def remove_item(self, item):
        self.items.remove(item)



