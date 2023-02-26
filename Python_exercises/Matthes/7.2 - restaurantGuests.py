# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:38:17 2023

@author: Evandro Rhari
"""

invited = int(input("Welcome to White Canary! How many people are comming with you?\n"))

if invited >= 8:
    print("Sorry, we don't have a table this large " +
          "Please, wait.")
else:
    print("Magnificent! Please, follow me.")
