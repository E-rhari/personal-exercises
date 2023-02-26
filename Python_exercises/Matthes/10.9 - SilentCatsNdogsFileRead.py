# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 21:40:26 2023

@author: Evandro Rhari
"""

def read_file_lines(file):
    try:    
        unreadFile = open(file)
        readFile = unreadFile.readlines()
        unreadFile.close()
    except FileNotFoundError:
        pass
        return []
    return readFile


print("Cat names:")
for cat in read_file_lines("cats.txt"):
    print("\t - " + cat.rstrip().title())
    
print("\nDog names: ")    
for dog in read_file_lines("dogs.txt"):
    print("\t - " + dog.rstrip().title())