# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 21:26:45 2023

@author: Evandro Rhari
"""

sandwich_orders = ['tuna', 'cheese', 'ham']
finished_sandwich = []


while sandwich_orders:
    preparing = sandwich_orders.pop()
    finished_sandwich.append(preparing)
    print("Your " + preparing + " sandwich is now ready!")
    