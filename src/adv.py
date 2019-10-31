from room import Room
from player import Player
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

def getPlayer():
    nameInput = input("Set your character's name: ")
    global myplayer
    myplayer = Player(nameInput, room['outside'])
    print(myplayer.current_room)

def move():
    global moveInput
    moveInput = input("Enter directional command: ")
    game(moveInput)

def game(mInput):
    if mInput == 'n':
        x = getattr(myplayer.current_room, "n_to", "can't go that way")
        myplayer.current_room = x
        print(myplayer.current_room)
        move()
    
    elif mInput == 'e':
        x = getattr(myplayer.current_room, "e_to", "can't go that way")
        myplayer.current_room = x
        print(myplayer.current_room)
        move()
    
    elif mInput == 's':
        x = getattr(myplayer.current_room, "s_to", "can't go that way")
        myplayer.current_room = x
        print(myplayer.current_room)
        move()
    
    elif mInput == 'w':
        x = getattr(myplayer.current_room, "w_to", "can't go that way")
        myplayer.current_room = x
        print(myplayer.current_room)
        move()
    
    elif mInput == 'q':
        exit
    else:
        print("Invalid key")
        move()

getPlayer()
move()
game(moveInput)