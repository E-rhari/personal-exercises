# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 18:58:55 2023

@author: Evandro Rhari
"""

guests = open("guests.txt", "a")
guest = input("Qual seu nome?\n")
guests.write(f"{guest}\n")
print("Seu nome foi adicionado à lista 'guests.txt'!")
guests.close()