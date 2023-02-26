# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 10:26:41 2023

@author: Evandro Rhari
"""

users = ['ademir', 'rhari', 'grim', 'tesla', 'salazar']
if users:
    for user in users:
        if user == 'ademir':
            print("Greetings, Mr. " + user.capitalize() + ". It's a pleasure " +
                  "to have you here! * sips wine *")
        else:
            print("Oh, it's you, " + user.capitalize() + ". Com'on, speak up." +
                  " Tell me what'ya want already an get off.")
else:
    print("It's so lonly in here... I wonder why...")