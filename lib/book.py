#!/usr/bin/env python3

# Define the Book class
class Book:
    def __init__(self, title, page_count):
        # Set the title of the book
        self.title = title
        # Set the page count of the book (uses the property setter)
        self.page_count = page_count

    @property
    def page_count(self):
        # Getter for the page_count attribute
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Setter for the page_count attribute, ensures value is an integer
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        # Print a message indicating the page has been turned
        print("Flipping the page...wow, you read fast!")

