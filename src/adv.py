from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("You are outside, looking at a slightly ooky cave entrance, with something glinting and gleaming faintly in the dusky half-light inside.",
                     "North of you, the cave mount beckons, creepily but irresistibly..."),

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


# Main
#
# Make a new player object that is currently in the 'outside' room.

player_name = input("Welcome player! Please give us your name: ")

player = Player(player_name, room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here)

directions = {'n': 'n_to', 'N': 'n_to', 's': 's_to', 'S': 's_to', 'e': 'e_to', 'E': 'e_to', 'w': 'w_to', 'W': 'w_to'}


while True:
    print(player.room.name)
    print(player.room.description)

    choice = input(f'Which way next, {player.name}? ')

    direction = directions[choice]
    try:
        player.room = getattr(player.room, direction)
    
    except AttributeError:
        print("Sorry, you can't go that way, try another direction.")
        

# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

