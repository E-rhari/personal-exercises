# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 21:40:16 2023

@author: Evandro Rhari
"""

anwser = ' '
places = []

while anwser.lower() not in 'no':
    anwser = input("If you could go anywhere, where would you go?\n")
    places.append(anwser)
    anwser = input("Would you like to insert another answer?\n")

print("\n--Pool Results:--")
for place in places:
    print(f"    {place}")