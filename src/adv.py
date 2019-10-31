from room import Room
from player import Player
import re
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
#
# Main
#
def get_player():
    name_input = input("Set your character's name: ")
    global my_player
    my_player = Player(name_input, room['outside'])
    print(my_player.current_room)

def get_input():
    global move_input
    move_input = input("Enter directional command: ")
    game(move_input)

def move(dir):
    x = getattr(my_player.current_room, str(dir), "can't go that way")
    my_player.current_room = x
    print(my_player.current_room)
    get_input()


def game(m_input):

    if re.search("[ensw]", m_input):
       move(f"{m_input}_to")

    elif m_input == 'q':
        exit
    else:
        print("Invalid key")
        get_input()

get_player()
get_input()
game(move_input)