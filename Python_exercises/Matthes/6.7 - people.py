# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 21:35:53 2023

@author: Evandro Rhari
"""

orlando =  {
            'name': 'orlando',
            'surname': 'da serra negra',
            'age': 31,
            'city': 'serra negra',
            }

james =    {
            'name': 'james',
            'surname': 'bols',
            'age': 29,
            'city': 'norte',
           }

enki =     {
            'name': 'enki',
            'surname': '',
            'age': 18,
            'city': 'mato'
           }

people = [orlando, james, enki]

for person in people:
    for key, value in person.items():
        print(f'{key.title()}: {str(value).title()}')
    print('\n')