# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:56:49 2023

@author: Evandro Rhari
"""

print("PEPERONI MUSSARELA! Welcome to my pizzeria! "+
      "What toppings are 'ya havin'?")
pizza = []
active = True

while active:
    anwser = " "
    while anwser.lower() not in 'no':
        anwser = input("")
        pizza.append(anwser.lower())
        print("Mwuah mwuah! Buonno! Something else?")
    
    pizza.pop()
    
    
    print("\nAwesome, so you are having a", end="")
    vowel = ['a', 'e', 'i', 'o', 'u']
    if pizza[0][0] in vowel:
        print("n ", end="")
    else:
        print(" ", end="")
    
    
    if len(pizza) == 1:
        print(pizza[0], end="")
        pizza.pop()
    
    for topping in sorted(pizza, reverse=True):
        top = pizza.pop()
        print(top, end ="")
        if len(pizza) == 1:
            print(" and ", end="")
        elif len(pizza) != 0:
            print(",", end="")
            
            
    anwser = input(" pizza, correct?\n")
    if anwser.lower() in 'no':
        print("\nMamma mia! So please say it again!")
    else:
        print("\nBuonno! It will be ready in {never} minutes!")
        active = False