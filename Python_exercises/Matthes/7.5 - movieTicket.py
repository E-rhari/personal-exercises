# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:48:53 2023

@author: Evandro Rhari
"""

total = int(input("How many people are whatching Puss in Boots with you?\n"))

n = 1
while n <= total:
    age = int(input(f"\nHow old is the {n}º person?\n"))
    if age < 3:
        print("How cute. You still are going to annoy people, but is not like "+
              "you are going to whatch the movie. You can go for free.")
    elif age < 12:
        print("Awesome. It'll cost you 10 bucks")
    else:
        print("That will be $15")
    n+=1