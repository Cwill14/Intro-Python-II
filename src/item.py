class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Name: {self.name}\n  Description: {self.description}"
    def __repr__(self):
        return f"\n\tName: {repr(self.name)}\n\t Description: {repr(self.description)})\n"