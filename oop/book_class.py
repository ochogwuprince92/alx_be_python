# book_class.py
# This script defines a Book class and demonstrates the use of Python magic methods.

class Book:
    # Constructor (__init__) to initialize a Book object with title, author, and year
    def __init__(self, title, author, year):
        # Initialize instance variables for the book's title, author, and year
        self.title = title
        self.author = author
        self.year = year

    # Destructor (__del__) to print a message when a Book object is deleted
    def __del__(self):
        # Print the message indicating that the book object is being deleted
        print(f"Deleting {self.title}")

    # String representation method (__str__) for a user-friendly display of the Book
    def __str__(self):
        # Return a formatted string with the book's title, author, and year
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official representation method (__repr__) for recreating the Book object
    def __repr__(self):
        # Return a string that could be used to recreate the Book object
        return f"Book('{self.title}', '{self.author}', {self.year})"
