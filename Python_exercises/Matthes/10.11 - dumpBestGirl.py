# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 15:34:25 2023

@author: Evandro Rhari
"""

import json

bestGirl = input("Who is best Girl?\n")
with open("users_best_girl.json", "w") as file:
    json.dump(bestGirl, file)
print("Ok thanks, I've saved that information")
