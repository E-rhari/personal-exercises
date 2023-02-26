# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 09:33:36 2023

@author: Evandro Rhari
"""

orlando =  {
            'name': 'orlando',
            'surname': 'da serra negra',
            'age': 31,
            'city': 'serra negra',
            }

for key, value in orlando.items():
    print(f'{key.title()}: {str(value).title()}')