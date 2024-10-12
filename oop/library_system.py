# library_system.py
# This script defines a system to model a library with different types of books using inheritance and composition.

# Base Class: Book
class Book:
    def __init__(self, title, author):
        """Initialize the common attributes for all books."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"

# Derived Class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize the EBook with title, author, and file_size attributes."""
        super().__init__(title, author)  # Call the base class (Book) constructor
        self.file_size = file_size  # Unique attribute for EBook

    def __str__(self):
        """Return a string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived Class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize the PrintBook with title, author, and page_count attributes."""
        super().__init__(title, author)  # Call the base class (Book) constructor
        self.page_count = page_count  # Unique attribute for PrintBook

    def __str__(self):
        """Return a string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Composition: Library class to manage books
class Library:
    def __init__(self):
        """Initialize an empty list to store books."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library."""
        for book in self.books:
            print(book)
