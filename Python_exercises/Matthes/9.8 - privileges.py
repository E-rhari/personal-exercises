# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 15:54:36 2023

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
    
        
admin = Admin("Evandro", "e-rhari")
admin.privileges.show_privileges()