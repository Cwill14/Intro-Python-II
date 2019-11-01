# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, room_items=[]):
        self.name = name
        self.description = description
        self.room_items = room_items
    def __str__(self):
        s = f"\nRoom: {self.name}\n  Description: {self.description}\n"
        if len(self.room_items) > 0:
            s += f"  Items: \n"
            for i, v in enumerate(self.room_items, start=1):
                s += f"      {i}. {v.name}\n        Description: {v.description}\n"
        else:
            pass
        return s
    def __repr__(self):
        return f"Room({repr(self.name)})"

    def add_item(self, item):
        self.room_items.append(item)
    def remove_item(self, item):
        self.room_items.remove(item)
        