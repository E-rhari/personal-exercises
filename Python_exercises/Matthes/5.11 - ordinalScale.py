# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 11:09:03 2023

@author: Evandro Rhari
"""

numbers = [number for number in range(1,10)]

print('Ordinal Scale:')
for number in numbers:
    print('\t\t\t  ' + str(number), end='')
    if number == 1:
        print('st')
    elif number == 2:
        print('nd')
    elif number == 3:
        print('rd')
    else:
        print('th')