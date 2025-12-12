#!/usr/bin/env python3

class Book:
    pass 
    """
    A class to represent a book in the bookstore.
    
    Attributes:
        title (str): The title of the book
        page_count (int): The number of pages in the book
    """
    
    def __init__(self, title, page_count):
        """
        Initialize a Book object.
        
        Args:
            title (str): The title of the book
            page_count (int): The number of pages in the book
        """
        self.title = title
        self.page_count = page_count
    
    @property
    def page_count(self):
        """Get the page count of the book."""
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        """
        Set the page count of the book.
        
        Args:
            value: The page count to set
            
        Validates that page_count is an integer.
        """
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value
    
    def turn_page(self):
        """
        Simulate turning a page in the book.
        
        Prints a message indicating the page has been turned.
        """
        print("Flipping the page...wow, you read fast!")