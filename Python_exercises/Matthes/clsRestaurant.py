# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:09:28 2023

@author: Evandro Rhari
"""

from string import capwords

class Restaurant():
    """Models a restaurant by name, cusine and state(open/closed)"""
    
    def __init__(self, name, cuisine):
        self.name = str(name)
        self.cuisine = str(cuisine)
        self.open = False
        self.number_served = 0
        
        
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
            
    def set_number_served(self, number_served):
        """Stablish the 'number_served' class attribute"""
        self.number_served =+ number_served