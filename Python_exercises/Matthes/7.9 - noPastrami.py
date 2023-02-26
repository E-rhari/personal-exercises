# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 21:35:46 2023

@author: Evandro Rhari
"""

sandwich_orders = ['tuna', 'pastrami', 'cheese', 'pastrami', 'ham', 
                   'pastrami']
finished_sandwich = []

if 'pastrami' in sandwich_orders:
    print("My appologies, we don't have pastrami")
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

while sandwich_orders:
    preparing = sandwich_orders.pop()
    finished_sandwich.append(preparing)
    print("Your " + preparing + " sandwich is now ready!")