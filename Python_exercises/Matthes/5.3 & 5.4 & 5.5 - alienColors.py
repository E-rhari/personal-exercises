# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 11:32:26 2023

@author: Evandro Rhari
"""

import random as rand

alien_type = ('green', 'yellow', 'red', 'none')
score = 0

for i in range(5):
    alien = rand.choice(alien_type)
    if alien == 'none':
        print("Oh, damn! You missed!")
    else:
        if alien == 'green':
            score += 5
        elif alien == 'yellow':
            score += 10
        elif alien == 'red':
            score += 15
        print("Wowee! You've just hit a " + alien + " alien!")
        
print("You scored " + str(score) + " points!")