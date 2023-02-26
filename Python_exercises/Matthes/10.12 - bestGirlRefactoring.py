# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:07:08 2023

@author: Evandro Rhari
"""

import json
from string import capwords

def load_best_girl():
    try:
        with open("users_best_girl.json") as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def input_best_girl():
    bestGirl = input("Who is best Girl?\n")
    with open("users_best_girl.json", "w") as file:
        json.dump(bestGirl, file)
    print("Ok thanks, I've saved that information\n")

def recall_best_girl():
    bestGirl = load_best_girl()
    if not bestGirl:
        input_best_girl()
        bestGirl = load_best_girl()
    print(f"If I can reacall correctly, you think that {capwords(bestGirl)}"+
          " is best girl.")
    
recall_best_girl()