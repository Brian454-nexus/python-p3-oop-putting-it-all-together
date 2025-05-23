#!/usr/bin/env python3

# Define the Shoe class
class Shoe:
    def __init__(self, brand, size):
        # Set the brand of the shoe
        self.brand = brand
        # Set the size of the shoe (uses the property setter)
        self.size = size
        # Initialize the condition attribute to None
        self.condition = None

    @property
    def size(self):
        # Getter for the size attribute
        return self._size

    @size.setter
    def size(self, value):
        # Setter for the size attribute, ensures value is an integer
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        # Print a message indicating the shoe has been repaired
        print("Your shoe is as good as new!")
        # Set the condition attribute to 'New' after repair
        self.condition = "New"