# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 18:42:01 2023

@author: Evandro Rhari
"""

print("Friendship ended with <PYTHON> now <C++> is my best friend.")
with open("learning_python.txt") as file:
    text = file.read()
    print(text.replace("Python", "C++"))