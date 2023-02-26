# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 21:10:35 2023

@author: Evandro Rhari
"""

x = input("First number: ")
y = input("Second number: ")

try:
    print(int(x) + int(y))
except ValueError:
        print("Number given must be an integer\n")
