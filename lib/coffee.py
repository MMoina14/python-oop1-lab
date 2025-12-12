#!/usr/bin/env python3

class Coffee:
    pass  
     
    """
    A class to represent a coffee product in the bookstore.
    
    Attributes:
        size (str): The size of the coffee (Small, Medium, or Large)
        price (float): The price of the coffee
    """
    
    def __init__(self, size, price):
        """
        Initialize a Coffee object.
        
        Args:
            size (str): The size of the coffee (Small, Medium, or Large)
            price (float): The price of the coffee
        """
        self.size = size
        self.price = price
    
    @property
    def size(self):
        """Get the size of the coffee."""
        return self._size
    
    @size.setter
    def size(self, value):
        """
        Set the size of the coffee.
        
        Args:
            value (str): The size to set
            
        Validates that size is Small, Medium, or Large.
        """
        if value not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value
    
    def tip(self):
        """
        Add a tip to the coffee price.
        
        Prints a thank you message and increases the price by 1.
        """
        print("This coffee is great, here's a tip!")  
        self.price += 1