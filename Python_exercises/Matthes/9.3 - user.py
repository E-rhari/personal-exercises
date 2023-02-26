# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 12:59:39 2023

@author: Evandro Rhari
"""

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
            
            
user = User("Evandro", "e-rhari", age=16, occupation='student')
user.describe_user()
print("")

user = User("Shizuku", "BestGirl", birthday={'month': 'april', 'day':3}, 
            occupation='student')
user.describe_user()
print("")

user = User("Emma", "Emmama", birthday={'month': 'february', 'day':5}, 
            occupation='student')
user.describe_user()
print("")