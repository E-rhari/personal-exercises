# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 12:36:13 2023

@author: Evandro Rhari
"""

from string import capwords

class Restaurant():
    """Models a restaurant by name, cusine and state(open/closed)"""
    
    def __init__(self, name, cuisine):
        self.name = str(name)
        self.cuisine = str(cuisine)
        self.open = False
        
    def describe_restaurant(self):
        """Prints a small string of text describing the restaurant by its name
        and cuisine"""
        print(f"{capwords(self.name)} is a exquisite {capwords(self.cuisine)} "+
              "restaurant.")
    
    def open_close_restaurant(self):
        """Change the value of self.open (open/close) depending in its incoming 
        state, printing a string of text describing the change"""
        if self.open == False:
            self.open == True
            print(f"{capwords(self.name)} is now open!")
        else:
            self.open == False
            print(f"{capwords(self.name)} is now closed!")
            
            
kasuminsBakery = Restaurant("kasumin's bakery", "koppepan")
print(kasuminsBakery.name)
print(kasuminsBakery.cuisine)

kasuminsBakery.describe_restaurant()
kasuminsBakery.open_close_restaurant()
kasuminsBakery.open_close_restaurant()
                            