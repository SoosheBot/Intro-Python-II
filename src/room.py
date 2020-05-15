# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        # return self.name
       return f'{self.name} is in {self.description}'

