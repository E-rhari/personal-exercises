# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:19:35 2023

@author: Evandro Rhari
"""

from time import sleep

class User():    
    """Models a user by name, login information and adittional info"""
    def __init__(self, name, username, password, **info):
        self.name = name
        self.username = username
        self.password = password
        self.info = info
        self.attempt = 1
        
    def describe_user(self):
        """Prints a predetermineted message about the info we have about the 
        user"""
        print(f"name: {str(self.name)}")
        print(f"username: {str(self.username)}")
        
        for key, value in self.info.items():
            print(f"{str(key)}: {str(value)}")
            
    def login_mistake(self):
        """Adds 1 to the login attempt counter"""
        self.attempt += 1
            
        
print("--Create Account--")
name = input("Name: ")
username = input("Userame: ")
password = input("Password: ")
user = User(name, username, password)

login_attempt = ''
password_attempt = ''
active = True
while active:
    print(f"\nLogin attempt nº{str(user.attempt)}")
    login_attempt = input("Username: ")
    password_attempt = input("Passowrd: ")
    
    if login_attempt != user.username or password_attempt != user.password:
        print("Username or password mistaken. Try again.")
        user.login_mistake()
    else:
        print("--Sucess--!")
        active = False
    if user.attempt > 3:
        wait = (user.attempt - 1) * 10
        print(f"Too many mistakes. Pelase wait {wait} seconds")
        sleep(wait)