# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:43:05 2023

@author: Evandro Rhari
"""

from random import randint

class Dice():
    """Models a user determineted sided dice and rolls a user determineted
    amount of it"""
    def roll(self, sides, amount=1):
        """Rolls the amount of dices determined by the user, defaulted as 1"""
        self.sides = sides
        self.amount = amount
        self.result = []
        for n in range(self.amount):
            self.result.append(randint(1, self.sides))
        return self.result
            
            
            
dice = Dice()
results = dice.roll(20,5)
for result in results:
    print(result)