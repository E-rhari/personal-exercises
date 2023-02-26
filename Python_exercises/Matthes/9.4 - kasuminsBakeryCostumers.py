# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:11:22 2023

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
        self.number_served =+ number_served
        
        
kasuminsBakery = Restaurant("kasumins bakery", "Koppepan")
print(f"Number of costumers served: {str(kasuminsBakery.number_served)}")
print("--[Due to frustantion from the lack of costumers, Kasumi called her " 
      "friends over]--")
kasuminsBakery.set_number_served(11)
print(f"Number of costumers served: {str(kasuminsBakery.number_served)}")