# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 15:57:12 2023

@author: Evandro Rhari
"""

import json
from string import capwords

try:
    with open("users_best_girl.json") as file:
        bestGirl = json.load(file)
except FileExistsError:
    bestGirl = input("Who is best Girl?\n")
    with open("users_best_girl.json", "w") as file:
        json.dump(bestGirl, file)
    
print(f"If I can reacall correctly, you think that {capwords(bestGirl)}"+
      " is best girl.")