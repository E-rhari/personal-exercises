# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 19:41:31 2023

@author: Evandro Rhari
"""

pool = open("pool.txt", "a")
answer = " "

while answer.lower() not in "no":
    answer = input("Do you like programming?\nR: ")
    pool.write(answer)
    answer = input("If you would like to, please give your oppinion about it: ")
    pool.write(f"; {answer}\n")
    answer = input("Would you like to keep this survey going?\nR: ")
    
pool.close()
print("Good. Pool is now closed.")