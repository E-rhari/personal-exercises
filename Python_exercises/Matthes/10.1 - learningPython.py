# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 18:21:35 2023

@author: Evandro Rhari
"""

with open("learning_python.txt") as file:
    text = file.read()
    print(text)
    file.seek(0)
    
    for line in file:
        print(line.rstrip())
    
    file.seek(0)
    linelist = file.readlines()
    
for line in linelist:
    line = line.rstrip()
    print(line)