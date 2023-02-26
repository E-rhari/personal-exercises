# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 10:38:52 2023

@author: Evandro Rhari
"""

current_users = ['ademir', 'rhari', 'grim', 'tesla', 'salazar']
new_users = ['konj', 'rhari', 'salazar', 'neemo', 'grim']

for user in new_users:
    if user.lower() in current_users:
        print(f"{user}? Shitty pick. Someone else already picked that name. " +
              "Choose an other, better, username.")
    else:
        print(f"{user}? Ok. That's okay username")
