# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, items):
        self.name = name
        self.location = location
        self.items = items
    
    def player_moves(self, next_position, current_position):
        position = next_position + "to"
        if hasattr(current_position, position):
            return getattr(current_position, position)
        else:
            print(f'You cannot go that way friend. Try again.')
        return (current_position)

