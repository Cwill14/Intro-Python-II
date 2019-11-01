from room import Room
from player import Player
from item import Item
import re
import sys
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("sword", "an ancient weapon, but still sharp")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("staff", "elegant white staff")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("empty chest", "recently opened")]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Main
def get_play_input():
    play_input = input("Ready? press 'enter' to continue")
    if play_input == "enter":
        print(my_player.current_room)
        return
    else:
        pass
def get_player():
    name_input = input("Set your character's name: ")
    global my_player
    my_player = Player(name_input, room['outside'], [{Item("torch", "a simple torch")}, {Item("hat", "just a hat")}])
    print("Commands:")
    print("  n, e, s, w: move north, east, south, or west\n  r: see current room\n  p: see player information\n  i: see inventory\n  q: quit\n\n")
    get_play_input()
    print(my_player.current_room)

def get_input():
    global move_input
    # move_input = sys.argv
    move_input = input("Type command, press Enter to submit: ")
    game(move_input)

def move(dir):
    x = getattr(my_player.current_room, str(dir), "can't go that way")
    if x == "can't go that way":
        print(x)
        get_input()
    else:
        my_player.current_room = x
    print(my_player.current_room)
    get_input()

def loop_list(l):
    # v = [True for i in l if i.name == item]
    # print(f"name: {name}")
    # print(f"l: {l}")
    # answer = [ v for v in l if v == name]
    answer = [ v for v in l]
    print(f"list: {l}")
    print(f"answer: {answer}")

    return answer

def pickup(item_name):
    room_result = loop_list(my_player.current_room.room_items)
    result_item = room_result[0]

    if result_item.name == item_name:
        p_result = loop_list(my_player.inventory)

        if result_item not in p_result:
            my_player.current_room.remove_item(result_item)
            my_player.add_to_inventory(result_item)
        else:
            print(f"You already have the {item_name}")
    else:
        print(f"{item_name} does not exist in {my_player.current_room.name}")

def drop(item):
    my_player.drop_item(item)
    my_player.current_room(item)
    print(f"You have dropped the {item}")

def game(m_input):
    x = re.split("\s", m_input)
    if len(x) == 1:
        if re.search("[ensw]", m_input):
           move(f"{m_input}_to")
        elif m_input == 'r':
            print(my_player.current_room)
            get_input()
        elif m_input == "p":
            print(my_player)
            get_input()
        elif m_input == "i":
            print(my_player.inventory)
            get_input()
        elif m_input == "q":
            exit
        else:
            print("Invalid key")
            get_input()
    else:
        verb = x[0]
        noun = x[1]
        # print(f"noun: {noun}")
        if verb == "take":
            pickup(noun)
            get_input()
        elif verb == "drop":
            drop(noun)
            get_input()
        else:
            print("Invalid key")
            get_input()

get_player()
get_input()
game(move_input)