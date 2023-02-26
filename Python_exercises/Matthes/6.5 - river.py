# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:00:50 2023

@author: Evandro Rhari
"""

rivers = {
         'nilo': 'egypt',
         'macae': 'brazil',
         'tiger': 'iraq',
         'river': 'you',
        }

for key, value in rivers.items():
    if value == 'you':
        print('The river flows into you')
    else:
        print(f'The {key.title()} river flows into {value.title()}')
        
print('\nAll the rivers:')
for river in rivers.keys():
    if river != 'river':
        print(river.title())
        
print('\nAll the countries:')
for country in rivers.values():
    if country != 'you':
        print(country.title())