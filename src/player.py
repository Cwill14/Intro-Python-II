# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f"Player Information: \n  Name: {self.name}\n  Location: {self.current_room.name}\n  Inventory: {self.inventory}"
    
    def __repr__(self):
        return  f"Item({repr(self.name)})"

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"You have picked up the {item}")

    def drop_item(self, item):
        self.inventory.remove(item)
        print(f"You have dropped the {item}")

