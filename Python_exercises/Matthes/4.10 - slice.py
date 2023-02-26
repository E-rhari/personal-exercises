# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 08:19:54 2023

@author: Evandro Rhari
"""

import math


million = [n for n in range (1,1001)]

print("The 3 first list items are:")
for number in million[:3]:
    print(number)

print("\nThe 3 middle list items are:")
mid = math.ceil(len(million)/2)
for number in million[mid-2:mid+1]:
    print(number)

print("\nThe 3 last list items are:")
for number in million[len(million) - 3:]:
    print(number)