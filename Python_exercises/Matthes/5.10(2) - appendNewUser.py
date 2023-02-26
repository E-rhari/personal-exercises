# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 10:47:26 2023

@author: Evandro Rhari
"""

users = ['ademir', 'rhari', 'grim', 'tesla', 'salazar']
submission = 'a'

while 1:
    submission = input("Username: ")
    if submission.lower() in users:
        print(f"The username {submission} is unavaliable. Please try another.\n")
    else:
        break
    
users.append(submission.lower())
print("You have been assigned successfully, " + users[-1])