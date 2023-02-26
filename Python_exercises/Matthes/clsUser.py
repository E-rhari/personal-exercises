# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:23:18 2023

@author: Evandro Rhari
"""

from string import capwords

class User():
    """Models a user by name, username and adittional info"""
    def __init__(self, name, username, **info):
        self.name = name
        self.username = username
        self.info = info
        
    def describe_user(self):
        """Prints a predetermineted message about the info we have about the 
        user"""
        print(f"name: {str(self.name)}")
        print(f"username: {str(self.username)}")
        
        for key, value in self.info.items():
            print(f"{str(key)}: {str(value)}")