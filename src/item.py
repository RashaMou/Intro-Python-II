class Item:
    def __init__(self, name, function, description):
        self.name = name
        self.function = function
        self.description = description

    def examine_item(self):
        print(f'Name: {self.name}')
        print(f'Function: {self.function}. {self.description}')

