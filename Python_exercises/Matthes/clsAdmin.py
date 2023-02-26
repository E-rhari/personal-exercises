# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:26:58 2023

@author: Evandro Rhari
"""

from string import capwords
from clsUser import User

class Admin(User):
    """Models a special user with priviliges"""
    def __init__(self, name, username, **info):
        super().__init__(name, username, **info)
        self.privileges = Privileges()
    
    
class Privileges():
    """Models Admin's priviliges"""
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        """Prints user's priviliges"""
        print("Privileges: ")
        for privilege in self.privileges:
            print(f"    {capwords(privilege)}") 