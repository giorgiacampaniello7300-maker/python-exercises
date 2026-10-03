class Player: 
    def __init__(self, name, items, location):
        self.name = name
        self.items = items
        self.location = location

    def moving(self, new_location):
        self.location = new_location