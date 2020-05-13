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

#My Notes
# when the game first runs, start with an intro and then an input for the player to enter a direction n,s,e,w and that takes them into the room




# input("Do you wish to enter the castle? Press Q to quit, if your soul is crusty and lacks adventure , or N to continue into the Foyer. ")
#
# Main
#
# Make a new player object that is currently in the 'outside' room.
print("You wake up from a nap to find yourself somehow outside of a slightly ooky cave, with something glinting and gleaming faintly in the dusky half-light inside. You are now having An Adventure!")
player_start = Room("outside", ["Outside Cave Entrance",
                     "North of you, the cave mount beckons"])
player_name = input("Welcome player! Please give us your name: ")
print(f"Welcome, {player_name}! You are currently {player_start}. Do you wish to continue? Enter Yes or No and press Enter")


    # input(f"Great! We knew you were the adventurous type, {player_name}! Please choose N to enter the cave and all the adventure that lies in wait! ")

    # print("We're sorry to see you go, you will now wake up from your nap in your own bed, wondering about that strange dream and that ooky cave forever.")

    # print("Please choose Yes or No to continue the adventure.")




# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here)

# input("Where do you want to go next? Select N, S, W, E")
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

